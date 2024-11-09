from flask import Flask, render_template, request
from app import app
import dao



@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')

    prods = dao.load_products(cate_id = cate_id)

    return render_template("index.html", categories = cates, products = prods)

if __name__ == "__main__":
    app.run(debug=True)