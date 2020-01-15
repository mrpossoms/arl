import os

from flask import Flask
from flask import render_template
from flask import request

app = Flask('ARL', static_url_path='')


@app.route("/")
def index():
    return render_template("colorado/index.html")


if __name__ == '__main__':
    port = 8080
    if 'PORT' in os.environ:
        port = os.environ['PORT']

    if os.environ['TEMPLATES_AUTO_RELOAD'] is not None:
        app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.run(port=port, host='0.0.0.0')

