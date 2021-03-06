#Create a Function that reverse a string;

def reverseString(inputString):
    #return inputString[::-1]
    rString = ''
    for i in range(len(inputString)-1,-1,-1):
        rString += inputString[i]
    return rString
def main():

    givenString = 'I am from New York'
    print(reverseString(givenString))

if __name__ == '__main__':
    main()
