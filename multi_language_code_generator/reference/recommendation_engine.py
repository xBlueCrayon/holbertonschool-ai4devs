class RecommendationEngine:

    def __init__(self):
        pass

    def calculate_popularity(self, products):
        popularity_scores = {}

        for product in products:
            product_id = product["product_id"]
            rating = product.get("rating", 0)

            if rating < 0:
                rating = 0

            popularity_scores[product_id] = rating

        return popularity_scores

    def generate_recommendations(self, user_data, products, limit=5):

        purchases = set(user_data.get("purchases", []))

        popularity_scores = self.calculate_popularity(products)

        recommendations = []

        for product in products:

            product_id = product["product_id"]

            if product_id not in purchases:

                recommendations.append({
                    "product_id": product_id,
                    "score": popularity_scores[product_id]
                })

        recommendations.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return recommendations[:limit]


if __name__ == "__main__":

    user_data = {
        "user_id": 101,
        "purchases": [12, 15]
    }

    products = [
        {"product_id": 12, "rating": 4.2},
        {"product_id": 15, "rating": 4.8},
        {"product_id": 20, "rating": 4.9},
        {"product_id": 25, "rating": 4.5},
        {"product_id": 30, "rating": 4.7}
    ]

    engine = RecommendationEngine()

    recommendations = engine.generate_recommendations(
        user_data,
        products
    )

    print(recommendations)
