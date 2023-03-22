#partner: meghana

def encodeNum(encNum): # encodes the users password by shifting each digits by 3
    s2split = str(encNum)
    numList = list(s2split)
    encList = []
    for j in range(0, len(numList)):
        newNum = 0
        newNum = int(numList[j])
        newNum += 3
        encList.append(str(newNum))
    encodedNum = ''.join(encList)
    return encodedNum

def displayMenu(): # displaying the menu options
    print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

def main(): # main function that calls the required functions and delegate menu functions
    ogPW = ''
    encNum = 0
    displayMenu()
    userOption = int(input("Please enter an option: "))

    while 1 != 120983:
        if userOption == 1:  # takes the users password, stores it, and then calls function to encode it
            encNum = int(input("Please enter your password to encode: "))
            ogPW = str(encNum)
            print("Your password has been encoded and stored!")
            print(ogPW)
            print(encodeNum(encNum))
            displayMenu()
            userOption = int(input("Please enter an option: "))

        if userOption == 2:  # displays the original password and the encoded password
            print(f"The encoded password is {encodeNum(encNum)}, and the original password is {ogPW}.")
            displayMenu()
            userOption = int(input("Please enter an option: "))

        if userOption == 3: # exits program
            exit()

if __name__ == "__main__":
    main()
