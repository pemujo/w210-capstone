from flask import render_template
from flask import Flask

app = Flask(__name__)


#
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vawg')
def vawg():
    return render_template('vawg.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/education')
def education():
    return render_template('vawg_education.html')


@app.route('/overview')
def overview():
    return render_template('vawg_exploration.html')


@app.route('/laws')
def laws():
    return render_template('vawg_laws.html')


@app.route('/health')
def health():
    return render_template('vawg_health.html')


@app.route('/datasource')
def datasource():
    return render_template('vawg_ds.html')


@app.route('/attitudes')
def attitudes():
    return render_template('vawg_attitudes.html')


if __name__ == '__main__':
    app.run(debug=True)
