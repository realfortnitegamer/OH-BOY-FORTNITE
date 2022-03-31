import time
import os

def search(id , list):
    for x , item in enumerate(list):
        if item == id:
            return(x)
            # print(item)
            # print(list[x + 1])
            # print(list[x + 2])
    
def create(file, list):
    print("please enter your STUDENT ID!!!!!")
    studentID = input()
    print("please enteer you're name!!!!!!")
    nameM = input()
    print("please enter your gpa!!!!!!!!!!!")
    gpa = input()
    file.write("," + studentID + "," + nameM + "," + gpa)
    print(list)
    list.extend([studentID, nameM, gpa])
    print(list)

if __name__ == "__main__":
    cwd = os.getcwd()
    with open(cwd + "\data.txt", "r+") as f:
        innards = f.read().split(",")
        print(innards)
        print("Hi welcome to student saver my name is tudetn saver and i will be saving students today, would you like to 1. Create 2. Read 3. Update 4. Delete 5. Fortnite ???????")
        epicReply = input()
        if epicReply == "5":
            for x in range(1000):
                print("fortnite")
            time.sleep(10)
            x = {}
            for i in range(1000000):
                x = {1: x}
            repr(x)
        elif epicReply == "4":
            pass
        elif epicReply == "3":
            pass
        elif epicReply == "2":
            tempID = input("thats stupid, put your id in: ")
            val = search(tempID, innards)
            print(innards[val])
            print(innards[val + 1])
            print(innards[val + 2])
        elif epicReply == "1":
            create(f, innards)
        else:
            print("you suck at typing a number +dumb + ratio + u fell offf (or u type wrong number!!!!!)!!!!!")
            
