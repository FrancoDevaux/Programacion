from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtenerRepoPoliza
from modelos.entidades.polizaInmueble import PolizaInmueble
from modelos.entidades.polizaInmuebleEscolar  import PolizaInmuebleEscolar

repositorio_poliza = obtenerRepoPoliza()

bp_poliza = Blueprint("bp_poliza", __name__)



@bp_poliza.route("/poliza", methods=["GET"])
def obtener_polizas():
    polizas = repositorio_poliza.obtener_polizas()
    for poliza in polizas:
        print(poliza.toDiccionario())
    return jsonify([poliza.toDiccionario() for poliza in polizas]), 200
    #return jsonify([poliza.toDiccionario() for poliza in polizas]), 200

@bp_poliza.route("/poliza/<int:numero>", methods=["GET"])
def obtener_poliza(numero):
    poliza = repositorio_poliza.obtener_poliza(numero)
    if poliza:
        return jsonify(poliza.toDiccionario()), 200
    return jsonify({"mensaje": "Poliza no encontrada"}), 404


@bp_poliza.route("/poliza", methods=["POST"])
def agregar_poliza():
    if request.is_json:
        datos = request.get_json()
        
        if 'numero' not in datos or 'explocion' not in datos or 'incendio' not in datos or 'robo' not in datos:
            return jsonify({"mensaje": "Faltan datos"}), 400
        
        if repositorio_poliza.existeNumero(datos['numero']):
            return jsonify({"mensaje": "Ya existe una poliza con ese numero"}), 400
        
        if 'cantPersonas' in datos:
            if 'montoEquipamiento' not in datos or 'montoInmobiliario' not in datos or 'montoPersona' not in datos:
                return jsonify({"mensaje": "Faltan datos"}), 400
            
            try:
                poliza = PolizaInmuebleEscolar.fromDiccionario(datos)
                repositorio_poliza.agregar_poliza(poliza)
                return jsonify(poliza.toDiccionario()), 201
            except ValueError as e:
                return jsonify({"mensaje": str(e)}), 400
        else:
            try:
                poliza = PolizaInmueble.fromDiccionario(datos)
                repositorio_poliza.agregar_poliza(poliza)
                return jsonify(poliza.toDiccionario()), 201
            except ValueError as e:
                return jsonify({"mensaje": str(e)}), 400
            

@bp_poliza.route("/poliza/<int:numero>", methods=["DELETE"])
def eliminar_poliza(numero):
    if repositorio_poliza.existeNumero(numero):
        if repositorio_poliza.eliminar_poliza(numero):
            return jsonify({"mensaje": "Poliza eliminada"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar la poliza"}), 500
    return jsonify({"mensaje": "Poliza no encontrada"}), 404
           

@bp_poliza.route("/poliza/<int:numero>", methods=["PUT"])
def modificar_poliza(numero):
    if request.is_json:
        datos = request.get_json()
        
        if 'explocion' in datos or 'incendio' in datos or 'robo' in datos:
            return jsonify({"mensaje": "No se puede modificar la cobertura"}), 400
        
        if 'numero' in datos:
            return jsonify({"mensaje": "No se puede modificar el numero"}), 400
        
        if 'cantPersonas' in datos:
            if 'montoEquipamiento' not in datos or 'montoInmobiliario' not in datos or 'montoPersona' not in datos:
                return jsonify({"mensaje": "Faltan datos"}), 400
            
            if repositorio_poliza.existeNumero(numero):
                try:
                    poliza = PolizaInmuebleEscolar.fromDiccionario(datos)
                    repositorio_poliza.modificar_poliza(poliza)
                    return jsonify(poliza.toDiccionario())
                except ValueError as e:
                    return jsonify({"mensaje": str(e)}), 400
            else:
                return jsonify({"mensaje": "Poliza no encontrada"}), 404
        else:
            if repositorio_poliza.existeNumero(numero):
                try:
                    poliza = PolizaInmueble.fromDiccionario(datos)
                    repositorio_poliza.modificar_poliza(poliza)
                    return jsonify(poliza.toDiccionario())
                except ValueError as e:
                    return jsonify({"mensaje": str(e)}), 400
            else:
                return jsonify({"mensaje": "Poliza no encontrada"}), 404
    return jsonify({"mensaje": "Datos no validos"}), 400