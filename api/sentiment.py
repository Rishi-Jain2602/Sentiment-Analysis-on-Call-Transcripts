from flask import Flask, jsonify,request
from transformers import pipeline
import re

pipe = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
app = Flask(__name__)

def parse_transcript(text):
    dialogues = re.findall(r"\[(.*?)\]([^\[]*)", text)
    parsed_dialogues = [{"speaker": speaker, "text": dialogue.strip()} for speaker, dialogue in dialogues]
    return parsed_dialogues

def analyze_sentiment(parsed_dialogue):
    result = []
    for dialogue in parsed_dialogue:
        result_dialogue = pipe(dialogue['text'])
        result.append({"speaker": dialogue['speaker'], "text": dialogue['text'], "score": result_dialogue[0]})
    return result 


@app.route('/analyze',methods = ['POST'])
def get_data():
    data = request.get_json()
    transcript_content = data.get("transcript","")
    if transcript_content:
        parsed_dialogue = parse_transcript(transcript_content)
        sentiment_result = analyze_sentiment(parsed_dialogue)
        return jsonify(sentiment_result)
    
    return jsonify({'Status':'Error in File'}),400

if __name__ == '__main__':
    app.run(debug=True)
