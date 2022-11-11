from flask import Flask
#se importa la libreria flahs

app= Flask(__name__)

@app.route('/')
def index():
    return "servidor en ejecucion"

# Configurar variables de entorno
    # export FLASK_APP=init 
    # indica el archivo inicio

    # export FLASK_ENV=development 
    # indica el ambiente de desarrollo

# Iniciar proyecto
# flask run

token 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
