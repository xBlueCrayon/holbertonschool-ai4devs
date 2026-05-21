from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.5},
    {"product_id": 2, "rating": 4.8}
]

user = {
    "user_id": 1,
    "purchases": [1, 2]
}

results = engine.generate_recommendations(user, products)

assert results == []
