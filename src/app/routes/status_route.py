import json

from flask import Blueprint, Response
from flask_api import status as http_status

status = Blueprint('status', __name__)


@status.route('/', methods=['GET'])
def get_status():

    status_body = {
        'status': 'running',
        'service': 'dockerized-api',
        'version': '1.0.0'
    }

    return Response(
        json.dumps(status_body),
        status=http_status.HTTP_200_OK,
        mimetype='application/json'
    )
