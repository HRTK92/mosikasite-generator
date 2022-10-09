# flask app
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    query = request.args.get('query')
    mosikasite = request.args.get('mosikasite')
    res = requests.get(f'https://www.google.com/search?q={query}&hl=ja', headers={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36'})
    html = res.text.replace('<div id="taw"><div><div></div></div>', f'''<div id="taw"><div><div><p class="gqLncc card-section KDCVqf Ww4FFb vt6azd" aria-level="3" role="heading"><spanclass="gL9Hy">もしかして:</span> <a class="gL9Hy" href="/search?hl=ja&amp;q={mosikasite}"><b >{mosikasite}</b></a></p></div></div>''')
    html = re.sub(r'href="/(.*?)"', r'href="https://www.google.com/\1"', html)
    html = re.sub(r'src="/(.*?)"', r'src="https://www.google.com/\1"', html)
    #html = re.sub('<div class="HK0d3e" aria-label="Google"></div>',
    #              '<style>font-family: Roboto,Helvetica Neue,Arial,sans-serif;font-size: small;-webkit-text-size-adjust: 100%;color: #1558d6;-webkit-tap-highlight-color: rgba(0,0,0,.1);max-height: 999999px;background: url(/images/nav_logo325_hr.webp) no-repeat;background-position: 0 -374px;background-size: 167px;height: 36px;width: 92px;</style><div class="HK0d3e" aria-label="Google"></div>', html)
    return html

if __name__ == '__main__':
    app.run()
