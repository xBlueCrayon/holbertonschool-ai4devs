from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 100, "rating": 5.0}
]

user = {
    "user_id": 77,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products
)

assert len(results) == 1
assert results[0]["product_id"] == 100
