import json
from random import choice
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

with open(Path(__file__).parent / "randomizer.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)


@app.route("/")
def home():
    quote = choice(quotes)

    return render_template(
        "index.html", image_url="https://blog.darwinbox.com/hubfs/MicrosoftTeams-image%20%282%29-1.png", repo_url="https://github.com/winsonlar/myrepo", quote=quote
    )


if __name__ == "__main__":
    app.run(debug=True)
