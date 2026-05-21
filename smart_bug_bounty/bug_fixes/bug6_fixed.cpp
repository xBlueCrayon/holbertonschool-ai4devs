#include <iostream>

using namespace std;

int countEvenNumbers(int values[], int size) {

    int count = 0;

    for (int i = 0; i < size; i++) {

        if (values[i] % 2 == 0) {
            count++;
        }
    }

    return count;
}

int main() {

    int numbers[] = {2, 5, 8, 11, 14};

    int size = 5;

    int result = countEvenNumbers(numbers, size);

    cout << "Even numbers: " << result << endl;

    return 0;
}