import subprocess

subprocess.run('alembic revision --autogenerate', shell=True)
# subprocess.run('alembic upgrade head', shell=True)