from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def index():
    return time.time()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

