from flask import render_template, url_for, flash, redirect, request, Blueprint,make_response,session
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt,bootstrap
import ast,random,string
from flask_session import Session
from app.models import User, Product

 #, send_reset_emai
products= Blueprint('products',__name__)

@products.route("/item/<int:id>")
def item(id):
    product = Product.query.get_or_404(id)
    reviews = ast.literal_eval(product.reviews)
    tags = ast.literal_eval(product.tags)
    list = []
    items = Product.query.all()
    for item in items:

        if tags[0] in item.tags:
            list.append(item)
        else:

            pass
    random.shuffle(list)
    list= list[:3]

    return render_template('products/products.html',product = product,reviews=reviews,list = list)


@products.route("/wishlist/<int:id>",methods = ['POST','GET'])
@login_required
def wishlist(id):
    page = request.args.get('page')

    user = current_user
    product = Product.query.get_or_404(id)
    wishlist = user.wishlist
    wishlist = wishlist +' '+ (str(id))
    user.wishlist = wishlist
    db.session.commit()
    print(user.wishlist)

    if page:
        return redirect(page)
    return redirect(url_for('main.home'))

    # return render_template('main/base.html')

@products.route('/wishlist/items/',methods = ['POST','GET'])
@login_required
def wishlist_items():
    user = current_user
    wishlist = user.wishlist
    wishlist = list(map(int,wishlist.split()))
    wishlist = list(set(wishlist))
    wishlist = Product.query.filter(Product.id.in_(wishlist)).all()
    return render_template('products/wishlist.html',wishlist=wishlist)

@products.route('/add_to_cart/<int:id>/',methods = ['POST','GET'])
@login_required
def add_to_cart(id):
    page = request.args.get('page')
    if session.get("cart"):
        cart = session.get('cart')
        # print(cart)
        session["cart"] = cart + ' ' +str(id)
    else:
        session["cart"] = str(id)
    if page:
        return redirect(page)
    return redirect(url_for('main.home'))


@products.route('/cart/',methods = ['POST','GET'])
@login_required
def cart():
    cart = session.get('cart')
    # print(cart)
    user = current_user
    if cart:
        cart = list(map(int,cart.split()))
        cart = list(set(cart))
        cart = Product.query.filter(Product.id.in_(cart)).all()
    else:
        pass
    return render_template('products/cart.html',cart=cart)

@products.route('/remove_from_cart/<int:id>/',methods = ['POST','GET'])
@login_required
def remove_from_cart(id):
    cart = session.get('cart')
    print(cart)
    # user = current_user
    if cart:
        cart = list(map(int,cart.split()))
        cart = list(set(cart))


        cart.remove(id)
        cart = ' '.join(map(str,cart))
        session["cart"] = cart


    else:
        pass
    return redirect(url_for('main.home'))
