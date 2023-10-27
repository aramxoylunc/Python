# exoeriment with variables, data types, and arithmetic operations

a = str(input("input number _ "))
b = str(input("input number _ "))
print (a+b)

a = int(input("input number _ "))
b = int(input("input number _ "))
print (a+b)


a = 25
b = 125678.876
c = 7262541890665432918816352810662517919363672928272
d = float(4294967295789012345678907543210754376854.256783)
print ("a = ", a)
print ("b = ", b)
print ("c = ", c)
print ("d = ", float(d))
print ("d = ", int(d))

list1 = ["aram", a, b, True]
' list1[0] = "Aram" '
print (list1)
print (list1[0], list1[1])

tuple1 = tuple(list1)
' tuple1[0] = "Aram" '
print (tuple1)
print (tuple1[0], tuple1[1])

print ("it is interesting " * 20)
print ("it " + "is " + "interesting")

answer = input("What you think.is it interesting? _ ")

if answer == "yes" or answer == "y" or answer == "interesting":
    print ("rigth answer")
else:
    print ("wrong answer")


a = 25
b = 10

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)