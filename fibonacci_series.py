fibo=[0,1]
for i in range(0,20):
    toappend = fibo[i]+fibo[i+1]
    fibo.append(toappend)

print(fibo)



