def textswapper():
    file1 = input("enter 1st file name")
    file2 = input("enter 2nd file name")

    with open(file1,'r') as a:
        data_a = a.read()

    with open(file2,'r') as a:
        data_b = a.read()

    with open(file2,'w') as a:
        a.write(data_a)

    with open(file1,'w') as a:
        a.write(data_b)
textswapper()