"""
This module contains 'emotion_detector' function that will return a dictionary
showing various emotions and their scores after emotion analysis
"""

import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    head =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    r = requests.post(url, headers= head, json= data)
    result = r.json()['emotionPredictions'][0]['emotion']
    scores = list(result.values())
    emotions = list(result.keys())
    max_score = max(scores)
    Index = scores.index(max_score)
    dominant_emotion = emotions[Index]
    result['dominant_emotion'] = dominant_emotion
    return result
    
