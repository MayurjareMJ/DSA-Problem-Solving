# 🧮 12. Integer to Roman
# Difficulty: Medium
# Topics: String, Math, Hash Table
# Problem Statement

# Roman numerals are represented by seven different symbols with the following values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

# Roman numerals are formed by combining symbols and adding their values.
# However, certain numbers use subtractive notation:

# IV = 4 (one less than 5)

# IX = 9 (one less than 10)

# XL = 40 (ten less than 50)

# XC = 90 (ten less than 100)

# CD = 400 (one hundred less than 500)

# CM = 900 (one hundred less than 1000)

# Only the symbols I, X, C, and M can be repeated up to three times in succession.

# Task

# Given an integer num, convert it to a Roman numeral.

# Example 1:

# Input:

# num = 3749


# Output:

# "MMMDCCXLIX"


# Explanation:

# 3000 → MMM

# 700 → DCC

# 40 → XL

# 9 → IX
# → Combined: "MMMDCCXLIX"

# Example 2:

# Input:

# num = 58


# Output:

# "LVIII"


# Explanation:
# 50 → L, 8 → VIII, combined → "LVIII"

# Example 3:

# Input:

# num = 1994


# Output:

# "MCMXCIV"


# Explanation:
# 1000 → M
# 900 → CM
# 90 → XC
# 4 → IV
# → "MCMXCIV"

# Constraints:

# 1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of integer values to their Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman = ""
        i = 0
        
        # Build the Roman numeral
        while num > 0:
            count = num // val[i]
            roman += syms[i] * count
            num -= val[i] * count
            i += 1
        
        return roman
