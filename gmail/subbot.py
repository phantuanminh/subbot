import time
from webbot import Browser
import pyautogui # its use for keyboard inputs.
import win32console,win32gui

class SubBot():
    
    email = []
    password = []
    
    def __init__(self,filename):
        self.filename = filename

    def readFile(self):
        with open(self.filename) as fp:
            for line in fp:
                file_email,file_passwords = line.split()
                self.email.append(file_email)
                self.password.append(file_passwords)
        
    def hide(self):
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window,0)
        
    def main(self):
        for i in range(0,len(self.email)):
            web = Browser()
            self.hide()
            web.go_to('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            web.type(self.email[i] , into='Email')
            web.click('NEXT' , tag='span')
            time.sleep(1)
            web.type(self.password[i], into='Password' , id='passwordFieldId')
            web.click('NEXT' , tag='span') # you are logged in . woohoooo
            time.sleep(15)
            web.go_to('youtube.com/channel/UCjlvnAqts8AyYjHrVmXf_5A')
            time.sleep(2)
            web.click('Subscribe',tag='yt-formatted-string')
            time.sleep(2)
            pyautogui.hotkey('alt','f4')

sb = SubBot("file.txt")
sb.readFile()
sb.main()
