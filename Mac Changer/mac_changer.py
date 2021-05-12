import subprocess,random

# Function to generate random segments for the new mac address
def random_seg(flag):
    num=random.randint(10,99)
    if(flag and num%2!=0):
        return random_seg(True)
    if(flag==False or (flag and num%2==0)):
        sub=str(num)
        return sub
    
print("****Here is a list of network interfaces connected to your device ****")
subprocess.run("ifconfig",shell=True)
interface=input("Enter the interface whoose mac adress has to be chnged :")
subprocess.run("sudo ifconfig "+interface+" down",shell=True)

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

subprocess.run("sudo ifconfig "+interface+" hw ether "+new_mac,shell=True)
subprocess.run("sudo ifconfig "+interface+" up",shell=True)
print("Mac_Adress of "+interface+" is sucessfully changed to "+new_mac)
