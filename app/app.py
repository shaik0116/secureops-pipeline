import os
import sqlite3
import subprocess
import hashlib
from flask import Flask, request, jsonify
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# VULNERABILITY 1 — Hardcoded credential
# detect-secrets will flag this line.
DB_PASSWORD = "SuperSecret123!"  # noqa: S105


# VULNERABILITY 2 — Weak hash function
# Bandit will flag hashlib.md5 as insecure.
def hash_password_insecure(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()  # noqa: S324


# VULNERABILITY 3 — SQL Injection
# Bandit will flag the f-string query construction.
def get_user_insecure(username: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin')")
    query = f"SELECT * FROM users WHERE username = '{username}'"  # noqa: S608
    cursor.execute(query)
    return cursor.fetchone()


# VULNERABILITY 4 — Command Injection
# Bandit will flag subprocess with shell=True.
def ping_host_insecure(host: str) -> str:
    result = subprocess.run(  # noqa: S602
        f"ping -c 1 {host}", shell=True, capture_output=True, text=True
    )
    return result.stdout


# CORRECT PATTERN — fetch secrets from Azure Key Vault using Managed Identity
def get_secret_from_keyvault(secret_name: str) -> str:
    vault_url = os.environ.get("AZURE_KEY_VAULT_URL", "")
    if not vault_url:
        return "KEY_VAULT_URL_NOT_SET"
    credential = ManagedIdentityCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "secureops-api", "version": "1.0.0"})


@app.route("/api/user", methods=["GET"])
def get_user():
    username = request.args.get("username", "")
    user = get_user_insecure(username)
    return jsonify({"user": user})


@app.route("/api/ping", methods=["POST"])
def ping():
    data = request.get_json()
    host = data.get("host", "127.0.0.1")
    result = ping_host_insecure(host)
    return jsonify({"result": result})


@app.route("/api/secret", methods=["GET"])
def fetch_secret():
    secret_name = request.args.get("name", "db-connection-string")
    get_secret_from_keyvault(secret_name)
    return jsonify({"secret_name": secret_name, "retrieved": True})


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=8080, debug=debug_mode)
