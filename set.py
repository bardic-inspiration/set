import random

board = []
score = 0

def initializeBoard():
    score = 0
    for i in range(0,11):
        #make these random numbers
        board.append((random.randint(0,2),random.randint(0,2),random.randint(0,2),random.randint(0,2)))

def encodeItem(item):
    enc = ''
    for i in range(len(item)):
        if item[i] == 0: enc.append('|')
        elif item[i] == 1: enc.append('\\')
        elif item[i] == 2: enc.append('/')
        else: enc.append(' ')
    return enc

# def translateItem(enc):

# returns a list of four random numbers between 0 and 2
def newItem():
    item = []
    for i in range(0,3):
        item.append(random.randint(0,2))
    return item

#prints the board on a 4x3 grid
def printBoard(b):
    for i in range(len(b)):
        if i % 4 == 3:
            print(f'{encodeItem(b[i])}\t\n')
        else:
            print(f'{encodeItem(b[i])}\t')

#checks the validity of a set.  returns True if valid, False if invalid
def check(sett):
    try: 
        len(sett)
    except: 
        print(f'Invalid Input. Try Again.\n')
        return False
    else:
        if len(sett) = 3: 
            for i in range(0,2):
                if len(sett[i] != 4):
                    print(f'Invalid Set Item Length: {str(sett[i])}. Try Again.\n') 
                    return False
            for e in range(0,3):
                    if (sett[0][e] + sett[1][e] + sett[2][e]) % 3 == 0: 
                        return True
                    else:
                        print(f'Not a match. Try Again.\n') 
                        return False
        else:
            print(f'Invalid Set Length: {str(sett)}.\n')
            return False
    finally:
        return False

#chooses a set on the board given 3 numbers between 0 and 11
def selectSet(a, b, c):
    sett = (board[a], board[b], board[c])
    if check(sett):
        score += 1
        print(f'Correct!  Sets identified: {str(score)}.\n')
        board[a] = newItem()
        board[b] = newItem()
        board[c] = newItem()
    return sett