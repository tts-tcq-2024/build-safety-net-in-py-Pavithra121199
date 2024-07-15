#Global mapping for soundex codes
mapping = {
    'B': '1', 'F': '1', 'P': '1', 'V': '1',
    'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}

def get_soundex_code(c):
    c = c.upper()
    return mapping.get(c, '')                 # Default to '' for non-mapped characters

def initialize_soundexcode_withfirstletter(soundex, first_letter):
    soundex.append(first_letter.upper())

def is_non_mapped_character(c):
    return get_soundex_code(c) == ''

def is_same_code_and_not_separated(code, previous_code, previous_char):
    return code == previous_code and previous_char not in 'AEIOU'

def process_single_character(current_char, previous_char, soundex, s_index, previous_code):
    code = get_soundex_code(current_char)
    prev_code = previous_code[0]
    if is_non_mapped_character(current_char):
        return
    if is_same_code_and_not_separated(code, prev_code, previous_char):
        return
    soundex.append(code)
    s_index[0] += 1
    previous_code[0] = code
	
def process_allcharacters(name, soundex, s_index, previous_code):
    previous_char = name[0].upper()
    for i in range(1, len(name)):
        if s_index[0] >= 4:
            break
        current_char = name[i].upper()
        process_single_character(current_char, previous_char, soundex, s_index, previous_code)
        previous_char = current_char

def pad_with_zeros(soundex, s_index):
    while s_index[0] < 4:
        soundex.append('0')
        s_index[0] += 1

def generate_soundex(name):            
    if not name:
        return "0000"         # for empty string
    soundex = []
    initialize_soundexcode_withfirstletter(soundex, name[0])
    previous_code = [get_soundex_code(name[0])]
    s_index = [1]

    process_allcharacters(name, soundex, s_index, previous_code)
    pad_with_zeros(soundex, s_index)

    return ''.join(soundex[:4])               # Ensure the output is exactly 4 characters
