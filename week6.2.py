class A:
    def Method(self):
        print("A class is defined")
        super().Method()
class B:
    def Method(self):
        print("B class is defined")
        super().Method()
class C(A,B):
    def Method(self):
        print("C is defined")
        super().Method()
        obj=C()
        obj.Method()