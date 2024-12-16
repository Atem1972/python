import sys  #import argumen that will be provided on the street
import os   # import to run command on our sys
import time  # when you want to put sleep command on my script


#stop, start, restart daemon script
"""args = sys.argv    #1
print(args[2])"""

# how to fine out if the clien did not enter e rightfull 3 argument ie stop start restart
          #index1 is stop index2 start
#2
"""if len(sys.argv) < 2 or  sys.argv[1] not in ('stop','start','restart'):  
    print("please provide a valid choice ('stop','start','restart')")"""
time.sleep(4) 
# we can put the above argv in function format
def validity_check():
    if len(sys.argv) < 2 or  sys.argv[1] not in ('stop','start','restart'):  
        print("please provide a valid choice ('stop','start','restart')")

validity_check() 

#what module do will need to start a daemon in linx? import os

def start_d():
    os.system('systemctl start httpd')

def stop_d():
    os.system('systemctl stop httpd')

def restart_d():
    os.system('systemctl restart httpd')        

if __name__=='_main_':   # all of the below not execute when someone call this function
    validity_check()  
    if sys.argv[1] == 'stop' :    
        stop_d()
    elif sys.argv[1] == 'start' :           #OR
         start_d()
    else:
        restart_d()                        #OR




      #THIS
def main():
    validity_check()
    if sys.argv[1] == 'stop' :
        stop_d()
    elif sys.argv[1] == 'start' :
         start_d()
    else:
        restart_d()     

if __name__=='__main__':
    main()                 