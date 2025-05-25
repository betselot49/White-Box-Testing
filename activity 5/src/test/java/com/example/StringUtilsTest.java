package com.example;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;

public class StringUtilsTest {

    StringUtils utils = new StringUtils();

    @Test
    @DisplayName("testIsPalindrome_True")
    public void testIsPalindrome_True() {
        assertTrue(utils.isPalindrome("Madam"));
        assertTrue(utils.isPalindrome("A man, a plan, a canal, Panama"));
        System.out.println("✓ testIsPalindrome_True()    → Passed");
    }

    @Test
    @DisplayName("testIsPalindrome_False")
    public void testIsPalindrome_False() {
        assertFalse(utils.isPalindrome("Hello"));
        assertFalse(utils.isPalindrome(null));
        System.out.println("✓ testIsPalindrome_False()   → Passed");
    }

    @Test
    @DisplayName("testReverse")
    public void testReverse() {
        assertEquals("olleH", utils.reverse("Hello"));
        assertEquals("321", utils.reverse("123"));
        assertNull(utils.reverse(null));
        System.out.println("✓ testReverse()              → Passed");
    }

    @Test
    @DisplayName("testCountVowels")
    public void testCountVowels() {
        assertEquals(2, utils.countVowels("Hello"));
        assertEquals(5, utils.countVowels("education"));
        assertEquals(0, utils.countVowels("bcdfg"));
        assertEquals(0, utils.countVowels(null));
        System.out.println("✓ testCountVowels()          → Passed");
    }
}
