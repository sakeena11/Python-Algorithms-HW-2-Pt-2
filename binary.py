test_inputs = [15, 16, 21, 23, 16383, 16384, 0]
for num in test_inputs: 
    list = []

    def convert_binary(num):
        if int(num) > 0:
            (convert_binary(int(num)//2))
        list.append(int(num) % 2)    

    convert_binary(num)

    count = list.count(1)
    print(f"# of 1s in binary expression for {num} is {count}")
    print()

