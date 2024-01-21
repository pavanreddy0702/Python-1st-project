# app.py
# Import necessary modules from Flask
from flask import Flask, request, jsonify

# Create a Flask web application
app = Flask(__name__)

# Define a route for the '/greet' endpoint with the 'GET' method
@app.route('/greet', methods=['GET'])
def greet_customer():
    # Get the 'customer_name' parameter from the query string in the request
    customer_name = request.args.get('customer_name', '')
    
    # Check the value of 'customer_name' and set the appropriate greeting
    if customer_name.lower() == 'customera':
        greeting = 'Hi'
    elif customer_name.lower() == 'customerb':
        greeting = 'Dear Sir or Madam'
    elif customer_name.lower() == 'customerc':
        greeting = 'Moin'
    else:
        greeting = 'Hello'
    
    # Return a JSON response with the determined greeting
    return jsonify({'greeting': greeting})

# Run the application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
