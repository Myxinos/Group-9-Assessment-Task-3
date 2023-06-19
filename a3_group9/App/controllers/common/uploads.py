import json
import time
import os
import platform

from flask import Blueprint, request
from werkzeug.utils import secure_filename

common_uploads = Blueprint('common_uploads', __name__, )


@common_uploads.route('/uploads/index.html', methods=['GET', 'POST'])
def index():
    path = request.args.get('path')
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_date = str(time.time())
        runtime_dir = os.path.dirname(os.path.abspath(__file__))
        sys = platform.system()
        if sys == "Windows":
            base_dir = runtime_dir.split('\App')
        else:
            base_dir = runtime_dir.split('/App')
        static_dir = os.path.join(base_dir[0], 'static/uploads/' + path)
        f.save(os.path.join(static_dir, file_date + filename))
        ret = {"state": 1, "path": file_date + filename, "msg": "upload success"}
        return json.dumps(ret)
