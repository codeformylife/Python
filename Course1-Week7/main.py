largest = None
smallest = None
while True:
    num = raw_input("Enter a number:")
    if num == "done": break
    try: 
       nom = int(num)
    except: 
       print ("Invalid input")
       continue

    if largest is None:
        largest = nom
    elif nom >  largest:
        largest = nom

    if smallest is None:
        smallest = nom
    elif nom < smallest:
        smallest = nom


print ("Maximum is", largest)
print ("Minimum is", smallest)