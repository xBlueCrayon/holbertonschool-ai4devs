public class bug3_fixed {

    public static int findMax(int[] numbers) {

        int max = numbers[0];

        for (int i = 0; i < numbers.length; i++) {

            if (numbers[i] > max) {
                max = numbers[i];
            }
        }

        return max;
    }

    public static void main(String[] args) {

        int[] values = {4, 7, 2, 9, 1};

        int result = findMax(values);

        System.out.println("Max value: " + result);
    }
}