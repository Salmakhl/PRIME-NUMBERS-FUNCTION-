def prim():
  tab=[]
  for i in range(1,nbr) :
      X = 0
      for j in range (1,i+1) :
        if i % j == 0 :
            X = X + 1
      if X == 2 :
               tab.append(i)
  return tab
nbr=int(input("enter a number :"))
print("the prime nuber less tan",nbr,prim())


     