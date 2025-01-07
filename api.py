from flask import Flask, render_template, request, redirect, url_for
import os
from mura import predict_image

app = Flask(__name__)

# Ensure the "public" directory exists
UPLOAD_FOLDER = 'public'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']

    if file.filename == '':
        return "No file selected", 400

    if file:
        # Save the file to the "public" directory
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        result = predict_image(file_path)
        print(result)

        return f"File uploaded successfully: <a href='/{file_path}'>{file.filename}</a>"

if __name__ == '__main__':
    app.run(debug=True)