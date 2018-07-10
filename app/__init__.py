from flask import Flask
from flask_httpauth import HTTPBasicAuth
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection

app = Flask(__name__)
auth = HTTPBasicAuth()

cassandra_auth_provider = PlainTextAuthProvider(username='mamot', password='9L1reyib')
cluster = Cluster(['128.199.145.148'], auth_provider = cassandra_auth_provider)
session = cluster.connect()
session.set_keyspace('kaspa')

connection.register_connection('clusterKaspa', session=session)

from app import routes