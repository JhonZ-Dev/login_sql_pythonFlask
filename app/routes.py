from functools import wraps
from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models import Usuarios, Productos
from app.decorators import login_required



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Usuario o contraseña inválidos')
            return redirect(url_for('login'))
        session['user_id'] = user.id
        flash('¡Inicio de sesión exitoso para {}!'.format(username))
        print("exitoso")
        return redirect(url_for('home'))
    return render_template('login.html')



@app.route('/', methods=['GET', 'POST'])
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



@app.route('/index')
@login_required
def index():
    return render_template('index.html')

"""Cerrar sesion"""
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión exitosamente.')
    return redirect(url_for('index'))

"""---------------------------------CRUD PRODUCTOS--------------------------"""

@app.route('/agregar-producto', methods=['GET', 'POST'])
@login_required
def agregar_producto():
    if request.method ==  'POST':
        prod_nombre = request.form['prod_nombre']
        prod_precio = request.form['prod_precio']
        prod_descrp = request.form['prod_descrp']
        prod_ivapro = request.form['prod_ivapro']
        new_producto = Productos(prod_nombre=prod_nombre,   
                                 prod_precio = prod_precio,
                                prod_descrp = prod_descrp,
                                prod_ivapro = prod_ivapro)
        db.session.add(new_producto)
        db.session.commit()
        flash('Producto agregado correctamente')
        return redirect(url_for('home'))
    return render_template('agregar_producto.html')


"""Listar"""
@app.route('/home')
@login_required
def home():
    productos = Productos.query.all()
    return render_template('home.html', productos=productos)


"""EDITAR"""
@app.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    """obtener el id de un objeto"""
    productos = Productos.query.get_or_404(id)
    if request.method ==  'POST':
        productos.prod_nombre = request.form['prod_nombre']
        productos.prod_precio = request.form['prod_precio']
        productos.prod_descrp = request.form['prod_descrp']
        productos.prod_ivapro = request.form['prod_ivapro']
        db.session.commit()
        flash('Producto actualizado correctamente')
        return redirect(url_for('home.html'))
    return render_template('editar_producto.html', productos=productos)


