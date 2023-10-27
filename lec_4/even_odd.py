# distingwish odd and even

def even_odd (st) :
    list0 = st.split ()
    list_odd = []
    list_even = []
    for i in list0 :
        if ( int(i) % 2 == 0 ) :
            list_even.append(int(i))
        else :
            list_odd.append(int(i))
    return list_even, list_odd

# main

st = str(input("enter a list of numbers separated by spaces: "))

list_even, list_odd = even_odd (st)

print (list_even)
print (list_odd)