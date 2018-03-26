from flask import Flask
from datetime import datetime
import calendar
app = Flask(__name__)

@app.route('/')
def index():
    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())
    return str(unixtime * 1000)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

