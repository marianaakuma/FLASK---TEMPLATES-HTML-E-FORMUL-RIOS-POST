from flask import Flask
from models import Usuarios
from db import db

app = Flask(__name__)  # Corrigido: 'flask' para 'Flask'

# Corrigido: string do banco de dados e número de barras
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)

# Corrigido: 'if__name__=='_main':' para 'if __name__ == "__main__":'
if __name__ == "__main__":
    with app.app_context():  # Corrigido: 'pp_context' para 'app_context'
        db.create_all()
    app.run(debug=True)
