dec_value = 0
values_list = []
keep_on = True

def convert():
    
    global dec_value
    global keep_on
    global values_list
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
                if item > 1:
                    bin_check = False
            if bin_check:
                wrong_input = False
            else:
                print("It is not a binary value")
                bin_check = True
        elif bin_value == "q": # this is used to exit the program
            keep_on = False
            break
        else:
            print("It is not an integer")
                
    if wrong_input == False:
        bin_list = bin_list[::-1]

        for num in bin_list:
            dec_value += num*2**power_ticker
            power_ticker += 1
        
        values_list.append(dec_value)
        print(dec_value)

    
    return dec_value, keep_on

def run():
    
    global dec_value
    global values_list
    global keep_on

    print("To quit press 'q'")

    while keep_on:
        convert()
        dec_value = 0     

    print(values_list)

run()