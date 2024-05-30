from app import db
from werkzeug.security import check_password_hash,generate_password_hash

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def __repr__(self):
        return '<Usuarios {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_nombre = db.Column(db.String(100), nullable=False)
    prod_precio = db.Column(db.Float, nullable=False)
    prod_descrp = db.Column(db.String(100), nullable=False)
    prod_ivapro = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'


