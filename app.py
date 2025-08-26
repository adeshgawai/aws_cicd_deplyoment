from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles both GET and POST requests for the main calculator page.
    - GET: Renders the calculator page.
    - POST: Evaluates the expression sent from the form and returns the result.
    """
    result = ''
    error = ''
    expression = ''
    
    if request.method == 'POST':
        # Get the expression from the form's 'display' input field
        expression = request.form.get('display', '')
        try:
            # IMPORTANT: Using eval() can be a security risk if the input is not
            # controlled. For this calculator, we assume the input is only from
            # the calculator buttons, which is a controlled environment.
            # Avoid using eval() with untrusted user input in real applications.
            if expression:
                result = eval(expression)
            else:
                result = ''
        except Exception as e:
            # Handle any errors during evaluation (e.g., division by zero, syntax error)
            error = "Invalid Expression"
            result = ''
            
    # Render the main HTML page, passing the result, error, and expression to it
    return render_template('index.html', result=result, error=error, expression=expression)

# This ensures the app runs only when the script is executed directly

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8080) #for deployment run
    # app.run(host="127.0.0.1", port=8080,debug=True) # for local run