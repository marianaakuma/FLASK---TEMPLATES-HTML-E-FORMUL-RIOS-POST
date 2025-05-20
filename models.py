from utils import db

class Usuarios(db.Model):
    __tablename__= "usuarios"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome,senha):
        self.nome = nome
        self.senha = senha
    
    def __repr__(self):
        return "<Usuario {}>".format(self.nome)