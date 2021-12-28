def lovefunc( flower1, flower2 ):
    return bool((flower2+flower1)%2)

print(lovefunc(1,4)) #T
print(lovefunc(2,4))#F
print(lovefunc(0,5))#T
print(lovefunc(1,1))#F
print(lovefunc(0,0))#F