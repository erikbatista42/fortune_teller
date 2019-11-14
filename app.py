from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/')
# def index():
#     """Renders the home page with link to Fortune page."""
#     return render_template('index.html')

@app.route("/")
def fortune():
    """Renders Fortune page."""
    return render_template("fortune_form.html")

@app.route("/results")
def results():
    """Displays the user's fortune."""
    fav_beverage = request.args.get('beverages')
    quote = ""
    if fav_beverage == "none":
        quote = "You'll have a normal day today"
    elif fav_beverage == "coffee":
        quote = "You'll have lots of energy for the rest of today"
    elif fav_beverage == "water":
        quote = "You'll feel healthy for the rest of today"
    elif fav_beverage == "soda":
        quote = "You'll feel sick for the rest of today"
    elif fav_beverage == "juice":
        quote = "You'll semi energy for the rest of the the day"
    else:
        quote = "Unfortunately, you don't have a future... "
    return render_template("fortune_results.html", quote=quote)