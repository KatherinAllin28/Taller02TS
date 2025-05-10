import random
import socket
from data.pokeneas_data import pokeneas

def get_random_pokenea():
    return random.choice(pokeneas)

def get_pokenea_json():
    elegido = get_random_pokenea()
    return {
        "id": elegido["id"],
        "nombre": elegido["nombre"],
        "altura": elegido["altura"],
        "habilidad": elegido["habilidad"],
        "contenedor_id": socket.gethostname()
    }

def get_pokenea_html_data():
    elegido = get_random_pokenea()
    elegido["contenedor_id"] = socket.gethostname()
    return elegido
