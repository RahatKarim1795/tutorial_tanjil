#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''

    user_input1 = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ").strip().lower()
    
    if user_input1 in ["=", "<", ">", "q"]:
        return user_input1
    else:
        raise Exception("Invalid entry.")

def goToNewSite(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''   
    new_site = input("URL: ").strip().lower()

    bck.push(current)

    fwd.clear()

    return new_site

    
def goBack(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''
    try:
        back_site = bck.pop()

    except:
        print("Cannot go back")
        return current
    else:
        fwd.push(current)
        return back_site
    

def goForward(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    try:
        forward_site = fwd.pop()

    except:
        print("Cannot go forward")
        return current
    else:
        bck.push(current)
        return forward_site

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
                
            elif action == '<':
                current = goBack(current, back, forward)

            elif action == '>':
                current = goForward(current, back, forward)

            elif action == 'q':
                quit = True

        # print(f'Back: {back}')
        # print(f'Forw: {forward}')
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    