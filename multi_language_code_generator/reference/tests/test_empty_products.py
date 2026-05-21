from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

results = engine.generate_recommendations(
    {"user_id": 1, "purchases": []},
    []
)

assert results == []
