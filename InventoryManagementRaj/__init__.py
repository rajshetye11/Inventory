from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '323b22caac41acbf'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

from InventoryManagementRaj import routes

db.create_all()
db.session.commit()


app.run(debug=True)
app.run(host='0.0.0.0', port=8080)
