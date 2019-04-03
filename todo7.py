class Demo:
    def __init__(self):
#        self.dic = {}
        self.people ={}
        self.i = 1

    def addtask(self, task):

        global i
        self.people[self.i] = {'task': task, 'is_deleted': False, 'is_complete': False}
        if self.i in self.people:
            self.i += 1
            return True
        else:
            return False



    def viewtask(self):
        print("TASK ID \t TASK NAME")
        for l in self.people:
            if self.people[l]['is_deleted'] is False:
                print(l, '\t\t\t', self.people[l]['task'])
        print("-----*****------")
        return

    def delete_one_task(self, number):
        if number in self.people:
            self.people[number]['is_deleted'] = True
            return True
        else:
            print("task is not in the list")
            return False

    def completed_task(self, c):
        if c in self.people:
            self.people[c]['is_complete'] = True
            return True
        else:
            return False
    def completed_list(self):
        print("TASK ID \t TASK NAME")
        for d in self.people:
            if self.people[d]['is_complete'] is True:
                print(d, '\t\t\t', self.people[d]['task'])
        print("-----*****------")

        return


    def delete_multiple(self, many):
        print("-----*****------")
        for k in many:
            if int(k) in self.people:
                self.people[int(k)]['is_deleted'] = True
                if self.people[int(k)]['is_deleted'] is True:
                    return True
                else:
                    return False
        print('seleced tasks r deleted')
        print('**--------******')



if __name__ == '__main__':
    t = Demo()
    press = 0
    while press <= 8:
        press = int(input('\n 1.to add task \n 2.to view task  \n 3.delete any task \n.4.enter task which is completed \n 5.view completed task\n 6.exit\n7.delete all\n8.delete selected tasks\nENTER YOUR CHOICE-->'))

        if press == 1:
            task = input('enter the task--> ')
            a = t.addtask(task)
            if a:
                print('**--------******')
                print("----task is added in your list-----")
                print('**--------******')
            else:
                print('**--------******')
                print("not added in your list")
                print('**--------******')

        elif press == 2:
            if len(t.people) == 0:
                print("-----*****------")
                print('empty list')
                print("-----*****------")

            else:
                print("-----*****------")
                t.viewtask()
            print("-----*****------")

        elif press == 3:
            number = int(input('enter key to delete the task \n'))
            if len(t.people) == 0:
                print("-----*****------")
                print('empty list ')
                print("-----*****------")
            else:
                t.delete_one_task(number)
                print("---your task is deleted successfully---")

        elif press == 4:
            c = int(input('--enter which task is completed ?--'))
            if len(t.people) == 0:
                print('empty list')
            else:
                if c in t.people:
                    print(' your task  is deleted')
                    t.completed_task(c)
                    print("---task marked completed successfully---")
                    print("-----*****------")


        elif press == 5:
            if len(t.people) == 0:
                print("-----*****------")
                print("<-No task is completed->")
                print("-----*****------")
            else:
                print("-----*****------")
                print('completed tasks are')
                t.completed_list()

        elif press == 7:
            t.people.clear()
            print("-----*****------")
            print('all tasks are deleted')
            print("-----*****------")

         #   t.delete_all()

        elif press == 6:
            print("thank u")
            break

        elif press == 8:
            many = []
            n = int(input("enter how many elements u want to delete?"))
            for i in range(n):
                many.append(input('enter task id to be deleted'))
            t.delete_multiple(many)

        else:

            print('wrong choice')
            choice = input("do u want to continue yea/no?")
            if choice == 'yes' or choice == 'y':
                press = 7
            else:
                break


