from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from app import db
from app.models.image import Image
from app.utils.image_processing import process_upload
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def upload():
    images = Image.query.filter_by(user_id=current_user.id).all()
    image_data = session.get('image_data', [])
    return render_template('upload.html', images=images, image_data=image_data)

@main_bp.route('/upload', methods=['POST'])
@login_required
def handle_upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('main.upload'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('main.upload'))
    if file:
        file_path = os.path.join('app/static/uploads', file.filename)
        file.save(file_path)
        result = process_upload(file, current_user.id)
        if 'error' in result:
            flash(result['error'])
            return redirect(url_for('main.upload'))
        else:
            flash('Upload successful','success')
            image_data = result.get('images', [{'filename': os.path.basename(file_path), 'coordinates': [], 'image_id': os.path.splitext(file.filename)[0]}])
            session['image_data'] = image_data 
            print(f"Image Data to Pass: {image_data}")
            return render_template('upload.html', images=Image.query.filter_by(user_id=current_user.id).all(), image_data=image_data)

@main_bp.route('/historic_data')
@login_required
def historic_data():
    images = Image.query.filter_by(user_id=current_user.id).all()
    return render_template('historic_data.html', images=images)