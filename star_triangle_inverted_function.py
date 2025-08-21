def star_triangle_inverted(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end = " ")
        print()
n = int(input("Enter no. of lines: "))
star_triangle_inverted(n)