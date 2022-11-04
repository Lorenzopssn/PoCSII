#String Split and Join
def split_and_join(line):
    # write your code here
    a=line.split(" ")
    b= "-".join(a)
    return b

#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    print('Hello'+' '+first_name+' '+last_name+'! You just delved into python.')

#Mutations
def mutate_string(string, position, character):
    x=list(string)
    x[position]=character
    final=''.join(x)
    return final

#String Validators
    s = input()
    def check_is_isalnum(ms):
        for el in ms:
            if el.isalnum():            
                return True
                break
    def check_string(ms):
            #chceck if it contains at least one alphabetic charcater
            if ms.isdigit():
                print(False)
            else:
                print(True)
            #check if it contains at least one digit
            if ms.isalpha():
                print(False)
            else:
                print(True)
            #if it only contans digit I cannot know 
            #if it is upper or lower so i return false
            if ms.isdigit():
                print(False)
                return False
            else:
                if ms.isupper():
                    print(False)
                else:
                    print(True)
                if ms.islower():
                    return False
                else:
                    return True
    check_is_isalnum(s)
    if check_is_isalnum(s) == True:
        print(True)
        print(check_string(s))
    else:
        print(False)
        print(False)
        print(False)
        print(False)
        print(False)