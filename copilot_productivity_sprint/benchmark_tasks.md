# Benchmark Tasks

## Task 1 - Expense CRUD API

**Requirements:**  
Implement CRUD operations for expense management.

**Inputs:**  
- Expense amount
- Category
- Description
- Date

**Outputs:**  
- Created expense record
- Updated expense record
- Deleted expense confirmation

**Acceptance Criteria:**  
- Returns HTTP 201 on creation
- Returns HTTP 200 on retrieval
- Returns HTTP 404 for invalid IDs
- Validates positive expense amounts


---

## Task 2 - Budget Alert System

**Requirements:**  
Create a system that monitors budgets and generates alerts when limits are exceeded.

**Inputs:**  
- Budget limit
- Expense transactions
- Budget category

**Outputs:**  
- Remaining budget amount
- Overspending alert
- Budget summary

**Acceptance Criteria:**  
- Calculates remaining budget correctly
- Sends alerts when spending exceeds limit
- Updates totals after new expenses
- Prevents negative budget values


---

## Task 3 - Savings Goal Tracker

**Requirements:**  
Develop a module that tracks savings progress toward financial targets.

**Inputs:**  
- Goal name
- Target amount
- Current savings amount

**Outputs:**  
- Savings progress percentage
- Remaining target amount
- Goal completion status

**Acceptance Criteria:**  
- Calculates progress accurately
- Updates progress automatically
- Prevents invalid target amounts
- Displays completed goals correctly