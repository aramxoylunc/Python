
def open_file():

    try:
        str0 = int(input("whitch file do you want to open: (input numeric name): "))
    except ValueError :
        str0 = "fail"
        print ("you are inputed non_numeric input")
    try:
        file_object = open(str0, "r")
    except FileNotFoundError :
        file_object = open("fail.txt","a+")
        print (str0 + " file doesn't exist.")

    print ("file content:\n" + file_object.read() + "\nfile content ended:\n")
    print ("thank you for your valid filename, it's unusual nowdays")

    return file_object

result = open_file()


