from flask import render_template, request, redirect, flash
from flask import flash, redirect
from utils import db
import os
from flask_migrate import Migrate
from models.Usuario import Usuario
from flask import Blueprint
from controllers.Usuario import bp_usuarios


app = Flask(__name__)
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')



app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
