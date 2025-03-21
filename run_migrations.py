import os
import sys
import django
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erp_config.settings")
    os.environ["PYTHONIOENCODING"] = "utf-8"
    os.environ["LANG"] = "es_ES.UTF-8"
    
    try:
        django.setup()
        execute_from_command_line(["manage.py", "migrate"])
    except Exception as e:
        print(f"Error durante la migración: {e}") 