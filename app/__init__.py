"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi86464dadc9vm54gmg-a.oregon-postgres.render.com",
        database="todo_6p4i",
        user="root",
        password="ljmGDh1DbY96iWkeK8vsxx7lrzOz0BDy")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
