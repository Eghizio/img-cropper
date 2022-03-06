from flask import Flask, render_template, request, Response
from crop import crop_image

app = Flask(__name__)

@app.route("/", methods=["GET"])
def client():
    return render_template("client.html")

@app.route("/images", methods=["POST"])
def crop():
    img = request.json["img"]
    cropped_img = crop_image(img)
    return { "img": cropped_img }
    # return Response(img, mimetype="image/png")


# TODO: Resize endpoint, fix horizontal cropping.