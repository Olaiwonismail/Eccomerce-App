import json,codecs
from app import create_app

app = create_app()
from app.models import Product
from app import db

f = open('C:\\Users\\DELL\\Downloads\\my_project\\products.json')

# returns JSON object as a dictionary
datas = json.load(f)

db.create_all()
# if __name__ == '__main__':
#     app.run(debug=True)
# Iterating through the json list
for data in datas['products']:
    # print(len(data['tags']))
    # print(len(data['returnPolicy']))
    # print(len(data['shippingInformation']))
    # print(len(data['reviews']))
    if data.get("brand"):
        brand = data["brand"]
    else:
        brand = None
    item =Product(
        title = data["title"],
    description=data["description"],
    price =data["price"],
    # image=str(data["images"]),
    stock =data["stock"],
    ratings =data["rating"],
    # buyer =data[],
    brand =brand,
    category = data['category'],
    thumbnail=data["thumbnail"],
    tags =str(data['tags']),
    returnPolicy = data['returnPolicy'],
    shippingInformation = data['shippingInformation'],
    reviews = str(data['reviews'])

)

    db.session.add(item)
    db.session.commit()


f.close()
