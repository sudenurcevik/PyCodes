def matrix():
    augmented_confirmation=input("augmented or not(please enter t if augmented):")
    row=input("Please enter the number of row:")
    işlem="[ "
    for i in range(int(row)):
        i=input("Please enter the rows:")
        son="( "
        numbers=i.split(",")
        if augmented_confirmation=="t":
            for a in numbers[:-1]:
                son += f"{a}, "
            son=son[:-2]
            son+= f"| {numbers[-1]}  "
        else:
            for a in numbers:
                son += f"{a}, "
        son = son[:-2] + ")"
        işlem += son + ", "

    işlem = işlem[:-2] + " ]"
    print(işlem)

matrix()