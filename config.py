import os

def get_env(name, default=None):
    value = os.getenv(name)
    if value is None or str(value).strip() == "":
        return default
    return value

DB_CONFIG = {
    "host": get_env("DB_HOST", get_env("MYSQLHOST")),
    "user": get_env("DB_USER", get_env("MYSQLUSER")),
    "password": get_env("DB_PASSWORD", get_env("MYSQLPASSWORD")),
    "database": get_env("DB_NAME", get_env("MYSQLDATABASE")),
    "port": int(get_env("DB_PORT", "3306")),
    "connection_timeout": 10,
    "use_pure": True,
}

SECRET_KEY = get_env("SECRET_KEY", "rutan_secret")

UPLOAD_FOLDER = "static/uploads"

IMG_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
DOC_EXTENSIONS = {"pdf"}
