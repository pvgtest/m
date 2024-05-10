import numpy as np
j = int(input("Enter the number from 0 to 9 : "))

step_function = lambda x:1 if x>=0 else 0

training_data = [
    {'input':[1,1,0,0,0,0] , 'label':1},
    {'input':[1,1,0,0,0,1] , 'label':0},
    {'input':[1,1,0,0,1,0] , 'label':1},
    {'input':[1,1,0,0,1,1] , 'label':0},
    {'input':[1,1,0,1,0,0] , 'label':1},
    {'input':[1,1,0,1,0,1] , 'label':0},
    {'input':[1,1,0,1,1,0] , 'label':1},
    {'input':[1,1,0,1,1,1] , 'label':0},
    {'input':[1,1,1,0,0,0] , 'label':1},
    {'input':[1,1,1,0,0,1] , 'label':0},
]

weights = np.array([0,0,0,0,0,1])

for data in training_data:
    input=np.array(data['input'])
    label=data['label']
    output = step_function(np.dot(input, weights))
    error=label-output
    weights+=input*error


input = np.array([int(x) for x in list('{0:06b}'.format(j))])

output_value=step_function(np.dot(input,weights))
if output_value==0:
    output="odd"
else:
    output="even"

print(j," is ",output)