public class Bug5 {
    public static void main(String[] args) {
        // Store an integer as a String
        String text = 123; // BUG: type mismatch
        System.out.println(text);

        int correctNumber = 123;
        System.out.println("Correct number: " + correctNumber);

        // Additional example
        String anotherText = "456";
        System.out.println("Another text: " + anotherText);
    }
}
