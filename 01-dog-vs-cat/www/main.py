from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

from test import predict

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        fp, tempname = tempfile.mkstemp(prefix='image_', suffix='.png', dir='data/test') #'data/test/image_000.jpg'
        file.save(tempname)
        testfilename = 'data/test/%s' % os.path.basename(tempname)
        preds = predict(testfilename)
        print(preds)

    return render_template('main.html')

