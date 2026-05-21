# AI Debug Log

## Bug 1 - bug1.py

**Prompt Used:**  
This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis:**  
The loop exceeds the valid list index range and causes an IndexError.

**Suggested Fix:**  

Change:

```python
for i in range(start_index, len(items) + 1):
```

to:

```python
for i in range(start_index, len(items)):
```

**Alternative Fixes Tested:**  
Used Python slicing:

```python
return items[-n:]
```

**Result:**  
The fix works correctly and returns the expected list items.


---

## Bug 2 - bug2.py

**Prompt Used:**  
This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis:**  
The code raises a ZeroDivisionError because the divisor is zero.

**Suggested Fix:**  

Add validation before division:

```python
if divisor == 0:
    return []
```

**Alternative Fixes Tested:**  
Used try/except exception handling.

**Result:**  
The fix prevents the runtime crash successfully.


---

## Bug 3 - bug3.js

**Prompt Used:**  
This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis:**  
The average calculation divides by the wrong value.

**Suggested Fix:**  

Change:

```javascript
return total / (numbers.length - 1);
```

to:

```javascript
return total / numbers.length;
```

**Alternative Fixes Tested:**  
Stored the array length in a separate variable.

**Result:**  
The function now calculates the correct average.


---

## Bug 4 - bug4.js

**Prompt Used:**  
This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis:**  
The function performs string concatenation instead of numeric addition.

**Suggested Fix:**  

Convert both values to numbers:

```javascript
let total = Number(price1) + Number(price2);
```

**Alternative Fixes Tested:**  
Used parseInt() conversion.

**Result:**  
The function now returns the correct numeric result.


---

## Bug 5 - bug5.c

**Prompt Used:**  
This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis:**  
The loop accesses memory outside the array boundary.

**Suggested Fix:**  

Change:

```c
for (int i = 0; i <= 5; i++)
```

to:

```c
for (int i = 0; i < 5; i++)
```

**Alternative Fixes Tested:**  
Used sizeof() to calculate array length dynamically.

**Result:**  
The program now safely prints all array elements.


---

## Bug 6 - bug6.py

**Prompt Used:**  
This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?

**AI Diagnosis:**  
The function definition is missing a colon, causing a SyntaxError.

**Suggested Fix:**  

Change:

```python
def greet_user(name)
```

to:

```python
def greet_user(name):
```

**Alternative Fixes Tested:**  
Checked indentation and function formatting.

**Result:**  
The program now runs correctly and prints the greeting message.
