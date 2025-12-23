def printPowerset(arr,set_size):
    power_set_size = 2 ** set_size
    # Loop through numbers from 0 to 2^n - 1
    for outer in range(power_set_size):
        subset = ""
        for inner in range(set_size):
            # Check if jth bit is 1 set or not
            if outer &(1 << inner):
                subsert += str(arr[inner]) + " "
                print("{", subset.strip(),"}")

            # DRIVER CODE
            arr = [1 , 2, 3]    
            printPowerset(arr ,len(arr))

