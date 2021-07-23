# Handler file to initialize the flask application

from flask_script import Manager, Server
from app import startApp
from config import config

# Find environment settings
settings = config["development"]
app = startApp(settings)

manager = Manager(app)
# Change default server port
manager.add_command("runserver", Server(host="localhost", port=8001))

if __name__ == "__main__":
    manager.run()
