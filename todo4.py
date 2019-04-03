import sys
dic={}
lis=[]
items=[]
temp=[]
press=0
i=1
while(press <=8):
            press=int(input('\n 1.to add task \n 2.to view task  \n 3.delete any task \n.4.enter task which is completed \n 5.view completed task\n 6.exit\n7.delete all\n8.delete selected tasks\nENTER YOUR CHOICE-->'))
            if press == 1:
                task = input('enter the task ')
                lis.append({'task':task,'id':i,'is_deleted':False,'is_complete':False})
                i+=1
            elif press == 2:
                if not lis:
                    print('empty list')
                else:
                    for l in lis:
                        if not l['is_deleted']:
                            print(l['id'],l['task'])
            elif press == 3:
                if not lis:
                    print('empty list ')
                else:
                    number=int(input('enter key to delete the task \n'))
                    for l in lis:
                        if number == l['id']:
                            print ('task deleted')
                            l['is_deleted']=True
            elif press == 4:
                if not lis:
                    print('empty list')
                else:
                    c=int(input('enter which task is completed ?'))
                    for l in lis:
                        if c == l['id']:
                            print ('task completed')
                            l['is_complete']=True
                    print ('wrong id')
            elif press == 5:
                if not lis:
                    print("no task is completed")
                else:
                    print ('completed task are')
                    for l in lis:
                        if  l['is_complete']==True:
                            print(l['id'],l['task'])
            elif press==7:
                 lis.clear()
                 print('all tasks deleted')

            elif press == 6:
                print('thanks :)')
                sys.exit(0)
            elif press==8:
                n=int(input('enter how many '))
                for i in range(n):
                    items.append(int(input('enter task id to be deleted')))
                for j in items:
                    for l in lis:
                        if j ==l['id']:
                            l['is_deleted']=True
                print('seleced tasks r deleted')
            else:
                print('try again')
                sys.exit(0)
            
