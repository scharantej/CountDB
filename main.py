
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


# Static variable persists across app lifecycle
counter_value = 0


@app.route('/', methods=['GET'])
def index():
    """
    handler for GET requests on the website's home page
    """
    return render_template('index.html', counter=counter_value)


@app.route('/increment', methods=['POST'])
def increment():
    """
    Handler for POST requests made when the increment button is clicked
    """
    global counter_value  # Using the global keyword to access the variable in the current scope
    counter_value += 1
    # return redirect(url_for('index')), 200 # Manually setting status code to 200, which is default for successful responses
    return redirect(url_for('index'))  # Redirects to the index route with the default status code (302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
