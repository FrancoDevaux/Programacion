from flask import Flask
from rutas.rutas_alumnos import bp_alumnos



app = Flask(__name__)

app.register_blueprint(bp_alumnos)

if __name__ == "__main__":
    app.run(debug=True) 
