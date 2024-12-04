from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoAlumnos
from modelos.entidades.alumno import Alumno

repositorio_alumnos = obtenerRepoAlumnos()


#Crear un BluePrint para la ruta alumnos
bp_alumnos = Blueprint("bp_alumnos", __name__)

#Crear las rutas
@bp_alumnos.route("/alumnos", methods=["GET"]) 
def obtener_todos_los_alumnos():
    lista_dicc = []
    for alumno in repositorio_alumnos.obtenerTodos():
        lista_dicc.append(alumno.toDiccionario())
    return jsonify(lista_dicc), 200  #codigo de respuesta HTTP 200 OK


@bp_alumnos.route("/alumnos/<int:legajo>", methods=["GET"])
def obtener_alumno_por_legajo(legajo):
    alumno_encontrado = repositorio_alumnos.obtenerPorLegajo(legajo)
    if alumno_encontrado is not None:
        return jsonify(alumno_encontrado.toDiccionario()), 200
    else:
        return jsonify({"mensaje": "No se econtro el legajo ingresado"}), 404 #codigo de respuesta HTTP 404 Not Found


@bp_alumnos.route("/alumnos", methods=["POST"])
def agregar_alumno():
    if request.is_json:
        datos = request.get_json()
        alumno = Alumno.fromDiccionario(datos)
        if not repositorio_alumnos.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            if repositorio_alumnos.agregar(alumno):
                return jsonify({"mensaje": "Alumno agregado", "alumno":datos}), 201
            else:
                return jsonify({"mensaje": "Error al agregar alumno"}), 400
        else:
            return jsonify({"mensaje": "Ya existe un alumno con ese legajo"}), 400
    else:
        return jsonify({"mensaje": "El contenido del request no es JSON"}), 400

def agergar_alumno_desde_diccionario(dicc:dict):
    if request.is_json:
        datos = request.get_json()
        if not repositorio_alumnos.existeAlumnoConLegajo(dicc["legajo"]):
            if repositorio_alumnos.agregarDesdeDiccionario(datos):
                return jsonify({"mensaje": "Alumno agregado", "alumno":dicc}), 201
            else:
                return jsonify({"mensaje": "Error al agregar alumno"}), 400
        else:
            return jsonify({"mensaje": "Ya existe un alumno con ese legajo"}), 400
    else:
        return jsonify({"mensaje": "El contenido del request no es JSON"}), 400
     
    