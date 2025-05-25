package com.example;

public class StringUtils {

    public boolean isPalindrome(String input) {
        if (input == null) return false;
        String cleaned = input.replaceAll("[^a-zA-Z]", "").toLowerCase();
        String reversed = new StringBuilder(cleaned).reverse().toString();
        return cleaned.equals(reversed);
    }

    public String reverse(String input) {
        if (input == null) return null;
        return new StringBuilder(input).reverse().toString();
    }

    public int countVowels(String input) {
        if (input == null) return 0;
        return (int) input.toLowerCase().chars()
                .filter(c -> "aeiou".indexOf(c) >= 0)
                .count();
    }
}




