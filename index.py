num1 = int(input("please enter first num : "))
num2 = int(input("please enter second num : "))
opr = input("please enter opertor (+, -, /, *) : ")
result = ""
action = "true"

# debugging Function
def debug():
    global result, action
    opretor = input("Enter opertor (+, -, /, *) : ")

    if opretor == "+":
        result = num1 + num2
    elif opretor == "-":
        result = num1 - num2
    elif opretor == "/":
        if num2 == 0:
            action = "false"
            print("Cannot divide by zero!")
            return
        result = num1 / num2
    elif opretor == "*":
        result = num1 * num2
    else:
        action = "false"
        print("Invalid operator again!")
        return

    # IMPORTANT PART: debug ke result ko print bhi karo
    # print("Result :", result)
    action = "done"   # so program knows result printed here already


# Main logic
if num2 == 0 and opr == "/":
    action = "false"
    print("please enter second value greater then 0")

elif opr == "+":
    result = num1 + num2

elif opr == "-":
    result = num1 - num2

elif opr == "/":
    result = num1 / num2

else:
    action = "false"
    print("please select correct opertor...")
    debug()


# Final output
if action == "false":
    print("thanks")

elif action == "done":   # ONLY print if debug ne print nahi kiya
    print("Result :", result)