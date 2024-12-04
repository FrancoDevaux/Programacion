from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorios import obtenerRepoTemaAlumnos

repositorio_temasAlumnos = obtenerRepoTemaAlumnos()
bp_temasAlumnos = Blueprint('bp_temasAlumnos', __name__)

@bp_temasAlumnos.route('/examenesDisponibles/<int:IDinterno>', methods=['GET'])
def obtener_examenes_disponibles(IDinterno):
    temaAlumno = repositorio_temasAlumnos.obtenerPorAlumnoID(IDinterno)
    if temaAlumno is None:
        return jsonify({"mensaje": "No se encontró el alumno"}), 404
    return jsonify(temaAlumno.toDiccionario()), 200



