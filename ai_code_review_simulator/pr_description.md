# Pull Request: Add Expense Category Filtering Feature

## Summary

This pull request introduces a new expense category filtering feature for the expense tracking application. Users can now filter expenses dynamically based on categories such as Food, Transport, Utilities, Entertainment, and Health.

The feature improves usability by helping users quickly locate specific expense records and analyze spending habits more efficiently.

---

## Feature Overview

The new functionality includes:

- Category-based filtering
- Dynamic filtering logic
- Improved expense retrieval workflow
- Input validation for filter parameters
- Support for empty and invalid filter cases
- Unit tests for filtering behavior

Estimated implementation size: ~150 LOC.

---

## Changes

### Added

- `filter_expenses()` function in `expenses.py`
- Category validation logic
- Filtering support for:
  - Food
  - Transport
  - Utilities
  - Entertainment
  - Health
  - Other
- New helper method for category normalization

### Updated

- Expense retrieval logic
- Existing expense list processing
- Validation handling for unknown categories

### Tests Added

- Filter by single category
- Filter with multiple expenses
- Empty category handling
- Invalid category validation
- No matching results scenario

---

## Example Implementation

```python
def filter_expenses(expenses, category):

    if not category:
        return expenses

    normalized = category.strip().lower()

    return [
        expense
        for expense in expenses
        if expense["category"].lower() == normalized
    ]
```

---

## Motivation

Users previously had to manually scan all expense entries to locate records belonging to a specific category. This became inefficient as datasets grew larger.

The filtering feature improves:

- User productivity
- Expense analysis
- Dashboard usability
- Financial reporting accuracy

---

## Context

Related issue: #27

The feature was requested during testing of the expense tracker dashboard where users reported difficulty locating category-specific expenses quickly.

The implementation follows existing project coding standards and preserves backward compatibility.

---

## Validation

### Manual Testing

- Tested with multiple expense categories
- Tested with empty expense lists
- Tested invalid category values
- Confirmed existing expense retrieval still works

### Automated Testing

All existing and new tests pass successfully.

Coverage includes:

- Valid filtering
- Invalid filtering
- Edge cases
- Empty datasets
- Mixed category datasets

---

## Files Added / Modified

### Added

- `expenses.py`
- `tests/test_filter_expenses.py`

### Modified

- `dashboard.py`
- `expense_service.py`

---

## Expected Outcome

Users can now:

- Filter expenses instantly
- Improve spending analysis
- Reduce time spent searching records
- View cleaner dashboards

---

## Final Notes

The feature is lightweight, backward compatible, and designed for future expansion such as:

- Multi-category filtering
- Date + category combined filters
- Advanced search functionality
- Dashboard analytics integration