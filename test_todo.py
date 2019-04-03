from todo7 import Demo


class Test:

    def setup_method(self):
        self.t1 = Demo()
        self.t1.addtask('adasdasd')


    def test_addtask(self):
        x = 'call'
        r = self.t1.addtask(x)
        print(r)
        print("in addtask")
        assert r


    def test_deltask(self):
        y = 1
        p = self.t1.delete_one_task(y)
        print(p)
        print("in delete  one task")
        assert p


    def test_completetask(self):
        z = 1
        q = self.t1.completed_task(z)
        print("in completed list ")
        print(q)
        assert q

    def test_muldelete(self):
        n = self.t1.delete_multiple([1, 2, 3])
        print(n)
        print("multiple tasks deleted ")
