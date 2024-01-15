from flask import Flask, render_template ,request
from flask_cors import CORS, cross_origin
from textSummarizer.pipeline.prediction import PredictionPipeline


app = Flask(__name__)
CORS(app)

class ClientAPP:
    def __init__(self):
        self.predict_obj =  PredictionPipeline()
    
    
@app.route('/',methods=['GET','POST']) 
@cross_origin()
def index():   
    return render_template('index.html') 


@app.route('/submit',methods=['POST']) 
@cross_origin()
def submit():
    if request.method == 'POST':
        user_input = request.form.get('userTextarea')  
            
    summary = clapp.predict_obj.predict(user_input)   
    return f"{summary}" 
    # return render_template('index.html')  


if __name__=="__main__":
    clapp = ClientAPP()
    app.run(debug=True)