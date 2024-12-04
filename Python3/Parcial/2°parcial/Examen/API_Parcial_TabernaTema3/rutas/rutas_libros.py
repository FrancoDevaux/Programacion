from flask import Blueprint, jsonify, request
from modelos.entidades.libroDigital import LibroDigital
from modelos.entidades.libroFisico import LibroFisico
from modelos.repositorios.repositorios import obtenerRepoLibros

repo_libros = obtenerRepoLibros()

bp_libros = Blueprint('bp_libros', __name__)


@bp_libros.route('/libros', methods=['GET'])
def obtener_libros():
    libros = repo_libros.obtenerLibros()
    lista_libros = []
    for libro in libros:
        lista_libros.append(libro.toDiccionario())
    return jsonify(lista_libros), 200



@bp_libros.route('/libros/<int:ISBN>', methods=['GET'])
def obtener_libro(ISBN):
    libro = repo_libros.obtenerLibroPorISBN(ISBN)
    if libro == None:  
        return jsonify({'mensaje': 'Libro no encontrado'}), 404
    return jsonify(libro.toDiccionario()), 200  #Corregi el codigo de estado de 400 a 200


@bp_libros.route('/libros', methods=['POST'])  
def agregar_libro():
    if request.is_json:
        datos = request.get_json()
        
        if 'ISBN' not in datos or 'titulo' not in datos or 'autor' not in datos or 'editorial' not in datos or 'precio' not in datos or 'stock' not in datos:
            return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400
        
        if repo_libros.existeLibro(datos['ISBN']):
            return jsonify({'mensaje': 'Ya existe un libro con ese ISBN'}), 400
        
        if 'formato' in datos:
            if 'tamanioMB' not in datos or 'proteccionDeCopia' not in datos:
                return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400
            try:
                libro = LibroDigital.fromDiccionario(datos)
                repo_libros.agregarLibro(libro)
                return jsonify({'mensaje': 'Libro agregado'}), 200
            except ValueError as e:
                return jsonify({'mensaje': str(e)}), 400
            
        else:
            if 'alto' not in datos or 'ancho' not in datos or 'grosor' not in datos or 'tapaDura' not in datos or 'peso' not in datos:
                return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400
            try:
                libro = LibroFisico.fromDiccionario(datos)
                repo_libros.agregarLibro(libro)
                return jsonify({'mensaje': 'Libro agregado'}), 200
            except ValueError as e:
                return jsonify({'mensaje': str(e)}), 400
    else:
        return jsonify({'Error': 'El formato no es un json'}), 400
    
            
            
        
@bp_libros.route('/libros/<int:ISBN>', methods=['DELETE'])
def borrar_libro(ISBN):
    if repo_libros.existeLibro(ISBN):
        if repo_libros.eliminarLibro(ISBN):
            return jsonify({'mensaje': 'Libro eliminado'}), 200
        else:
            return jsonify({'mensaje': 'Error al eliminar el libro'}), 500
    else:
        return jsonify({'mensaje': 'Libro no encontrado'}), 404
    



@bp_libros.route('/libros/<int:ISBN>', methods=['PUT'])
def modificar_libro(ISBN):
    if repo_libros.existeLibro(ISBN):
        if request.is_json:
            datos = request.get_json()
            if 'formato' in datos:
                if 'tamanioMB' not in datos or 'proteccionDeCopia' not in datos:
                    return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400
                try:
                    libro = LibroDigital.fromDiccionario(datos)
                    if repo_libros.modificarLibro(ISBN, libro):
                        return jsonify({'mensaje': 'Libro modificado'}), 200
                    else:
                        return jsonify({'mensaje': 'Error al modificar el libro'}), 500
                except ValueError as e:
                    return jsonify({'mensaje': str(e)}), 400
            else:
                if 'alto' not in datos or 'ancho' not in datos or 'grosor' not in datos or 'tapaDura' not in datos or 'peso' not in datos:
                    return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400
                try:
                    libro = LibroFisico.fromDiccionario(datos)
                    if repo_libros.modificarLibro(ISBN, libro):
                        return jsonify({'mensaje': 'Libro modificado'}), 200
                    else:
                        return jsonify({'mensaje': 'Error al modificar el libro'}), 500
                except ValueError as e:
                    return jsonify({'mensaje': str(e)}), 400
        else:
            return jsonify({'mensaje': 'El formato no es un json'}), 400
    else:
        return jsonify({'mensaje': 'Libro no encontrado'}), 404
                    
    
            
        

                



        
        
            
        
        


        

        
        