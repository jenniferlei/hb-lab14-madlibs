
"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return """
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/madlibs/static/madlibs.css">
        <title>Home Page</title>
    </head>
    <body>

    <h1>Home Page</h1>

    Hi! This is the home page.
    <br>
    <a href="/hello">Click to continue</a>

    </body>
</html>"""


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    """Starting game or telling user goodbye depending on response"""

    play_game = request.args.get("game option")

    if play_game == "Yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    """Create madlib"""

    person = request.args.get("person")
    noun = request.args.get("noun")
    color = request.args.get("color")
    adjectives = request.args.get("adjectives")

    return render_template("madlib.html", person=person, noun=noun, color=color, adjective=adjectives)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
