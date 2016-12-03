import os
import sys,traceback

def main():
	try:
		print("\n\033[1;36mWelcome to Ubuntu Hub Theme installer\033[1;m")
		print("\n\033[1;31m======= Author : Harshil ===========\033[1;m")
		print("\nBefore install themes please update ...\npress ENTER for apt-get update")
		update_flag=input()
		os.system("sudo apt-get update")
		'''print(''\n1) Install Ubuntu Tweak Tool
			     2) Install Ubuntu Themes ')
		main_opn_flag = int(input())
		while (main_opn_flag == 1 ): '''
		theme_flag = 0
		while(theme_flag != 99 ):
			print(''' 
	Please enter your options ? 
	1) Yosembiance
	2) Vivacious Colors Gtk
	3) Ambiance & Radiance Flat Colors Suit
	4) Ambiance & Radiance Colors Theme
	5) Arc Theme (Light & Dark Versions)
	6) Paper
	7) Flatabulous 
	8) Ambiance Crunchy Themes
	9) Papirus Icon
	10) Trevilla
	11) Revival Icon
	12) Masalla Icon
	13) Numix-Circle Icon 
	99) Exit
				''')
			theme_flag=int(input("\n\033[1;31menter>\033[1;m"))
			
			if(theme_flag == 1 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/themes -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install yosembiance-gtk-theme -y")
				print("\n\033[1;36mYosembiance theme installed successfully...\033[1;m")
			elif(theme_flag == 2 ) :
				cmd1 = os.system("sudo add-apt-repository ppa:ravefinity-project/ppa -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install vivacious-colors-gtk-dark -y")
				cmd4 = os.system("sudo apt-get install vivacious-colors-gtk-light -y")
				print("\n\033[1;36mVivacious Colors Gtk theme installed successfully...\033[1;m")
			elif(theme_flag == 3 ):
				cmd1 = os.system("sudo add-apt-repository ppa:ravefinity-project/ppa -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install ambiance-flat-colors -y ")
				cmd4 = os.system("sudo apt-get install radiance-flat-colors -y")
				print("\n\033[1;36mAmbiance & Radiance Flat Colors Suit theme installed successfully...\033[1;m")
			elif(theme_flag == 4 ):
				cmd1 = os.system("sudo add-apt-repository ppa:ravefinity-project/ppa -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install ambiance-colors radiance-colors -y ")
				print("\n\033[1;36mAmbiance & Radiance Colors Theme theme installed successfully...\033[1;m")
			elif(theme_flag == 5 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/themes -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install arc-theme -y ")
				cmd4 = os.system("sudo apt-get install arc-icons")
				print("\n\033[1;36mArc Theme (Light & Dark Versions) installed successfully...\033[1;m")
			elif(theme_flag == 6 ):
				cmd1 = os.system("sudo add-apt-repository ppa:snwh/pulp -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install paper-gtk-theme -y ")
				cmd4 = os.system("sudo apt-get install paper-icon-theme -y ")
				print("\n\033[1;36mPaper theme installed successfully...\033[1;m")
			elif(theme_flag == 7 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/themes -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install flatabulous-theme -y ")
				print("\n\033[1;36mFlatabulous theme installed successfully...\033[1;m")
			elif(theme_flag == 8 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/themes -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install ambiance-crunchy -y ")
				print("\n\033[1;36mAmbiance Crunchy Themes theme installed successfully...\033[1;m")
			elif(theme_flag == 9 ):
				cmd1 = os.system("sudo add-apt-repository ppa:varlesh-l/papirus-pack -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install papirus-gtk-icon-theme -y ")
				print("\n\033[1;36m Papirus Icon theme installed successfully...\033[1;m")
			elif(theme_flag == 10 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/icons -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install trevilla-icons -y ")
				print("\n\033[1;36mTrevilla theme installed successfully...\033[1;m")
			elif(theme_flag == 11 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/icons2 -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install revival-icons -y ")
				print("\n\033[1;36mRevival Icon theme installed successfully...\033[1;m")
			elif(theme_flag == 12 ):
				cmd1 = os.system("sudo add-apt-repository ppa:noobslab/icons -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install masalla-icon-theme -y ")
				print("\n\033[1;36mMasalla Icon theme installed successfully...\033[1;m")
			elif(theme_flag == 13 ):
				cmd1 = os.system("sudo add-apt-repository ppa:numix/ppa -y ")
				cmd2 = os.system("sudo apt-get update -y")
				cmd3 = os.system("sudo apt-get install numix-icon-theme -y ")
				print("\n\033[1;36m Numix-Circle Icon theme installed successfully...\033[1;m")
			else:
				print("\nTerminating ....\
					\nBye ...")
				exit()
				
	except  KeyboardInterrupt:
		print("Bye..")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
	main()

