from flask import render_template, request, redirect, flash
from models.Usuario import Usuario
from utils import db
from flask import Blueprint

bp_usuarios = Blueprint("usuarios", __name__, template_folder='usuario') 

@bp_usuarios.route('/recovery')
def recovery():
	usuarios = Usuario.query.all()
	return render_template('usuarios_recovery.html', usuarios = usuarios)


@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuarios_create.html')

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')

        if senha != csenha:
            flash('As senhas não coincidem!', 'danger')
            return render_template('usuarios_create.html', nome=nome, email=email)

        senha_hash = generate_password_hash(senha)
        usuario = Usuario(nome=nome, email=email, senha=senha_hash)
        db.session.add(usuario)
        db.session.commit()

        flash('Dados cadastrados com sucesso!', 'success')
        return redirect(url_for('.recovery'))
    
@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        return render_template('usuarios_create.html')

    if id and request.method == 'GET':
        usuario = Usuario.query.get(id)
        return render_template('usuarios_update.html', usuario=usuario)

    if request.method == 'POST':
        usuario = Usuario.query.get(id)
        usuario.nome = request.form.get('nome')
        usuario.email = request.form.get('email')

        if (request.form.get('senha') and request.form.get('senha') == request.form.get('csenha')):
            usuario.senha = request.form.get('senha')
        else:
            flash('Senhas não conferem')
            return redirect(url_for('.update', id=id))

        db.session.add(usuario)
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect(url_for('.recovery', id=id))


@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  if id==0:
    flash('É preciso definir um usuário para ser excluído')
    return redirect(url_for('.recovery'))

  if request.method == 'GET':
    usuario = Usuario.query.get(id)
    return render_template('usuarios_delete.html', usuario = usuario)

  if request.method == 'POST':
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuário excluído com sucesso')
    return redirect(url_for('.recovery'))
    #return redirect(url_for('/usuarios/recovery'))