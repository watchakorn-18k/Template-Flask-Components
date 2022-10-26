from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="components/templates")

import components

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
