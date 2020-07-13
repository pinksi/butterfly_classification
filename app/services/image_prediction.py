from PIL import Image, ImageOps
import numpy as np
from loguru import logger
import requests
import json


def predict_image(image):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    d = {"instances": [data[0].tolist()]}
    r = requests.post(
        "http://localhost:9000/v1/models/butterfly_classify:predict", json=d
    )
    results = r.text
    predicted_values = json.loads(results).get("predictions", [])
    prediction = list(predicted_values[0])
    classes = [
        "Danaus_plexippus",
        "Heliconius_charitonius",
        "Heliconius_erato",
        "Junonia_coenia",
        "Lycaena_phlaeas",
        "Nymphalis_antiopa",
        "Papilio_cresphontes",
        "Pieris_rapae",
        "Vanessa_atalanta",
        "Vanessa_cardui",
    ]
    predicted_probability = max(prediction)
    predicted_class = classes[prediction.index(predicted_probability)]
    return predicted_class, predicted_probability
