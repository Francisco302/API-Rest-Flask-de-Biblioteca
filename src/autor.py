
from connection import db, ma



class Autor(db.Model):
    __tablename__ = "autor"
    idAutor = db.Column(db.Integer, primary_key=True)
    codigoAutor = db.Column(db.String(8), unique=True)
    nombreAutor = db.Column(db.String(32))
    apellidoAutor = db.Column(db.String(32))
    autors = db.relationship('Libro')

    def __init__(self, codigoAutor, nombreAutor, apellidoAutor):
        self.codigoAutor = codigoAutor
        self.nombreAutor = nombreAutor  
        self.apellidoAutor = apellidoAutor  




class AutorSchema(ma.Schema):
    class Meta:
        fields = ('idAutor', 'codigoAutor', 'nombreAutor', 'apellidoAutor')

