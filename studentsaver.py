import time
import os


class student():
    def __init__(self, startNum):
        self.startingIndex = startNum

    def update(self, list, name, gpa):
        list[self.startingIndex + 1] = name
        list[self.startingIndex + 2] = gpa
        return(list)

    def delete(self, list):
        for x in range(3):
            list.pop(self.startingIndex)
        return(list)

def search(id , list):
    for x , item in enumerate(list):
        if item == id:
            return(x)
            # print(item)
            # print(list[x + 1])
            # print(list[x + 2])
    return False

def writeLines(file, list):
    writeString = ""
    for i in range(0, len(list) - 1):
        writeString += list[i] + "\n"
    writeString += list[len(list) - 1]
    file.seek(0)
    file.write(writeString)
    file.truncate()
    
def create(file, list):
    print("please enter your STUDENT ID!!!!!")
    studentID = input()
    print("please enter you're name!!!!!!")
    nameM = input()
    print("please enter your gpa!!!!!!!!!!!")
    gpa = input()
    list.extend([studentID, nameM, gpa])
    writeLines(file, list)


if __name__ == "__main__":
    cwd = os.getcwd()
    with open(cwd + "\data.txt", "r+") as f:
        innards = f.read().split("\n")
        print(innards)
        print("Hi welcome to student saver my name is tudetn saver and i will be saving students today, would you like to: \n1. Create\n2. Read\n3. Update\n4. Delete\n5. Fortnite ???????")
        epicReply = input()
        if epicReply == "5":
            for x in range(10):
                print("fortnite")
            print("quit")
            exit()
        elif epicReply == "4":
            deleteID = search(input("ID?: "), innards)
            if deleteID is False:
                print("ID NOT FOUND")
            else:
                yuh = student(deleteID)
                innards = yuh.delete(innards)
                writeLines(f, innards)
        elif epicReply == "3":
            updateID = search(input("ID?: "), innards)
            if updateID is False:
                print("ID NOT FOUND")
            else:
                yuh = student(updateID)
                name = input("new name: ")
                gpa = input("new gpa: ")
                innards = yuh.update(innards, name, gpa)
                writeLines(f, innards)
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
            
