from Test_Cases.test_data import *
from Page_object_model.locaters import *
# from Test_Cases.data import *

login = Test_LoginPage()

# login.login_page('admin@yourstore.com','admin')
# print(login)
login.Test_CustomersPage("admin@yourstore.com",'admin',role="Guests",gender="male",Email_id="korrapatichaitanyakumar@gmail.com",Password1="Amma**17",firstname="Chaitanya",lastname="korrapati",date="7/2/1996",
    Companyname= "Capgemini",value="Vendor1",description="this is chaitanya kumar")









# role="Guests",gender="male",Email_id="korrapatichaitanyakumar@gmail.com",Password1="Amma**17",firstname="Chaitanya",lastname="korrapati",date="7/2/1996",
#     Companyname= "Capgemini",value="Vendor1",description="this is chaitanya kumar"