from flask import Flask
from config import Config
from extensions import db  # 🔥 Importamos `db` de outro arquivo

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # 🔥 Inicializa o banco com o app

# 🔥 Importamos `routes` SOMENTE depois da inicialização do app
with app.app_context():
    from routes import *
    from models import *
    db.create_all()  # Criamos o banco apenas uma vez

if __name__ == "__main__":
    app.run(debug=True)
