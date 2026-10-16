# Q1
def word_f(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency
sentence = input("Enter a sentence: ")
result = word_f(sentence)
print(result)

# Q2
def words_f(sentence):
    word=sentence.replace('',' ')
    word=word.split()
    g={}
    for k in word:
        if k in g:
            g[k] +=1
        else:
            g[k]=1
    return g
sentence=input('enter the sentence')
y=words_f(sentence)
print(y)            
# Q3
def non_f(sentence):
    word=sentence.replace('',' ')
    word=word.split()
    h=[]
    for j in word:
        count=0
        for i in word:
            if i==j:
                count+=1
        if count==1:
            h.append(j)
            break
      
    return h
sentence=input("enter the sentence")
z=non_f(sentence)
print(z)
# Q4
def two_f(a,b):
    word=a.replace('',' ')
    war=b.replace('',' ')
    if war in word:
        return 'anagram'
    else:
        return'anagram'
a=input('enter the string')
b=input('enter the string')
c=two_f(a,b)
print(c)             
#Q5
def first_f(sentence):
    word = sentence.replace(' ', '')
    for i in range(len(word)):
        for j in range(i):
            if word[i] == word[j]:
                return word[i]
    return None

sentence = input('Enter the string: ')
x = first_f(sentence)
print(x)
#Q6
def all_f(number):
    c=[]
    for k in number:
        if k!=0:
            c.append(k)
    zeros=number.count(0)
    c.extend([0]*zeros)
    return c
number=list(map(int,input('enter the numbers').split()))    
x=all_f(number)
print(x)
#Q7
def second_highest(numbers):
    unique = list(set(numbers))
    unique.sort()
    if len(unique) < 2:
        return None
    return unique[-2]
numbers = [10, 20, 40, 30, 40, 20]
print(second_highest(numbers))
# Q8
def remove_dupl(number):
    r=[]
    for k in number:
        if k not in r:
            r.append(k)
    return k
number=list(map(int,input('enter the numbers').split()))  
y=remove_dupl(number)
print(y)  
#Q9
def missing_number(nums, n):
    for i in range(1, n + 1):
        if i not in nums:
            return i
nums = [1, 2, 4, 5, 6]
n = 6
s=missing_number(nums, n)
print(s)

#Q10

def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []
nums = [2, 7, 11, 15]
target = 9
p=find_pair(nums, target)
print(p)

#Q11

def closest_zero(nums):
    closest = nums[0]
    for i in nums:
        if abs(i) < abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i > closest:
            closest = i
    return closest
nums = [-8, -3, 2, 5, -2]
v=closest_zero(nums)
print(v)

#Q12

def common_elements(list1, list2):
    result = []
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
t=common_elements(list1, list2)
print(t)

# Q13

def rotate_right(nums, k):
    if len(nums) == 0:
        return nums
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k != 0 else nums
nums = [1, 2, 3, 4, 5]
k = 2
u=rotate_right(nums, k)
print(u)

#Q14

def max_consecutive_sum(nums):
    maximum = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        total = nums[i] + nums[i + 1]
        if total > maximum:
            maximum = total
    return maximum
nums = [4, 7, 2, 9, 5]
e=max_consecutive_sum(nums)
print(e)

# Q15

def all_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])
                if pair not in pairs:
                    pairs.append(pair)
    pairs.sort()
    return pairs
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
a=all_pairs(nums, target)
print(a)
