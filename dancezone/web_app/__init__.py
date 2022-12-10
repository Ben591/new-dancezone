# this is the "web_app/__init__.py" file...

import os
from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes

load_dotenv()

Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)