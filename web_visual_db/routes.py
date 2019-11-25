from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = ''


@app.route("/home")
@app.route("/")
def home():
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)