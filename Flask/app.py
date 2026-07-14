from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-key-change-in-production"

# Story scenes, in the order they appear in the Tableau story.
# Each entry maps to one exported PNG in static/images/.
STORY_SCENES = [
    {
        "id": "overview",
        "label": "Overview",
        "image": "overview.png",
        "title": "Where the risk sits today",
        "text": (
            "The story opens with the full picture: how many respondents in the "
            "dataset live with heart disease today, and how that splits across "
            "the population before we slice by any single factor. Everything "
            "that follows drills into this baseline."
        ),
    },
    {
        "id": "gender-risk",
        "label": "Gender Risk",
        "image": "gender_risk.png",
        "title": "Does sex change the risk?",
        "text": (
            "Comparing female and male respondents side by side shows a "
            "modestly higher heart disease share among men, though the gap is "
            "narrower than most people expect. Sex alone is a weak predictor "
            "on its own \u2014 it matters far more once combined with the "
            "lifestyle and clinical factors on the next scenes."
        ),
    },
    {
        "id": "lifestyle-factors",
        "label": "Lifestyle Factors",
        "image": "lifestyle_factors.png",
        "title": "Habits that move the needle",
        "text": (
            "Smoking and alcohol use are cross-tabulated against heart disease "
            "outcomes here. Respondents who smoke show a visibly higher share "
            "of heart disease than non-smokers, while heavy drinking on its "
            "own is a weaker signal \u2014 it's the combination of habits that "
            "compounds risk."
        ),
    },
    {
        "id": "race-conditions",
        "label": "Race & Conditions",
        "image": "race_conditions.png",
        "title": "Demographics and existing conditions",
        "text": (
            "The final scene breaks the dataset down by race and cross-references "
            "diabetes against stroke history. White respondents make up the "
            "largest share of records (70.4%), followed by Black respondents "
            "(24.2%), with the remaining groups \u2014 Hispanic, Asian, American "
            "Indian/Alaska Native, and Other \u2014 together under 5%. Diabetes "
            "and stroke history both correlate strongly with heart disease "
            "prevalence, more strongly than any single demographic factor."
        ),
    },
]

# Live Tableau Public embeds. Update these two URLs any time you republish
# the workbook -- nothing else in the templates needs to change.
TABLEAU_DASHBOARD_EMBED_URL = (
    "https://public.tableau.com/views/Heart_Disease_17831700829680/"
    "HeartDiseaseDashboard?:showVizHome=no&:embed=true&:language=en-US"
)
TABLEAU_STORY_EMBED_URL = (
    "https://public.tableau.com/views/Heart_Disease_17831700829680/"
    "Story?:showVizHome=no&:embed=true&:language=en-US"
)

DASHBOARD_PANELS = [
    {
        "title": "Gender vs Heart Disease",
        "text": "Total respondents by sex, with heart disease cases highlighted in orange.",
    },
    {
        "title": "Diabetic vs Stroke",
        "text": "Heart disease counts cross-tabulated by diabetes and stroke history, split by race.",
    },
    {
        "title": "Race-wise Heart Disease",
        "text": "Share of heart disease cases by race, as a proportion of the full dataset.",
    },
    {
        "title": "Smoking and Alcohol Impact",
        "text": "Heart disease counts by smoking status, further split by alcohol consumption.",
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html", panels=DASHBOARD_PANELS, embed_url=TABLEAU_DASHBOARD_EMBED_URL
    )


@app.route("/story")
def story():
    return render_template(
        "story.html", scenes=STORY_SCENES, embed_url=TABLEAU_STORY_EMBED_URL
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in every field before sending.", "error")
            return redirect(url_for("contact"))

        # No email backend is wired up yet -- this is where you'd call
        # your mail service (e.g. Flask-Mail) with name/email/message.
        flash("Thanks, {}! Your message has been received.".format(name), "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
