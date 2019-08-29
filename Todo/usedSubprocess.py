   
import subprocess
#apt-add-repository universe
cmd = "ifconfig |grep -A 5 'eth1'|grep 'RX packet'|awk '{print $6}'"
#while True:
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#pc = p.stdout.read().decode('utf-8').replace(': ',':').replace('\t','').splitlines()
pc = p.stdout.read().decode('utf-8')
pc = pc.replace('(','')
pc = float(pc)
while True:
    if pc >=160:
        print(" I M Done!!!!")
        sys.exit()

    else:
        print(pc)
#pe = p.stderr.read().decode('utf-8')
