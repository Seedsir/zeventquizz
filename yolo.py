import subprocess

subprocess.run('alembic upgrade head', shell=True)