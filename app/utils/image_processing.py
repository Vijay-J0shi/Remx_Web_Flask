import requests
import os
import json
import cv2
import numpy as np
from flask import current_app
from app import db
from app.models.image import Image

def call_aws_api(file):
    url = current_app.config['AWS_API_URL']
    file.seek(0)
    files = {'files': (file.filename, file)}
    try:
        response = requests.post(url, files=files)
        print(f"AWS API Response Status: {response.status_code}")
        print(f"AWS API Response: {response.text}")
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError:
                print("Failed to parse JSON response")
                return {'error': 'API response is not valid JSON'}
        return {'error': f'API call failed with status {response.status_code}: {response.text}'}
    except requests.exceptions.RequestException as e:
        print(f"AWS API Error: {str(e)}")
        return {'error': f'API call failed: {str(e)}'}

def process_upload(file, user_id):
    result = call_aws_api(file)
    print(f"Result from call_aws_api: {result}")
    if 'error' in result:
        return result
    image_data_list = []
    if isinstance(result, list):
        for item in result:
            if 'error' not in item:
                image_data = save_image_data(item, file, user_id)
                if image_data:
                    image_data_list.extend(image_data if isinstance(image_data, list) else [image_data])
    else:
        if 'error' not in result:
            image_data = save_image_data(result, file, user_id)
            if image_data:
                image_data_list.extend(image_data if isinstance(image_data, list) else [image_data])
    return {'success': True, 'images': image_data_list} if image_data_list else {'success': True}

def save_image_data(data, file, user_id):
    print(f"Data to save: {data}")
    coordinates = data.get('max_confidence_coordinate', data.get('coordinates', [])[0] if data.get('coordinates') else [])
    if not coordinates or len(coordinates) < 4:
        x_min, y_min, x_max, y_max = 0, 0, 0, 0
    else:
        x_min, y_min, x_max, y_max = map(int, coordinates[:4])

    image_data_list = []
    base_name = os.path.splitext(file.filename)[0]
    output_filename = f"processed_{base_name}.jpg"

    if file.filename.lower().endswith('.zip'):
        file_path = os.path.join('app/static/uploads', file.filename)
        image = Image(
            image_id=data.get('image', base_name),
            filename=output_filename,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            user_id=user_id
        )
        db.session.add(image)
        db.session.commit()
        image_data_list.append({
            'filename':output_filename ,
            'image_id': data.get('image', base_name),
            'coordinates': [x_min, y_min, x_max, y_max]
        })
        
        if os.path.exists(file_path):
            os.remove(file_path)
        return image_data_list if image_data_list else None
    else:
        # Handle single image
        
        output_path = os.path.join('app/static/uploads', output_filename)
        file_path = os.path.join('app/static/uploads', file.filename)
        image = cv2.imread(file_path)
        if image is not None:
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
            cv2.imwrite(output_path, image)
            if os.path.exists(file_path):
                os.remove(file_path)
            image = Image(
                image_id=data.get('image_id', data.get('image', base_name)),
                filename=os.path.basename(output_path),
                x_min=x_min,
                x_max=x_max,
                y_min=y_min,
                y_max=y_max,
                user_id=user_id
            )
            db.session.add(image)
            db.session.commit()
            image_data_list.append({
                'filename': os.path.basename(output_path),
                'image_id': base_name,
                'coordinates': [x_min, y_min, x_max, y_max]
            })
    return image_data_list if image_data_list else None