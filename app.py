from flask import Flask, jsonify, render_template_string
import random
import socket

app = Flask(__name__)

pokeneas = [
    {
        "id": 1,
        "nombre": "Arepachu",
        "altura": "0.8m",
        "habilidad": "Electroarepa",
        "imagen": "c:\Users\knath\Downloads\ChatGPT Image 4 may 2025, 19_33_16.png",
        "frase": "Parce, la vida es como una arepa, depende de con qué la rellenes."
    },
    {
        "id": 2,
        "nombre": "Juancharizard",
        "altura": "1.7m",
        "habilidad": "Fuego paisa",
        "imagen": "c:\Users\knath\Downloads\ChatGPT Image 4 may 2025, 19_36_49.png",
        "frase": "El que madruga... ve más pokeneas."
    },
    {
        "id": 3,
        "nombre": "Neatle",
        "altura": "0.5m",
        "habilidad": "Hierba de montebello",
        "imagen": "c:\Users\knath\Downloads\ChatGPT Image 4 may 2025, 19_40_30.png",
        "frase": "No hay batalla que un buen guaro no aliviane."
    }
]

# Ruta JSON
@app.route('/pokenea/json')
def pokenea_json():
    elegido = random.choice(pokeneas)
    data = {
        "id": elegido["id"],
        "nombre": elegido["nombre"],
        "altura": elegido["altura"],
        "habilidad": elegido["habilidad"],
        "contenedor_id": socket.gethostname()
    }
    return jsonify(data)

# Ruta HTML
@app.route('/pokenea/frase')
def pokenea_frase():
    elegido = random.choice(pokeneas)
    contenedor_id = socket.gethostname()
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pokenea: {elegido['nombre']}</title>
        <style>
            body {{ font-family: Arial; text-align: center; padding: 50px; }}
            img {{ width: 300px; border-radius: 20px; }}
            .frase {{ font-size: 24px; margin-top: 20px; font-style: italic; }}
            .id {{ margin-top: 30px; font-size: 14px; color: gray; }}
        </style>
    </head>
    <body>
        <h1>{elegido['nombre']}</h1>
        <img src="{elegido['imagen']}" alt="{elegido['nombre']}">
        <div class="frase">"{elegido['frase']}"</div>
        <div class="id">Contenedor ID: {contenedor_id}</div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
