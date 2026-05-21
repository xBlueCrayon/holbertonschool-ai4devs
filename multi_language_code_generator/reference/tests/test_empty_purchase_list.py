from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.5},
    {"product_id": 2, "rating": 4.9}
]

user = {
    "user_id": 55,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products
)

assert len(results) == 2
assert results[0]["product_id"] == 2
