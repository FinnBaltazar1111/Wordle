import os
os.system('pip install requests')
os.system('pip install json')
from flask import Flask
import os,datetime,requests,json
yr=datetime.datetime.now().year
mn=datetime.datetime.now().month
dy=datetime.datetime.now().dy
url = 'https://www.nytimes.com/svc/wordle/v2/'+yr+'-'+mn+'-'+dy+'.json'
app = Flask(__name__)
@app.route('/')
def index():
    return request.get(url)['solution']
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
