from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoSocio
from modelos.entidades.socio import Socio


repositorio_socio = obtenerRepoSocio()

bp_socios = Blueprint("bp_socios", __name__)


# Ruta consultar todos los socios registrados (GET)
@bp_socios.route("/socios", methods=["GET"])
def obtenerSocios():
    return jsonify([socio.toDiccionario() for socio in repositorio_socio.obtenerTodos()])


# Ruta para buscar un socio en particular por DNI (GET)
@bp_socios.route("/socios/<DNI>", methods=["GET"])
def obtenerSocio(DNI):
    socio = repositorio_socio.obtenerPorDNI(DNI)
    if socio:
        return jsonify(socio.toDiccionario())
    return jsonify({"mensaje": "Socio no encontrado"}), 404


# Ruta para agregar un socio (POST)
@bp_socios.route("/socios", methods=["POST"])
def agregarSocio():
    if request.is_json:
        datos = request.get_json()

        if "DNI" not in datos or  "nombre" not in datos or "apellido" not in datos or "direccion" not in datos or "telefono" not in datos:
            return jsonify({"mensaje": "Faltan datos"}), 400
        if repositorio_socio.existeDNI(datos["DNI"]):
            return jsonify({"mensaje": "El DNI ya existe"}), 400
        
        try:
            socio = Socio.fromDiccionario(datos)
            repositorio_socio.agregar(socio)
            return jsonify({"mensaje": "Socio agregado"}), 201
        except ValueError as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "El cuerpo de la solicitud no es JSON"}), 400
    

# Ruta modificar los datos de un socio ingresando su DNI (PUT)
@bp_socios.route("/socios/<DNI>", methods=["PUT"])
def modificarSocio(DNI):
    if request.is_json:
        datos = request.get_json()
        try:
            repositorio_socio.modificarPorDNI(DNI, datos["nombre"], datos["apellido"], datos["direccion"], datos["telefono"])
            return jsonify({"mensaje": "Socio modificado"}), 200
        except ValueError as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "El cuerpo de la solicitud no es JSON"}), 400
    
# Ruta para eliminar un socio ingresando su DNI (DELETE)
@bp_socios.route("/socios/<DNI>", methods=["DELETE"])
def eliminarSocio(DNI):
    if repositorio_socio.existeDNI(DNI):
        repositorio_socio.eliminarPorDNI(DNI)
        return jsonify({"mensaje": "Socio eliminado"}), 200
    return jsonify({"mensaje": "Socio no encontrado"}), 404