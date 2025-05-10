from flask import Blueprint, jsonify, render_template
from services.pokenea_service import get_pokenea_json, get_pokenea_html_data

pokenea_bp = Blueprint('pokenea', __name__)

@pokenea_bp.route('/pokenea/json')
def pokenea_json():
    return jsonify(get_pokenea_json())

@pokenea_bp.route('/pokenea/frase')
def pokenea_frase():
    data = get_pokenea_html_data()
    return render_template("pokenea_frase.html", **data)
