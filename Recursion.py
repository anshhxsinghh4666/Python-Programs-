# RECURSION : When a function calls itself repeatedly.
#             (Its like advance version of loops)
# NOTE: Codes written using loops can be written using recursion and vice versa.

# Example: Print numbers from 5 to 1 using recursion.
# Recursive Funaction`
def show(n):
    if(n==0):  # base case (Stopping Condition) (when n becomes 0 recursion will stop) (Stoppping Condition/value is not included i.e 0)
        return
    print(n)
    show(n-1)  # recursive call

show(5)  # -> 5, 4 = n-1, 3 = n-2, 2 = n-3, 1 = n-4


# Call Stack: Layers in function

#     ->  The call stack is a data structure that keeps track of the function calls in a program. It is a stack-based data structure, meaning that the last function called is the first one to be executed and the first function called is the last one to be executed.
#         In the provided code snippet, the call stack is used to manage the recursive function calls. When the show(5) function is called, it creates a new frame on the call stack. This frame contains the local variables and the return address for the function. The function then checks the base case (n == 0), and if it is true, it returns i.e function ends. Otherwise, it prints the current value of n, makes a recursive call to show(n-1), and waits for the recursive call to finish.
#         As the recursive calls are made, each new frame is added to the top of the call stack. When the base case is reached, the recursive calls start to unwind, and the frames are removed from the call stack in reverse order. This process continues until all the frames are removed, and the program execution is completed.
#         In summary, the call stack is used to manage the function calls in a program, ensuring that the correct order of execution is maintained and that the program can handle recursive function calls.
#         After execution of whole funaction i, the call stack will be empty.


def show(n):
    if(n==0):  # base case (Stopping Condition) (when n becomes 0 recursion will stop) (Stoppping Condition/value is not included i.e 0)
        return
    print(n)
    show(n-1)
    print("END")

show(3)

# Output: 3 
#         2
#         1
#         END
#         END
#         END

# Check notepad for notes.