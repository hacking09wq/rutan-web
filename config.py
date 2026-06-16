import os
from urllib.parse import urlparse, unquote

def get_env(name, default=None):
    value = os.getenv(name)
    if value is None or str(value).strip() == "":
        return default
    return str(value).strip()

def build_db_config():
    db_url = get_env("DB_URL")

    if db_url:
        parsed = urlparse(db_url)

        return {
            "host": parsed.hostname,
            "user": unquote(parsed.username or ""),
            "password": unquote(parsed.password or ""),
            "database": (parsed.path or "/railway").lstrip("/"),
            "port": int(parsed.port or 3306),
            "connection_timeout": 10,
            "use_pure": True,
        }

    return {
        "host": get_env("DB_HOST"),
        "user": get_env("DB_USER"),
        "password": get_env("DB_PASSWORD"),
        "database": get_env("DB_NAME", "railway"),
        "port": int(get_env("DB_PORT", "3306")),
        "connection_timeout": 10,
        "use_pure": True,
    }

DB_CONFIG = build_db_config()

SECRET_KEY = get_env("SECRET_KEY", "rutan_secret")

UPLOAD_FOLDER = "static/uploads"

IMG_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
DOC_EXTENSIONS = {"pdf"}
