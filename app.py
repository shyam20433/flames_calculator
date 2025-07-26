from flask import Flask, render_template, request
from flames import flames, flames_calculator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        name1 = request.form['name1'].strip().lower()
        name2 = request.form['name2'].strip().lower()
        new_stack = flames_calculator(name1, name2)
        result = flames(["f","l","a","m","e","s"], new_stack, 0, name1, name2)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) 