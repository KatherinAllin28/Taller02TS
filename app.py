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
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229156-a8ab3cd8-2c7c-4628-8b9a-b60ec0d7e7a3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MDk0NzcsIm5iZiI6MTc0NjQwOTE3NywicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNTYtYThhYjNjZDgtMmM3Yy00NjI4LThiOWEtYjYwZWMwZDdlN2EzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAxMzkzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE3NTUxYTg2NjNkNzA4NDI4MzdkNmUxZGYyMTMwZjBmNTY2ZjkxNTY3OTRhZmJmYzI2MmU1YzFlZTMzZTMyOTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.n5zFoTeXQRxT-qQldFJmB88gg5G77AcJ7Sd1iLsPnPk",
        "frase": "Firme con los firmes y lo que no es verde no sirve."
    },
     {
        "id": 5,
        "nombre": "Machopaisa",
        "altura": "1.2m",
        "habilidad": "Puño de arepa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440234763-67e38d53-3e0d-4d53-8507-7ae8714f7ff0.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTA3ODcsIm5iZiI6MTc0NjQxMDQ4NywicGF0aCI6Ii82ODkyODQyMy80NDAyMzQ3NjMtNjdlMzhkNTMtM2UwZC00ZDUzLTg1MDctN2FlODcxNGY3ZmYwLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMDEyN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWIxZTgxZTNjZDA5MTAzOGNjMzcxY2E2NzQyMjgxMDMxY2NjMmYxY2VkYzY5MDg2MzQ5NDM4ZDExN2RjOTYxZmImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.KNx3eWwGmUx3IMmS1gBweqJJ96igP2pzPTEf55sLtIY",
        "frase": "El que no lucha por lo suyo, no merece un sancocho."
    },
     {
        "id": 6,
        "nombre": "Reggaetompoleon",
        "altura": "1.9m",
        "habilidad": "Flow explosivo",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440234470-ba0b579f-d725-4e61-9439-ebd9810ff7dd.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTA1OTEsIm5iZiI6MTc0NjQxMDI5MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMzQ0NzAtYmEwYjU3OWYtZDcyNS00ZTYxLTk0MzktZWJkOTgxMGZmN2RkLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAxNTgxMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhMmY1ZTc5NzUyYmY5Y2FlZjFhYWNkODMzZDk0OGY5ZjM1YWNlMTQ5ZjNmZjlmYzYxM2RjMjRkMjA2N2I5YzMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.-UILX3xFAkMqLMzH_SqI_1xNqHx-xR7glNiS8NU9OKo",
        "frase": "El ritmo mueve montañas, parcero."
    },
     {
        "id": 7,
        "nombre": "Gengarrote",
        "altura": "1.4m",
        "habilidad": "Risa malvada de fonda",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440235269-73ca3bb9-a68e-4350-94c9-9591a494cef8.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTExMjcsIm5iZiI6MTc0NjQxMDgyNywicGF0aCI6Ii82ODkyODQyMy80NDAyMzUyNjktNzNjYTNiYjktYTY4ZS00MzUwLTk0YzktOTU5MWE0OTRjZWY4LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMDcwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU4OGI5NDVmOTc2MWMyZWUyZDJlZWNlZTQwNjgwOGRmMTY0NzM5MTQ5MmJhMGY2Y2RmMGFlZWFjZDljMTE1ZWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.a-EskROOQiiLNBtEiUSMGp2hMsKNUAJtjGcP6uLgwPE",
        "frase": "Si te asustás, es porque no sos de aquí."
    },
     {
        "id": 8,
        "nombre": "Snorlaxito",
        "altura": "2.1m",
        "habilidad": "Sueño empapado de bandeja paisa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440235007-48849570-2b73-459a-b1b7-f5a217a663c2.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTA5NzYsIm5iZiI6MTc0NjQxMDY3NiwicGF0aCI6Ii82ODkyODQyMy80NDAyMzUwMDctNDg4NDk1NzAtMmI3My00NTlhLWIxYjctZjVhMjE3YTY2M2MyLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMDQzNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMzNzMwMjk5MGM1MTE4MjQ0NmY0MWJkZjMwZWI2M2M1NDM5ODQ1MTE1NjE1NWJjOGUzMDk2NmI2N2ZhMzM2OWQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.MpqDHSxIM_NXATHruMSUPIJrUpw42jVi7Osexv23ZSs",
        "frase": "Dormir después del almuerzo es sagrado, mi llave."
    },
     {
        "id": 9,
        "nombre": "Jiggleneaza",
        "altura": "0.9m",
        "habilidad": "Canto vallenato paisa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440234010-4ec3f656-bfd6-4c82-a5ea-6c4d7f3d49f7.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTAyOTgsIm5iZiI6MTc0NjQwOTk5OCwicGF0aCI6Ii82ODkyODQyMy80NDAyMzQwMTAtNGVjM2Y2NTYtYmZkNi00YzgyLWE1ZWEtNmM0ZDdmM2Q0OWY3LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAxNTMxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAzYzNjNjc4NTQzYTY4NWI4NTgwNDBiNTRlZDdkOGZmZGNmMjIxMWJkYTc3OTdmNDFhNmMyMmI3MGE0YmViOWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.fJLO25wWMj_NSxx7nIkJGFuQ3J-MyKoMaQs5zGZ28yQ",
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
