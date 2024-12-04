from flask import Flask
from rutas.ruta_polizas import bp_poliza

app = Flask(__name__)

app.register_blueprint(bp_poliza)

if __name__ == "__main__":
    app.run(debug=True)
    



