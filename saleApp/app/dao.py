from itertools import product

from app.models import Category, Product


def load_categories():
    return Category.query.order_by('id').all()


def load_products(cate_id):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id == cate_id)

    return query.all()







