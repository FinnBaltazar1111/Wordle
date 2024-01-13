from flask import Flask,json
import os,datetime,requests
dayyay = datetime.today()
url = f'https://www.nytimes.com/svc/wordle/v2/{dayyay:%Y-%m-%d}.json'
app = Flask(__name__)
@app.route('/')
def index():
    return request.get(url)['solution']
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
