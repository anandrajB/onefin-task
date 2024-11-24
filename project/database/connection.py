import os
from pathlib import Path

from dotenv import load_dotenv

from .options import DATABASE_OPTIONS  # noqa

load_dotenv()

DEFAULT_DB_ENGINE = os.environ.get("DEFAULT_DB_ENGINE")
BASE_NAME = os.environ.get("APP_ENV")
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# -------------------#
#  FOR POSTGRES      #
# -------------------#


# DATABASE_CONFIG = {
#     "default": {
#         "ENGINE": DEFAULT_DB_ENGINE,
#         "NAME": os.environ.get(f"{BASE_NAME}_DB_NAME"),
#         "USER": os.environ.get(f"{BASE_NAME}_DB_USER"),
#         "PASSWORD": os.environ.get(f"{BASE_NAME}_DB_PASSWORD"),
#         "HOST": os.environ.get(f"{BASE_NAME}_DB_HOST"),
#         "PORT": os.environ.get(f"{BASE_NAME}_DB_PORT"),
#     },
# }


# -------------------#
#  FOR SQLITE        #
# -------------------#

DATABASE_CONFIG = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
