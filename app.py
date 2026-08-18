from flask import Flask, render_template

app = Flask(__name__)


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# ABOUT PAGE
# =========================

@app.route("/about")
def about():
    return render_template("about.html")


# =========================
# OUR WORK / PROGRAMS
# =========================

@app.route("/programs")
def programs():
    return render_template("programs.html")


# =========================
# EVENTS PAGE
# =========================

@app.route("/events")
def events():
    return render_template("events.html")


# =========================
# CAMPAIGNS PAGE
# =========================

@app.route("/campaigns")
def campaigns():
    return render_template("campaigns.html")


# =========================
# DONATION PAGE
# =========================

@app.route("/donate")
def donate():
    return render_template("donate.html")


# =========================
# VOLUNTEER PAGE
# =========================

@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")


# =========================
# GALLERY PAGE
# =========================

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


# =========================
# CONTACT PAGE
# =========================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# =========================
# RUN FLASK
# =========================

if __name__ == "__main__":
    app.run(debug=True)