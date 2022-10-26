from __main__ import app, render_template, url_for


@app.route("/")
def page_1():
    return render_template("home.html", title_name="page_1")
