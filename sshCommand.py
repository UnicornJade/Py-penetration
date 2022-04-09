import pexpect

PROMPT=['# ','>>> ','> ','\$ ']
def send_command(child,cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def connect(user,host,password):
    ssh_newKey='Are you sure you want to connecting'
    connStr='ssh '+user+'@'+host
    child=pexpect.spawn(connStr)
    #三种可能会出现的输出
    ret=child.expect([pexpect.TIMEOUT,ssh_newKey,'[p|P]assword:'])
    if ret==0:
        print('[-] Error Connecting')
        return
    if ret==1:
        child.sendline('yes')
        ret=child.expect([pexpect.TIMEOUT,'[p|P]assword:'])
    if ret==0:
        print('[-] Error Connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child
def main():
    host='192.168.183.129'
    user='ying'
    password='ying'
    child=connect(user,host,password)
    send_command(child,'ifconfig')

if __name__ == '__main__':
    main()