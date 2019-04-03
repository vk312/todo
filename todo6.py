class todo6:
    def __init__(self):
        self.dic = {}
        self.i = 1

    def addtask(self, task):
        global i
        self.dic.setdefault('task', []).append(task)
        self.dic.setdefault('id', []).append(self.i)
        self.dic.setdefault('is_deleted', []).append(False)
        self.dic.setdefault('is_complete', []).append(False)
        self.i += 1
        print(self.dic)
        print("task is added in your list")
        print("-----*****------")
        return 1

    def viewtask(self):
        if not self.dic:
                print('empty dictionary')
        else:0
            print("-----*****------")
            if self.dic["is_deleted"] is False:
                print(self.dic['id'], self.dic['task'])
        print("-----*****------")
        return

    def delete_one_task(self, number):
        if not self.dic:
            print("-----*****------")
            print('empty list ')
            print("-----*****------")
        else:
            print("-----*****------")
            if number in self.dic['id']:
                print(' your task  is deleted')
                self.dic['is_deleted'][number-1] = True
            print(self.dic)
        print("-----*****------")
        return 1

    def completed_task(self, c):
        if not self.dic:
            print('empty list')
            return 1
        else:
            print("-----*****------")
            if c in self.dic['id']:
                print('task marked As  completed')
                self.dic['is_complete'][c-1] = True
            print(self.dic)
            print("-----*****------")

    def completed_list(self):
        if not self.dic:
            print("-----*****------")
            print("no task is completed")
            print("-----*****------")
            return 0
        else:
            print("-----*****------")
            print('completed tasks are')
            if self.dic['is_complete'] is True:
                print(self.dic['id'], self.dic['task'])
        print("-----*****------")
        return 1

    def delete_all(self):
        self.dic.clear()
        print("-----*****------")
        print('all tasks are deleted')
        if len(self.dic) == 0:
            return 1
        else:
            return 0

    def delete_multiple(self, many):
        print("-----*****------")
        for k in many:
            if k in self.dic['id']:
                self.dic.update({'is_deleted': True})
        print('seleced tasks r deleted')



if __name__ == '__main__':
    t = todo6()
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
                many = {}
                n = int(input("enter how many elements u want to delete?"))
                for i in range(n):
                    many = input('enter task id to be deleted')
                t.delete_multiple(many)

            else:
                print('wrong choice')
                choice = input("do u want to continue yea/no?")
                if choice == 'yes' or choice == 'y':
                    press = 7
                else:
                    break
