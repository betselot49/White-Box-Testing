def count_vowels_and_consonants(text):
    vowels = 'aeiouAEIOU'  # d1: vowels
    v_count = 0            # d2: v_count
    c_count = 0            # d3: c_count
    for char in text:      # p-use: text
        if char.isalpha(): # p-use: char
            if char in vowels:  # p-use: char, vowels
                v_count += 1    # c-use: v_count | d4: v_count updated
            else:
                c_count += 1    # c-use: c_count | d5: c_count updated
    return v_count, c_count     # c-use: v_count, c_count



