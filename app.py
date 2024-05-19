from flask import Flask, request, render_template, url_for
from WebScraper.scraper import web_scraper

app = Flask("LM Sheet Creator")

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
               url = request.form['url']
               scraped_data = web_scraper(url)
               return render_template('index.html', url=url, scraped_data=scraped_data)
        return render_template('index.html')

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5500)
