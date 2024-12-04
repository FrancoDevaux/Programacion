from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoPrestamo
from modelos.repositorios.repositorios import obtenerRepoLibro
from modelos.repositorios.repositorios import obtenerRepoSocio
from modelos.entidades.prestamo import Prestamo

repositorio_prestamo = obtenerRepoPrestamo()
repositorio_libro = obtenerRepoLibro()
repositorio_socio = obtenerRepoSocio()


bp_prestamos = Blueprint("bp_prestamos", __name__)

@bp_prestamos.post("/prestamos")
def agregarPrestamo():
    if request.is_json:
        datos = request.get_json()
        if repositorio_socio.existeSocio(datos["id_socio"]) and repositorio_libro.existeLibro(datos["id_libro"]):
            prestamo = Prestamo(datos["id_socio"], datos["id_libro"])
            repositorio_prestamo.agregarPrestamo(prestamo)
            return jsonify({"mensaje": "Prestamo agregado"}), 200
        else:
            return jsonify({"mensaje": "Socio o libro no existe"}), 400
    else:
        return jsonify({"mensaje": "Formato incorrecto"}), 400