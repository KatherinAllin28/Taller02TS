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
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229163-d6b7ba8d-5234-4188-9d7e-a8c586fa3e61.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MDY5OTksIm5iZiI6MTc0NjQwNjY5OSwicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNjMtZDZiN2JhOGQtNTIzNC00MTg4LTlkN2UtYThjNTg2ZmEzZTYxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAwNTgxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU4NTliYjk1NmZmZDJmOGQ3YzlmOWQzNzQ2Nzk3ZGE3ZDYzN2Q5NGE5NjBiMGM0M2RjYTczZTVkNmY3MDk1YjEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.nAJP51FWuKrxRis8nQS-k82nZh2RsldMBKXeyHj-uDs",
        "frase": "Parce, la vida es como una arepa, depende de con qué la rellenes."
    },
    {
        "id": 2,
        "nombre": "Juancharizard",
        "altura": "1.7m",
        "habilidad": "Fuego paisa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229158-d3d13cf8-ce3f-4823-a176-c6ef5f5680b9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MDcwODcsIm5iZiI6MTc0NjQwNjc4NywicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNTgtZDNkMTNjZjgtY2UzZi00ODIzLWExNzYtYzZlZjVmNTY4MGI5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAwNTk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWFlMWVhY2IwNGUxZThlZThmZDEwYjZmMWZjYzk4MDgzMjlmY2QyZTdmOWY3MzkwMDc1YjE4MzA1MDdiMWFkNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.pEthgvxnqw4HeuWu_Q-N5jRf_62wprXc4BnzRLpveAo",
        "frase": "El que madruga... ve más pokeneas."
    },
    {
        "id": 3,
        "nombre": "Neatle",
        "altura": "1.5m",
        "habilidad": "Hierba de montebello",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229156-a8ab3cd8-2c7c-4628-8b9a-b60ec0d7e7a3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MDcwODcsIm5iZiI6MTc0NjQwNjc4NywicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNTYtYThhYjNjZDgtMmM3Yy00NjI4LThiOWEtYjYwZWMwZDdlN2EzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAwNTk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU3NThkODY2MDJjZTgwYjRhY2MxZjYxYTE0NmQ3NGY3ODAxNjFkNjFkMDQxNjkyYjM3MzRiM2RjNDQzMWRlNzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.8mT-u_s8kthlKqPQwU6ul15g52BaP_6qeVasaPgG6ps",
        "frase": "No hay batalla que un buen guaro no aliviane."
    },
     {
        "id": 4,
        "nombre": "Verdolaga",
        "altura": "1.8m",
        "habilidad": "Euforia alcólica",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229156-a8ab3cd8-2c7c-4628-8b9a-b60ec0d7e7a3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MDcwODcsIm5iZiI6MTc0NjQwNjc4NywicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNTYtYThhYjNjZDgtMmM3Yy00NjI4LThiOWEtYjYwZWMwZDdlN2EzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAwNTk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU3NThkODY2MDJjZTgwYjRhY2MxZjYxYTE0NmQ3NGY3ODAxNjFkNjFkMDQxNjkyYjM3MzRiM2RjNDQzMWRlNzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.8mT-u_s8kthlKqPQwU6ul15g52BaP_6qeVasaPgG6ps",
        "frase": "Firme con los firmes y lo que no es verde no sirve."
    },
     {
        "id": 5,
        "nombre": "Machopaisa",
        "altura": "1.2m",
        "habilidad": "Puño de arepa",
        "imagen": "https://example.com/machopaisa.png",
        "frase": "El que no lucha por lo suyo, no merece un sancocho."
    },
     {
        "id": 6,
        "nombre": "Reggaetompoleon",
        "altura": "1.9m",
        "habilidad": "Flow explosivo",
        "imagen": "https://example.com/reggaetompoleon.png",
        "frase": "El ritmo mueve montañas, parcero."
    },
     {
        "id": 7,
        "nombre": "Gengarrote",
        "altura": "1.4m",
        "habilidad": "Risa malvada de fonda",
        "imagen": "https://example.com/gengarrote.png",
        "frase": "Si te asustás, es porque no sos de aquí."
    },
     {
        "id": 8,
        "nombre": "Snorlaxito",
        "altura": "2.1m",
        "habilidad": "Sueño empapado de bandeja paisa",
        "imagen": "https://example.com/snorlaxito.png",
        "frase": "Dormir después del almuerzo es sagrado, mi llave."
    },
     {
        "id": 9,
        "nombre": "Jiggleneaza",
        "altura": "0.9m",
        "habilidad": "Canto vallenato paisa",
        "imagen": "https://example.com/jiggleneaza.png",
        "frase": "Con una canción se enamora hasta el más serio."
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
