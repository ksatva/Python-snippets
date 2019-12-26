def table(n):
   global call
   call =1
   xtable(n, call)

def xtable(n):
   for i in range(1, 11):
      print('{0} x {1} = {2}'.format(n,i,n*i))
      #print('next? ',end=' ')
      #reply = input()
      #if reply == ignorecase('n'):
       #   return 
      #else:
       #  xtable(n,call)
