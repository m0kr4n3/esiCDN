from pathlib import Path
from flask import Flask, render_template, request


# Instantiate a Flask app object
app: Flask = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

UPLOAD_FOLDER = '/content/'

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

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("admin.html", upload=False)
    elif request.method == "POST":
        try:
            f = request.files.getlist("files")
            for file in f:
                file_location = UPLOAD_FOLDER + file.filename
                file.save(file_location)
            return render_template("admin.html", upload=True, success=True)
        except:
            return render_template("admin.html", upload=True, success=False)

def main():
    """Run the flask app."""
    app.run(port=5000)


if __name__ == "__main__":
    main()