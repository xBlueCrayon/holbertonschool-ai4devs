from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

products = []

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(user, products)

assert results == []
