import requests
class Demo:
    def __init__(self):
        self.people ={}
        self.lis = []
        self.i = 1
        self.url = 'https://trial-todo.herokuapp.com/'

    def getmethod(self):
        getcall = requests.get(url=self.url)
        return getcall


    def addtask(self, task):
        global i
        self.people= {'subject': task}
        self.rget = requests.post('https://trial-todo.herokuapp.com/', json=self.people)
        #print(self.rget.text)
        print('task added')


    def viewtask(self,value):
        print("TASK ID \tSTATUS \tTASK NAME ")
        self.rget = Demo.getmethod(self)
        r = self.rget.json()
        if value is 'incomplete':
            for i in r['list']:
                if (i['done'] == False):
                    print(i['auto_increment_id'], '\t\t\t', i['done'], '\t\t\t', i['subject'])

        elif value is 'complete':
            for i in r['list']:
                if (i['done'] == True):
                    print(i['auto_increment_id'], '\t\t\t', i['done'], '\t\t\t', i['subject'])

        else:
            for i in r['list']:
                    print(i['auto_increment_id'], '\t\t\t', i['done'], '\t\t\t', i['subject'])

    def delete_one_task(self, number):
        self.rget = requests.delete(url=self.url+str(number))
        #print(self.rget)
        return self.rget

    def completed_task(self, c):
        self.people = {'done': True}
       # print(c)
        self.rget = requests.put(url=self.url + 'done/' + str(c)+'/', json=self.people)
        #print(self.rget)
        return self.rget


    def completed_list(self):
        print("TASK ID \tTASK NAME")
        self.rget = Demo.getmethod(self)

        r = self.rget.json()
        for j in r['list']:
            if j['done']:
                print(j['auto_increment_id'], '\t\t\t', j['subject'])
        print("-----*****------")


    def delete_multiple(self, many):
        print("-----*****------")
        self.rget = requests.get(url=self.url)
        #print(self.rget)
        r = self.rget.json()
        #print(r)
        for k in many:

            self.rdel = requests.delete(url=self.url + k)
        return self.rdel




if __name__ == '__main__':
    t = Demo()
    press = 0
    while press <= 8:
        press = int(input('\n 1.to add task \n 2.to view all tasks \n 3 view completed task\n 4.to view incomplete task \n5.delete one task \n.6.mark task which is completed \n 7.delete multiple tasks\nENTER YOUR CHOICE-->'))

        if press == 1:
            task = input('enter the task--> ')
            r = t.addtask(task)


        elif press == 2:
            t.viewtask('all')

        elif press == 3:
            t.viewtask('complete')   #to view completed tasks

        elif press == 4:
            t.viewtask('incomplete')    #to view in-completed tasks

        elif press == 5:
            number = int(input('enter key to delete the task \n'))
            r = t.delete_one_task(number)




        elif press == 6:
            c = int(input('--enter which task is completed ?--'))
            r= t.completed_task(c)

        elif press == 5:

                t.completed_list()

        elif press == 7:
            many = []
            n = int(input("enter how many elements u want to delete?"))
            for i in range(n):
                many.append(input('enter task id to be deleted'))
            r= t.delete_multiple(many)

        else:

            print('wrong choice')
            choice = input("do u want to continue yea/no?")
            if choice == 'yes' or choice == 'y':
                press = 7
            else:
                break


