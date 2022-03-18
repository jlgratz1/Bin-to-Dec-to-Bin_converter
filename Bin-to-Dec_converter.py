dec_value = 0
values_list = []

def convert():
    
    global dec_value
    bin_value = 0
    bin_list = []
    bin_check = True
    power_ticker = 0
    wrong_input = True

    while wrong_input:
        bin_value = input("Please enter a binary value: ")

        if bin_value.isdigit():
            bin_list = list(map(int, str(bin_value)))
            for item in bin_list:
                if 0 > item > 1:
                    bin_check = False
            if bin_check:
                wrong_input = False
            else:
                print("It is not a binary value")
        else:
            print("It is not an integer")
        
    bin_list = bin_list[::-1]

    for num in bin_list:
        dec_value += num*2**power_ticker
        power_ticker += 1
    
    return dec_value

def run():
    
    global dec_value
    global values_list
    keep_on = True
    exit_value = 0

    while keep_on:
        convert()
        values_list.append(dec_value)
        print(dec_value)
        exit_value = input("Need to convert anything else? [y/n]")
        if exit_value == "n":
            print(values_list)
            keep_on = False 
        dec_value = 0     

run()