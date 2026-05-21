from multi_language_code_generator.reference.tests.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.5}
]

results = engine.generate_recommendations(
    {},
    products
)

assert len(results) == 1
