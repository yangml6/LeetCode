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