from flask import (Flask, render_template, send_from_directory)
app = Flask(__name__, static_folder='/myvol')


@app.route("/index")
def start():
    return render_template( "index.html")


@app.route("/hello")
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
