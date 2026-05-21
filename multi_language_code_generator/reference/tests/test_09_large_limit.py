import sys
sys.path.append("..")

from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 4.5},
    {"product_id": 2, "rating": 4.8}
]

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products,
    limit=20
)

assert len(results) <= 20
