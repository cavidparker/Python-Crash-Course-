x = (input("enter the first number : "))
y = (input("enter the secound number : "))

try:
    z = int(x) / int(y)
    
except ZeroDivisionError as e:
    print("zer division error occurred")
    z = None

except Exception as e:
    print("excetion error:", type(e).__name__)
    z = None         

print("Division Answer: ",z)