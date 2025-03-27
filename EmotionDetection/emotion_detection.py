'''
This module provide a simplified wrapper over the 
IBM Watson NLP library Emotion Predict
'''
import json
import requests

# Define function to run emotion detection using
# IBM Emotion Detection functions
def emotion_detector(text_to_analyze):
    '''
    This function takes in the text to be analysed and 
    provide a emotion analysis
    '''
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)
    formatted_res = json.loads(response.text)

    if response.status_code == 200:
        try:
            emotions = formatted_res['emotionPredictions'][0]['emotion']
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            dominant_emotion = max(emotions, key=emotions.get) if any(emotions.values()) else None

            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion' : dominant_emotion
            }

            return emotion_scores
        except (KeyError, IndexError, TypeError):
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

