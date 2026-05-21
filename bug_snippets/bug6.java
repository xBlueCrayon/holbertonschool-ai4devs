public class Bug6 {
    public static void main(String[] args) {
        // Print numbers 0 to 4
        for (int i = 0; i <= 5; i++) { // BUG: should be i < 5
            System.out.println("Count: " + i);
        }

        // Another loop example
        for (int j = 0; j < 3; j++) {
            System.out.println("Secondary count: " + j);
        }
    }
}