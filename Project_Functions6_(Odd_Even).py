# EVEN AND ODD : WAF to check if a number entered by user is odd or even

def odd_even(n):
    if n % 2 == 0:
        print("Even")
        return odd_even
    else:
        print("Odd")
        return odd_even
    
odd_even(9)
odd_even(8)
print("END")

# OR

def even_odd(n):
    x=n%2
    if x==0:
        print("Even")
        return even_odd
    else:
        print("Odd")
        return even_odd

even_odd(9)
even_odd(8)
print("END")
