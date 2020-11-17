import os
import sys
while True:
	os.system("clear")
	os.system("tput setaf 4")
	print("""
  
  #            #              #     #           #
  #             #            #      # #       # #
  #              #          #       #  #     #  #
  #               #        #        #   #   #   #
  #                #      #         #    # #    #
  #                 #    #          #     #     #
  #                  #  #           #           #
  #########           ##            #           #



""")
	os.system("tput setaf 6")
	y=input('Press (1): To run a program \npress (2): To exit \n##########################################################\n')
	
	if (int(y)==1):
		w=0
		while w == 0:
			os.system("tput setaf 2")
			os.system("clear")
			print('#############################-LVM Partitions-############################')
			print("""
press(0):  To display  all available disk
press(1):  To create physical volume (pv)
press(2):  To display all physical volume(pv)
press(3):  To display perticular physical volume(pv)
press(4):  To create volume group (vg) 
press(5):  To display all volume group(vg)
press(6):  To display perticular volume group(vg)
press(7):  To create logical volume (lv)
press(8):  To display all logical volume(lv)
press(9):  To display perticular volume (lv)
press(10): To format logical volume(lv)
press(11): To mount logical volume(lv) to folder
press(12): To extend the size of logical volume (lv)
press(13): To format extended size of logical volume(lv)
press(14): To extend volume group (vg)
press(15): To display all the disk partition 
press(16): To remove logical volume(lv)
press(17): To remove volume group(vg)
press(18): To remove physical volume(pv)
press(19): To umount logical volume(lv)
""")
			os.system("tput setaf 7")
			print('#########################################################################')
			c=int(input('Enter the choice : '))
			if (c == 0):
				os.system("fdisk -l")
			elif (c == 1):
				r=0
				while r == 0:
					dn=input('enter the disk name :')
					os.system("pvcreate {}".format(dn))
					r=int(input('press 0 to create more physical volume(pv) or press (1) for other services  :'))
			elif (c == 2):
				os.system("pvdisplay")
			elif (c == 3):
				dn=input('enter the  PV name to display :')
				os.system("pvdisplay {}".format(dn))
			elif (c == 4):
				rm=input('enter vg name : ') 
				dn=input('enter the (pv) names to create (volume group) : ')
				os.system("vgcreate {} {}".format(rm,dn))
			elif (c == 5):
				os.system("vgdisplay ")
			elif (c == 6):
				dn=input('enter the  VG name to display :')
				os.system("vgdisplay {}".format(dn))
			elif (c == 7):
				s=input('enter the size :')
				ln=input('give the name to LV :')
				dn=input('enter the VG name :')
				os.system("lvcreate --size {}G --name {} {}".format(s,ln,dn))
			elif (c == 8):
				os.system("lvdisplay")
			elif (c == 9):
				dn=input('enter the  VG name :')
				ln=input('enter the LV name :')
				os.system("lvdisplay {}/{}".format(dn,ln))
			elif (c == 10):
				dn=input('enter the LV path :')
				os.system("mkfs.ext4 {}".format(dn))
			elif (c == 11):
				fn=input('enter the dir name to mount :')
				os.system("mkdir /{}".format(fn))
				dn=input('enter LV path to mount :')
				os.system("mount {} /{}".format(dn,fn))
			elif (c == 12):
				dn=input('enter the size to extend :')
				s=input('enter the path of lv :')
				os.system("lvextend --size +{}G {}".format(dn,s))
			elif (c == 13):
				ln=input('enter the path of LV to format \n example /dev/vgname/lvname  :')
				os.system("resize2fs {}".format(ln))
			elif (c == 14):
				dn=input('enter the VG name to extend  :')
				n=input('enter the disk name :')
				os.system("vgextend {} {}".format(dn,n))
			elif (c == 15):
				os.system("lsblk")
		
			elif (c == 16):
				dn=input('enter the  LV name to delete :')
				os.system("lvremove {}".format(dn))
			elif (c == 17):
				dn=input('enter the  VG name to delete :')
				os.system("vgremove {}".format(dn))
			elif (c == 18):
				dn=input('enter the  PV name to delete :')						
				os.system("pvremove {}".format(dn))
			elif (c == 19):
				fn=input('enter the dir name to umount :')
				#os.system("mkdir /{}".format(fn))
				#dn=input('enter LV path to mount :')
				os.system("umount /{}".format(fn))
			else:
				print('chose correct option')
			w=int(input('\n press 0 to continue or 1 for main menu :'))
	elif(int(y) == 2):
		os.system("tput setaf 7")
		os.system("clear")
		sys.exit()
	
	else:
        	print('chose correct option')
