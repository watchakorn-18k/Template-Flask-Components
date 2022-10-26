from __main__ import app, render_template, url_for


@app.route("/page-2")
def page_2():
    return render_template("home.html", title_name="Page 2")
