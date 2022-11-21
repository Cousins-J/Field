from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from flask import request
import tempfile
from pathlib import Path
import cv2
import sys
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def uploadvid():
    if request.method == 'POST':
        uploaded_file = request.files['upload']
        with tempfile.TemporaryDirectory() as td:
            temp_filename = Path(td) / 'uploaded_file'
            uploaded_file.save(temp_filename)
            
            vid = cv2.VideoCapture(str(temp_filename))
            currentframe = 0

            if not os.path.exists('data'):
                os.makedirs('data')
                
            while (True):
                
                success, frame = vid.read()

                cv2.imshow("Output", frame)
                cv2.imwrite(filename='./data/frame' + str(currentframe) + '.jpg',img= frame)
                currentframe +=1
                
                if currentframe == 9:
                    break
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                #    break
                
                    
            vid.release()   
            cv2.destroyAllWindows()


    return render_template('test.html')        

if __name__ == "__main__":
    app.run(debug=True)        
