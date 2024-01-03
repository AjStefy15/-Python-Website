from flask import Flask, render_template
import random

app = Flask(__name__)

colors = ["orange", "red", "blue", "green", "yellow"]
names = ["abc", "def", "ghi", "jkl", "mno"]

def get_placeholder():
    randColor = random.choice(colors)
    randName = random.choice(names)

    url = f"https://placehold.co/600x400/{randColor}/white?text=Hello+World"
    return url, randName

@app.route("/")
def index():
    meme_pic, subreddit = get_placeholder()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)