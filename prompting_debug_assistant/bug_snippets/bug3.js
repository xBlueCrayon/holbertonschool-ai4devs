function isEven(num) {
    // Check if a number is even
    return num % 2 == 1; // BUG: should be num % 2 == 0
}

// Test numbers
let testNumbers = [0, 1, 2, 3, 4, 5];
for (let i = 0; i < testNumbers.length; i++) {
    console.log(testNumbers[i], "is even?", isEven(testNumbers[i]));
}
