from flask import Flask                                                        
from twilio import twiml                                                       
 
app = Flask(__name__)                                                          
 
@app.route('/conference', methods=['POST'])                                    
def voice():
    response = twiml.Response()  
 
    with response.dial() as dial:                                          
        dial.conf("Rob's Blog Party")                                    
 
    return str(response)
 
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
