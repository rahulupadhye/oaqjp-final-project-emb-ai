'''
This module provide a simplified wrapper over the 
IBM Watson NLP library Emotion Predict
'''
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

    return response.text
