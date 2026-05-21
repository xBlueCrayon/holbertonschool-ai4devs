from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": "bad"}
]

scores = engine.calculate_popularity(products)

assert scores[1] == 0
