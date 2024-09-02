import sys
from collections import defaultdict

# Braille dictionary for letters, numbers, capitalization, and spaces
english_to_braille_map = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", "cap": ".....O", "num": ".O.OOO", " ": "......",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
}

# Create a reverse dictionary dynamically
braille_to_english_map = defaultdict(list)
for letter, braille in english_to_braille_map.items():
    braille_to_english_map[braille].append(letter)

def is_braille_input(text):
    # Check if input is Braille or English
    return all(char in "O." for char in text) and len(text) % 6 == 0

def translate_english_to_braille(text):
    result = []
    is_number_mode = False
    
    for char in text:
        if char.isdigit():
            if not is_number_mode:
                result.append(english_to_braille_map["num"])
                is_number_mode = True
            result.append(english_to_braille_map[char])
        else:
            if char == " ":
                is_number_mode = False  # Reset number mode after a space
            if char.isupper():
                result.append(english_to_braille_map["cap"])
                char = char.lower()
            result.append(english_to_braille_map[char])
    
    return "".join(result)

def translate_braille_to_english(braille_text):
    result = []
    is_capital_mode = False
    is_number_mode = False
    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i+6]
        possible_characters = braille_to_english_map.get(braille_char, [])
        
        if braille_char == english_to_braille_map["cap"]:
            is_capital_mode = True
        elif braille_char == english_to_braille_map["num"]:
            is_number_mode = True
        elif braille_char == english_to_braille_map[" "]:
            is_number_mode = False  # Reset number flag after a space
            result.append(" ")
        else:
            if is_number_mode:
                # If number mode is active, get the digit
                digit = next((c for c in possible_characters if c.isdigit()), "")
                result.append(digit)
            else:
                # Otherwise, get the letter
                letter = next((c for c in possible_characters if c.isalpha()), "")
                if is_capital_mode:
                    letter = letter.upper()
                    is_capital_mode = False
                result.append(letter)
    return "".join(result)

def main():
    if len(sys.argv) < 2:
        print("Please provide input text.")
        return
    
    input_text = " ".join(sys.argv[1:])
    
    if is_braille_input(input_text):
        output = translate_braille_to_english(input_text)
    else:
        output = translate_english_to_braille(input_text)
    
    print(output)

if __name__ == "__main__":
    main()
