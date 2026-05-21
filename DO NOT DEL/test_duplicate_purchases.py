from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.5},
    {"product_id": 2, "rating": 5.0}
]

user = {
    "user_id": 1,
    "purchases": [1, 1]
}

results = engine.generate_recommendations(user, products)

ids = [item["product_id"] for item in results]

assert 1 not in ids
