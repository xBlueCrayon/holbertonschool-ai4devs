from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": -5}
]

scores = engine.calculate_popularity(products)

assert scores[1] == 0
