import os,sys
#import shlex
import subprocess
from tkinter import *

ui=Tk()
ui.resizable(width=False, height=False)
ui.geometry("750x450+200+100")
ui.title("Gui-n2n")

#cmdline = ".\edge -c work -a 192.168.88.10 -k justdoit -l xfox.fun:8080"
# 第二个标签框架 <文本框 x1>
lableFrame2 = LabelFrame(ui, text='Service Log')
logtext = Text(lableFrame2, height=32, width=65)
logtext.pack()
lableFrame2.grid(column=1, row=1, sticky=N + S, padx=8, rowspan=3)
# 第一个标签框架 < 输入框x3  >
## 超级节点地址
lableFrame1 = LabelFrame(ui, text='Config')
Label0=Label(lableFrame1,justify=LEFT,text="SuperNode Addr:")
Label0.grid(column=0,row=1)
Input0 = Entry(lableFrame1, width=18)
Input0.grid(column=1, row=1,padx=3,pady=2)
## 社区名称
Label1 = Label(lableFrame1, justify=LEFT, text="Community Name:")
Label1.grid(column=0, row=2)
Input1 = Entry(lableFrame1, width=18)
Input1.grid(column=1, row=2, padx=3, pady=2)
## 加密密钥
Label2 = Label(lableFrame1, justify=LEFT, text="Encryption Key:")
Label2.grid(column=0, row=3)
Input2 = Entry(lableFrame1, width=18)
Input2.grid(column=1, row=3, padx=3, pady=2)
## 自订地址
Label3 = Label(lableFrame1, justify=LEFT, text="Custom IP Addr:")
Label3.grid(column=0, row=4)
Input3 = Entry(lableFrame1, width=18)
Input3.grid(column=1, row=4, padx=3, pady=2)
lableFrame1.grid(column=2, row=1, sticky=N, padx=10)
## 使用说明
HelpText = Label(ui, justify=CENTER, text="使用说明：\nhttps://xfox.fun/archives/1330")
HelpText.grid(column=2,row=3)



#控制区 Start
LableFrame3=LabelFrame(ui,text="Control")

##获取各项参数
SuperNodeAddr=Input0.get()
CommunityName=Input1.get()
EncryptionKey=Input2.get()
CustomIPAddr=Input3.get()
Parameter=" -c "+CommunityName+" -a "+CustomIPAddr+" -k "+EncryptionKey+" -l "+SuperNodeAddr
#cmdline="edge -c game -a 192.168.99.10 -k justdoit -l xfox.fun:8080"
Path=os.path.dirname(os.path.realpath(__file__))


def WindowsRun():
    CorePath=Path+"\edge.exe"
    cmdline=CorePath+Parameter
    core = subprocess.Popen([cmdline],
                            shell=True,
                            stdout=subprocess.PIPE,
                            encoding="utf-8")
    while True:
        line = core.stdout.readline()
        if ((line is None) and core.poll() !=None):
            logtext.insert(END,line)
            break
def LinuxRun():
    cmdline = "sudo edge " + Parameter
    core = subprocess.Popen([cmdline],
                            shell=True,
                            stdout=subprocess.PIPE,
                            encoding="utf-8")
    while True:
        line = core.stdout.readline()
        if ((line is None) and core.poll() != None):
            logtext.insert(END, line)
            break
def CoreRun():
    if sys.platform.startswith('linux'):
        LinuxRun()
        Status = True
        pass
    elif sys.platform.startswith('drawin'):

        pass
    elif sys.platform.startswith('win32') or sys.platform.startwith('cygwin'):
        WindowsRun()
        Status=True
        pass



## 启停按钮
StartButton=Button(LableFrame3,text="Start n2n",command=CoreRun())
StartButton.grid(column=1,row=1)
LableFrame3.grid(column=2, row=2, sticky=N+S+W+E)
#控制区 END

ui.mainloop()
