storage_get_count
#!/usr.bin.python3
"""create a Blueprint"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *

#!/usr/bin/python3
"""Creating views blueprints"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
master
