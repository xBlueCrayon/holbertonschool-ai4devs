from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"rating": 4.5},
    {"product_id": 2, "rating": 5.0}
]

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products
)

assert len(results) == 1
assert results[0]["product_id"] == 2
