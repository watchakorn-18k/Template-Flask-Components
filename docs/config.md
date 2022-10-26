Config

# File All

```
├───components
│   page_1.py
│   page_2.py
│   __init__.py
│
├───templates
│       home.html
│ app.py
```

`app.py` file and the file in components the import section must be the same such as.

app.py

```py
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="components/templates")

import components

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
```

and file `components/page_1.py`

```py
from __main__ import app, render_template, url_for


@app.route("/")
def page_1():
    return render_template("home.html", title_name="page_1")

```

`render_template` and `url_for` It is active on this page. So in the app.py file must be added to it.
