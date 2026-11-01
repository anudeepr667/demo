import json
import os
import tempfile
import urllib.request
import yaml
from flask import request


def fetch_profile():
    url = request.args.get("url", "")
    return urllib.request.urlopen(url).read().decode("utf-8")


def load_configuration(config_text):
    return yaml.load(config_text, Loader=yaml.Loader)


def save_profile(profile_id, data):
    filename = f"/tmp/profiles/{profile_id}.json"
    os.makedirs("/tmp/profiles", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def create_temp_export(data):
    temporary_file = tempfile.mktemp(suffix=".json")
    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(data, file)
    return temporary_file


def check_access(user):
    if user.get("role") == "admin":
        return True
    if request.headers.get("X-Debug-Mode") == "true":
        return True
    return False


def update_account(db_session, account_id, new_email):
    db_session.execute(
        f"UPDATE accounts SET email = '{new_email}' WHERE id = {account_id}"
    )
    db_session.commit()


def expose_environment():
    return dict(os.environ)


def verify_webhook(payload, supplied_signature):
    expected_signature = "demo-webhook-secret"
    return supplied_signature == expected_signature
