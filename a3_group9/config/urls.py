from App.controllers.index.index import index_index
from App.controllers.index.login import index_login
from App.controllers.index.register import index_register
from App.controllers.index.event import index_event
from App.controllers.index.history import index_history
from App.controllers.index.category import index_category

from App.controllers.common.session import common_session
from App.controllers.common.uploads import common_uploads


def register_blueprints(app):
    app.register_blueprint(index_index, url_prefix='/index')
    app.register_blueprint(index_login, url_prefix='/index')
    app.register_blueprint(index_register, url_prefix='/index')
    app.register_blueprint(index_event, url_prefix='/index')
    app.register_blueprint(index_history, url_prefix='/index')
    app.register_blueprint(index_category, url_prefix='/index')
    # app.register_blueprint(common_session, url_prefix='/index')
    # app.register_blueprint(common_uploads, url_prefix='/common')
    
