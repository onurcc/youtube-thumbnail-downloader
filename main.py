from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
import urllib.request as ur
from bs4 import BeautifulSoup
import webbrowser

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    img_page = None
    if request.method == 'POST' and 'link' in request.form:
        video_url = request.form['link']
        page = ur.urlopen(video_url).read()
        soup = BeautifulSoup(page, "html.parser")
        img_url = soup.findAll(attrs={"property":"og:image"})
        img_page = img_url[0]['content']
    return render_template('index.html', img_page=img_page)


if __name__ == '__main__':
    app.run(debug=True)
