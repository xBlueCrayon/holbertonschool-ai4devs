## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error  
**Notes**: The function fails when n == len(items).

## Bug 2 - bug2.py
**Intended Behavior**: Divide a by b safely.  
**Issue Type**: Runtime exception  
**Notes**: Division by zero triggers an exception.

## Bug 3 - bug3.js
**Intended Behavior**: Check if a number is even.  
**Issue Type**: Logical error  
**Notes**: Returns the opposite result because of incorrect modulo logic.

## Bug 4 - bug4.js
**Intended Behavior**: Print the array of numbers.  
**Issue Type**: Syntax error  
**Notes**: Missing closing bracket causes syntax failure.

## Bug 5 - bug5.java
**Intended Behavior**: Store an integer as a string and print it.  
**Issue Type**: Misuse of data types  
**Notes**: Causes compile-time type error because an integer is assigned to a String.

## Bug 6 - bug6.java
**Intended Behavior**: Print numbers from 0 to 4.  
**Issue Type**: Loop logic error  
**Notes**: Uses <= instead of <, prints an extra number.