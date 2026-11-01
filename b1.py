import subprocess
import yaml


def find_user(db_session, username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db_session.execute(query)


def run_ping(host):
    return subprocess.run(
        "ping -c 1 " + host,
        shell=True,
        capture_output=True,
        text=True,
    )


def load_settings(config_text):
    return yaml.load(config_text, Loader=yaml.Loader)
