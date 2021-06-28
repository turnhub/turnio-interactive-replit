from flask import Flask, request
import os
import requests
import random

app = Flask("app")

# Repl provides these environment variables, we use it
# to construct the URL that this repl will be accessible on.
repl_owner = os.environ.get("REPL_OWNER")
repl_slug = os.environ.get("REPL_SLUG")
repl_url = f"https://{repl_slug}.{repl_owner.lower()}.repl.co"

TOKEN = os.environ.get("TOKEN")


@app.route("/")
def hello_world():
    return f"The Turn UI integration API endpoint is at {repl_url}/interactive"


@app.route("/interactive", methods=["POST"])
def interactive():
    json = request.json

    return ""
