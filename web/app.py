from flask import *
from .deepfake import deepfake

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test')
def testgen():
    deepfake('tmp/test.jpg', 'tmp/test.mp4', 'tmp/test-out.mp4')
    return 'ok'


count = 0


@app.route('/gen', methods=['POST'])
def generate():
    img = request.files['img']
    imgpath = 'tmp/'+count+'_'+img.filename
    img.save(imgpath)
    vid = request.files['vid']
    vidpath = 'tmp/'+count+'_'+img.filename
    vid.save(vidpath)


def run():
    app.run()
