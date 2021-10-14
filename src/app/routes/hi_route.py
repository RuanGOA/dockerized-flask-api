import json

from flask import Blueprint, Response
from flask_api import status as http_status

hi = Blueprint('hi', __name__)


@hi.route('/', methods=['GET'])
def get_hi():
    
    hi_body = {
        'hi': ['Hi', 'Hola', 'Hei', 'Hi']
    }

    return Response(
        json.dumps(hi_body),
        status=http_status.HTTP_200_OK,
        mimetype='application/json'
    )
