from flask import Flask
from flask import render_template
from scrape import run as scrape_runner


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/abc', methods=['GET'])
def abc_view():
    return render_template('index.html')


@app.route('/box-office-mojo-scraper', methods=['POST'])
def box_office_scraper_view():
    scrape_runner()
    return {'data': [1, 2, 3]}


if __name__ == '__main__':
    app.run()
