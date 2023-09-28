import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def fail(text):
    print(Fore.GREEN + text)
def success(text):
    print(Fore.RED + text)

    
# #!/usr/bin/env python3

# import os
# import argparse
# from stat import ST_SIZE, ST_MODE, S_ISDIR, S_ISREG

# def list_files(path, show_hidden, show_all):
# #     print("""
# # Now wasnt that easy?
# # congrats! you have successfully ran "easy"
# # Please post this on social media or send me an email saying 'hey i figured it out!"
# # ls -hal""")
#     for filename in sorted(os.listdir(path)):
#         # Skip hidden files if the flag is not set
#         if not show_hidden and filename.startswith('.'):
#             continue

#         filepath = os.path.join(path, filename)
#         file_stat = os.stat(filepath)
        
#         # Determine if it's a directory or a file
#         if S_ISDIR(file_stat[ST_MODE]):
#             filetype = 'd'
#         elif S_ISREG(file_stat[ST_MODE]):
#             filetype = '-'
#         else:
#             filetype = '?'

#         # Format size
#         size = file_stat[ST_SIZE]

#         if show_all:
#             print(f"{filetype} {size:10} {filename}")
#         else:
            
#             print(filename)
# current_state = 0

# def game(required):
#     if required:
#         print("sorry required is false")
#     else:
#         print("sorry you forgot a flag, please add the '--required flag'")
# def main():
#     parser = argparse.ArgumentParser(description='List files and directories.')
#     parser.add_argument('-a', '--all', action='store_true', help='Show all entries.')
#     parser.add_argument('-H', '--hidden', action='store_true', help='Show hidden files.')
#     parser.add_argument('path', nargs='?', default='.', help='Directory path.')
#     parser.add_argument('-r', nargs='--required', default='False', help='not optional.')
    
#     args = parser.parse_args()
    
#     # list_files(args.path, args.hidden, args.all)
#     game(args.required)

# if __name__ == '__main__':
#     main()
#!/usr/bin/env python3
#--------------------------------------
# 
#!/usr/bin/env python3

import os
import argparse
from stat import ST_SIZE, ST_MODE, S_ISDIR, S_ISREG
from pyfiglet import Figlet
import string
import random
from time import sleep 
global state

def generate_random_string(size):
  chars = string.ascii_uppercase.replace("O","").replace("G","") + string.digits.replace("0","").replace("6","")
  random_string = ''.join(random.choice(chars).upper() for i in range(size))
  return random_string

def list_files(path, show_hidden, show_all):
    
    print("TODO")

def actually_list(path):
    for filename in sorted(os.listdir(path)):
        

        filepath = os.path.join(path, filename)
        file_stat = os.stat(filepath)
        
        if S_ISDIR(file_stat[ST_MODE]):
            filetype = 'd'
        elif S_ISREG(file_stat[ST_MODE]):
            filetype = '-'
        else:
            filetype = '?'

        size = file_stat[ST_SIZE]

        print(filename)

def captcha(question,answer):
    f = Figlet(font='doom')
    
    captcha_text =  generate_random_string(5)
    # print(captcha_text)
    print(f.renderText(captcha_text))
    answer = input(question)
    
    if captcha_text == answer:
        success("correct")
        return True
    fail("Error Incorrect Captcha")
    state = 'CAPTCHA'

    return False

def state_machine(args):
    state = 'INIT'
    # state = 'CAPTCHA'
    # state = "CHOOSE"
    state = "WIN"

    while True:
        sleep(5)
        if state == 'INIT':
            if args.required == "true":
                success("Success!")
                state = 'API_KEY_SET'
            else:
                fail("ERROR: go ask for 'help' and Read the manual")
                break    
        if state == 'API_KEY_SET':
            if args.API_KEY == "bruh":
                state = "CAPTCHA"
                
            else:
                print("""
check_ld cc
check_cc
BEGIN /tmp/ffconf.xECiIX7z.c
    1   int main(void){ return 0; }
END /tmp/ffconf.xECiIX7z.c
gcc -c -o /tmp/ffconf.xsCaoMWN.o /tmp/ffconf.xECiIX7z.c
gcc -o /tmp/ffconf.ApzYq7NQ /tmp/ffconf.xsCaoMWN.o
/usr/lib/gcc/x86_64-linux-gnu/4.6.1/../../../x86_64-linux-gnu/crt1.o: In function `_start':
(.text+0x12): set API_KEY to bruh. undefined reference to `__libc_csu_fini'
/usr/lib/gcc/x86_64-linux-gnu/4.6.1/../../../x86_64-linux-gnu/crt1.o: In function `_start':
(.text+0x19): undefined reference to `__libc_csu_init'
collect2: ld returned 1 exit status
""")
                fail("Python compiler test failed.")
                
                
                break
        elif state == "CAPTCHA":
            if not captcha("Are you NOT a robot? Please enaser this captcha\n>",args.captcha):
                break
            if not captcha("Are you SURE your NOT a robot? Please enaser this captcha\n>",args.captcha):
                break
            if not captcha("Are you REALLY SURE your NOT a robot? Please enaser this captcha\n>",args.captcha):
                break
            state = "CHOOSE"
        elif state == "CHOOSE":
            choice = input("Would you like to Continue? Y/N\n> ")
            if choice == "Y" or choice == "y" or choice == "yes" or choice == "yes".upper()  :
                fail("ERROR: incorrect answer, please answer NO")
                state == "CAPTCHA"
                if not captcha("Please enaser this captcha\n>",args.captcha):
                    break
            elif choice == "N" or choice == "n" or choice == "no" or choice == "NO":
                fail("ERROR: incorrect answer, please answer YES")
                state == "CAPTCHA"
                
            else:
                state = "WIN"
        elif state == 'WIN':
            f = Figlet(font='doom')
            fail(f.renderText("WIN"))
            fail("""
🥳🎊🎉🪅congrats!🥳🎊🎉🪅
Now wasnt that easy?
 you have successfully ran "easy"
Please post this on social media or send me an email saying 'hey i figured it out!'
------------------------------
>ls -l
""")
            actually_list(args.path)
            break
        else:
            print("something went wrong")
            break

def main():
    args = None
    parser = argparse.ArgumentParser(description='List files and directories.', usage='READ THE MANUAL')
    # parser.add_argument('-a', '--all', action='store_true', help='Show all entries.')
    # parser.add_argument('-H', '--hidden', action='store_true', help='Show hidden files.')
    parser.add_argument('--required', type=str, default=None, help='Required flag must be "true"')
    parser.add_argument('--API_KEY', type=str, default="nope", help='API Key.')
    parser.add_argument('--captcha', action='store_true', default="nope", help='captcha.')
    parser.add_argument('path', nargs='?', default='.', help='Directory path.') 
    
    # try:
    args = parser.parse_args()
    # except argparse.ArgumentError:
    #     print('Error: Required flag must be True')
    #     exit()
    # print(list(vars(args).values())[:-2])
    # print(args.required)
    if args.required == None:
        fail("Sorry, you forgot a flag. Please add the '--required' flag.")
        exit()
    state_machine(args)

if __name__ == '__main__':
    main()
