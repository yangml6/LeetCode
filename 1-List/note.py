#判断为空
nums = []
if not nums:
    print('nums is empty')

#For sequences , (strings, lists, tuples), use the fact that empty sequences are empty
#Yes:
if not seq:
if seq:
#No:
if len(seq):
if not len(seq)

if len(seq) == 0:
    print('seq is empty')


#'int' object is not iterable； 不能直接 for i in int_
# object of type 'int' has no len()； 不能 for i in range（len（int_））
#将之转换为 str
for i in str(int_):
    seq.append(i) #['1', '2', '4']
    seq2.append(int(i))#[1, 2, 4]


#字典 key 是唯一的

#set()能消除重复元素，集合类型,无序不重复

#collections
collections.Counter()  计数，键值对形式，元素为 key，计数为 value
.deque  双端队列 O(1)，list 是 O(n)
.orderedDict  有序字典



nums[:] = nums[n-k:] + nums[:n-k] 
nums = nums[n-k:] + nums[:n-k]
# The previous one can truly change the value of old nums, 
# but the following one just changes its reference to a new nums not the value of old nums.

#python3 xrange()改名为 range（）


nums[i], nums[zero] = nums[zero], nums[i]
#两个值交换