# ----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:

# Author: Tanjil Sarker Rafi
# Collaborators/references:
# ----------------------------------------------------

def getAction():
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''
    # TO DO: delete pass and write your code here
    user_input1 = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ").strip().lower()
    
    while True:
        if user_input1 in ["=", "<", ">", "q"]:
            return user_input1
        
        else:
            print("Invalid entry.")
            user_input1 = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ").strip().lower()
            
            
def goToNewSite(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    Update the list pages by slicing
    '''   
    # TO DO: delete pass and write your code here

    user_input2 = input("URL: ").strip().lower()

    pages[current + 1:] = [user_input2]
 
    return current + 1
    
    
def goBack(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    # TO DO: delete pass and write your code here
    if current > 0:
        return current - 1 
    else:
        print("Cannot go back.")
        return current


def goForward(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    # TO DO: delete pass and write your code here
    if current < 1:
        return current - 1
    else:
        print("Cannot go forward.")
        return current
    


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    #websites = ['dsdj','dshd.com','jfhjn.com','jfjf/copm']

    while not quit:
        print('\nCurrently viewing ', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)

        elif action == '<':
            currentIndex = goBack(currentIndex, websites)

        elif action == '>':
            currentIndex = goForward(currentIndex, websites)

        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')  
      

        
if __name__ == "__main__":
    main()


# list = [0,1,2,3,4]
# list = ['a','b','c','d','e']
# a = 2
# print(list[2])