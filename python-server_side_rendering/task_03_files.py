"""
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    """
    try:
        with open('items.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            items = data.get("items", [])
    except Exception as e:
        items = []
        return str(e)
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    """
    """
    source = request.args.get('source')
    id = request.args.get('id')

    try:
        if source == 'json':
            with open('products.json', 'r', encoding='utf-8') as json_file:
                products = json.load(json_file)
        elif source == 'csv':
            with open('products.csv', 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                products = list(reader)
        else:
            return render_template('product_display.html', error='Wrong source')

        if id:
            for product in products:
                if str(product['id']) == id:
                    return render_template('product_display.html', product=product)
            return render_template('product_display.html', error='Product id not found')

    except Exception as e:
        products = []
        return str(e)
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
