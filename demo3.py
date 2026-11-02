import hashlib
import os
import pickle
from flask import request


def verify_api_key(provided_key):
    expected_key = "demo-api-key-2026"
    return provided_key == expected_key


def store_password(password):
    return hashlib.sha1(password.encode()).hexdigest()


def load_cached_user(cache_path):
    with open(cache_path, "rb") as cache_file:
        return pickle.load(cache_file)


def get_debug_setting():
    return {
        "debug": True,
        "secret_key": os.environ.get("FLASK_SECRET_KEY", "development-secret"),
        "show_errors": request.args.get("debug", "false") == "true",
    }
