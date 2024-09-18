from flask import Flask, render_template, request, jsonify
import stripe
from config import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY

app = Flask(__name__)
app.config['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
app.config['STRIPE_SECRET_KEY'] = STRIPE_SECRET_KEY

stripe.api_key = app.config['STRIPE_SECRET_KEY']