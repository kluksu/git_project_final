
import re
from termcolor import colored
import sys
password=""
if(len(sys.argv)>1 and sys.argv[1]!="-f" ):
    password=sys.argv[1]
elif len(sys.argv)>2 and sys.argv[1]=="-f":
    password_file = open( sys.argv[2],"r")
    password=password_file.read()
regex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[\w~@#$%^&,*+/=`|{}:;!.?\"()\[\]-]{10,}$"
# regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{10,}$"
speciel="^(?=.*[!@#$%^&*])"
capital="^(?=.*[A-Z])"
lowerCase="^(?=.*[a-z])"
number="^(?=.*\d)"
def is_valid(password:str):
    """
    receives a string and prints information and exit code about password validation
    :param password:
    :return:
    """
    if re.search(regex,password):
        print(colored("password is valid", 'green'))
        exit(0)

    else:
        print(colored("password is invalid", 'red'))
        # if(re.match(speciel,password)):
        #     print(colored('no special characters are allowd', "red"))
        if(len(password)<10):
            print(colored("password must be at least 10 characters long", "red"))
        if not (re.match(capital, password)):
            print(colored('your password must include one capital letter at least', "red"))
        if not (re.match(lowerCase, password)):
            print(colored('your password must include one lower Case letter at least', "red"))
        if not (re.match(number, password)):
            print(colored('your password must include one digit at least', "red"))

        exit(1)




is_valid(password)
