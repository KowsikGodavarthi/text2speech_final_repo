n=169
if n>1:
     for i in range(2,int(n/2)+1):
             if(n%i) == 0:
                     print("Not a prime number")
                     break
             else:
                     print("Prime Number")
                     break
     else:
             print("Not a prime number")
