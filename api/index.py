from flask import Flask

app = Flask(__name__)

app.route('/')
def hone():
    return 'Hello Python + Flask on Vercel!'