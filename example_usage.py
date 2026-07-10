"""
example_usage.py -- Demonstrates CustomProductRecommenderClient
"""
from client import CustomProductRecommenderClient

def main():
    client = CustomProductRecommenderClient()
    result = client.match_quiz(
        quiz_responses={"skin_type": "dry", "concern": "aging"},
        catalog=[
            {"id": "p1", "tags": ["dry", "aging", "serum"]},
            {"id": "p2", "tags": ["oily", "acne"]}
        ]
    )
    print("[Quiz Match Result]")
    print(f"Product: {result['recommended_product_id']} | Confidence: {result['match_percentage']}%")

if __name__ == "__main__":
    main()
