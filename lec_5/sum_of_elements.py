
def sum_of_elements (lst,exclude_negative = False):
    sum = 0
    if (exclude_negative) :
        for i in lst :
            if int(i) > 0 :
                sum += int(i)
    else :
        for i in lst :
            sum += int(i)

    return sum


str0 = input("enter a list of numbers separated by space: ")
lst = str0.split()

str0 = input("do you want to exclude negative numbers?: (y or n): ")

if str0 == "y" or str0 == "yes" :
    exclude = True
elif str0 == "n" or str0 == "not" :
    exclude = False
else :
    print ("it considered to not exclude")

print (sum_of_elements(lst,exclude))