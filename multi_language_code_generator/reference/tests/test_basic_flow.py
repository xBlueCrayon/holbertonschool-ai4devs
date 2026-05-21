from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 10, "rating": 4.9},
    {"product_id": 20, "rating": 4.2}
]

user = {
    "user_id": 2,
    "purchases": []
}

results = engine.generate_recommendations(user, products)

assert len(results) > 0
