import base64
import random as rage
#Register:
class Rsgister:
    def Encode(self, password):
        password_bytes = password.encode('utf-8')  # Convert string to bytes
        encoded_bytes = base64.b64encode(password_bytes)  # Encode bytes in base64
        encoded_str = encoded_bytes.decode('utf-8')  # Convert base64 bytes to string
        return encoded_str

    def Decode(self, encoded_str):
        encoded_bytes = encoded_str.encode('utf-8')  # Convert base64 string to bytes
        decoded_bytes = base64.b64decode(encoded_bytes)  # Decode base64 bytes
        decoded_str = decoded_bytes.decode('utf-8')  # Convert bytes back to string
        return decoded_str
    
    
#login
class login(Rsgister):
    def log(self,Pass_for_login):
      ex = Rsgister()
      encode_byte = ex.Encode(Pass_for_login)
      return encode_byte

def Reg_user_cred():
    while True:
        User_name_for_Registers = input("Enter The User Name For Register : ")
        Pass_for_registers = input("Enter The Password For Register : ")
        if User_name_for_Registers and Pass_for_registers:
            return User_name_for_Registers,Pass_for_registers
        else:
            print("Both Feilds Are Required Please Fill This Fileds")
            
            
def Log_user_cred():
    while True:
        User_name_for_Logs = input("Enter The User Name For Login: ")
        Pass_for_Logs = input("Enter The Password For Login: ")
        if User_name_for_Logs and Pass_for_Logs:
            return User_name_for_Logs,Pass_for_Logs
        else:
            print("Both Feilds Are Required Please Fill This Fileds")

open("reg.txt","a")
open("userpass.txt","w") 
try:
    
    
    with open("reg.txt","r") as reader:
        empty = reader.read(1)
    if len(empty)==0:
        User_name_for_Register,Pass_for_register = Reg_user_cred()
        if User_name_for_Register =='' or Pass_for_register == '':
            print("Fill The User Name or Password  Field is Required")
           
            
        else:
            reg = Rsgister()
            Reg_pass = reg.Encode(Pass_for_register)
            with open("reg.txt","w") as regfile:
                regfile.write(Reg_pass)
                regfile.write(User_name_for_Register)
                regfile.close()
                
                print("------------------Regidtration successfull Please Proceed to The Login -------------------------------------------")
                open("userpass.txt","x")
    else:
        open("userpass.txt","w")  
        User_name_for_login,Pass_for_login = Log_user_cred()
        if User_name_for_login == " " and User_name_for_login == None and Pass_for_login == " " and Pass_for_login == None:
            print("User Name or Password field is required")
        else:  
            log = login()
            log_pass = log.log(Pass_for_login)
            with open("userpass.txt","w") as f:
                f.write(log_pass)
                f.write(User_name_for_login)
                f.close()
except:
    print("")
            


class Checking:
    def regCheck(ref):
        with open("userpass.txt","r")as fd:
            ref =fd.read()
        return ref
    def logCheck(ref2):
        with open("reg.txt") as df:
            ref2 = df.read()
        return ref2
    


reg_ck = Checking()


def Check_Correct():
    if reg_ck.regCheck() == reg_ck.logCheck() :
        print("User Name And PassWord Is Corrrect ")
    else:
        print("User Name or PassWord Is Incorrect")
        
        
if len(empty)!=0:
    Check_Correct() 