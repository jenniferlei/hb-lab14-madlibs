
"""A madlib game that compliments its users."""

from random import choice, sample

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
        <link rel="stylesheet" href="/static/madlibs.css">
        <title>Home Page</title>
    </head>
    <body>

    <h1>Home Page</h1>

    Hi! This is the home page.
    <br><br>
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

    nice_things = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=nice_things)


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

    madlib_story = choice(["madlib.html", "madlib2.html", "madlib3.html"])
    person = request.args.get("person")
    noun = request.args.get("noun")
    color = request.args.get("color")
    a_bunch_of_adjectives = request.args.getlist("adjective")

    return render_template(madlib_story, person=person, noun=noun, color=color, adjectives=a_bunch_of_adjectives)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
