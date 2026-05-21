# Bug Reports

## Bug Report - bug1.py

- **File Name:** bug1.py

- **Bug Summary:**  
  The function attempting to retrieve the last items of a list caused an IndexError.

- **Root Cause:**  
  The loop exceeded the valid list index range because it used:

  ```python
  range(start_index, len(items) + 1)
  ```

  which accessed one position beyond the last valid index.

- **Resolution:**  
  The AI suggested changing the loop condition to:

  ```python
  range(start_index, len(items))
  ```

  Manual testing confirmed the fix worked correctly.

- **Lessons Learned:**  
  Always verify loop boundaries when working with list indices to avoid off-by-one errors.


---

## Bug Report - bug2.py

- **File Name:** bug2.py

- **Bug Summary:**  
  The program crashed during execution with a ZeroDivisionError.

- **Root Cause:**  
  The divisor value passed into the function was zero, causing division by zero during runtime.

- **Resolution:**  
  The AI suggested validating the divisor before performing division:

  ```python
  if divisor == 0:
      return []
  ```

  Additional manual testing confirmed the function handled invalid divisors safely.

- **Lessons Learned:**  
  Input validation is important to prevent runtime exceptions and unexpected crashes.


---

## Bug Report - bug3.js

- **File Name:** bug3.js

- **Bug Summary:**  
  The average calculation returned incorrect results.

- **Root Cause:**  
  The total was divided by:

  ```javascript
  numbers.length - 1
  ```

  instead of the actual number of elements in the array.

- **Resolution:**  
  The AI suggested replacing the formula with:

  ```javascript
  total / numbers.length
  ```

  Manual verification confirmed the average calculation became accurate.

- **Lessons Learned:**  
  Mathematical formulas should always be verified carefully during debugging.


---

## Bug Report - bug4.js

- **File Name:** bug4.js

- **Bug Summary:**  
  The function concatenated values instead of adding them numerically.

- **Root Cause:**  
  One of the input values was a string:

  ```javascript
  const item1 = "100";
  ```

  which caused JavaScript to perform string concatenation.

- **Resolution:**  
  The AI suggested converting values to numbers before addition:

  ```javascript
  Number(price1) + Number(price2)
  ```

  Manual testing verified the output was now numeric.

- **Lessons Learned:**  
  Data types should always be validated before performing operations in JavaScript.


---

## Bug Report - bug5.c

- **File Name:** bug5.c

- **Bug Summary:**  
  The program accessed memory outside the array boundary.

- **Root Cause:**  
  The loop condition:

  ```c
  i <= 5
  ```

  attempted to access index 5 in an array containing only indices 0 to 4.

- **Resolution:**  
  The AI suggested changing the loop condition to:

  ```c
  i < 5
  ```

  Additional testing confirmed the array printed safely without invalid memory access.

- **Lessons Learned:**  
  Array boundaries must always be handled carefully in C to avoid undefined behavior.


---

## Bug Report - bug6.py

- **File Name:** bug6.py

- **Bug Summary:**  
  The Python program failed to execute because of a syntax error.

- **Root Cause:**  
  The function definition was missing a colon:

  ```python
  def greet_user(name)
  ```

- **Resolution:**  
  The AI suggested adding the missing colon:

  ```python
  def greet_user(name):
  ```

  Manual verification confirmed the script executed correctly afterward.

- **Lessons Learned:**  
  Small syntax mistakes can prevent an entire program from running and should be checked carefully.