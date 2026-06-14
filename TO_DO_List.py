#To-Do List
class To_do_list:
    def __init__(self):
        self.task=[]
    def addtask(self,task):
        self.task.append(task)
    def veiw(self):
        if len(self.task)==0:
            print("none task")
        else:
            for i,task in enumerate(self.task,start=1):
                print(f"{i}.{task}")
    def removetask(self ,index):
        if 0 <= index < len(self.task):
          reom = self.task.pop(index)
          print("Removed:", reom)
        else:
          print("Invalid index")
tololist=To_do_list()
while True:
    print("\n1.add")
    print("2.veiw")
    print("3.remove task")
    print("4.exit")
    ch=int(input("enter the choose number: "))
    print("\n")
    
    if ch==1:
        task=input("enter task to add: ")
        tololist.addtask(task)
    elif ch==2:
        tololist.veiw()
    elif ch==3:
        i=int(input("enter index you want to remove: "))
        tololist.removetask(i-1)
        
    elif ch==4:
      break
    else:
        print("invalid ")
    