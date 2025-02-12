# Configuracao do flask
import os


class Config:
    SECRET_KEY = "sua_chave_secreta_aqui"
    # 🔥 Definindo o banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(
        os.getcwd(), 'static/uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # Limite de 2MB por imagem
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
