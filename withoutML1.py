
import random2 as random
import requests
from sklearn.model_selection import train_test_split


f=open("colorset2.txt")
rawData=f.readlines()
X=[]
Y=[]
for each in rawData:
    color=each[:each.index(" ")]
    colorSplit=[color[:2],color[2:4],color[4:]]
    unhexed=[round(int(dd,16)/255,5) for dd in colorSplit]
    X.append(unhexed)
    Y.append(int(each[7]))
x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=1)

def fill_data(value):
    g=open("colorset2.txt","w")
    def randomColor():
        return ''.join([str(hex(random.randint(0,15)))[2:] for each in range(6)])
    count1=0
    count2=0
    count=0
    while count<value:
        color=randomColor()
        feed="https://webaim.org/resources/contrastchecker/?fcolor="+color+"&bcolor=FFFFFF&api"
        data =requests.get(feed)
        # print(data.text+"\t",count)
        check=1 if data.text[22]=="p" else 0
        each=color+" "+str(check)
        g.write(each+"\n")
        onlyC=each[:each.index(" ")]
        parts=[onlyC[0:2],onlyC[2:4],onlyC[4:]]
        digitPart=[int(inside,16) for inside in parts]
        if check==1 and count1<=value//2:
            # X.append(digitPart)
            # [Y.append(int(each[7])) for _ in range(3)]
            count1+=1
            count+=1
        elif check==0 and count2<=value//2:
            # X.append(digitPart)
            # [Y.append(int(each[7])) for _ in range(3)]
            count2+=1
            count+=1
    g.close()
# fill_data(300)
def fit(data_x,data_y,features,ransom):
    sets=[]
    for j in range(len(data_x)):
        max_i=-6
        max_i_val=["1"]
        min_i=6
        min_i_val=["1"]
        for k in range(ransom):
            sum=0
            state=[round(random.uniform(-1,1),5) for _ in range(3)]
            for i in range(features):
                sum+=data_x[j][i]*state[i]
            if sum>max_i:
                max_i=sum
                max_i_val[0]=state
            elif sum<min_i:
                min_i=sum
                min_i_val[0]=state
        temp=[round(min_i_val[0][i]+max_i_val[0][i],5) for i in range(3)]
        min_i_val[0]=temp
        max_i_val[0]=temp
        if data_y[j]==0:
            sets.append(min_i_val[0])
        else:
            sets.append(max_i_val[0])
    return sets
sets=fit(x_train,y_train,3,1000)

def find_best(sets,data_x,data_y):
    errors={}
    count=0
    for each in sets:
        print(each)
        error=0
        for i in range(len(data_x)):
            sum_i=0
            for k in range(len(sets[0])):
                sum_i+=data_x[i][k]*each[k]
            if data_y[i]==0:
               error+=sum_i-6
            else:
                error+=6+sum_i
        errors.update({count:error/75})
        count+=1
    return errors
result=find_best(sets,x_train,y_train)
errors=list(result.values())
mini=max(errors)
errors.sort()
ans=[0]
avg=[0]
for i in range(300):
    if result[i]==mini:
        ans=sets[i]
        # print("Minimum",sets[i])
e2=min(errors)
for each in result.keys():
    if result[each]==e2:
        avg=sets[each]
        # print("Averge ",sets[each])
avv=[ans[i]-avg[i] for i in range(3)]
if __name__=="__main__":    
    # print(avv)
    while True:
        
        dd=input("Enter Color Code")
        ddd=[dd[0:2],dd[2:4],dd[4:]]
        ddd=[int(each,16) for each in ddd]
        sum_i=0
        for k in range(len(avv)):
            sum_i+=ddd[k]*ans[k]
        if sum_i>0:
            print("Black Background!")
        else:
            print("White Background")
def predict(color): #color =[r,g,b]  # 0-> Black 
    print(ans)
    sum_i=0
    for k in range(len(avv)):
        sum_i+=color[k]*ans[k]
    return 0 if sum_i>0 else 1
# maxer=min(result)
# index=result.index(maxer)
# print(sets[index]

         