from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoLibro
from modelos.entidades.libro import Libro



repositorio_libro = obtenerRepoLibro()

bp_libros = Blueprint("bp_libros", __name__)

#Ruta para obtener todos los libros
@bp_libros.route("/libros", methods=["GET"])
def obetenerLibros():
    return jsonify([libro.toDiccionario() for libro in repositorio_libro.obtenerTodos()])


# Ruta para buscar un libro en particular por ISBN (GET)
@bp_libros.route("/libros/<ISBN>", methods=["GET"])
def obtenerLibro(ISBN):
    libro = repositorio_libro.obtenerPorISBN(ISBN)
    if libro:
        return jsonify(libro.toDiccionario())
    return jsonify({"mensaje": "Libro no encontrado"}), 404


# Ruta para agregar un libro (POST)
@bp_libros.route("/libros", methods=["POST"])
def agregarLibro():
    if request.is_json:
        datos = request.get_json()

        if "ISBN" not in datos or  "titulo" not in datos or "autor" not in datos or "anio" not in datos or "genero" not in datos:
            return jsonify({"mensaje": "Faltan datos"}), 400
        if repositorio_libro.existeISBN(datos["ISBN"]):
            return jsonify({"mensaje": "El ISBN ya existe"}), 400
        
        try:
            libro = Libro.fromDiccionario(datos)
            repositorio_libro.agregar(libro)
            return jsonify({"mensaje": "Libro agregado"}), 201
        except ValueError as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "El cuerpo de la solicitud no es JSON"}), 400
    

# Ruta modificar los datos de un libro ingresando su ISBN (PUT)
@bp_libros.route("/libros/<ISBN>", methods=["PUT"])
def modificarLibro(ISBN):
    if request.is_json:
        datos = request.get_json()
        try:
            repositorio_libro.modificarPorISBN(ISBN, datos["titulo"], datos["autor"], datos["anio"], datos["genero"])
            return jsonify({"mensaje": "Libro modificado"}), 200
        except ValueError as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "El cuerpo de la solicitud no es JSON"}), 400
    

# Ruta para eliminar un libro por su ISBN (DELETE)
@bp_libros.route("/libros/<ISBN>", methods=["DELETE"])
def eliminarLibro(ISBN):
    libro = repositorio_libro.obtenerLibro(ISBN)
    if libro:
        repositorio_libro.eliminarPorISBN(ISBN)
        return jsonify({"mensaje": "Libro eliminado"}), 200
    return jsonify({"mensaje": "Libro no encontrado"}), 404
