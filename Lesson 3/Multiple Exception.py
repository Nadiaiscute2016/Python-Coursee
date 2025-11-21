try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print("Result is : ", result)
    print("Result is : ", result)

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Please enter numerical value")
except NameError as ex:
    print("The exception is :", ex)
except:
    print("Some error occurred")
result = num1/num2
print("Result is : ", result)
print("Result1 is : ", result1)
finally:
     print("I will execute no matter what happens")