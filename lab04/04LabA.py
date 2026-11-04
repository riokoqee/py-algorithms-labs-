########## 1st task

def recursiveSum(n):
    if n == 0:
        return 0
    return n + recursiveSum(n - 1)

########## 2nd task

def recMin(numbers):
    if len(numbers) == 1:
        return numbers[0]
        
    minimum = findMinimum(numbers[1:])
    
    if numbers[0] < minimum:
        return numbers[0]
        
    return minimum
    
########## 3rd task
    
def palindrome(s):
    if len(s) <= 1:
        return True
        
    if s[0] != s[-1]:
        return False
    
    return palindrome(s[1:-1])

########## 4th task

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

########## 5th task

def recursiveFib(n):
    if n <= 1:
        return n
        
    return recursiveFib(n - 1) + recursiveFib(n - 2)

def iterativeFib():
    n = int(input("Type an integer: "))
    
    a = 0
    b = 1
    
    for i in range(n):
        a, b = b, a + b
        
    return a

########## 6th task  

def fileReader():
    with open("first.txt", "r") as file1:
        text1 = file1.read()
        
    with open("second.txt", "r") as file2:
        text2 = file2.read()
    
    if text1 == text2:
        print("Files are similar!")
    else:
        print("Files are different!") 
        
########## Task Choosing     
        
def taskChoice():

    choice = int(input("Choose which task you want to launch(1-6): "))
    
    if choice == 1:
        n = int(input("Type an integer: "))

        print(recursiveSum(n))
        
    elif choice == 2:
        numbers = list(map(int, input("Write a list of numbers: ").split()))

        if len(numbers) > 0:
            print(findMinimum(numbers))
        else:
            print("List is empty.")
    
    elif choice == 3:
        string = input("Write a string: ").lower()
        print(palindrome(string))
        
    elif choice == 4:
        a = int(input("Type first num: "))
        b = int(input("Type second num: "))

        print(gcd(a, b))
        
    elif choice == 5:
        fibTaskChoice = int(input("1 - Iterative form\
                                   2 - Recursive form"))
        if fibTaskChoice == 1:
            n = int(input("Type an integer: "))
            
            print(iterativeFib())
            
        elif fibTaskChoice == 2:
            n = int(input("Type an integer: "))

            print(recursiveFib(n))
            
    elif choice == 6:
        fileReader()
    
    else:
        print("Input is incorrect!")
        
taskChoice()
