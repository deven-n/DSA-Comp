/* Consider a telephone book database of N clients. Make use of a hash table implementation to quickly look up client‘s telephone number. 
   Make use of two collision handling techniques and compare them using number of comparisons required to find a set of telephone numbers 
   (Python)
*/

class hasht:
    arry = []
    for i in range (10):
        a = []
        arry.append(a)
    def insert(self , no):
        if (len(self.arry[no%10])==0):
            self.arry[no%10].append(no)
        else:
            print("Collision occured \nChoose which collision resulution technique you want to use \n1) open chaning \n2) linear probing")
            v = int(input())
            if(v == 1):
                self.arry[no%10].append(no)
            if(v==2):
                N = no%10
                T = N + 10
                N = N + 1
                while(len(self.arry[N%10]))!= 0 and T > N :
                    N = N + 1
                if (T == N):
                    print("Hash table is full!!!")
                else:
                    self.arry[N%10].append(no) 
 
 
    def printhash(self): 
        for i in range (len(self.arry)):
            print(i," " , end = "")
            if (len(self.arry[i])==0):
                print(" ----- ")
            else:
                for j in self.arry[i] :
                    print(j, " ", end ="")
                print(" ")
            
        
p1 = hasht()
c =-1
while c !=3:
    print("Enter 1 to add the no \nEnter 2 to display hashing table \nEnter 3 to exit") 
    c = int(input())
    if c == 1:
        print("Enter the no you want to insert")
        num = int(input())
        p1.insert(num)
    if c ==2:
        p1.printhash()

