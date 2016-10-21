

from flask_script import Manager, Server, prompt_bool
from flask_migrate import MigrateCommand

from pyfa_ng_backend import create_app, db

app = create_app()
manager = Manager(app)

@manager.command
def drop_db():
    if prompt_bool('Are you sure you want to lose all your data!?'):
        db.drop_all()

manager.add_command("runserver", Server("localhost", port=8000))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
