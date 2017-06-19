# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""retrieve people """

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import opentracing
import logging
import time
from jaeger_client import Config
from flask_opentracing import FlaskTracer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/velocity2017'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

config = Config(
    config={ # usually read from some yaml config
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
    },
    service_name='people-catalog-python',
)
opentracing_tracer = config.initialize_tracer()
tracer = FlaskTracer(opentracing_tracer, True, app)

class Person(db.Model):
    """ person model """
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    occupation = db.Column(db.String(255))

class PersonSchema(ma.Schema):
    """person schema """
    class Meta(object):
        """ meta information for the person schema """
        fields = ('id', 'first_name', 'last_name', 'occupation')

PERSON_SCHEMA = PersonSchema()
PEOPLE_SCHEMA = PersonSchema(many=True)

@app.route("/people")
def people_handler():
    """ retrieves all people """

    with opentracing.tracer.start_span('TestSpan') as span:
        span.log_event('test message', payload={'life': 42})

        per_page_str = request.args.get('per_page')
        if per_page_str is None:
            per_page_str = '50'
        page_str = request.args.get('page')
        if page_str is None:
            page_str = '1'

        per_page = int(per_page_str)
        page = int(page_str)

        offset = (page-1) * per_page

        people = Person.query.limit(per_page).offset(offset).all()
        return PEOPLE_SCHEMA.jsonify(people, many=True)

@app.route("/people/<person_id>")
def person_handler(person_id):
    """ retrieves a person by id """
    person = Person.query.get(person_id)
    return PERSON_SCHEMA.jsonify(person)

if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)


    app.run()

    time.sleep(2)
    opentracing_tracer.close()
