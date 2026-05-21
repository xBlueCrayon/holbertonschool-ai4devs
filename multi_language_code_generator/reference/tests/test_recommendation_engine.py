import unittest

from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine


class TestRecommendationEngine(unittest.TestCase):

    def setUp(self):
        self.engine = RecommendationEngine()

        self.products = [
            {"product_id": 1, "rating": 4.5},
            {"product_id": 2, "rating": 4.0},
            {"product_id": 3, "rating": 5.0},
            {"product_id": 4, "rating": 3.5},
            {"product_id": 5, "rating": 4.8}
        ]

    def test_basic_recommendation(self):
        user = {
            "user_id": 1,
            "purchases": [1]
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        self.assertEqual(results[0]["product_id"], 3)

    def test_limit_results(self):
        user = {
            "user_id": 1,
            "purchases": []
        }

        results = self.engine.generate_recommendations(
            user,
            self.products,
            limit=2
        )

        self.assertEqual(len(results), 2)

if __name__ == "__main__":
    unittest.main()
