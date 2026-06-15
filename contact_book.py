# ===== CONTACT BOOK =====

# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit

# Enter choice: 1

# Enter Name: Aman
# Enter Phone: 9876543210
# Enter Email: aman@gmail.com

# Contact Added!

class contact_book:
    def __init__(self):
        self.person={}
        
    def  Add_Contact(self,name,phone,email):
        self.person[name]={
            "Number_phone": phone,
            "Email_ID": email}

    def View_Contacts(self):
        if len(self.person)==0:
            print("no contact")
        else:
            print(self.person)
  
    def Search_Contact(self, name):
        if len(self.person)==0:
            print("no contact")
        else:   
               contact=self.person.get(name)
               if contact:
                   print(self.person.get(name).get( "Number_phone"))
                   print(self.person.get(name).get("Email_ID"))
               else:
                   print("contact name is invalid")
        
    
    def Update_Contact(self,name,key,value):
        if len(self.person)==0:
            print("no contact")
        else:   
               contact=self.person.get(name)
               if contact:
                   contact[key]=value
               else:
                   print("contact name is invalid")
         
    def Delete_Contact(self,name,key):
        if len(self.person)==0:
            print("no contact")
        else:   
               contact=self.person.get(name)
               if contact:
                   if key in contact:
                      del contact[key]
                      print(f"key: {key} is delete")
               else:
                   print("contact name is invalid")
contact=contact_book()
while True:
   print("\n1. Add Contact")
   print("2. View Contacts")
   print("3. Search Contact")
   print("4. Update Contact")
   print("5. Delete Contact")
   print("6. Exit")
   ch=int(input("enter the choose number: "))
   print("\n")
    

   if ch==1:
       name=input("enter the name: ")
       phone=input("enter phone no: ")
       email=input("enter email: ")
       contact.Add_Contact(name,phone,email)
   elif ch==2:
       contact.View_Contacts()
   elif ch==3:
       contact.Search_Contact(input("enter name: "))

   elif ch==4:
       name=input("enter the name: ")
       key=input("enter key name: ")
       value=input("enter the value be change : ")
       contact.Update_Contact(name,key,value)
   elif ch==5:
      name=input("enter the name: ")
      key=input("enter key name: ")
      contact.Delete_Contact(name,key)
   elif ch==6:
       break
   else:
       print("invalid choice")
                 