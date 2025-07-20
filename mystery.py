from flask import Blueprint, jsonify
import random
from utils.mystery_items import mystery_items

mystery_bp = Blueprint('mystery', __name__)

@mystery_bp.route('/mystery', methods=['GET'])
def mystery_box():
    item = random.choice(mystery_items)
    return jsonify(item)
