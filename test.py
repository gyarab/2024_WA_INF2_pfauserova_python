from unidecode import unidecode

ACCENTED_CHAR_MAP = {
    'À': 'A', 'Á': 'A', 'Â': 'A', 'Ã': 'A', 'Ä': 'A', 'Å': 'A', 'Æ': 'AE', 'Ç': 'C', 'È': 'E', 'É': 'E',
    'Ê': 'E', 'Ë': 'E', 'Ì': 'I', 'Í': 'I', 'Î': 'I', 'Ï': 'I', 'Ð': 'D', 'Ñ': 'N', 'Ò': 'O', 'Ó': 'O',
    'Ô': 'O', 'Õ': 'O', 'Ö': 'O', 'Ø': 'O', 'Ù': 'U', 'Ú': 'U', 'Û': 'U', 'Ü': 'U', 'Ý': 'Y', 'Þ': 'TH',
    'ß': 'SS', 'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'å': 'a', 'æ': 'ae', 'ç': 'c', 'è': 'e',
    'é': 'e', 'ê': 'e', 'ë': 'e', 'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i', 'ð': 'd', 'ñ': 'n', 'ò': 'o',
    'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ø': 'o', 'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u', 'ý': 'y',
    'þ': 'th', 'ÿ': 'y', 'Ž': 'Z', 'ž': 'z'
}

def is_prime(num):
    if not isinstance(num, int) or num < 1:
        raise ValueError("Input must be an integer greater than 1")
    elif  num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True

def caesar_encode(text):
    shift = 3
    result = ""
    text = unidecode(text)  # Convert accented characters to plain ASCII
    for char in text:
        if char.isalpha():
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                raise ValueError(f"Invalid character '{char}' in input.")  # Error for other characters
        elif char in "., ":
            result += char
        else:
            raise ValueError(f"Invalid character '{char}' in input.")  # Error for other characters
    return result

def caesar_decode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            else:
                raise ValueError(f"Invalid character '{char}' in input.")  # Error for other characters
        elif char in "., ":
            result += char
        else:
            raise ValueError(f"Invalid character '{char}' in input.")  # Error for other characters
    return result

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def remove_accents(text):
    return ''.join(ACCENTED_CHAR_MAP.get(char, char) for char in text)

def morse(text):
    result = ""
    text = remove_accents(text)  # Convert accented characters to plain ASCII
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            result += MORSE_CODE_DICT[char] + " "
        elif char.isdigit():
            result += MORSE_CODE_DICT[char] + " "
        elif char in "., ":
            result += char
        else:
            continue  # Ignore any special signs
    return result.strip()

if __name__ == "__main__":
    print(is_prime(1))
    print(caesar_encode("Hello, World."))  # Example usage
    print(caesar_decode("Khoor, Zruog.", 3))  # Example usage
    print(morse("Hello World 123"))  # Example usage
    print(morse("Žluťoučký kůň"))  # Example usage
