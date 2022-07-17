MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

string_to_decode1 = '..  .-.. .. -.- .  .--. -.-- - .... --- -.  ...-- .-.-.- .---- ----- '
string_to_decode2 = '..  -.- -. --- .-- --..--  -.-- --- ..-  -.-. .- -.  -.. ---  .. - '

morse = {}
for key, value in MORSE_CODE_DICT.items():
    morse[value] = key


def decode_string(string):
    decoded_str = ""
    for word in string.split("  "):
        for code in word.split(" "):
            if not code:
                continue
            decoded_str += morse[code]
        decoded_str += " "
    return decoded_str


print(decode_string(string_to_decode1))
print(decode_string(string_to_decode2))

