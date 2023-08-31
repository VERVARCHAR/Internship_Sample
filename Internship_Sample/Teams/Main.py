from Admin import Admin_Menu as ad_menu
from Admin import Admin_Check_Reserv as ad_C_R
from Admin import Admin_Manage_User as ad_M_U
from Admin import Admin_Regist_Site as ad_R_S
from User import User_Check_Info as us_C_I
from User import User_Check_Reserv as us_C_R
from User import User_Main as us_M
from User import User_Reserv_Site as us_R_S
from Login import Login_Main as lg



def check_input_format(max,command):
    if type(command) != 'int':
        return False
    else:
        if command > max:
            return False
        elif command != 9:
            return False
        else:
            return True
    

def Admin_Menu_Manage():
    m = ad_menu.Admin_Menu()
    if m == 1:
        ad_M_U.Admin_Manage_User()
    elif m == 2:
        ad_C_R.Admin_Check_Reserv()
    elif m == 3:
        ad_R_S.Admin_Regist_Site()
    elif m == 9:
        print("Exit")
    else:
        print("Re Try pls")
        Admin_Menu_Manage()
            
def Login_Manage():
    i = lg.Login()
    if(i == 0):
        Admin_Menu_Manage()
    else:
        print("USer")
    print(i)
    
Login_Manage()