import unittest

from recommendation_engine import RecommendationEngine


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

    def test_generate_recommendations(self):
        user = {
            "user_id": 1,
            "purchases": [1]
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        self.assertTrue(len(results) > 0)

    def test_exclude_purchased_products(self):
        user = {
            "user_id": 1,
            "purchases": [1, 2]
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        ids = [item["product_id"] for item in results]

        self.assertNotIn(1, ids)
        self.assertNotIn(2, ids)

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

    def test_empty_purchases(self):
        user = {
            "user_id": 1,
            "purchases": []
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        self.assertTrue(len(results) > 0)

    def test_all_products_purchased(self):
        user = {
            "user_id": 1,
            "purchases": [1, 2, 3, 4, 5]
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        self.assertEqual(len(results), 0)

    def test_negative_rating(self):
        products = [
            {"product_id": 1, "rating": -5}
        ]

        scores = self.engine.calculate_popularity(products)

        self.assertEqual(scores[1], 0)

    def test_sorting_order(self):
        user = {
            "user_id": 1,
            "purchases": []
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        self.assertGreaterEqual(
            results[0]["score"],
            results[1]["score"]
        )

    def test_missing_rating(self):
        products = [
            {"product_id": 1}
        ]

        scores = self.engine.calculate_popularity(products)

        self.assertEqual(scores[1], 0)

    def test_large_limit(self):
        user = {
            "user_id": 1,
            "purchases": []
        }

        results = self.engine.generate_recommendations(
            user,
            self.products,
            limit=20
        )

        self.assertTrue(len(results) <= 20)

    def test_duplicate_purchases(self):
        user = {
            "user_id": 1,
            "purchases": [1, 1, 2]
        }

        results = self.engine.generate_recommendations(
            user,
            self.products
        )

        ids = [item["product_id"] for item in results]

        self.assertNotIn(1, ids)
        self.assertNotIn(2, ids)


if __name__ == "__main__":
    unittest.main()
