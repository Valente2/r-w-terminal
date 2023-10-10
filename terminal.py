print("(c) Vescio labs  R-W terminal version 1.0")
run=True
data1=" "
data2=" "
data3=" "
while run==True:
    cmd=input("}")
    if cmd == "write":
        block=input("type in the block you would like to access ")
        if block == "1":
            data1=input("please enter data ")
        if block == "2":
            data2=input("please enter data ")
        if block == "3":
            data3=input("please enter data ")
    if cmd == "read":
        Rblock=input("what block would you like to read ")
        if Rblock == "1":
#in tribute to nanno tari
            print(data1,)
        if Rblock == "2":
            print(data2,)
        if Rblock == "3":
            print(data3,)
    if cmd=="read all":
        print(data1, data2, data3,)
    if cmd=="write all":
        data1=input("please enter data ")
        data2=input("please enter data ")
        data3=input("please enter data ")
        print("done!")
    if cmd=="end":
        run=False
    if cmd=="help":
        print("hello what you are reading is the help article: write alllows you to enter data into a block, read allows you to read what was in the block, read all reads the data in evrey block, write all allows you to write in all blocks in only 1 command, end exits the terminal oh and there are 3 blocks")
    if cmd=="log in":
        FNAME=input("please enter your frist name ")
        LNAME=input("please enter your last name ")
        PASS=input("please enter your password ")
        print("wellcome!")
    if cmd=="change password":
        PASS=input("please enter your new password")
    if cmd=="account details":
        print(FNAME, LNAME, PASS)
    if cmd=="show better help.txtd":
        print("this is the bettter help atrile: write will write to one of 3 blocks read will read one block read all will read all the blocks write all will write to all the blocks log in will give you three prombts to enter your frist name last name and password account details will dispaly your account detalis(YOU MUST LOG IN BEFORE YOU DISPLAY YOUR DETAILLS OR ELSE THERE WILL BE AN ERROR) change password will change your password help will give you the bad help article compare.exf is a file that will run that allows you to compare 2 numbers credits and copyright are what you think they are")
    if cmd=="run compare.exf":
        num1=input("enter number 1 ")
        num2=input("enter number 2 ")
        if num1 == num2:
            print(num1 + "=" + num2)
        if num1 > num2:
            print(num1 + ">" + num2)
        if num1 < num2:
            print(num1 + "<" + num2)
    if cmd=="credits":
        print("literly everything:Valente Virgilio Tari Vescio")
    if cmd=="copyright":
       print(" this project is open source but copying of the OS is legal but selling is illegal and should not be done beacause anyways why would you want to sell a 10 year olds work anyway!") 
#C'est fini
        
 
