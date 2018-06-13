def mul_table(n, i=1):
    print (n*i)
    if i != 15:
        mul_table(n,i+1)
mul_table(12)