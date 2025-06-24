from flask import flask
from modelo import usuario 
from db import db

app = flask(__name__)
app.config['SQLAlCHEMy__DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)



if __name__=='__main__':
     with app.app_contexto():
        db.create_all()
app.run(debug=True)
