import subprocess,random,optparse

# Function to take command line arguments & parse them
def get_args():
    parser=optparse.OptionParser()
    parser.add_option("--interface",dest="interface",help="Interface whoose mac address is to be changed")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Enter the interface whoose mac address has to changed. For more info use --help")
    else:
        return options.interface

# Function to generate random segments for the new mac address
def random_seg(flag):
    num=random.randint(10,99)
    if(flag and num%2!=0):
        return random_seg(True)
    if(flag==False or (flag and num%2==0)):
        sub=str(num)
        return sub

# Function to change the mac address
def changing_mac(interface):
    subprocess.run(["sudo","ifconfig",interface,"down"])
    new_mac=""
    for i in range(6):
        if(i==0):
            sub=random_seg(True)
        else:
            sub=random_seg(False)
        if (i==5):
            new_mac=new_mac+sub
        else:            
            new_mac=new_mac+sub+":"
    err=subprocess.run(["sudo","ifconfig",interface,"hw","ether",new_mac])
    subprocess.run(["sudo","ifconfig",interface,"up"])
    
    if(err.returncode==0):
        print("Mac_Adress of "+interface+" is sucessfully changed to "+new_mac)
    else:
        print("Task failed. Exiting")


# Calling the func to take the command line arguments
interface=get_args()

# Calling the func to change the mac address
changing_mac(interface)