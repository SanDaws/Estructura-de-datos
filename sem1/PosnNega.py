_sumne, _sumpo=0,0
for n in range(int(input())):
    dato=int(input())
    if dato >=0: _sumpo+=dato
    else:_sumne+= dato
print("positivos {}, negativos {}".format(_sumpo,_sumne))


