from db import db

class usuario(db.modelo):
    __tablename__ = 'usuarios'

    id = db.column(db.integer, primary_key=True)
    nome = db.column(db.string(30), unique=True)
    senha = db.column(db.string,(30), unique=True)
    