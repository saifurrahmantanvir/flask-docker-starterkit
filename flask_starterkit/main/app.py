from flask import Flask
from flask_starterkit.main.config import create_app

flask_app = create_app()


@flask_app.route("/")
def home_route():
    return "Introduction to DevOps CI/CD with Flask Starter Kit!"
