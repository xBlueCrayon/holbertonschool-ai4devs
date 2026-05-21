from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 5.0},
    {"product_id": 2, "rating": 4.5}
]

user = {
    "user_id": 10,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products
)

assert isinstance(results, list)
assert results[0]["product_id"] == 1
