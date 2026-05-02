"""
Unit tests for the emotion detector application.
"""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Unit tests for different dominant emotions.
    """

    def test_joy(self):
        """
        Test joy emotion.
        """
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy"
        )

    def test_anger(self):
        """
        Test anger emotion.
        """
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"],
            "anger"
        )

    def test_disgust(self):
        """
        Test disgust emotion.
        """
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust"
        )

    def test_sadness(self):
        """
        Test sadness emotion.
        """
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"],
            "sadness"
        )

    def test_fear(self):
        """
        Test fear emotion.
        """
        self.assertEqual(
            emotion_detector("I am really afraid that this will happen")["dominant_emotion"],
            "fear"
        )


if __name__ == "__main__":
    unittest.main()