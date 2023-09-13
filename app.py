# import the necessary modules
from flask import Flask , render_template , request , jsonify

# importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def index():
    return render_template('index.html')

# write a route for post request
@app.route('/predict-emotion' , methods = ['POST'])
def review():

    # extract the customer_review by writing the appropriate 'key' from the JSON data
    input_text = request.json.get('text')

    # check if the customer_review is empty, return error
    if not review:
        input_text= {
            "status":"error",
            "message":"Please enter some text"

        }

        return jsonify(input_text)

    # if review is not empty, pass it through the 'predict' function.
    # predict function returns 2 things : sentiment and path of image in static folder
    # example : Positive , ./static/assets/emoticons/positive.png

    else:
        predicted_emotion, predicted_emotions_img_url=predict(input_text)
        response={
            "status":"success",
            "data":{"predicted_emotion":predicted_emotion,
            "predicted_emotion_img_url": predicted_emotions_img_url
            }
        }
    

    
    return jsonify(response)


if __name__  ==  "__main__":
    app.run(debug = True)