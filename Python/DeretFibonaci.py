#  int h = 1, h2 = 1, result = 1;
       
#        // 1, 1, 2, 3, 5, 8
       
#        for (int i = 1; i <= 10; i++) 
#        {
#            System.out.print(result + " ");
#            result = h + h2; 
#            h = h2;
#            h2 = result;
#        }
h = 1 
h2 = 1
result = 1

for i in range (1 , 11 ):
    print(result , end = ' ')
    result = h + h2
    h = h2
    h2 = result
    