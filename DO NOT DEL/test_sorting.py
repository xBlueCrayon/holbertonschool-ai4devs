from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.0},
    {"product_id": 2, "rating": 5.0}
]

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(user, products)

assert results[0]["score"] >= results[1]["score"]
