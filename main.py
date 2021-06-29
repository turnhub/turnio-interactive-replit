from flask import Flask, request
import os
import requests

app = Flask("app")

# Repl provides these environment variables, we use it
# to construct the URL that this repl will be accessible on.
repl_owner = os.environ.get("REPL_OWNER")
repl_slug = os.environ.get("REPL_SLUG")
repl_url = f"https://{repl_slug}.{repl_owner.lower()}.repl.co"

TOKEN = os.environ.get("TOKEN")
HOST = os.environ.get("HOST", "https://whatsapp.turn.io")

@app.route("/")
def hello_world():
    return f"The Turn UI integration API endpoint is at {repl_url}/interactive"


@app.route("/interactive", methods=["POST"])
def interactive():
    json = request.json

    print(repr(json))

    if "messages" not in json:
      return ""

    [message] = json["messages"]

    if "text" != message["type"]:
      return ""

    from_ = message["from"]
    content = message["text"]["body"]

    print(f"replying via {HOST}/v1/messages")
    if "button-me" in content:
      requests.post(f"{HOST}/v1/messages", 
      headers={
        "Authorization": f"Bearer {TOKEN}"
      },
      json={
        "to": from_,
        "type": "interactive",
        "interactive": {
          "type": "button",
          "header": {
            "type": "image",
            "image": {
              "link": "https://upload.wikimedia.org/wikipedia/commons/5/58/Plastic_%26_fabric_buttons_showing_holes_%26_shank.jpg"
            }
          },
          "body": {
            "text": "This is an interactive button!"
          },
          "footer": {
            "text": "This is the footer"
          },
          "action": {
            "buttons": [{
              "type": "reply",
              "reply": {
                "title": "red",
                "id": "red-button-id"
              }
            }, {
              "type": "reply",
              "reply": {
                "title": "blue",
                "id": "blue-button-id"
              }
            }, {
              "type": "reply",
              "reply": {
                "title": "green",
                "id": "green-button-id"
              }
            }]
          }
        }
      })
    elif "list-me" in content:
      requests.post(f"{HOST}/v1/messages", 
      headers={
        "Authorization": f"Bearer {TOKEN}"
      },
      json={
        "to": from_,
        "type": "interactive",
        "interactive": {
          "type": "list",
          "header": {
            "type": "text",
            "text": "list button text"
          },
          "body": {
            "text": "This is an interactive button!"
          },
          "footer": {
            "text": "This is the footer"
          },
          "action": {
            "button": "list call to action",
            "sections": [{
              "title":"section 1",
              "rows": [
                {
                  "id":"row-1",
                  "title": "row-title-content",
                  "description": "row-description-content", 
                }
              ]
            },
            {
              "title":"section 2",
              "rows": [
                {
                  "id":"row-2",
                  "title": "row-title-content",
                  "description": "row-description-content",           
                }
              ]
            }]
          }
        }
      })
    return ""

app.run(host='0.0.0.0', port=8080)