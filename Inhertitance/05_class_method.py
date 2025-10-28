class employee:
    a = 1
    @classmethod #it will access class attributes even if we use instance attributes
    def show(pat):
        print(f"The class value is {pat.a}")
    
e = employee()
e.a = 45
e.show() 