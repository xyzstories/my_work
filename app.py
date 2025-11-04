from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    user_info = {
        "name": "Siddiqi",
        "interests": ["Track", "Mathematics", "Chemistry"],
        "age": 17,
        "school": "NMH"
    }
    return render_template("about.html", data = user_info)

@app.route("/contact")
def contact():
    contact_info = {
        "email": "siddiqikomou08@gmail.com",
        "phone": "413-676-6767",
        "instagram": "d1.siddiqi"
    }
    return render_template("contact.html", contact = contact_info)

if __name__ == "__main__":
    app.run(debug = True)

