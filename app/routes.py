from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Usuarios

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Usuario o contraseña inválidos')
            return redirect(url_for('login'))
        flash('¡Inicio de sesión exitoso para {}!'.format(username))
        print("exitoso")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verifica si el nombre de usuario ya existe en la base de datos
        existing_user = Usuarios.query.filter_by(username=username).first()
        if existing_user:
            flash('El nombre de usuario ya está en uso. Por favor, elige otro.')
            return redirect(url_for('registro'))
        # Crea un nuevo usuario y lo añade a la base de datos
        new_user = Usuarios(username=username)
        new_user.set_password(password)  # Almacena la contraseña en forma segura
        db.session.add(new_user)
        db.session.commit()
        flash('¡Usuario creado exitosamente! Por favor, inicia sesión.')
        return redirect(url_for('login'))
    return render_template('registro.html')
