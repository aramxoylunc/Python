# basic calculator

def basic(st):
    a = st.split()
    if a[1] == "+":
        return int(a[0]) + int(a[2])
    elif a[1] == "-":
        return int(a[0]) - int(a[2])
    elif a[1] == "*":
        return int(a[0]) * int(a[2])
    elif a[1] == "/":
        return int(a[0]) / int(a[2])


# main

while True:

    user_input = input()

    if user_input == "done":
        break

    print ( basic(user_input) )
