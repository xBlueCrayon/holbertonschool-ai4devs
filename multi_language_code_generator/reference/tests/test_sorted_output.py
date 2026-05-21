from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 2.0},
    {"product_id": 2, "rating": 5.0},
    {"product_id": 3, "rating": 4.0}
]

user = {
    "user_id": 99,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products
)

assert results[0]["product_id"] == 2
assert results[1]["product_id"] == 3
assert results[2]["product_id"] == 1
