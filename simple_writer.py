import random
import re

model={'START':['I','We','He','She','They']}
file_read=open("file")
file_list=file_read.read().strip().split()
text=''
for k in range(len(file_list)-1):
    text+=file_list[k]+" ";
    if file_list[k] not in model.keys():
        model[file_list[k]]=[file_list[k+1]];
    else:
        model[file_list[k]].append(file_list[k+1])
pivot = 'START'
for k in range(10000):
            rand=random.randint(0,len ( model[pivot] ) -1 )
            pivot=model[pivot][rand]
            print(pivot,end=' ')
            
