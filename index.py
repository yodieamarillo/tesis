from flask import Flask, render_template, request, make_response    
import uuid
from flask_socketio import SocketIO, emit
import random



app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bienvenida', methods=['POST','GET'])
def bienvenida():   
    return render_template('bienvenida.html')

@app.route('/instrucciones', methods=['POST','GET'])
def asignacion():   
    return render_template('instrucciones.html')

@app.route('/reglas')
def reglas():
    return render_template('reglas.html')

@app.route('/juego')
def id():    
    player_id= str(uuid.uuid4())
    return render_template('juego.html', player_id=player_id)

socketio = SocketIO(app)
### empezamos el código del juego
cards = {}  # Diccionario para almacenar las cartas de los jugadores




############
if __name__=="__main__":
    socketio.run(app, debug=True)

