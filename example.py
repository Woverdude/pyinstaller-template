__author__ = 'Woverdude'

from tempfile import NamedTemporaryFile

def main():

    filename = NamedTemporaryFile('w')

    print("Filename: ") + filename.name

    #Write to the file
    filename.write("Hello World!")

    print("Hello World!")

    #Don't tell me Python is magic and closes everything automatically for you
    filename.close()

    print("File closed.")

    #Pause to allow the user to read the output
    i = raw_input("Enter any character to continue...")

if __name__ == '__main__':
    main()
