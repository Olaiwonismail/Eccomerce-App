from flask import render_template, request, Blueprint
from app.models import Product
from app import db,bootstrap
from flask_login import login_required
main = Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
# @login_required
def home():
    # products = Product.query.all()

    page = request.args.get('page',1,type = int)
    # posts = Post.query.paginate(page=page ,per_page = 10)
    products = Product.query.paginate(page=page ,per_page = 12)

    return render_template('main/home.html',products=products)

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')
