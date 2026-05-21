from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.1},
    {"product_id": 2, "rating": 4.2},
    {"product_id": 3, "rating": 4.3}
]

user = {
    "user_id": 5,
    "purchases": [1]
}

results = engine.generate_recommendations(
    user,
    products
)

assert len(results) == 2
