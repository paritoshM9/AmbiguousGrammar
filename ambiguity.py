def NT_exist(string,word,uniq_NT): #to check if non-terminals are present in the string
    for char in string:
        if(char in uniq_NT):
            return True
    return False
def chance(string,word,S):#to check if the newstring 'can' form the given word or not
    num_a=[] #num_a= number of a's in word
   
    n_a=[]   #n_a= number of a's in string
    z=[]
    z1=[]
    x=[]
    x1=[]
    c=0
    c1=0
    c2=0
    for char in word:
        x.append(char)
    for i in range(len(x)-1):
        for j in  range(i+1,len(x)):
            if (x[i]!=x[j] and (x[i] not in z)):
                        z.append(x[i])
    for i in range(len(z)):
           num_a.append(0)
           n_a.append(0)
                        
    for char in word:
        for i in range(len(z)):
           if(char==z[i]):
             num_a[i]=num_a[i]+1
                                 
    for char in string:
        for i in range(len(z)):
           if(char==z[i]):
             n_a[i]=n_a[i]+1
                            
    for i in range(0,len(num_a)):
        if(n_a[i]>num_a[i]): #if no. of terminals in string is greater than
      # that of word , BACTRACK
          c2=1
    if("" not in S):
        if(len(string)>len(word)):
            print("**Backtrack**")
            return False
    else:
        
        if(len(string)>2*len(word) ):
           print('**Backtrack**')
           return False   
    if c2==0:
        return True
    
    else:
        print("**Backtrack**")
        return False
       
def LMD(string,word,prod,count,cnt,uniq_NT,start_index,S):
    
    if(NT_exist(string,word,uniq_NT)==False): # only terminals are there
        if(string==word): 
            print(string)
            count=count+1
            cnt.append(count)
            print('**Derived**')
        return False
   
    leftmost=""
    for char in string:
        if(char in uniq_NT):
            leftmost=char
            left_index=uniq_NT.index(leftmost)
            break;
    for i in range(len(prod[left_index])):
            
        newstring=string.replace(leftmost,prod[left_index][i],1) #replace the leftmost S by j'th production
        print(newstring)
        if(chance(newstring,word,S)): 
            if(LMD(newstring,word,prod,count,cnt,uniq_NT,start_index,S)): # Recursive call to function using new string
                
                return True
        newstring=string #backtrack to the previous generated string and substitute different value of production in the next iteration
    return False
def RMD(string,word,prod,count,cnt,uniq_NT,start_index,S):

    if(NT_exist(string,word,uniq_NT)==False): # only terminals are there
        if(string==word): 
            print(string)
            count=count+1
            cnt.append(count)
            print('**Derived**')
        return False
   
    rightmost=""
    newstring=''.join(reversed(string))
    for char in newstring:
        if(char in uniq_NT):
            rightmost=char
            right_index=uniq_NT.index(rightmost)
            break;
    for i in range(len(prod[right_index])):
            
        newstring=newstring.replace(rightmost,''.join(reversed(prod[right_index][i])),1) #replace the leftmost S by j'th production
        newstring=''.join(reversed(newstring))
        print(newstring)
        if(chance(newstring,word,S)): 
            if(RMD(newstring,word,prod,count,cnt,uniq_NT,start_index,S)): # Recursive call to function using new string
                
                return True
        newstring=''.join(reversed(string)) #backtrack to the previous generated string and substitute different value of production in the next iteration
    return False
    


p=int(input("Enter no. of productions:"))
S=[]
NT=[]
count_NT=0
uniq_NT=[]
#array for right hand side values of productions
print("Enter the productions ( use # to denote null string )\n")
for n in range(p):
    
    str=input()
    temp=str.split('->')
    if(temp[0] not in NT):
        
        uniq_NT.append(temp[0])
        count_NT+=1
    NT.append(temp[0])
    if(temp[1]=='#'):
        S.append("")
    else:
        S.append(temp[1])
prod=[[] for i in range(count_NT)]
for i in range(count_NT):
    for j in range(len(NT)):
        if(uniq_NT[i]==NT[j]):
            prod[i].append(S[j])

word=input("Enter the word to be checked: ")
start=input("Enter the Start Symbol: ")
start_index=uniq_NT.index(start)

count=0
right=[]
left=[]
print("Right Most Derivations:-")
for i in range(len(prod[start_index])):
    RMD(prod[start_index][i],word,prod,count,right,uniq_NT,start_index,S)
print("Left Most Derivation:-")
for j in range(len(prod[start_index])):
    LMD(prod[start_index][j],word,prod,count,left,uniq_NT,start_index,S)
print("The number of Right Most Derivations is:",len(right))
print("The number of Left Most Derivations is:",len(left))
if(len(left)>1 or len(right)>1):
            print("Ambiguous")
else:
    print("Not Ambiguous for the given word")








    
