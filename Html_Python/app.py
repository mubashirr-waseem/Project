from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return render_template('index.html', SUM=result)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = int(request.form['number'])
        if number % 2 == 0:
            result = "Even Number"
        else:
            result = "Odd Number"
    return render_template('index.html', result=result)
