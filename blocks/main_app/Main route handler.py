@app.route('/')
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
    app.run(debug=True)