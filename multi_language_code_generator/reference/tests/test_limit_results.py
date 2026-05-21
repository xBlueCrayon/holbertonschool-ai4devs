from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 5.0},
    {"product_id": 2, "rating": 4.0}
]

results = engine.generate_recommendations(
    {"user_id": 1, "purchases": []},
    products,
    limit=1
)

assert len(results) == 1
