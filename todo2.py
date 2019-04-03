#import sqlite3
import array
import sys
class Todo:
    def __init__(self):
        self.arr=['book ticket','make a call','send mail']
        self.com=[]
    def start(self):
        print('welcome to todo app')
    def choice(self):
        press = 0
        flag = 0
        while(press !=7):
            press=int(input('\n 1.to add task \n 2.to view task  \n 3.delete any task \n 4.to exit\n5.enter task which is completed \n 6.view completed task\n'))
            if press == 1:
                task = input('enter task ')
                self.arr.append(task);
            elif press == 2:
                print('list of to do are :\n')
                for i in range(0,len(self.arr)):
                    print (i+1,self.arr[i])
            elif press == 3:
                number=int(input('enter id to delete the task \n'))
                #if number==self.arr[i]:
                print(self.arr.pop(number-1),"deleted")
            elif press == 4:
                print('thanks :)')
                sys.exit()
            elif press == 5:
                c=int(input('enter which task is completed ?'))
                #self.com.append(c-1)
                com=self.arr.copy.copy(c)
            elif press == 6:
                print ('completed task are')
                for i in range(0,len(self.com)):
                    print(i+1,self.arr[i])
            else:
                print('try again')
               
t=Todo()
t.start()
t.choice()
