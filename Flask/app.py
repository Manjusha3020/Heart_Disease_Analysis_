from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@app.route("/story")
def story():
    return render_template("story.html", title="Story")


from flask import request, flash, redirect, url_for

app.secret_key = "heart_disease_analysis"

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        print(name)
        print(email)
        print(subject)
        print(message)

        flash("Your message has been sent successfully!")

        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact")


if __name__ == "__main__":
    app.run(debug=True)