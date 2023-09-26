dato=int(input())
for n in {2,3,5,7,13}:
    if n==13:
        print("no es multiplo de ninguno de los primeros cuatro primos")
        break
    elif dato%n==0:
        print("es multiplo de {}".format(n))
        break
     