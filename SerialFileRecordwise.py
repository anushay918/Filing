import os
def addrecord():
    newfile = open('123.txt','wt')
    studentname = input('Enter student name:' + '\t')
    while studentname != '':
        studentclass = input('Enter student class:' + '\t')
        studentage = input('Enter student age:' + '\t')

        newfile.write(studentname + '#' + studentclass + '#' + studentage + '\n')

        studentname = input('Enter student name or leave blank to end:' + '\t')
    newfile.close()

addrecord()

def searchrecord():
    try:
        newfile = open('123.txt','rt')
        searchname = input('Enter a name to search:   ')
        studentname = ''
        record = newfile.readline()
        while record != '' and studentname != searchname:
            studentname = ''
            studentclass = ''
            studentage = ''
            field = 0
            for i in range(len(record)):
                thischar = record[i]
                if thischar == '#':
                    field = field + 1
                elif field == 0:
                    studentname = studentname + thischar
                elif field == 1:
                    studentclass = studentclass + thischar
                else:
                    studentage = studentage + thischar
            record = newfile.readline()
        if studentname == searchname:
            print(studentname, studentclass, studentage)
        else:
            print('Name not found')
        newfile.close()
    except:
        print('file does not exist')

searchrecord()

def deleterecord():
    try:
        deletename = input('Enter name to delete:  ')
        newfile = open('123.txt','rt')
        tempfile = open('temp.txt','wt')
        record = newfile.readline()
        found = False
        while record != '':
            studentname,studentclass,studentage = record.split('#')
            if studentname != deletename:
                tempfile.write(studentname + '#' + studentclass + '#' + studentage)
            else:
                found = True
            record = newfile.readline()
        tempfile.close()
        newfile.close()
        if found == True:
            os.remove('123.txt')
            os.rename('temp.txt','123.txt')
        else:
            os.remove('temp.txt')
    except:
        print('file doesnot exist')

deleterecord()

def editrecord():
    try:
        newfile = open('123.txt','rt')
        tempfile = open('temp.txt','wt')
        searchname = input('Enter name to edit:  ')
        record = newfile.readline()
        found = False
        while record != '':
            studentname, studentclass, studentage = record.split('#')
            if studentname != searchname:
                tempfile.write(studentname + '#' + studentclass + '#' + studentage)
            else:
                found = True
                newname = input('Enter new name or leave black to remain same:  ')
                if newname == '':
                    newname = studentname
                newclass = input('Enter new class or leave black to remain same:  ') 
                if newclass == '':
                    newclass = studentclass
                newage = input('Enter new age or leave black to remain same:  ')
                if newage == '':
                    newage = studentage.strip()
                tempfile.write(newname + '#' + newclass + '#' + newage + '\n')
            record = newfile.readline()
        tempfile.close()
        newfile.close()
        if not found:
            print('name not found')
            os.remove('temp.txt')
        else:
            os.remove('123.txt')
            os.rename('temp.txt','123.txt')
    except:
        print('file doesnt exist')

editrecord()

def displayrecords():
    try:
        newfile = open('123.txt','rt')
        record = newfile.readline()
        while record != '':
            studentname, studentclass, studentage = record.split('#')
            print(studentname, studentclass, studentage)
            record = newfile.readline()
    except:
        print('File doesnt exist')
        
displayrecords()
    
