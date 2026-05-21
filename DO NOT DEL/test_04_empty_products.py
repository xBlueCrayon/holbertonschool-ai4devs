import sys
sys.path.append("..")

from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

user = {
    "user_id": 1,
    "purchases": []
}

results = engine.generate_recommendations(user, [])

assert results == []
