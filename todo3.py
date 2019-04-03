import sys
dic={}
#dic={"1":"book movie","2":"make a call","3":"java notes"}
#print(dic['3'])
dic1={}
#dic1['nation']='india'
#print(dic1)

press= 0
while(press <=7):
            press=int(input('\n 1.to add task \n 2.to view task  \n 3.delete any task \n.4.enter task which is completed \n 5.view completed task\n 6.exit\n'))
            length=len(dic)
            if press == 1:
                task = input('enter the task ')
                length=len(dic)
                length+=1
                dic[length]=task
            elif press == 2:
                if length==0:
                    print('empty list')
                else:
                    print('list of to do are :\n')
                    print( dic)
            elif press == 3:
                if length == 0:
                    print('empty list ')
                else:
                    number=int(input('enter key to delete the task \n'))
                    print(dic.pop(number))
                    print('deleted')
            elif press == 4:
                if length==0:
                    print('empty list')
                else:
                    c=int(input('enter which task is completed ?')) 
                    dic1= {c : dic[c]}
                    #dic1=da.copy()
                    dic.pop(c)
                    print(dic1)
            elif press == 5:
                leng=len(dic1)
                if leng==0:
                    print("no task is completed")
                else:
                    print ('completed task are')
                    for i in dic1:
                        print (dic1)
            elif press == 6:
                print('thanks :)')
                sys.exit(0)
            else:
                print('try again')
                sys.exit(0)
            
