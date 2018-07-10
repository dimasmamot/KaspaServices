import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get['SECRET_KEY'] or 'i-ll-be-damned-for-sure-if-this-is-weak'
    CASSANDRA_USERNAME = os.environ.get['CASSANDRA_USERNAME']
    CASSANDRA_PASSWORD = os.environ.get['CASSANDRA_PASSWORD']
    CASSANDRA_CLUSTER_HOST = os.environ.get['CASSANDRA_CLUSTER_HOST']