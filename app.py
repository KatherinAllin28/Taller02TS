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
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229163-d6b7ba8d-5234-4188-9d7e-a8c586fa3e61.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNjMtZDZiN2JhOGQtNTIzNC00MTg4LTlkN2UtYThjNTg2ZmEzZTYxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWUwNDNjN2U0OWE1NmIyM2ZlYzI1NGEzOWIwNDU5Mjc2MmIyMjMyZjkyNjIyN2FiZjQwNDg4ZmMyMDAyMWQ1MTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.5HIJSGovSjN46awCa5B4U-k5uzoY4eZls4rcpbW_LfY",
        "frase": "Parce, la vida es como una arepa, depende de con qué la rellenes."
    },
    {
        "id": 2,
        "nombre": "Juancharizard",
        "altura": "1.7m",
        "habilidad": "Fuego paisa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229158-d3d13cf8-ce3f-4823-a176-c6ef5f5680b9.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNTgtZDNkMTNjZjgtY2UzZi00ODIzLWExNzYtYzZlZjVmNTY4MGI5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQxZmFiOTNlZmE3NjFiZDM3NTljOTlmZDY4MTJjNDZiZDlmYjY3MWVjY2VjNmQ0NmFlNWNiZjFlYzM4MjY5ZmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.TZD7ezoCN3GdoTpuI8bCllgjrMJqFAkzQ9MOD9T5oqE",
        "frase": "El que madruga...ve más pokeneas."
    },
    {
        "id": 3,
        "nombre": "Neatle",
        "altura": "1.5m",
        "habilidad": "Hierba de montebello",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229156-a8ab3cd8-2c7c-4628-8b9a-b60ec0d7e7a3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMjkxNTYtYThhYjNjZDgtMmM3Yy00NjI4LThiOWEtYjYwZWMwZDdlN2EzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVjNGRiZjFmODNjZDVkNDg0NTE1NWY3ODhmMTFkYjYzN2U0ZDBjZTNmZjcwOGFmOTZkYzUzYjI2N2Q0M2JlYWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.rqM6VKbsmJebIvzsA9-1grIc7RYl09ojROGdW7j52Us",
        "frase": "No hay batalla que un buen guaro no aliviane."
    },
     {
        "id": 4,
        "nombre": "Verdolaga",
        "altura": "1.8m",
        "habilidad": "Euforia alcólica",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440229597-a2137bd3-b642-4ef7-b6c3-d262db48d5c7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMjk1OTctYTIxMzdiZDMtYjY0Mi00ZWY3LWI2YzMtZDI2MmRiNDhkNWM3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQ4ZmM4YjY4OWJiNGVhMjE4N2VlZDU5M2IyNmI3M2RiY2FkZTY4OWJjNGFiMzdiYTM2NDFiNGQ2Njg5ZGRkNzMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.avB95IgIeefGHUAkBSErL3aXIzf51aDPsW9WisG1IPI",
        "frase": "Firme con los firmes y lo que no es verde no sirve."
    },
     {
        "id": 5,
        "nombre": "Machopaisa",
        "altura": "1.2m",
        "habilidad": "Puño de arepa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440234763-67e38d53-3e0d-4d53-8507-7ae8714f7ff0.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMzQ3NjMtNjdlMzhkNTMtM2UwZC00ZDUzLTg1MDctN2FlODcxNGY3ZmYwLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBhMWI1MjE4ZWIxZThjZGQ0ZTY0NWZkZjlkNzM0YTg1ZDBkOWMxYjAzYWVhZmFjNWMwOTQ1YzkxNzYzNjkxODcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.GCL4fheSFrIukiobDIKZKyQE1dED6s6qbe1myqfB6QI",
        "frase": "El que no lucha por lo suyo, no merece un sancocho."
    },
     {
        "id": 6,
        "nombre": "Reggaetompoleon",
        "altura": "1.9m",
        "habilidad": "Flow explosivo",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440234470-ba0b579f-d725-4e61-9439-ebd9810ff7dd.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMzQ0NzAtYmEwYjU3OWYtZDcyNS00ZTYxLTk0MzktZWJkOTgxMGZmN2RkLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWUwMzJhOGJmYTE2ZTcyOTkyMGY2NmQ0N2E3MmJjMWQwNGM1OTA4ZjFiZjFhMjY0NTBlYzIzOThkM2MyMTg1MDQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.IWMQMrFZesXlp2_jZA9P-bm60S2bsR1KqQnwfDaYyxY",
        "frase": "El ritmo mueve montañas, parcero."
    },
     {
        "id": 7,
        "nombre": "Gengarrote",
        "altura": "1.4m",
        "habilidad": "Risa malvada de fonda",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440235269-73ca3bb9-a68e-4350-94c9-9591a494cef8.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMzUyNjktNzNjYTNiYjktYTY4ZS00MzUwLTk0YzktOTU5MWE0OTRjZWY4LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNhOTBjZjNlNjdmMDZhODdkMTgxYmM0YWFlNWRhMzBkNDcwM2E4MjEyMmRmZjc5YzI4YzE4OWYxNDg4YmRjYjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.dNEuyby6etppyTZsifm4UKfiGx3ZQXL7RSKaFmqa8Og",
        "frase": "Si te asustás, es porque no sos de aquí."
    },
     {
        "id": 8,
        "nombre": "Snorlaxito",
        "altura": "2.1m",
        "habilidad": "Sueño empapado de bandeja paisa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440235007-48849570-2b73-459a-b1b7-f5a217a663c2.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMzUwMDctNDg4NDk1NzAtMmI3My00NTlhLWIxYjctZjVhMjE3YTY2M2MyLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQwZGMzMzEzOGYwNmZiOTdkMzA4M2RjMGNjOTIwMTRhNzNhYWQ1ZWZiMzYzNmFlOTk2Y2JiNGJlZTcyZWIzYTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OtvisYz3e9GruKi2lhcnxBMyhHeNQAf-tPkpuBME1l0",
        "frase": "Dormir después del almuerzo es sagrado, mi llave."
    },
     {
        "id": 9,
        "nombre": "Jiggleneaza",
        "altura": "0.9m",
        "habilidad": "Canto vallenato paisa",
        "imagen": "https://private-user-images.githubusercontent.com/68928423/440234010-4ec3f656-bfd6-4c82-a5ea-6c4d7f3d49f7.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDY0MTE1ODEsIm5iZiI6MTc0NjQxMTI4MSwicGF0aCI6Ii82ODkyODQyMy80NDAyMzQwMTAtNGVjM2Y2NTYtYmZkNi00YzgyLWE1ZWEtNmM0ZDdmM2Q0OWY3LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MDUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTA1VDAyMTQ0MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkyNzYwNTFhNGEwNDZjNDA4OTE2ODEwN2RiMDAwYjEwMDJkNmNkYWQyZTY5MGRhNzk1YjYzZTkzZGFhOWQ0MzMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.spU4wanjeullZq7a2oRIhy9YAhz1RE38BFARSBeZ8xs",
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
