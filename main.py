from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index ():
    card_data=(
        ("Offensive class", "These classes are the main grunt of your team, they are meant to be the ones that are doig the dirty work. These classes are: Scout, soldier and pyro ", "Button Text", "static/images/logo.png"),
        ("Defensive class", "description", "Button Text", "static/images/logo.png"),
        ("title", "description", "Button Text", "static/images/logo.png"),
        ("title", "description", "Button Text", "static/images/logo.png"),
        ("title", "description", "Button Text", "static/images/logo.png"),
        ("title", "description", "Button Text", "static/images/logo.png"),
    )
    return render_template("index.html", cards = card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
