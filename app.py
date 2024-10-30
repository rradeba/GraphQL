from flask import Flask
from flask_graphql import GraphQLView
import graphene
from schemas.genreSchema import Query, Mutation  
from models.model import db  
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'mysql+pymysql://root:843RnR$$@localhost:3306/bakery_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)  
)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

