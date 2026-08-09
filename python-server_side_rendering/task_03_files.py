from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_data = read_json()
    elif source == 'csv':
        products_data = read_csv()
    else:
        return render_template(
            'product_display.html',
            error='Wrong source',
            products=[]
        )

    if product_id:
        products_data = [
            product for product in products_data
            if str(product['id']) == product_id
        ]

        if not products_data:
            return render_template(
                'product_display.html',
                error='Product not found',
                products=[]
            )

    return render_template(
        'product_display.html',
        products=products_data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
