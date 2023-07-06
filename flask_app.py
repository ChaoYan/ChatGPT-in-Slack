from slack_app import app

# Initialize Flask app
from flask import Flask, request

flask_app = Flask(__name__)

# SlackRequestHandler translates WSGI requests to Bolt's interface
# and builds WSGI response from Bolt's response.
from slack_bolt.adapter.flask import SlackRequestHandler

handler = SlackRequestHandler(app)


# Register routes to Flask app
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    # handler runs App's dispatch method
    return handler.handle(request)


@flask_app.route("/")
def foo():
    return "Hello, World!"


if __name__ == "__main__":
    flask_app.run()
