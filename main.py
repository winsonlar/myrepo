import json
from random import choice
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

with open(Path(__file__).parent / "randomizer.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)


@app.route("/")
def home():
    image = "https://blog.darwinbox.com/hubfs/MicrosoftTeams-image%20%282%29-1.png"
    repo = "https://github.com/winsonlar/myrepo"
    quote = choice(quotes)

    return render_template(
        "index.html", image_url=image_url, repo_url=repo_url, quote=quote
    )


if __name__ == "__main__":
    app.run(debug=True)
