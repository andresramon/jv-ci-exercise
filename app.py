import time
import os
from flask import Flask
from counter import get_hit_count

app = Flask(__name__)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello docker ds friends! I have been seen {} times.\n'.format(count)