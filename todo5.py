class todo:
    def __init__(self):
        self.lis = []
        self.items = []
        self.temp = []
        self.i = 1

    def addtask(self, task):
        global i
        self.lis.append({'task':task,'id':self.i, 'is_deleted': False, 'is_complete': False})
        self.i += 1
        print("task is added in your list")
        print("-----*****------")
        return 1

    def viewtask(self):
        if not self.lis:
            print('empty list')
        else:
            print("-----*****------")
            for l in self.lis:
                if not l['is_deleted']:
                    print(l['id'], l['task'])
        print("-----*****------")
        return

    def delete_one_task(self, number):
        if not self.lis:
            print("-----*****------")
            print('empty list ')
            print("-----*****------")
        else:
            print("-----*****------")
            for l in self.lis:
                if number == l['id']:
                    print(' your task  is deleted')
                    l['is_deleted'] = True
        print("-----*****------")
        return 1

    def completed_task(self, c):
        if not self.lis:
            print('empty list')
            return 1
        else:
            print("-----*****------")
            for i in self.lis:
                if c == i['id']:
                    print('task marked As  completed')
                    i['is_complete'] = True
            print("-----*****------")

    def completed_list(self):
        if not self.lis:
            print("-----*****------")
            print("no task is completed")
            print("-----*****------")
            return 0
        else:
            print("-----*****------")
            print('completed tasks are')
            for l in self.lis:
                if l['is_complete'] == True:
                    print(l['id'], l['task'])
        print("-----*****------")
        return 1

    def delete_all(self):
        self.lis.clear()
        print("-----*****------")
        print('all tasks are deleted')
        if self.lis.length == 0:
            return 1
        else:
            return 0

    def delete_multiple(self, many):
        print("-----*****------")
        for i in many:
            for l in self.lis:
                if i == l['id']:
                    l['is_deleted'] = True
        print('seleced tasks r deleted')



if __name__ == '__main__':
    t = todo()
    press = 0
    while press <= 8:
            press = int(input('\n 1.to add task \n 2.to view task  \n 3.delete any task \n.4.enter task which is completed \n 5.view completed task\n 6.exit\n7.delete all\n8.delete selected tasks\nENTER YOUR CHOICE-->'))
            if press == 1:
                task = input('enter the task--> ')
                t.addtask(task)

            elif press == 2:
                t.viewtask()

            elif press == 3:
                number = int(input('enter key to delete the task \n'))
                t.delete_one_task(number)

            elif press == 4:
                c = int(input('enter which task is completed ?'))
                t.completed_task(c)

            elif press == 5:
                t.completed_list()

            elif press == 7:
                t.delete_all()

            elif press == 6:
                print("thank u")
                break

            elif press == 8:
                many = []
                n = int(input("enter how many elements u want to delete?"))
                for i in range(n):
                    many.append(int(input('enter task id to be deleted')))
                t.delete_multiple(many)

            else:
                print('wrong choice')
                choice = input("do u want to continue yea/no?")
                if choice == 'yes' or choice == 'y':
                    press = 7
                else:
                    break
