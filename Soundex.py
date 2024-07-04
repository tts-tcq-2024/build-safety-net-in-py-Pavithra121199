
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
    return mapping.get(c, '0')         # Default to '0' for non-mapped characters

def initialize_soundex(soundex, first_letter):    #Initializes the Soundex code with the first letter of the name
    soundex[0] = first_letter.upper()

def handle_singlecharacter(current_char, soundex, s_index, previous_code):   # Handles processing of a single character to append its Soundex code to soundex
    code = get_soundex_code(current_char)
    if code != '0' and code != previous_code[0]:
        soundex[s_index[0]] = code
        s_index[0] += 1
        previous_code[0] = code

def process_singlecharacter(name, soundex, s_index, previous_code):  # Processes each character in name to generate its Soundex code and append to soundex
    for i in range(1, len(name)):
        if s_index[0] >= 4:
            break
        handle_singlecharacter(name[i], soundex, s_index, previous_code)

def pad_with_zeros(soundex, s_index):    #Fills the remaining positions in soundex with '0'
    while s_index[0] < 4:
        soundex[s_index[0]] = '0'
        s_index[0] += 1

def generate_soundex(name):      #Generates the Soundex code for a given name
    if not name:
        return ""
    soundex = [''] * 4
    initialize_soundex(soundex, name[0])
    previous_code = ['']
    s_index = [1]
    process_singlecharacter(name, soundex, s_index, previous_code)
    pad_with_zeros(soundex, s_index)
    return ''.join(soundex)
