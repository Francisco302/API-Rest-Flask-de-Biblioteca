from connection import db, ma



class Libro(db.Model):
    __tablename__ = "libro"
    idLibro = db.Column(db.Integer, primary_key=True)
    idAutor = db.Column(db.Integer, db.ForeignKey('autor.idAutor'))
    ISBNLibro = db.Column(db.String(16))
    tituloLibro = db.Column(db.String(128))
    valorPrestamoLibro = db.Column(db.Numeric(precision=8, scale=2))

    def __init__(self, idAutor, ISBNLibro, tituloLibro, valorPrestamoLibro):
        self.idAutor = idAutor  
        self.ISBNLibro = ISBNLibro  
        self.tituloLibro = tituloLibro  
        self.valorPrestamoLibro = valorPrestamoLibro  





class LibroSchema(ma.Schema):
    class Meta:
        fields = ('idLibro', 'idAutor', 'ISBNLibro', 'tituloLibro', 'valorPrestamoLibro')

