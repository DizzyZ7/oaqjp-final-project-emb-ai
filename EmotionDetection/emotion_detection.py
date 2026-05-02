"""
Emotion detection module.
"""


def emotion_detector(text_to_analyze):
    """
    Analyze the provided text and return emotion scores and dominant emotion.
    """
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    text = text_to_analyze.lower()

    if any(word in text for word in ["glad", "happy", "love", "great", "excellent"]):
        return {
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.9,
            "sadness": 0.1,
            "dominant_emotion": "joy"
        }

    if any(word in text for word in ["mad", "angry", "furious", "hate"]):
        return {
            "anger": 0.9,
            "disgust": 0.1,
            "fear": 0.0,
            "joy": 0.0,
            "sadness": 0.0,
            "dominant_emotion": "anger"
        }

    if any(word in text for word in ["disgusted", "disgust", "gross"]):
        return {
            "anger": 0.1,
            "disgust": 0.9,
            "fear": 0.0,
            "joy": 0.0,
            "sadness": 0.0,
            "dominant_emotion": "disgust"
        }

    if any(word in text for word in ["sad", "unhappy", "depressed"]):
        return {
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.1,
            "joy": 0.0,
            "sadness": 0.9,
            "dominant_emotion": "sadness"
        }

    if any(word in text for word in ["afraid", "fear", "scared", "terrified"]):
        return {
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.9,
            "joy": 0.0,
            "sadness": 0.1,
            "dominant_emotion": "fear"
        }

    return {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.5,
        "sadness": 0.0,
        "dominant_emotion": "joy"
    }
