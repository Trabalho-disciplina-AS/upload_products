import requests
import random
import os
import json


def add_discount(products):
    new_products = []
    for product in products:
        if product["discount"]:
            product["discount_price"] = round(random.uniform(10.0, 30.0), 2)
        product["discount_price"] = 0.0
        new_products.append(product)
    return new_products


path = f"{os.getcwd()}\\images"
products = json.loads(open("product.json").read())
products = add_discount(products)

for product in products:
    image_byte = open(f"{path}\\{product['image']}.png", "rb")
    image_file = [("image", (f"{product['image']}.png", image_byte, "image/png"))]
    response = requests.post(
        "http://localhost:5005/products", headers={}, data=product, files=image_file
    )

    print(response.text)