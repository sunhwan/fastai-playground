from flask import Flask
from flask import render_template
from flask import request, send_file, abort
from werkzeug.utils import secure_filename

from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

import os
import tempfile
from test import predict

DATADIR = './data/test'

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if not os.path.exists(DATADIR):
            os.system(f'mkdir -p {DATADIR}')
        fp, tempname = tempfile.mkstemp(prefix='image_', suffix='.png', dir=DATADIR) #'data/test/image_000.jpg'
        file.save(tempname)
        testfilename = f'{DATADIR}/%s' % os.path.basename(tempname)
        preds = predict(testfilename)
        return render_template('main.html', preds=preds, filename=os.path.basename(tempname))

    return render_template('main.html')

@app.route("/uploaded_file/<filename>")
def uploaded_file(filename):
    imgfile = os.path.join(DATADIR, filename)
    if os.path.exists(imgfile):
        return send_file(imgfile)
    return abort(404)
