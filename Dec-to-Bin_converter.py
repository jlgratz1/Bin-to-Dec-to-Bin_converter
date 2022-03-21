bin_value = 0
dec_value = 0
values_list = []
keep_on = True
bin_list = []


def user_input():
    
    global keep_on
    global dec_value
    wrong_input = True

    while wrong_input:
        dec_value = input("Please enter a decimal value: ")

        if not (dec_value.isdigit() or dec_value == "q"):
            print("It is not an integer")
        
        if dec_value == "q": # this is used to exit the program
            keep_on = False
            return keep_on
        else:
            return dec_value

def conversion(dec_value):

    global bin_list

    while dec_value != 0:
        dec_value = int(dec_value)
        bin_list.append(dec_value%2)
        dec_value = dec_value // 2
                
    bin_list = bin_list[::-1]
    bin_value = int(''.join(map(str,bin_list))) 
    values_list.append(bin_value)
    print(bin_value)
    
    return bin_value, keep_on

def run():
    
    global bin_value
    global values_list
    global keep_on
    global bin_list

    print("To quit press 'q'")
    user_input()
    
    while keep_on:
        conversion(dec_value)
        bin_value = 0
        bin_list = []
        user_input()   

    print(values_list)

run()