import base64 
import paramiko 
#host = 'x.x.x.x'
host = '' #hostanme or ip
username = 'username' 
passwd = 'password' 
#key = paramiko.RSAKey(data=base64.b64decode(b'AAA...')) 
for i in range(1,2):     
    host = host
    try:         
        client = paramiko.SSHClient()         
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())         
        client.load_system_host_keys()         
        client.connect(host, username= username, password= passwd)         
        #USE TO TEST ON SMARTS-BENCH2
        #stdin, stdout, stderr = client.exec_command('iperf3 -c x.x.x.x -p 5201 & rsh x.x.x.x iperf3 -c x.x.x.x -p 5202')
        #USE TO TEST ON STORAGE-BENCH2
        pak = "fuseutils"
        #cmd = "zypper in -y "+pak
        cmd = "w"
        stdin, stdout, stderr = client.exec_command(cmd)
        #print(stdout)         
        for line in stdout:             
            #print('... ' + line.strip('\n'))
            print(line.strip('\n'))         
        client.close()     
    except Exception as e:         
        print(e)