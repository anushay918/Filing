import os
def addrecord():
    newfile = open('123.txt','at')
    studentname = input('Enter a name: (Leave Blank to end)')
    while studentname != '':
        studentclass = input('Enter class:  ')
        studentage = input('Enter age:  ')

        newfile.write(studentname + '\n')
        newfile.write(studentclass + '\n')
        newfile.write(studentage + '\n')

        studentname = input('Enter name:  ')
    newfile.close()

addrecord()

def displayrecord():
    try:
        newfile = open('123.txt','rt')
        studentname = newfile.readline()
        while studentname != '':
            studentclass = newfile.readline()
            studentage = newfile.readline()
            print(studentname, end=' ')
            print(studentclass, end=' ')
            print(studentage, end=' ')
            studentname = newfile.readline()
        newfile.close()
    except:
        print('file doesnot exist')

displayrecord()

def searchrecord():
    x = input('Enter name to search')
    try:
        newfile = open('123.txt','rt')
        studentname = newfile.readline()
        studentclass = newfile.readline()
        studentage = newfile.readline()
        while studentname.strip() != x and studentname != '':
            studentname = newfile.readline()
            studentclass = newfile.readline()
            studentage = newfile.readline()
        if studentname.strip() != x:
            print('Name not found')
        else:
            print(studentname, studentclass, studentage)
    except:
        print('File doesnt exist')
        
searchrecord()

def deleterecord():
    x = input('Enter name to delete:  ')
    try:
        found = False
        newfile = open('123.txt','rt')
        tempfile = open('temp.txt','wt')
        studentname = newfile.readline()
        while studentname != '':
            studentclass = newfile.readline()
            studentage = newfile.readline()
            
            if studentname.strip() != x:
                tempfile.write(studentname)
                tempfile.write(studentclass)
                tempfile.write(studentage)
            else: 
                found = True
            studentname = newfile.readline()
        newfile.close()
        tempfile.close()
        if found == False:
            os.remove('tempfile.txt')
        else:
            os.remove('123.txt')
            os.rename('temp.txt','123.txt')
    except:
        print("File doesn't exist")
deleterecord()

def editrecord():
    x = input('Enter name to edit')
    try:
        newfile = open('123.txt','rt')
        tempfile = open('temp.txt','wt')
        studentname = newfile.readline()
        found = False
        while studentname != '':
            studentclass = newfile.readline()
            studentage = newfile.readline()
            
            if studentname.strip() != x:
                tempfile.write(studentname)
                tempfile.write(studentclass)
                tempfile.write(studentage)
            else:
                print(studentname, studentclass, studentage)
                newname = input('Enter new name or leave blank to keep original')
                if newname == '':
                    newname = studentname.strip()
                newclass = input('Enter new class or leave blank to keep original')
                if newclass == '':
                    newclass = studentclass.strip()
                newage = input('Enter new age or leave blank to keep original')
                if newage == '':
                    newage = studentage.strip()
                tempfile.write(newname + '\n')
                tempfile.write(newclass + '\n')
                tempfile.write(newage + '\n')
                found = True
            studentname = newfile.readline()
        tempfile.close()
        newfile.close()
        if found == False:
            os.remove('temp.txt')
        else:
            os.remove('123.txt')
            os.rename('temp.txt','123.txt')
    except:
        print("File wasn't found")
editrecord()
