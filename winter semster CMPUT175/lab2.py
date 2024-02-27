def getInputFile():
    """takes input from user, checks whether it is a txt file and returns the filename"""
    
    while True:
        x = input("Name of file: ")

        ext = x.split(".")

        # if ext[1] == "txt":
        #     print("a")
        # ext = x[len(x)-4] + x[len(x)-3] + x[len(x)-2] + x[len(x)-1]

        if ext[1] == "txt":
            return x
        else:
            print("Wrong extension file")

        
filename = getInputFile()

def decrypt(file):
    """Takes a filename and uses the first line as a cipher key"""
    """to decode the second line and print it"""

    f = open(file, "r")
    read = f.readlines()
    key = int(read[0].strip())
    encrypted = read[1].strip().lower()
    f.close()

    msg = ""

    for i in encrypted:

        if i == " ":
            msg += i

        else:
            ascii = ord(i)
            change = ascii - key

            if change < 97:
                diff = 97 - change
                change = 123 - diff
            
            decrypted_ascii = chr(change)

            msg += decrypted_ascii
    
    print(msg)

decrypt(filename)