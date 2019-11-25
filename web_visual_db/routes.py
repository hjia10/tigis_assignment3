from flask import Flask, render_template

app = Flask(__name__)

data = ['rob', 'webster', 37]


@app.route("/")
def home():
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)