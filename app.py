import os
from flask import Flask, render_template, request, redirect, url_for
from convert import image_to_ascii

app = Flask(__name__)

# Define the directory to store uploaded images
UPLOADS_FOLDER = "uploads"

# Ensure the "uploads" directory exists
os.makedirs(UPLOADS_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            input_image_path = os.path.join(UPLOADS_FOLDER, "input_image.jpg")
            uploaded_file.save(input_image_path)
            ascii_art = image_to_ascii(input_image_path, output_width=100)
            return render_template("index.html", ascii_art=ascii_art)
    return render_template("index.html", ascii_art=None)

if __name__ == "__main__":
    app.run(debug=True)
