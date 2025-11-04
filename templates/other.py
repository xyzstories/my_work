from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    info = {
        "name": "Siddiqi Komou",
        "age": 17,
        "school": "NMH",
    }
    hobbies = {
        "athletic": ["Track and Field", "Bodybuilding", "Powerlifting"],
        "academic": ["Calculus", "Chemistry", "Literature"],
        "experimental": ["Theory", "Philosophy", "Art"],
    }
    contact = {
        "email": "skomou27@nmhschool.org",
        "insta": "cristiano",
        "github": "xyzstories",
    }
    return render_template("index.html", info = info, hobbies = hobbies, contact = contact)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


