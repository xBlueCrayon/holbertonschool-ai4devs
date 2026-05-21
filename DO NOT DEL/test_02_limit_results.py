import sys
sys.path.append("..")

from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = [
    {"product_id": 1, "rating": 5.0},
    {"product_id": 2, "rating": 4.8},
    {"product_id": 3, "rating": 4.6}
]

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(
    user,
    products,
    limit=2
)

assert len(results) == 2
