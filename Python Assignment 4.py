#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Triangle:
 def __init__(self, side1, side2, side3):
  self.side1 = side1
  self.side2 = side2
  self.side3 = side3
  print ("Initialised Triagle super class [" +  str(side1) + "," + str(side2) + "," + str(side3) + "]")

class Triangle_Utilities(Triangle):
 
 def __init__(self, side1, side2, side3):
  print ("Initialised Utils Child class" )
  super(Triangle_Utilities, self).__init__(side1, side2, side3)

 def get_area(self):
  s = (self.side1 + self.side2 + self.side3)/2
  print (str(s))
  return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

instance = Triangle_Utilities(3,4,5)
print ("Area of triangle = " + str(instance.get_area()) )


# In[2]:


class list_Utilities:
 def __init__(self, wordlist):
  self.wordlist = wordlist
  print ("Initialised list_Utilities object")

 def filter_long_words(self, n):
  return list(filter(lambda x:len(x) > n, self.wordlist))

instance = list_Utilities(["This","is","a","beautiful","day"])
print ("New List of Words  => " + str(instance.filter_long_words(3)) ) 


# In[3]:


def map_Words_to_Length(List):
    ''' This function Map's the words with their corresponding length'''
    return list(map(len, List))

word_List=list(input("Input : Please enter Words : ").split(","))
#List Comprehension has been done to remove white trailing white spaces
List=[x.strip() for x in word_List]
#function Execution
Words_lengths=map_Words_to_Length(List)

print("Output: Length of Words are :",Words_lengths )


# In[4]:


def vowel_checker(inputChar):
    #docstring
    '''This function will return True/False based upon input character provided by user'''
    return_value=''
    if(len(inputChar)==1):
        vowel_list=['a','e','i','o','u']
        if (inputChar.lower() in vowel_list):
            return_value= True
        else:
            return_value= False
    else:
        return_value="Please enter single character only!"        
    return return_value

#Ask user's Input
print("Enter character to check that it is Vowel or not")
input_value = input("Input Value: ")
#Function Execution
output_value=vowel_checker(input_value) 
#Output
print("Output Value:",output_value)


# In[5]:


print("Enter character to check that it is Vowel or not")
input_value = input("Input Value: ")

#Function Execution
output_value=vowel_checker(input_value) 

#Output
print("Output Value:",output_value)


# In[ ]:




