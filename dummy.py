import time
import csv 


from PIL import Image
img = Image.open('enaira.png')
 
# Output Images
#img.show()

 
my_list=[] 
my_dict={}
emailPassword={} 
with open("./posapplicant.csv", 'r') as file:
    csvreader = csv.reader(file)
    
    for row in csvreader:
           
        my_list.append(row)
        emailPassword[row[1]]   = row[3]
emailPassword.pop('email')
#print(emailPassword)  
#print(my_list) 
my_dicts={'receivers':'8067760310', 'a':'08067760310'}    
#print(type(my_dicts.items()))
def  mubbs(args):
    return args

    
for key,value in my_dicts.items():
    if len(value)==10:
        value='0'+value
    
    else:
        value=value
        
        
        time.sleep(1)
    print(mubbs(key),"%s" %(key),f"hello,{key}")
for list in my_list:
    my_dict[list[1]]=[list[2],list[3]]
     
my_dict.pop('email')
#print(my_dict)
dicts={}

lists=['a','b','c','a','e','f','g','h','i']
#print(range(len(lists)),len(lists))
i=0

while i < len(lists):
    
    dicts[lists[i]]=[lists[i+1],lists[i+2]]
    if lists[i] in dicts.keys():
        lists[i]=lists[i]+'1'
    i=i+3    

#print(dicts.keys())
def FIFO(param):
    try:
        i=0
        while i < len(param):
            print(param[i])
            i=i+1
    except:
        if(type(param)==int):
            print('Str or List expected')
FIFO(12)

def smallInt(param):
    i=0
    try:
        if(len(param)==1):
            return param
        else:
            while i <len(param):
                if(param[-1]>param[i])
    except:
        pass
