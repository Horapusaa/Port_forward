#/user/bin/env/pythoon

import subprocess

user_name=input("Enter Your VPS Username : ")
ip_address=input("Enter Your VPS IP : ")
my_port=input("Enter Your Matchine Port want to public : ")
vps_port=input("Enter Your Vps Port want to public : ")

print("Connecting to ",ip_address)

subprocess.run("ssh -R "+vps_port+":127.0.0.1:"+my_port+" "+user_name+"@"+ip_address ,shell=True)


exit()