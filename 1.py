try: 
   
    lineNum = 0                                                                                             # Pre determins all of the variables for the code
    Aray1 = False
    Dictionary1 = False
    Comment1 = False

    file = open("project2.py", "r")                                                                         # Opens the python2.py file in read only mode
    s = file.readlines()

    for line in s:                                                                                          # Will execute the following for every line in python2.py

        if line.startswith('#'):                                                                            # Filters out comments from the code
           pass

        elif line == "\n":                                                                                  # Filters out empty lines from the code
          pass

        elif line.__contains__('"""') and not line.__contains__('-"""'):                                    # Filters out the tripple quote comments and their contents form the code
           Comment1 = True
        
        elif line.__contains__('-"""') and Comment1 == True:                                                # Finds the end of the quoted comment to continue counting
           Comment1 = False
           
        elif line.__contains__('= {') or line.__contains__('= {') and not line.__contains__('}') :          # Filters out list / dictionary from multiple lines
           Dictionary1 = True

        elif line.__contains__('}') and Dictionary1 == True:                                                # Identifies the end of the list / dictionary
           Dictionary1 = False
           lineNum = lineNum + 1

        elif line.__contains__('= [') and not line.__contains__('[]'):                                      # Identifies the begining of the list
            Aray1 = True

        elif line.__contains__(']') and Aray1 == True:                                                      # Identifies the end of the list
            Aray1 = False
            lineNum = lineNum + 1

        elif line.__contains__('= []') or line.__contains__('=[]'):                                         # Sorts out lists with no contents 
            lineNum = lineNum + 1

        elif Aray1 == False and Dictionary1 == False and Comment1 == False:
            lineNum = lineNum + 1

    file.close()                                                                                            # Closes the python2.py file
    print("There are", lineNum, "lines of code in the file" )                                               # Tells the user how to proceed and the number of lines
    input("Please click enter to close . . .")

except IOError:                                                                                             # Catches the IOError if the file does not exist
    print("This file does not exist")
    input("Please click enter to close . . .")