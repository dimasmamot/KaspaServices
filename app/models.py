from cassandra.cqlengine import columns, models, connection
from cassandra.cqlengine.models import Model
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context

connection.set_default_connection('clusterKaspa')
models.DEFAULT_KEYSPACE = 'kaspa'

class User(Model):
    username = columns.Text(primary_key=True)
    first_name = columns.Text()
    last_name = columns.Text()
    email = columns.Text()
    password_hash = columns.Text()
    group = columns.Text(default="client")
    company = columns.Text()
    time_joined = columns.DateTime(default=datetime.now())

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    
    def set_admin(self):
        self.group = "admin"