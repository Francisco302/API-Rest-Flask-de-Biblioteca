from connection import db, ma

class DetallePrestamo(db.Model):
    __tablename__ = "detalleprestamo"
    idDetalleP = db.Column(db.Integer, primary_key=True)
    idLibro = db.Column(db.Integer, db.ForeignKey('libro.idLibro'))
    idPrestamo = db.Column(db.Integer,db.ForeignKey('prestamo.idPrestamo'))
    cantidadDetalleP = db.Column(db.Integer)
    fechaEntregaDetalleP = db.Column(db.DateTime)
   

    def __init__(self, idLibro, idPrestamo, cantidadDetalleP, fechaEntregaDetalleP):
        self.idLibro = idLibro  
        self.idPrestamo = idPrestamo  
        self.cantidadDetalleP = cantidadDetalleP  
        self.fechaEntregaDetalleP = fechaEntregaDetalleP  


class DetallePrestamoSchema(ma.Schema):
    class Meta:
        fields = ('idDetalleP', 'idLibro', 'idPrestamo', 'cantidadDetalleP', 'fechaEntregaDetalleP')
