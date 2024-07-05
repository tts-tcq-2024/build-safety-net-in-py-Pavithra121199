def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '')                 # Default to '' for non-mapped characters

def initialize_soundex(soundex, first_letter): #Initializes the Soundex code with the first letter of the name.
    soundex.append(first_letter.upper())

def process_single_character(current_char, previous_char, soundex, s_index, previous_code):
    current_code = get_soundex_code(current_char)
    previous_code_value = previous_code[0]
    if current_code == '':                   # Skip if it is a non-mapped character
        return
    if current_code == previous_code_value and not (
            previous_char in 'AEIOU' or (previous_char in 'HWY' and previous_char)):               # Skip if current code is the same as the previous and not separated by a vowel or HWY
        return

    soundex.append(current_code)
    s_index[0] += 1
    previous_code[0] = current_code

def process_single_character(current_char, previous_char, soundex, s_index, previous_code):    
    code = get_soundex_code(current_char)
    prev_code = get_soundex_code(previous_char)

    if code == '':                         # Skip if it is a non-mapped character
        return 
	
    if code == previous_code[0] and previous_char not in 'AEIOU':        # Skip if current code is the same as the previous and not separated by a vowel
    	return
    soundex.append(code)
    s_index[0] += 1
    previous_code[0] = code

def process_characters(name, soundex, s_index, previous_code):
    previous_char = name[0].upper()
    for i in range(1, len(name)):
        if s_index[0] >= 4:
            break
        current_char = name[i].upper()
        process_single_character(current_char, previous_char, soundex, s_index, previous_code)
        previous_char = current_char

def pad_with_zeros(soundex, s_index):             #Fills the remaining positions in soundex with '0'.
    while s_index[0] < 4:
        soundex.append('0')
        s_index[0] += 1

def generate_soundex(name):             # Generates the Soundex code for a given name.
    if not name:
        return "0000"  # Return "0000" for empty names

    soundex = []
    initialize_soundex(soundex, name[0])
    previous_code = [get_soundex_code(name[0])]
    s_index = [1]

    process_characters(name, soundex, s_index, previous_code)
    pad_with_zeros(soundex, s_index)

    return ''.join(soundex[:4])  # Ensure the output is exactly 4 characters
