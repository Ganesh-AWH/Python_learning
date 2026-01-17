import stripe
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

# Stripe API Keys
stripe.api_key = "your_stripe_test_key"

# --- MODELS ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    # Relationship to a Cart or Orders could go here

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False) # Price in cents (Stripe requirement)
    img_url = db.Column(db.String(250))

# --- ROUTES ---
@app.route('/')
def home():
    products = Product.query.all()
    return render_template("index.html", items=products)

@app.route('/create-checkout-session/<int:product_id>', methods=['POST'])
def create_checkout_session(product_id):
    product = Product.query.get(product_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': product.name},
                'unit_amount': product.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('cancel', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/success')
def success():
    return "<h1>Payment Successful! Thank you for your order.</h1>"

if __name__ == "__main__":
    app.run(debug=True)