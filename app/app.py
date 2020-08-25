import requests
from flask import Flask, request, jsonify
from flask import render_template
from loguru import logger

from services.image_prediction import predict_image

app = Flask(__name__)


@app.route("/hello/", methods=["GET"])
def hello_world():
    return "Hello, World!"


@app.route("/predict/butterfly/", methods=["POST"])
def image_prediction():
    if request.headers["Content-Type"].startswith("multipart/form-data"):
        image = request.files.get("image", "")
    else:
        logger.error(f"INVALID_REQUEST >> Files not found!")

    file_name = image.filename
    logger.info(f"Sending request for: {file_name}")
    data = predict_image(image)
    res = {
        "file_name": file_name,
        "predicted_class": data[0],
        "predicted_probability": data[1],
    }
    # return jsonify(res), 200
    return render_template("index.html", title="Welcome", data=[res])


@app.route("/")
def index():
    return render_template("index.html", title="Welcome")


if __name__ == "__main__":
    app.run()
