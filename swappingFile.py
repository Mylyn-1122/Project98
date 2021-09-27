def swappContent():
    firstFile = input("Name of the first file: ")

    fileOne=open(firstFile, 'r')
    dataA = fileOne.read()

    secondFile = input("name of sencond file: ")

    fileTwo=open(secondFile, 'r')

    dataB = fileTwo.read()

    fileOneW=open(firstFile, 'w')
    fileOneW.write(dataB)
    fileTwoW=open(secondFile, 'w')
    fileTwoW.write(dataA)

    


    

swappContent()
