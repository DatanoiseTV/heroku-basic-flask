from flask import Flask
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now(timezone.utc)
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc) # use POSIX epoch
    posix_timestamp_micros = (now - epoch) // timedelta(microseconds=1)
    posix_timestamp_millis = posix_timestamp_micros // 1000 # or `/ 1e3` for float
    return str(posix_timestamp_millis)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

