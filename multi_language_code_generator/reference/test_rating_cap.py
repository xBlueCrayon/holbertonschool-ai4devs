from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 10}
]

scores = engine.calculate_popularity(products)

assert scores[1] == 5
