#Enjoy this fancy display of text which you could consider very useless but its here now.
print("------------------------------------")
print("        Sqaure Addition Tool*       ")
print(" Concept by : Cocoatwix - scares009 ")
print("     Automation by : noExplorer     ")
print("------------------------------------")
#This is where the big deal is happening.
print("Available scripts to use: chainVerifier , numberLocator , GenerateNumber_ALL (Type 'info' to get information about this program, 'credits' for credits.)") #Implementing a script
method = input("Please use one of the mentioned scripts in order to continue ")
if method == "chainVerifier":
    import time
    a = 1
    print("Define number x")
    x=input()
    digits=len(x) #locate the amount of digits
    #print(digits) #print them numbers (DEBUG ONLY)
    number = x #following code is provided from kite.com
    sum_of_digits = sum(int(digit) for digit in str(number)) #find the digitsum

    #print(sum_of_digits) #print it (DEBUG ONLY)
    D = digits #assign D as amount of digits
    DS = sum_of_digits #assign DS as digitsum
    RES = ((D*DS)*2) 
    print("Num", RES)

    while True:
        z = str(RES)
        digits = len(z)
        number = z
        sum_of_digits = sum(int(digit) for digit in str(number))
        D = digits
        DS = sum_of_digits
        RES = ((D*DS)*2)
        print("Num", a+1 , RES)
        a = a+1
        time.sleep(0.2)
if method == "numberLocator" :
    import time
    D = 0
    DS = 0
    print("Please specify value of 'y' ")
    y = int(input())
    z = 1
    RES = (y/2)
    while True :
        D = (RES / z)
        DS = D
        if D.is_integer():  #Somebody for the PCMR Discord helped me resolve an issue here. Kudos to them.
            print("Your number containts ", D , "digits and the sum of those digits must be ", DS)
            print("Try to think of examples with those parameters and pick the one with the least value between them.")
            z = z+1
            time.sleep(0.3) #Consider this as a "bottleneck" but it does help in readability
        else:
            #print("Previous number is float. Retrying.") #DEBUG
            z = z+1
            #time.sleep(1) #DEBUG

if method == "info" :
   import time
   print("")
   print("Square addition tool.")
   print("Version 0.0.1ef . Scripted on: 23rd Nov. 2021 . Finished on 5th Dec. 2021.")
   print("Early Beta.")
   print("To find out more about this concept visit the link or scan the QR Code below:")
   print("")
   print("▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄ ▄▄▄▄▄▄▄")  
   print("█ ▄▄▄ █ ▄  ▄▄██  ▀█ ▄ █ ▄▄▄ █ ") 
   print("█ ███ █ ██▄█ ███▄▀▀█  █ ███ █ ") 
   print("█▄▄▄▄▄█ ▄▀▄ █▀▄ ▄▀█▀█ █▄▄▄▄▄█ ") 
   print("▄▄▄▄  ▄ ▄▀ ▀  ▄  ███▀▄  ▄▄▄ ▄ ") 
   print("█▀▀█▀▄▄██▀   ▄▄▀█ ▄▀█ ███ ▄▄▀ ") 
   print(" ▀▀▀▀▄▄ █▄ █▀▀▄█ ▄▀▄▀▀▀▀▀▄▄ ▀ ") 
   print("▀  ▀▄▄▄ █▀▀▀▄ ▀ █▀ ██▄▀█▄ ███ ") 
   print(" ▀▀ ▀▄▄▄█▄▀▄▀▄▄█  ▄ █▄▀▀█▄ █  ") 
   print("▄  ███▄ ▀▄█▄██▀█▄ ▀ ▀▀ █ ▀█▀  ") 
   print(" ▄█▀▄ ▄▀██▀▄█ █▄▀█▄███▄▄▄▄█   ") 
   print("▄▄▄▄▄▄▄ ▀ █▄█▀▄   ▀▄█ ▄ ██▀█▀ ") 
   print("█ ▄▄▄ █   █ ▄███▄▄▀ █▄▄▄█▀▄█▄ ") 
   print("█ ███ █ █▀ █▀  ▀▀  ▀▀█ ▄▀▀▄ █ ") 
   print("█▄▄▄▄▄█ ██ ▀  █▄█ ▀██  ▀ █ █ ")   
   print("https://www.youtube.com/watch?v=hGQdsibB2is")
   print("Program quits automatically after 30 seconds.")
   time.sleep(30)

   #DO NOT TOUCH
import random


def seq_to_int(seq, base=10):
    """Convert sequence of digits to an integer."""
    result = 0
    for i, x in enumerate(reversed(seq)):
        if 0 <= x < base:
            result += x * base ** i
        else:
            msg = f"Invalid value in `seq` for given `base`"
            raise ValueError(msg)
    return result


def int_to_seq(n, base=10):
    """Convert an integer to a sequence of digits."""
    if n == 0:
        return [0]
    elif n < 0:
        raise ValueError("`n` must be non-negative.")
    else:
        result = []
        while n:
            result.append(n % base)
            n //= base
        return result[::-1]


def random_digits_given_sum(num_digits, sum_value, base=10):    
    digits = []
    max_digit = base - 1
    if sum_value > max_digit * num_digits:
        return digits
    sum_left = sum_value
    num_left = num_digits
    while num_left > 0:
        if sum_left > max_digit:
            min_rand = max(0, sum_left - max_digit * (num_left - 1))
            max_rand = max_digit
            digit = random.randint(min_rand, max_rand)
        elif sum_left >= 0 and num_left > 1:
            min_rand = 0
            max_rand = sum_left
            digit = random.randint(min_rand, max_rand)
        elif sum_left >= 0 and num_left == 1:
            digit = sum_left
        else:
            raise ValueError        
        digits.append(digit)
        sum_left -= digit
        num_left -= 1
    # ensure first digit is not 0
    if digits[0] == 0:
        non_zero_indices = [i for i, digit in enumerate(digits) if digit]
        i = random.choice(non_zero_indices)
        digits[0], digits[i] = digits[i], digits[0]
    # shuffle remaining digits
    shuffled = digits[1:]
    random.shuffle(shuffled)
    return digits[0:1] + shuffled

if method == "GenerateNumber_ALL" :
    import random
    import time
    from time import sleep
    print(">Please run 'numberLocator' before using this script!!")
    print(">Large values will/may take longer to generate a number.")
    selectedMethod2 = input("Please specify method | Available: Legacy , newOne : ")
    if selectedMethod2 == "Legacy" :
            o = int(input("Please specify range. MUST be same as your DS and D. "))
            sp = int(input("Do you want timeout after every generation? (0 counts as none) "))
            t = []
            def f(s, i):
                r = sum(map(int, s))
                if i == n:
                    if r == x:
                        t.append(s)
                else:
                    for q in range(int(o)) if len(s) else range(1, int(o)):
                        if r + q <= x:
                            f(s + str(q), i + 1)
            n = int(input("Amount of digits (D): "))
            x = int(input("Sum of digits (DS): "))
            while True:
                f("", 0)
                print(random.choice(t))
                sleep(sp)

if selectedMethod2 == "newOne": #Took AGES to implement. Because indents hate me. Enjoy the McClunky implementation.
    required_length = int(input("Please specify amount of Digits ")); 
    required_sum = int(input("Please specify DigitSum "));
    sp = int(input("How much delay between generations? "))
    p = 0
    while True:
        z = seq_to_int(random_digits_given_sum(required_length, required_sum)); 
        print("Num" , p , z);
        print("Checking LEN and SUM...")
        num = z
        leng = len(str(z))
        sumg = sum_of_digits = sum(int(digit) for digit in str(num))
        print("Length : ", leng , "Sum of Digits: " , sumg)
        time.sleep(sp)
        print("")
        p = p + 1

if method == "credits" :
    import time
    print("")
    print("-----------------------------")
    print("BIG THANKS TO THESE PEOPLE:")
    print("Ratery and norok2 on StackOverflow. They made the 'GenerateNumber' scripts. And many others in the question I made.")
    print("kite.com . They provided to me the 'sum_of_digits' code.")
    print("BigTeePee on PCMR Discord. Helped fix an issue on the 'numberLocator' script.")
    print("scares009 / Cocoatwix . Original creator of this concept.")
    print("And YOU. For testing this program, and using it!")
    print("-----------------------------")
    print("")
    print("Program quits automatically after 30 seconds.")
    time.sleep(30)

#DO NOT TOUCH
import random


def seq_to_int(seq, base=10):
    """Convert sequence of digits to an integer."""
    result = 0
    for i, x in enumerate(reversed(seq)):
        if 0 <= x < base:
            result += x * base ** i
        else:
            msg = f"Invalid value in `seq` for given `base`"
            raise ValueError(msg)
    return result


def int_to_seq(n, base=10):
    """Convert an integer to a sequence of digits."""
    if n == 0:
        return [0]
    elif n < 0:
        raise ValueError("`n` must be non-negative.")
    else:
        result = []
        while n:
            result.append(n % base)
            n //= base
        return result[::-1]


def random_digits_given_sum(num_digits, sum_value, base=10):    
    digits = []
    max_digit = base - 1
    if sum_value > max_digit * num_digits:
        return digits
    sum_left = sum_value
    num_left = num_digits
    while num_left > 0:
        if sum_left > max_digit:
            min_rand = max(0, sum_left - max_digit * (num_left - 1))
            max_rand = max_digit
            digit = random.randint(min_rand, max_rand)
        elif sum_left >= 0 and num_left > 1:
            min_rand = 0
            max_rand = sum_left
            digit = random.randint(min_rand, max_rand)
        elif sum_left >= 0 and num_left == 1:
            digit = sum_left
        else:
            raise ValueError        
        digits.append(digit)
        sum_left -= digit
        num_left -= 1
    # ensure first digit is not 0
    if digits[0] == 0:
        non_zero_indices = [i for i, digit in enumerate(digits) if digit]
        i = random.choice(non_zero_indices)
        digits[0], digits[i] = digits[i], digits[0]
    # shuffle remaining digits
    shuffled = digits[1:]
    random.shuffle(shuffled)
    return digits[0:1] + shuffled