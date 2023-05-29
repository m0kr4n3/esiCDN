# flask app that reads a specific file and returns the contents and listens on port 8080
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    try:
        files = open('/logs.txt','r').read().strip().split('\n')
        files = [f.split(' ')[1] for f in files if f.split(' ')[0] == 'miss']
        files = list(set(files))
    except:
        files = "No logs found"
    return render_template('index.html', files=files)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)