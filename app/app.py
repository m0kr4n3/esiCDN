from pathlib import Path
from flask import Flask, redirect, url_for, render_template


# Instantiate a Flask app object
app: Flask = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')

# Get the parent directory of this script. (Global)
DIR_PATH= Path(__file__).parent




def get_files():
    content = Path('/content/')
    return [str(f).split('/')[-1] for f in content.iterdir() if f.is_file()]


@app.route("/files/<file_name>")  # 
def serve_file(file_name: str):
    """Set up a dynamic routes for directory items at /files/.

    Args:
        file_name (str): regular file.

    Returns:
        Response: regular file.
    """
    # check if the extension of the file is mp4
    ext = file_name.split('.')[-1]
    file_name = file_name.split('.')[0]
    if [-1] == 'mp4':
        # serve the video
        return redirect(url_for('stream', v=f'{file_name}.m3u8'))
    
    return redirect(url_for('content', filename='file_name'))


def html_ul_of_items():
    """Create a unordered list of anchors/links to file routes.

    Returns:
        str: a <ul> with N <li> elements where N is the number of
            elements in __file__'s directory.
    """
    
    html = open('./templates/list-files.html', 'r').read()

    for dir_item in get_files():
        ext = dir_item.split('.')[-1]
        file_name = dir_item.split('.')[0]
        if ext == 'mp4':
            html += f"<li><a href='/stream?v={file_name}.m3u8'>{dir_item}</a`></li>"
        else:
            html += f"<li><a href='/content/{dir_item}'>{dir_item}</a`></li>"
    html += "</li></ul> </ul>"
    html += "</div></body></html>"
    return html

# route / that will render index.html
@app.route("/")  
def index():
    return render_template("index.html")

@app.route("/stream/")
def stream():
    return render_template("stream.html")

@app.route("/list-files/")  # 
def content():
    """Root route which displays an unordered list of directory items.

    Returns:
        str: a <ul> with N <li> elements where N is the number of
            elements in __file__'s directory.
    """
    return html_ul_of_items()


def main():
    """Run the flask app."""
    app.run(port=5000)


if __name__ == "__main__":
    main()