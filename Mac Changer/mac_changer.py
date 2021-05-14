'''
** Modules used : 
     subprocess - This module is used to run any linux comand from this python script
     random - This module is used for generating a random mac address
     optparse - This module helps to parse the value of command line arguments that are entered from command line
     hex - This module is used to convert a number to hexadecimal
     re - This module is used for regular expression
'''

import subprocess,random,optparse,re

# Function to take command line arguments & parse them
def get_args():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface whoose mac address is to be changed")
    (options,arguments)=parser.parse_args()    
    if not options.interface:
        parser.error("[-] Enter the interface whoose mac address has to changed. For more info use --help")
    else:
        return options.interface
    

# Displaying Current mac_address
def current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig",interface]) 
    # ifconfig_result is a byte object
    mac_address=re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if mac_address:
        print("[+] Current mac_adress of "+interface+" is "+ mac_address.group(0))
    else:
        print("[-] Could not read the mac address")
    return


# Function to generate random segments for the new mac address
def random_seg(flag):
    num=random.randint(10,99)
    if(flag and num%2!=0):
        return random_seg(True)
    if(flag==False or (flag and num%2==0)):
        sub=str(hex(num).lstrip("0x").rstrip("L"))
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
    
    #err is an object that contains info about the process executed/failed    
    if(err.returncode==0):
        print("[+] Mac_Adress of "+interface+" is successfully changed to "+new_mac)
    else:
        print("[-] Task failed. Exiting")


# Calling the func to take the command line arguments
interface=get_args()

# Displaying the current mac_address
current_mac(interface)

# Calling the func to change the mac address
changing_mac(interface)