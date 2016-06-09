import os, sys, time, docopt
'''
Application to make multiple django apps, it creates apps with the file arguments that you provide
and the respective folders are created in the app root folder that you can specify with -fn option.

If you choose to create just the folders then you can use the -s options
If you choose to create folders and apps but do not need the addapplist.txt then use option -ia

Usage:

  DjangoMakeApp.py -a FILE... [Options]


Options:
  -a FILE               Apps list follows this options
  --apps FILE           Apps list follows this options
  -h, -? --help         Show this help message and exit
  -v, --version         Show version and exit
  -s, --skip            Skips the django manage.py startapp
  -fn, --foldername     Application Folder name
  -ia                   skip creating install apps file
'''

def mapsHelp():
	clearscrn()
	ht = '''Python maps.py is a Django appfolder and app creator
	Usage:
	Python maps.py /a "home,about,services,blog,contact" [/s] [/fn] AppRootFolder
	/a : list of apps to be created will create in default 'apps' folder
	/s : skip django app creation and create only folders
	/fn: creates approotfolder default approotfolder is 'apps'
	/h or /? or /help: this help file

	______________________________________________________________
	'''
	print(ht)

def clearscrn():
	if sys.platform == 'win32': os.system("cls")
	else: os.system("clear")

def createAppFolders(folders, appFolder):
	''' function to create app folders /a argument
	'''
	folist=[]
	folist = folders.split(',')

	try:
		for fn in folist:
			time.sleep(0.5)
			folderName='.\\{}\\{}'.format(appFolder,fn)
			if not os.path.exists(folderName):
				os.makedirs(folderName)
				os.system("Python manage.py startapp {} {}".format(fn, folderName))
				with open("addapplist.txt", "a+") as text_file:
					text_file.write("'{}.{}',\n".format(appFolder,fn))



	except:
		print('this was not finished please check your rights on this machine.')	

def createAppRoot(folder):
	''' function to create app root /fn argument
	'''	
	try:
		if not os.path.exists(folder):
			os.makedirs(folder)
			return True
		else:
			return False

	except:
		print('this was not finished please check your rights on this machine.')
		return True


total = len(sys.argv)
arguments = sys.argv
clearscrn()
print ('Application will be created')
time.sleep(1.5)
with open("addlist.txt", "w+") as text_file: text_file.write("")
if total == 3:
	if createAppRoot(arguments[1]): createAppFolders(arguments[2],arguments[1])

helptxt = '''
Thanks for using maps.py
------------------------
Usage:
python .\maps.py <application root> "<app_folder1>,<app_folder2>,..."
python .\maps.py apps "home,about,services,projects,contact"

Please do not forget to copy the contents of addlist.txt to your setting.py
Put the contents under installed apps

Happy Djangoing....
'''
print("{}".format(helptxt))
time.sleep(0.25)
