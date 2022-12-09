from flask import Flask, request,flash,render_template,redirect,url_for,session
from config import *
from flask_bcrypt import generate_password_hash,check_password_hash

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/home')
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("home.html")


@app.route('/',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form["jina"]
        email = request.form["arafa"]
        password = request.form["siri"]
        password = generate_password_hash(password)
        User.create(name=name,email=email,password=password)
        flash("Signed Up successfully")
    return render_template("sign up.html")


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["arafa"]
        password = request.form["siri"]
        try:
            user = User.get(User.email == email)
            hashedPassword = user.password
            if check_password_hash(hashedPassword,password):
                # Assign a session and redirect to home page
                session["email"] = email
                session["logged_in"] = True
                return redirect(url_for("home"))
            else:
                flash("Wrong email or password")
        except:
            flash("User does not exist")
    return render_template("Login.html")


@app.route('/shop')
def shop():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    shop = Product.select()
    return render_template("Shop.html", shop=shop)


@app.route('/sellproducts',methods=["GET","POST",])
def sellproducts():
    if request.method == "POST":
        name = request.form["sell"]
        price = request.form["pesa"]
        Product.create(name=name,price=price)
        flash("Product added to shop")
    return render_template("sell products.html")


@app.route('/remove/<int:id>')
def remove(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    Product.delete().where(Product.id == id).execute()
    flash("Product removed from shopping cart")
    return redirect(url_for("cart"))


@app.route('/productdetails/<int:id>')
def productdetails(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    productdetails = Product.select().where(Product.id == id)
    return render_template("Product Details.html", productdetails=productdetails)

@app.route('/cart/',)
def cart():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    cart = Product.select()
    return render_template("shopping cart.html", cart=cart)


# @app.route('/add/<int:id>',)
# def add_to_cart(id):
#     if not session.get("logged_in"):
#         return redirect(url_for("login"))
#     if request.method == "POST":
#         product = request.form.get((Product.id == id)






if __name__ == '__main__':
    app.run()
