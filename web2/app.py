import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    rand_num = random.randint(1, 100000)
    return f'Hello, World! I am server web2. A random number is {rand_num}'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
