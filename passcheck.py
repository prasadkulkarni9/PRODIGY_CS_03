import maskpass
from colorama import Fore,Back

art = '''
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝'''

print(Fore.LIGHTYELLOW_EX+art)


def check_pass(password): 
    min_len = 8
    max_len = 20
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in '@#$%^&*()_-+={}[]|\:;"<>,.?/~`' for char in password)


    strong_pass = (
            max_len >= len(password) >= min_len and
            lower and
            upper and
            digit and
            special_char 
    )

    print("Password feedback:")
    if strong_pass:
        print(Back.BLACK+Fore.YELLOW+"Great! Your password is strong.")
    else:
        if not max_len >= len(password) >= min_len:
            print(Back.BLACK+Fore.RED+">> Password must have 8-20 characters.")
        if not lower or not upper:
            print(Back.BLACK+Fore.RED+">> Include both lowercase and uppercase letters.")
        if not digit:
            print(Back.BLACK+Fore.RED+">> Include numbers.")
        if not special_char:
            print(Back.BLACK+Fore.RED+">> Include special characters.")

exitnow = False
while not exitnow:
    print(Fore.GREEN+'***Press ctrl to HIDE/UNHIDE your Password***')
    user_pass = maskpass.advpass(prompt=Back.LIGHTBLACK_EX+Fore.WHITE+"Enter your password: ")
    check_pass(user_pass)

    postprompt = input(Fore.WHITE+"Do you want to check another password? y/n \n").lower()
    if postprompt == "n":
        exitnow = True
        print("App Closed")
