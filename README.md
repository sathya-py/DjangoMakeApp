# DjangoMakeApp
Python script to create folders in the Django root folder and create applications with the same name.

You could create mulitple django apps with the following cmd command please use elevated privledges for your cmd. This script was tested and is used in Windows 10 env with Powershell and cmd with administrator prevlidge.

Prerequiste:
- django must be installed effectively in a virtual env
- manage.py active
- django project must have already been created

Ex: python .\djangomakeapp.py Applications "home,about,service,casestudy,faq,media,books,download,jobs,contact"
------------------------------Appiications app root of the project
------------------------------"home,about,service,casestudy,faq,media,books,download,jobs,contact" are the apps that will be created

Output: 
Folder (AppRootFolder):
- Application 

Apps in the folder:
- Applications\home
- Applications\about
- Applications\service
- Applications\casestudy
- Applications\faq
- Applications\media
- Applications\books
- Applications\download
- Applications\jobs
- Applications\contact

Runs the following command after the folder creations
python manage.py startapp home Application\home

djangomakeapp also creates a addlist.txt in the same folder which you can add to settings.py under Installed_Apps

I will improve this further as and when i find time. I am exchanging thoughts with Valdimir (docopt) for a robust script.
