# O(n) time | O(n) space - where n is the length of the input string
def bestDigits(number, numDigits):
    # Write your code here.
    stack = []

    for digit in number:
        while numDigits > 0 and len(stack) > 0 and digit > stack[len(stack) - 1]:
            numDigits -= 1
            stack.pop()

        stack.append(digit)

    while numDigits > 0:
        numDigits -= 1
        stack.pop()
        
    return "".join(stack)
