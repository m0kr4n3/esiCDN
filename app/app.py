from pathlib import Path
from flask import Flask, render_template


# Instantiate a Flask app object
app: Flask = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')



# route / that will render index.html
@app.route("/")  
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/stream/")
def stream():
    return render_template("stream.html")

@app.route("/list-files/")  # 
def content():
    content = Path('/content/')
    files =  [str(f).split('/')[-1] for f in content.iterdir() if f.is_file()]

    return render_template("list-files.html", files=files)


def main():
    """Run the flask app."""
    app.run(port=5000)


if __name__ == "__main__":
    main()