function calculateAverage(numbers) {
    let total = 0;

    console.log("Calculating average");

    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }

    console.log("Total is:", total);

    return total / (numbers.length - 1);
}

const values = [10, 20, 30, 40];

console.log(calculateAverage(values));
