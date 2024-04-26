from collections import deque

d = deque()

def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    d = deque(s)  

    while len(d) > 1:
        if d.popleft() != d.pop(): 
            return f"{s} not a palindrome"
    return "Yes, all characters match"


input_str = "Alla"
result = is_palindrome(input_str)
print(f"'{input_str}' is a palindrome? {result}")