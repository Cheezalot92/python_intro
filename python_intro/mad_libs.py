def my_function():
    print("Hello, World")

# Call the function
my_function()



def mad_libs():
    story = "Today I saw a %s , it was very %s."


    #word use..
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    #story stuff here.. 
    fill_story = story % (noun, verb)

    #print story..
    print(fill_story)

#gametime
mad_libs()

