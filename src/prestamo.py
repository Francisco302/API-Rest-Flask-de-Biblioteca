from connection import db, ma



class Prestamo(db.Model):
    __tablename__ = "prestamo"
    idPrestamo = db.Column(db.Integer, primary_key=True)
    numeroPrestamo = db.Column(db.Integer   )
    fechaPrestamo = db.Column(db.DateTime)
    descripcionPrestamo = db.Column(db.String(256))
   

    def __init__(self, numeroPrestamo, fechaPrestamo, descripcionPrestamo):
        self.numeroPrestamo = numeroPrestamo  
        self.fechaPrestamo = fechaPrestamo  
        self.descripcionPrestamo = descripcionPrestamo  


class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('idPrestamo', 'numeroPrestamo', 'fechaPrestamo', 'descripcionPrestamo')
