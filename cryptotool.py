#Python 3.7 
try:
  import hashlib
  import sys
except ImportError as err: 
    raise (f'Couldnt Load Module {err}')
def sha256():
    inp = input("Enter a passphrase to crypt   ").encode('utf-8')
    m = hashlib.sha256()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def md5():
    inp = input("Enter a passphrase to crypt   ").encode('utf-8')
    m = hashlib.md5()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def sha1():
    inp = input("Enter a passphrase to crypt  ").encode('utf-8')
    m = hashlib.sha1()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def blake2b():
    inp = input("Enter a passphrase to crypt  ").encode('utf-8')
    m =  hashlib.blake2b()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def blake2s():
    inp = input("Enter a passphrase to crypt  ").encode('utf-8')
    m =  hashlib.blake2s()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def sha224():
    inp = input("Enter a passphrase to crypt  ").encode('utf-8')
    m =  hashlib.sha224()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def sha384():
    inp = input("Enter a passphrase to crypt  ").encode('utf-8')
    m =  hashlib.sha384()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def sha512():
    inp = input("Enter a passphrase to crypt   ").encode('utf-8')
    m =  hashlib.sha512()
    m.update(inp)
    a = m.hexdigest()
    print(a)
def banner():
    print(""" 
  

        _________                        __             .___ 
        \_   ___ \_______   ____ _____ _/  |_  ____   __| _/ 
        /    \  \/\_  __ \_/ __ \\__  \\   __\/ __ \ / __ |  
        \     \____|  | \/\  ___/ / __ \|  | \  ___// /_/ |  
        \______  /|__|    \___  >____  /__|  \___  >____ |  
                \/             \/     \/          \/     \/  
        ___.         
        \_ |__ ___.__.
        | __ <   |  |
        | \_\ \___  |
        |___  / ____|
            \/\/     
                    .__          __    
        _____ _____  |  |   ____ |  | __
      /     \\__  \ |  | _/ __ \|  |/ /
      |  Y Y  \/ __ \|  |_\  ___/|    < 
      |__|_|  (____  /____/\___  >__|_ \
            \/     \/          \/     \/    
      """)
def banner2():
    print(""" 
 _     _                    
| |   | |                              
| |__ | |  ____  ____   ____   _   _   
|  __)| | / _  ||  _ \ |  _ \ | | | |  
| |   | |( ( | || | | || | | || |_| |  
|_|   |_| \_||_|| ||_/ | ||_/  \__  |  
                |_|    |_|    (____/     
 _______                                           _               
(_______)                                    _    (_)              
 _____    ____    ____   ____  _   _  ____  | |_   _   ___   ____  
|  ___)  |  _ \  / ___) / ___)| | | ||  _ \ |  _) | | / _ \ |  _ \ 
| |_____ | | | |( (___ | |    | |_| || | | || |__ | || |_| || | | |
|_______)|_| |_| \____)|_|     \__  || ||_/  \___)|_| \___/ |_| |_|
                              (____/ |_|                           
                                __   
                              (_ \  
                            _   \ \ 
                            (_)   ) )
                            _  _/ / 
                            (_)(__/                 
                                                """)
def second_page():
    print("""

    9/Enecryption Alrgoithms Available In This Tool
    10/Quit The program
    99/Return to Previous Page
    
    
    """)
    user_input =  input("y/n ")
    if user_input == '9':
        print(""" >>> Current Encryption Algorithms Available In This Tool 
'sha256' , 'sha1' , 'sha224' , 'sha384' , 'sha512' , 'md5' , 'blake2b' , :'blake2s' <<<
         """)
        second_page()
    elif user_input == '10' or user_input == 'exit' or user_input == 'quit':
        banner2()
        sys.exit()
    elif user_input == '99':
        print("    You Have Been Returned To The Main Menu")
        main()
    else:
        print("    Enter A Valid Choice")
        main()
        banner2()
def main():
    print(""" 
    This is A Cryptography Tool Allow You To Crpyt Your Passphrase With Your Chosen Encryption Algorithm
    Created With Python 3.7 (Should Work Fine With Version 3 In General)
    Not Been Tested In Python 2x
    This Tool Also Needs The Hashlib Library In Python
    Visit https://docs.python.org/3/library/hashlib.html For More Informations About The Library That Been Used In This Program
    
    1/SHA_256 (Secured Hash Algorithm 256 )
    2/SHA_1 (Secured Hash Alrgorithm 1)
    3/SHA_224 (Secured Hash Algoritmth 224)
    4/SHA_384 (Secured Hash Algorithms 384) 
    5/SHA_512 (Secured Hash Algorimths 512)
    6/MD5(Message Digest 5)
    7/Blake2b
    8/Blake2s
    33/Next Page
    
    """)
    choice = input("Enter Your Choice ")
    if choice == '1':
        sha256()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y' or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '2':
        sha1()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '3':
        sha224()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '4':
        sha384()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '5':
        sha512()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '6':
        md5()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '7':
        blake2b()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '8': 
        blake2s()
        print("Do You Want To Rerun It Again ")
        i = input("y/n ")
        if i == 'y'or i == 'Y':
          main()
        else:
          banner2()
          sys.exit()
    elif choice == '33':
        second_page()

    elif choice == '10' or choice == 'exit' or choice == 'quit':
        banner2()
        sys.exit()
    else: 
		# print('Please Enter A Valid Choice')
        main()
banner()
main()