function calculateAverage(numbers) {
    let total = 0;

    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }

    return total / (numbers.length - 1);
}

const values = [10, 20, 30, 40];

console.log(calculateAverage(values));
