from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return render_template("form.html", result="", show=False)

@app.route('/calculate', methods=['POST'])
def calculate():
    firsNumber = request.form['firstNumber']
    secondNumber = request.form['secondNumber']
    if request.form['type'] == 'plus':
        return render_template("form.html", result=plus(firsNumber, secondNumber), show=True)
    elif request.form['type'] == 'minus':
        return render_template("form.html", result=minus(firsNumber, secondNumber), show=True)
    elif request.form['type'] == 'multiple':
        return render_template("form.html", result=multiple(firsNumber, secondNumber), show=True)
    elif request.form['type'] == 'divide':
        return render_template("form.html", result=divide(firsNumber, secondNumber), show=True)
    else:
        return render_template("form.html", result='Err: Not support type', show=True)

def plus(a, b):
    return str(int(a) + int(b))

def minus(a, b):
    return str(int(a) - int(b))

def multiple(a, b):
    return str(int(a) * int(b))

def divide(a, b):
    return str(int(a) / int(b))


app.run()
