def get_account(database_path):
    account_id = request.args.get("account_id", "")
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, email, balance FROM accounts WHERE id = " + account_id
    )
    return cursor.fetchall()


def download_report(report_name):
    report_path = os.path.join("/srv/reports", report_name)
    with open(report_path, "rb") as report:
        return report.read()


def update_profile(db, user_id):
    new_email = request.form.get("email", "")
    db.execute(
        f"UPDATE users SET email = '{new_email}' WHERE id = {user_id}"
    )
    db.commit()
