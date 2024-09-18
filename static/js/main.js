// Stripe checkout initialization
const stripe = Stripe('YOUR_STRIPE_PUBLIC_KEY');
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', function() {
  fetch('/create-checkout-session', {
    method: 'POST',
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(session) {
    return stripe.redirectToCheckout({ sessionId: session.id });
  })
  .then(function(result) {
    if (result.error) {
      alert(result.error.message);
    }
  })
  .catch(function(error) {
    console.error('Error:', error);
  });
});// Event listener for checkout button
document.addEventListener('DOMContentLoaded', function() {
  const checkoutButton = document.getElementById('checkout-button');

  checkoutButton.addEventListener('click', function() {
    fetch('/create-checkout-session', {
      method: 'POST',
    })
    .then(function(response) {
      return response.json();
    })
    .then(function(session) {
      return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function(result) {
      if (result.error) {
        alert(result.error.message);
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
    });
  });
});