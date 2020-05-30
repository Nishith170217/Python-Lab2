def multiplication_table():
    for i in range (0,10):
        for j in range(1,i+1):
            print("{0}{1}{2}{3}{4:02d}{5}".format(j,"*",i,"=",i*j," "),end="")
            j=j+1
        print("\r")
    
multiplication_table()
