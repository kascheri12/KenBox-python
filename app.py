#
# KenBox WebApp
#
from KenBox import KenBox
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    children = None
    if request.method == 'POST':
        children = request.form.get('children')
        parent = KenBox()
    return render_template('index.html',results=children)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
