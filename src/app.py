from connection import request, db, jsonify, app, and_
from autor import Autor, AutorSchema
from libro import Libro, LibroSchema
from prestamo import Prestamo, PrestamoSchema
from detallePrestamo import DetallePrestamoSchema, DetallePrestamo
from sqlalchemy import desc
from flask_cors import CORS, cross_origin





'''
    Endpoint de autores
'''

autor_schema = AutorSchema()
autores_schema = AutorSchema(many=True)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/autores', methods=['Post'])
def create_autor():
  try:
    nombreAutor = request.json['nombreAutor']
    apellidoAutor = request.json['apellidoAutor']

    autores = Autor.query.order_by(desc(Autor.idAutor)).all()
    resultAutores = autores_schema.dump(autores)

    for a in resultAutores:
      print(a)

    numeroPrestamo = (int(resultAutores[0]['idAutor']) +1) * 50


    new_autor= Autor(numeroPrestamo, nombreAutor, apellidoAutor)
    db.session.add(new_autor)
    db.session.commit()
    return autor_schema.jsonify(new_autor)
  
  except:
    return 'Ocurrio un error'



@app.route('/autores', methods=['GET'])
def get_autors():
  try:
    all_autors = Autor.query.all()
    result = autores_schema.dump(all_autors)
    return jsonify(result)
  except Exception as e:
    return 'Error autores ' 

@app.route('/autores/<id>', methods=['GET'])
def get_autor(id):
  autor = Autor.query.get(id)
  return autor_schema.jsonify(autor)

@app.route('/autoresByCoincidence/<coincidence>', methods=['GET'])
def get_autoresByCoincidence(coincidence):
  autores = Autor.query.filter(Autor.codigoAutor.like("%{0}%".format(coincidence)) | Autor.nombreAutor.like("%{0}%".format(coincidence)) | Autor.apellidoAutor.like("%{0}%".format(coincidence)))
  return autores_schema.jsonify(autores)

@app.route('/autores/<idAutor>', methods=['PUT'])
def update_autor(idAutor):
  autor = Autor.query.get(idAutor)
  codigoAutor = request.json['codigoAutor']
  nombreAutor = request.json['nombreAutor']
  apellidoAutor = request.json['apellidoAutor']

  autor.codigoAutor = codigoAutor
  autor.nombreAutor = nombreAutor
  autor.apellidoAutor = apellidoAutor

  db.session.commit()

  return autor_schema.jsonify(autor)

@app.route('/autores/<idAutor>', methods=['DELETE'])
def delete_autor(idAutor):
  autor = Autor.query.get(idAutor)
  db.session.delete(autor)
  db.session.commit()
  return autor_schema.jsonify(autor)



'''
    Endpoint de libros
'''


libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)


@app.route('/libro', methods=['Post'])
def create_libro():
  idAutor = request.json['idAutor']
  ISBNLibro = request.json['ISBNLibro']
  tituloLibro = request.json['tituloLibro']
  valorPrestamoLibro = request.json['valorPrestamoLibro']
  print(Autor.query.get(idAutor))

  if Autor.query.get(idAutor):
    new_libro= Libro( idAutor, ISBNLibro, tituloLibro, valorPrestamoLibro)
    db.session.add(new_libro)
    db.session.commit()
    return libro_schema.jsonify(new_libro)

  else:
    return jsonify('No se pudo insertar')

detallesPrestamo_schema = DetallePrestamoSchema(many=True)  


@app.route('/libro', methods=['GET'])
def get_libros():
  all_libros = Libro.query.all()
  result = libros_schema.dump(all_libros)
  return jsonify(result)

@app.route('/detallesTotal', methods=['GET'])
def get_detalleTotal():
  all_detalles = DetallePrestamo.query.all()
  result = detallesPrestamo_schema.dump(all_detalles)
  return jsonify(result)


@app.route('/cantidadLibroPorDia/<string:inicio>/<string:final>', methods=['GET'])
def get_cantidadLibroPorDia(inicio: str, final: str):
  #inicio = request.json['fechaInicio']
  #final = request.json['fechaFinal']
  detalles = DetallePrestamo.query.filter(and_(DetallePrestamo.fechaEntregaDetalleP <= final, DetallePrestamo.fechaEntregaDetalleP >= inicio))
 
  result = detallesPrestamo_schema.dump(detalles)
  tmpFecha = ""
  count = 0
  '''
  data = {}
  for d in result:
    if not d['fechaEntregaDetalleP'] in data.keys():
    
      data.update({d['fechaEntregaDetalleP']: 0})
    data[d['fechaEntregaDetalleP']] += int(d['cantidadDetalleP'])
  '''
  
  data = {}
  for d in result:
    if not d['fechaEntregaDetalleP'] in data.keys():
    
      data.update({d['fechaEntregaDetalleP']: 0})
    data[d['fechaEntregaDetalleP']] += int(d['cantidadDetalleP'])
  
  dataFinal = []
  for key, value in data.items():
    dataFinal.append({
      'date': key,
      'cantidad': value
    })
  return jsonify(dataFinal)


@app.route('/libro/<id>', methods=['GET'])
def get_libro(id):
  libro = Libro.query.get(id)
  return libro_schema.jsonify(libro)

@app.route('/librosByCoincidence/<coincidence>', methods=['GET'])
def get_librosByCoincidence(coincidence):
  libros = Libro.query.filter(Libro.tituloLibro.like("%{0}%".format(coincidence)) | Libro.ISBNLibro.like("%{0}%".format(coincidence)))
  return libros_schema.jsonify(libros)

@app.route('/libro/<idLibro>', methods=['PUT'])
def update_libro(idLibro):
  libro = Libro.query.get(idLibro)
  idAutor = request.json['idAutor']
  autor = Autor.query.get(idAutor)
  ISBNLibro = request.json['ISBNLibro']
  tituloLibro = request.json['tituloLibro']
  valorPrestamoLibro = request.json['valorPrestamoLibro']

  if autor:
    libro.codigoLibro = idAutor
    libro.idAutor = idAutor
    libro.ISBNLibro = ISBNLibro
    libro.tituloLibro = tituloLibro
    libro.valorPrestamoLibro = valorPrestamoLibro
    db.session.commit()
    return libro_schema.jsonify(libro)
  else:
    return 'No se pudo actualizar'

@app.route('/libro/<idLibro>', methods=['DELETE'])
def delete_libro(idLibro):
  libro = Libro.query.get(idLibro)
  db.session.delete(libro)
  db.session.commit()
  return libro_schema.jsonify(libro)


'''
    Endpoints de Prestamo
'''

# Cabecera prestamo
# detalle con id de cabecera

prestamo_schema = PrestamoSchema()
prestamos_schema = PrestamoSchema(many=True)




@app.route('/prestamo', methods=['Post'])
def create_prestamo():
  fechaPrestamo = request.json['fechaPrestamo']
  descripcionPrestamo = request.json['descripcionPrestamo']
  detallesPrestamo = request.json['detallesPrestamo']

  prestamos = Prestamo.query.order_by(desc(Prestamo.idPrestamo)).all()
  resultPrestamos = prestamos_schema.dump(prestamos)
  for a in resultPrestamos:
    print(a)

  numeroPrestamo = (int(resultPrestamos[0]['idPrestamo']) +1) * 50
  new_prestamo= Prestamo( numeroPrestamo, fechaPrestamo, descripcionPrestamo)
  
  try:
    db.session.add(new_prestamo)
    db.session.flush()

    if detallesPrestamo:
      for detalle in detallesPrestamo:
        new_detalle = DetallePrestamo(detalle['idLibro'],new_prestamo.idPrestamo,detalle['cantidadDetalleP'],detalle['fechaEntregaDetalleP'])
        print(new_detalle.idPrestamo)
        db.session.add(new_detalle)

        if  not Libro.query.get(new_detalle.idLibro):
          return 'Libro no existe.'
    db.session.commit()
    return jsonify('Ingresado correctamente')

  except Exception as e:
    return 'No se pudo insertar '  + str(e)


@app.route('/prestamo/<id>', methods=['PUT'])
def update_prestamo(id):
  prestamo =Prestamo.query.get(id)
  fechaPrestamo = request.json['fechaPrestamo']
  descripcionPrestamo = request.json['descripcionPrestamo']
  detallesPrestamoNew = request.json['detallesPrestamo']

  prestamo.fechaPrestamo = fechaPrestamo
  prestamo.descripcionPrestamo = descripcionPrestamo

  detallesPrestamo = DetallePrestamo.query.filter_by(idPrestamo = id)
  #db.session.delete(prestamo)
  for detalle in detallesPrestamo:
    db.session.delete(detalle)
  for detalle in detallesPrestamoNew:
    print(detalle)
    d =  DetallePrestamo(detalle['idLibro'],prestamo.idPrestamo,detalle['cantidadDetalleP'],detalle['fechaEntregaDetalleP'])
    db.session.add(d)

  db.session.commit()
  # for detalle in detallesPrestamo:
  #   deleteDetalle(detalle)
  #   createDetalle(detalle)

  #db.session.commit()
  return prestamo_schema.jsonify(prestamo)

def deleteDetalle(idDetalleP):
  detalleTmp = DetallePrestamo.query.filter_by(idDetalleP = idDetalleP)
  print(detalleTmp)
  db.session.delete(detallePrestamo_schema.jsonify(detalleTmp))
  #db.session.commit()
  return detallePrestamo_schema.jsonify(d)

def createDetalle(detalle):
  try:
    db.session.add(detalle)
    #db.session.commit()
    return detallePrestamo_schema.jsonify(detalle)
  
  except:
    return jsonify('Ocurrio un error')


 

  '''
  try:

    if detallesPrestamo:
      for detalle in detallesPrestamo:
        new_detalle = DetallePrestamo(detalle['idLibro'],new_prestamo.idPrestamo,detalle['cantidadDetalleP'],detalle['fechaEntregaDetalleP'])
        print(new_detalle.idPrestamo)
        db.session.add(new_detalle)

        if  not Libro.query.get(new_detalle.idLibro):
          return 'Prestamo no existe.'
    db.session.commit()
    return 'Inserto correctamente'
  
  except Exception as e:
    return 'No se pudo insertar '  + str(e)
'''
@app.route('/prestamo', methods=['GET'])
def get_prestamo():
  all_prestamo = Prestamo.query.all()
  result = prestamos_schema.dump(all_prestamo)
  return jsonify(result)

detallePrestamo_schema =DetallePrestamoSchema()
detallesPrestamo_schema =DetallePrestamoSchema(many=True)


@app.route('/prestamo/<id>', methods=['GET'])
def get_prestamoById(id):
  p = Prestamo.query.get(id)
  result = prestamo_schema.dump(p)
  return jsonify(result)

@app.route('/prestamosByCoincidence/<coincidence>', methods=['GET'])
def get_prestamoByCoincidence(coincidence):
  prestamos = Prestamo.query.filter(Prestamo.fechaPrestamo.like("%{0}%".format(coincidence)) | Prestamo.numeroPrestamo.like("%{0}%".format(coincidence)) | Prestamo.descripcionPrestamo.like("%{0}%".format(coincidence)))
  return prestamos_schema.jsonify(prestamos)


@app.route('/detallesPrestamo', methods=['GET'])
def get_detallesPrestamo():
  all_detallePrestamo = DetallePrestamo.query.all()
  result = detallesPrestamo_schema.dump(all_detallePrestamo)
  return jsonify(result)

@app.route('/detallePrestamo/<id>', methods=['GET'])
def get_detallePrestamo(id):
  detallePrestamo = DetallePrestamo.query.get(id)
  return detallePrestamo_schema.jsonify(detallePrestamo)


@app.route('/detalleDePrestamo/<idPrestamo>', methods=['GET'])
def get_detallePrestamoByPrestamo(idPrestamo):
  detallePrestamo = DetallePrestamo.query.filter_by(idPrestamo = idPrestamo).first()
  return detallePrestamo_schema.jsonify(detallePrestamo)

@app.route('/detallesDePrestamo/<idPrestamo>', methods=['GET'])
def get_detallesPrestamoByPrestamo(idPrestamo):
  detallesPrestamo = DetallePrestamo.query.filter_by(idPrestamo = idPrestamo)
  return detallesPrestamo_schema.jsonify(detallesPrestamo)


@app.route('/prestamo/<idPrestamo>', methods=['DELETE'])
def delete_prestamo(idPrestamo):
  prestamo = Prestamo.query.get(idPrestamo)
  db.session.delete(prestamo)
  detallesPrestamo = DetallePrestamo.query.filter_by(idPrestamo = idPrestamo)
  for detalle in detallesPrestamo:
    db.session.delete(detalle)
  db.session.commit()

  return libro_schema.jsonify(prestamo)

'''
    Endpoints de reporte
'''
# Report segun un dia determinado






@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})




if __name__ == "__main__":
    app.run(debug=True)