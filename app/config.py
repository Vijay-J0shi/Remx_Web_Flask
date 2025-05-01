import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "instance", "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AWS_API_URL = 'http://ec2-13-49-46-41.eu-north-1.compute.amazonaws.com/api/predict/upload'