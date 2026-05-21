# Cross-Language Specification - Recommendation Engine

## Algorithm Description

The recommendation engine analyzes user purchase history and product ratings to generate personalized product recommendations.

The algorithm performs the following operations:
- Reads user purchase and rating data
- Calculates product popularity scores
- Identifies similar user preferences
- Generates top recommended products
- Excludes already purchased items

The implementation should be compatible across multiple programming languages such as Python, JavaScript, Java, and C#.

---

## Input Format

The algorithm accepts the following input structure:

### User Data

```json
{
  "user_id": 101,
  "purchases": [12, 15, 18],
  "ratings": {
    "12": 4,
    "15": 5,
    "18": 3
  }
}
```

### Product Dataset

```json
[
  {
    "product_id": 20,
    "category": "Electronics",
    "rating": 4.5
  }
]
```

### Input Rules

- User IDs must be integers
- Product IDs must be unique
- Ratings must range from 1 to 5
- Purchase lists may be empty
- Product datasets may contain thousands of entries

---

## Output Format

The algorithm returns a ranked recommendation list.

### Example Output

```json
{
  "user_id": 101,
  "recommendations": [
    {
      "product_id": 22,
      "score": 0.95
    },
    {
      "product_id": 31,
      "score": 0.89
    }
  ]
}
```

### Output Rules

- Recommendations must be sorted by score descending
- Already purchased products must not appear
- Maximum recommendation count should be configurable
- Empty recommendations should return an empty list

---

## Edge Cases

### Empty Purchase History

Users without purchase history should receive popular trending products.

### Missing Ratings

Products without ratings should receive default scoring values.

### Duplicate Purchases

Duplicate product entries should be ignored during recommendation calculations.

### Large Datasets

The algorithm must support large datasets efficiently without excessive memory usage.

### Invalid Rating Values

Ratings outside the range 1–5 must be rejected or normalized.

### Unknown Product IDs

Missing product records should be skipped safely without application crashes.

---

## Test Cases

### Test Case 1 - Normal Recommendation

**Input:**  
- User purchases: [12, 15]
- Product ratings available

**Expected Output:**  
- Ranked recommendation list excluding purchased products

---

### Test Case 2 - Empty Purchase History

**Input:**  
- User purchases: []

**Expected Output:**  
- Trending or highest-rated products returned

---

### Test Case 3 - Duplicate Purchases

**Input:**  
- Purchases: [12, 12, 15]

**Expected Output:**  
- Duplicate products processed only once

---

### Test Case 4 - Invalid Ratings

**Input:**  
- Rating value: 8

**Expected Output:**  
- Validation error or normalized rating

---

### Test Case 5 - Large Dataset Processing

**Input:**  
- 100,000 products
- 1 million ratings

**Expected Output:**  
- Recommendations generated within acceptable response time

---

### Test Case 6 - Unknown Product ID

**Input:**  
- Product ID not found in dataset

**Expected Output:**  
- Missing products skipped safely

---

## Performance Requirements

- Recommendation generation under 2 seconds for standard datasets
- Memory-efficient processing for large datasets
- Scalable for concurrent recommendation requests

---

## Cross-Language Compatibility Requirements

### Python
- Use dictionaries and list comprehensions efficiently
- Avoid excessive nested loops

### JavaScript
- Use asynchronous processing when necessary
- Support Node.js runtime environments

### Java
- Use object-oriented design principles
- Optimize collection handling

### C#
- Use LINQ for filtering and sorting
- Support asynchronous task execution

---

## Validation Rules

- Input JSON must follow schema format
- Product IDs must exist in dataset
- Scores must range between 0.0 and 1.0
- Recommendation count must not exceed configured limits

---

## Summary

This cross-language specification defines a scalable recommendation engine capable of generating personalized product suggestions consistently across multiple programming languages and runtime environments while handling validation, performance, and edge-case requirements.