class employee:
    def __init__(self):
        self.items = []



    def insert(self):
        n = int(input("Enter number of records: "))
        for i in range(n):
            ename = input("Employee name: ")
            eid = int(input("Employee id: "))
            salary = float(input("Employee salary: "))
            self.items.append([ename, eid, salary])

    def delete(self):
        eid = int(input("Enter employee id to delete: "))
        for row in self.items:
            if row[1] == eid:   # match ID
                self.items.remove(row)
                print("Record deleted")
                return
        print("Record not found")
    def display(self):
        print("Employee Records:")
        for i in self.items:
            print(i)
s = employee()
s.insert()
s.display()
s.delete()
s.display('')
print("hello world")