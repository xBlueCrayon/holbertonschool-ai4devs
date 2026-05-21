from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.5}
]

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products,
    limit=0
)

assert results == []
