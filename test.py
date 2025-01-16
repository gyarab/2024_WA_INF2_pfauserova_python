def fibonacci(n):
    if not isinstance(n,int) or n < 0:
        raise ValueError("Input must be a positive integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:   
        return fibonacci(n-1) + fibonacci(n-2)
    


    

def is_prime(num):
    if not isinstance(num, int) or num < 1:
        raise ValueError("Input must be an integer greater than 1")
    elif num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True
if __name__ == "__main__":  
    print(fibonacci(3)) 
    print(is_prime(1))  


def caesar_encode(text):
    shift = 3
    result = ""
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

if __name__ == "__main__":
    print(fibonacci(3)) 
    print(is_prime(1))
    print(caesar_encode("Hello, World."))  # Example usage
    print(caesar_decode("Khoor, Zruog.", 3))  # Example usage