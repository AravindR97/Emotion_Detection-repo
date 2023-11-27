from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text = request.args['textToAnalyze']
    result = emotion_detector(text)

    if result['dominant_emotion'] == None:
        message = "Invalid text! Please try again!"
    else:
        message = f"""For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 
        'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. 
        The dominant emotion is {result['dominant_emotion']} """
    
    return message

@app.route("/")
def index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 5000)
