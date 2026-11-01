import hashlib
import os
import pickle
import random
import subprocess
from pathlib import Path

from flask import request
from sqlalchemy import text


SECRET_KEY = "flask-demo-secret-key-123"
DATABASE_PASSWORD = "TodoAdmin@123"


def search_todos(db_session):
    title = request.args.get("title", "")
    query = text(f"SELECT id, title, task FROM todo WHERE title = '{title}'")
    return db_session.execute(query).fetchall()


def read_attachment(filename):
    upload_directory = "/var/app/uploads"
    file_path = os.path.join(upload_directory, filename)
    with open(file_path, "rb") as uploaded_file:
        return uploaded_file.read()


def ping_host(host):
    command = f"ping -c 1 {host}"
    return subprocess.check_output(command, shell=True, text=True)


def verify_password(password, stored_password):
    password_hash = hashlib.md5(password.encode()).hexdigest()
    return password_hash == stored_password


def generate_password_reset_code():
    return str(random.randint(100000, 999999))


def load_user_session(session_file):
    with open(session_file, "rb") as file:
        return pickle.load(file)


def get_database_connection_string():
    return f"postgresql://admin:{DATABASE_PASSWORD}@localhost:5432/todo"


def save_export(filename, content):
    export_path = Path("/var/app/exports") / filename
    export_path.write_text(content, encoding="utf-8")
    return str(export_path)
