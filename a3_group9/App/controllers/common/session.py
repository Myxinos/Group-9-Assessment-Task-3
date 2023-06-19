import json

from flask import Blueprint, session
from App.models.models import User

common_session = Blueprint('common_session', __name__, )


@common_session.route('common/session.html', methods=['GET'])
def getsession():
    status = 0
    msg = "get error"
    user_info = session.get('user_info')
    if user_info is None:
        msg += "，username does not exist"
    else:
        user_info = User.query.filter(User.username == user_info["username"]).first()
        status = 1
        msg = user_info.username
    ret = {"status": status, "msg": msg}
    return json.dumps(ret)
