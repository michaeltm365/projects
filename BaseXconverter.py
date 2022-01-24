import math
base_or_dec = input("Input 'd' to convert a number from decimal to base X. Input 'b' to convert a number from Base X to decimal: ")
while base_or_dec != "d" and base_or_dec != "b":
    base_or_dec = input("Input 'd' to convert a number from decimal to base X. Input 'b' to convert a number from Base X to decimal: ")
if base_or_dec == "d":
    og = int(input("Input your decimal integer: "))
    base_x = int(input("Input the base you want your number converted to (1-9): "))
    conv = []
    while og != 0:
        conv.insert(0,og % base_x)
        og = math.floor(og / base_x)
    print("Your number in base",base_x,"is:")
    for i in conv:
        print(i, end="")
else:
    og = (input("Input your integer: "))
    og = [int(a) for a in str(og)]
    base_x = int(input("Input the base your number is in (2-9): "))
    conv = 0
    place_value = 1
    num_length = len(og)
    print(num_length)
    for i in og:
        i = int(i)
        if i>0:
            conv += i * (base_x ** (num_length - place_value))
        place_value += 1
    print("Your number in decimal is:")
    print(conv)

        
            
    
    
    
        
    

                    

                
