from flask import Flask, render_template, request, jsonify
import stripe
from config import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY

app = Flask(__name__)
app.config['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
app.config['STRIPE_SECRET_KEY'] = STRIPE_SECRET_KEY

stripe.api_key = app.config['STRIPE_SECRET_KEY']# Configuration settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['PRODUCT_NAME'] = 'Wet Option'
app.config['PRODUCT_DESCRIPTION'] = 'Innovative wet option product'
app.config['PRODUCT_PRICE'] = 1999  # Price in cents
app.config['PRODUCT_CURRENCY'] = 'usd'# Stripe API key setup
stripe.api_key = app.config['STRIPE_SECRET_KEY']@app.route('/')
def index():
    return render_template('index.html', 
                           product_name=app.config['PRODUCT_NAME'],
                           product_description=app.config['PRODUCT_DESCRIPTION'],
                           product_price=app.config['PRODUCT_PRICE'] / 100,  # Convert cents to dollars
                           stripe_public_key=app.config['STRIPE_PUBLIC_KEY'])

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': app.config['PRODUCT_CURRENCY'],
                        'unit_amount': app.config['PRODUCT_PRICE'],
                        'product_data': {
                            'name': app.config['PRODUCT_NAME'],
                            'description': app.config['PRODUCT_DESCRIPTION'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.host_url + '?success=true',
            cancel_url=request.host_url + '?canceled=true',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(debug=True)@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': app.config['PRODUCT_CURRENCY'],
                        'unit_amount': app.config['PRODUCT_PRICE'],
                        'product_data': {
                            'name': app.config['PRODUCT_NAME'],
                            'description': app.config['PRODUCT_DESCRIPTION'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.host_url + '?success=true',
            cancel_url=request.host_url + '?canceled=true',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)