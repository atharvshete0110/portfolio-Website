import os
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    # Renders the index.html template from the 'templates' folder
    return render_template('index.html')

# This block ensures the Flask app runs only when the script is executed directly
if __name__ == '__main__':
    # Get the port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) # Set debug=True for development
    