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

def initialize_soundexcode(name):      #Function to initialize the Soundex code with the first letter of the name.    
    if not name:
        return ""
    return name[0].upper()

def append_soundex_codes(soundex, name):        # Function to append Soundex codes for characters in name to soundex
    prev_code = get_soundex_code(soundex[0])
    for char in name[1:]:
        if len(soundex) >= 4:
            break       
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code

def padwithzeros_soundex(soundex):         # Function to pad soundex with zeros to ensure it is exactly 4 characters long.
    return soundex.ljust(4, '0')

def generate_soundex(name):       # Function to generate the Soundex code for a given name
    soundex = initialize_soundexcode(name)
    if not soundex:
        return "0000"      
    append_soundex_codes(soundex, name)
    return padwithzeros_soundex(soundex)
