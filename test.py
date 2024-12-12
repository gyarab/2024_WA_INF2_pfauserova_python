def fibonacci(n):
    if not isinstance(n,int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence
if __name__ == "__main__":  
    print(fibonacci(0)) 