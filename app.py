from flask import Flask, render_template, url_for, redirect, request, make_response, jsonify
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = f"{os.getcwd()}/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ".mp4"

def extensions(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]
    if ext.lower() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/errors/exceeded_filesize")
def efs():
    return render_template("ftb.html")

@app.route("/errors/bad_filename")
def bfn():
    return render_template("bext.html")

@app.route("/errors/no_filename")
def nfn():
    return render_template("nfn.html")


@app.route("/8364687d095e", methods=["POST", "GET"])
def upload():
    if request.method == "POST":

        if request.files:

            file = request.files["image"]


            if file.filename == "":
                return redirect(url_for('nfn'))

            if not extensions(file.filename):
                print("That file is not allowed.")
                return redirect(url_for('bfn'))

            else: 
                filename = secure_filename(file.filename)
                
                file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                if os.path.getsize(os.path.join(app.config["IMAGE_UPLOADS"], filename)) >= 5242880:
                    print("file too big")
                    os.remove(f"{os.getcwd()}/uploads/{file.filename}")
                    return redirect(url_for('efs'))
                

            print(f"\n\nFile: {file}\nPath: {os.getcwd()}/uploads/{file.filename}")

            return redirect(url_for('index'))




if __name__ == "__main__":
	app.run(debug=True)