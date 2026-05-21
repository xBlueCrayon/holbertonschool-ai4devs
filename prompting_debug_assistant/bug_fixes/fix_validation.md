# Fix Validation Report

## Bug 1 - bug1_fixed.py

- **Input:** items = [1,2,3,4,5], n = 2
- **Expected Output:** [4,5]
- **Actual Output:** [4,5] ✅
- **Test Result:** PASS

### Notes
The loop boundary was corrected to avoid accessing an invalid list index.


---

## Bug 2 - bug2_fixed.py

- **Input:** numbers = [10,20,30], divisor = 2
- **Expected Output:** [5.0,10.0,15.0]
- **Actual Output:** [5.0,10.0,15.0] ✅
- **Test Result:** PASS

### Notes
Validation was added to prevent division by zero.


---

## Bug 3 - bug3_fixed.js

- **Input:** [10,20,30,40]
- **Expected Output:** 25
- **Actual Output:** 25 ✅
- **Test Result:** PASS

### Notes
The average formula was corrected by dividing using the proper array length.


---

## Bug 4 - bug4_fixed.js

- **Input:** "100", 50
- **Expected Output:** 150
- **Actual Output:** 150 ✅
- **Test Result:** PASS

### Notes
The values are now converted to numbers before addition.


---

## Bug 5 - bug5_fixed.c

- **Input:** Array with 5 elements
- **Expected Output:** Print values 1 to 5 safely
- **Actual Output:** Values printed correctly ✅
- **Test Result:** PASS

### Notes
The loop boundary was corrected to prevent invalid memory access.


---

## Bug 6 - bug6_fixed.py

- **Input:** "Akshay"
- **Expected Output:** Hello, Akshay
- **Actual Output:** Hello, Akshay ✅
- **Test Result:** PASS

### Notes
The missing colon was added to the function definition.