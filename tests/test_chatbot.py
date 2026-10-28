import unittest
from app import app
from chatbot_engine import get_answer, normalize_text

class ChatbotTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CareDesk Assistant", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_known_question(self):
        response = self.client.post("/api/chat", json={"message": "Where is the hospital located?"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lahore", response.get_json()["reply"])

    def test_empty_message_rejected(self):
        response = self.client.post("/api/chat", json={"message": "   "})
        self.assertEqual(response.status_code, 400)

    def test_non_string_message_rejected(self):
        response = self.client.post("/api/chat", json={"message": 12})
        self.assertEqual(response.status_code, 400)

    def test_unknown_question_fallback(self):
        answer, match, score = get_answer("Can I bring my pet dragon to the moon?")
        self.assertIsNone(match)
        self.assertIn("couldn't find", answer)

    def test_normalization(self):
        self.assertEqual(normalize_text("  HELLO!!!   There "), "hello there")

if __name__ == "__main__":
    unittest.main()
