#!/usr/bin/env python
# coding: utf-8

# In[2]:


def binarysearch(a,lindex,rindex,key):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2
        if a[mindex]==key:
            return mindex
        if a[mindex]>key:
            rindex=mindex-1
        else:
            lindex=mindex+1
    return -1;
a=[1,2,3,4,5,6,7,8]
key=int(input("enter element to search"))
res=binarysearch(a,0,7,key)
if res!=-1:
     print("it is found")
else:
    print("it is not found")


# In[3]:


#Bubble sort 
def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end=" ")
        
list1=[3256,234,436,768,345,56]
bubblesort(list1)


# In[4]:


#creating a string
str = "application"
print(str)

str1 ='application'
print(str1)

str2 = """application test
          working
          completed
          list
          strings
          python"""
print(str2)


# In[5]:


str ="application"
print(str)
print("str[0]=",str[0])
print("str[1]=",str[1])
print("str[-3]=",str[-3])
print("str[-2]=",str[-2])
print("str[2]=",str[2])
print("str[2:-2]=",str[2:-2])
print("str[3:5]=",str[3:5])


# In[6]:


#count of upper case letters
def countupperletters(str):
    cnt=0
    for i in range (len(str)):
        if(str[i]<="A" or str[i]>="Z"):
            cnt=cnt+1;
        else:
            i=i+1;
    return cnt

print(countupperletters("HJKHJH")) 


# In[7]:


# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
     
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  
  
s=str(input("Enter The Character"))

ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 


# In[17]:


# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
     
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False


s=input("Enter The Character")

ans = isPalindrome(s) 
  
if ans == True: 
    print("Yes") 
else: 
    print("No") 


# In[19]:


#count of digits of a number
n=int(input("Enter The Number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)    


# In[1]:


def countchars(str):
    return len(str)
s=str(("Enter a String"))
countchars(s)


# In[2]:


def countdigit(n):
    return len(n)

countdigit("123456789")


# In[4]:


#count of upper case letters
def countupperletters(str):
    count=0
    for i in range (len(str)):
        if(str[i]<="A" or str[i]>="Z"):
            count=count+1;
        else:
            i=i+1;
    return count
            
print(countupperletters("OIOIOI"))            


# In[5]:


str='H'
str1='i'
str1.islower()


# In[6]:


def printdigits(str):
    return print(str)


str="Applications"
printdigits(str)


# In[10]:


def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end="")
    return " "        
          
print(printdigits("Miketesting 124123"))        


# In[11]:


def printingdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            a=int(str[i])
            sum=sum+a;
               
         
        
    return sum;


print(printingdigits("sad554673jjkx"))


# In[12]:


def printingdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            a=int(str[i])
            sum=sum+a;
               
         
        
    return sum;


print(printingdigits("kdjfh657546hd657"))


# In[14]:


#adding the even numbers in the string
def evensumdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            a=int(str[i])
            if(a%2==0):
                sum=sum+a;
    return sum
            
            
            
print(evensumdigits("ojgqbe30816425b2rt"))


# In[ ]:




