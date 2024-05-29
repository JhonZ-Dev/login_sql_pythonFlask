import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mssql+pyodbc://DESKTOP-3KMPQST\\PRGWEB2:@DESKTOP-3KMPQST/FlaskLoginDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False