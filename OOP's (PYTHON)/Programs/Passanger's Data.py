class Train:
    def __init__(self, name, aadhar_no, mobile_no):
        self.train_name = "Indian Railways"
        print(self.train_name)
        self.passenger_data = []
        self.book(name, aadhar_no, mobile_no)
        
    def book(self, name, aadhar_no, mobile_no):
        temp_name = input(f"Confirm the name ----> ").title()
        temp_aadhar_no = int(input(f"Confirm the aadhar no ----> "))
        temp_mobile_no = int(input(f"Confirm the mobile number ----> "))

        if temp_name == name and temp_aadhar_no == aadhar_no and temp_mobile_no == mobile_no:
            self.passenger_data.append((name, aadhar_no, mobile_no))
            print('Data has been stored!!')
        else:
            print("Try again")

name = input(f"Enter the name ----> ").title()
aadhar_no = int(input(f"Enter the aadhar no ----> "))
mobile_no = int(input(f"Enter the mobile number ----> "))
p1 = Train(name, aadhar_no, mobile_no)
print(p1.passenger_data)
