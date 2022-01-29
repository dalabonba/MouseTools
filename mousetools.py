# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:43:11 2022

@author: upup5
"""
import pyautogui
import keyboard
from tkinter import Tk, Label, StringVar, Entry, Button, scrolledtext, Radiobutton, IntVar
# from tkinter.ttk import Combobox



if __name__ == '__main__':
    
    def swich():
        if "未啟動" in statusVal.get():
            statusVal.set("已啟動，按下ctrl+alt+a來停用")
            if radioValue.get()==1:
                pyautogui.mouseDown()
                
                
        else:
            statusVal.set("未啟動，按下ctrl+alt+a來啟動")
            if radioValue.get()==1:
                pyautogui.mouseUp()
            
    keyboard.add_hotkey('ctrl+alt+a', swich)



# #----------------------------window----------------------
window = Tk()
window.geometry('450x340')
window.title("自動滑鼠控制工具")
window.resizable(False, False)




# #-----lable---------
lable_status=Label(window,text="狀態:")
lable_status.grid(row=0,column=0, ipadx=10, pady=10 ,padx=5)#ipad:內部邊界   pad:外邊界

statusVal = StringVar()
statusVal.set("未啟動，按下ctrl+alt+a來啟動")
lable_statusVal=Label(window,textvariable=statusVal)
lable_statusVal.grid(row=0,column=1, ipadx=10, pady=10)

lable_mouseDown=Label(window,text="滑鼠長按:")
lable_mouseDown.grid(row=1,column=0, ipadx=10, pady=10)

# lableMp3=Label(window,text=".mp3")
# lableMp3.grid(row=1,column=2, pady=10)

# lableLang=Label(window,text="語言:")
# lableLang.grid(row=2,column=0, ipadx=10, pady=10)

# lableLang=Label(window,text="存檔位置")
# lableLang.grid(row=3,column=0, ipadx=10, pady=10)
# #-------------------



#---------radioButton----------------
radioValue = IntVar()

radio_mouseDown_left = Radiobutton(window, text='左鍵', variable=radioValue, value=1)
radio_mouseDown_left.grid(row=1,column=1, ipadx=10, pady=10)
radio_mouseDown_left.select()

radio_mouseDown_middle = Radiobutton(window, text='中鍵', variable=radioValue, value=2)
radio_mouseDown_middle.grid(row=1,column=2, ipadx=10)

radio_mouseDown_right = Radiobutton(window, text='右鍵', variable=radioValue, value=3)
radio_mouseDown_right.grid(row=1,column=3, ipadx=10)
#-----------------------------------



# #-----combobox---------
# comboLang = Combobox(window,values=supLangList,state="readonly")
# comboLang.grid(row=2,column=1, ipadx=10, pady=10)
# comboLang.current(len(supLangList)-2)#combobox從0開始算。選擇第{61-2}項

# comboPath = Combobox(window,values=["桌面","執行檔所在位置"],state="readonly")
# comboPath.grid(row=3,column=1, ipadx=10, pady=10)
# comboPath.current(0)
# #-----scrolledtext-----
# scrolledTextMain = scrolledtext.ScrolledText(window ,width=23, height=8)
# scrolledTextMain.grid(row=0, column=1)
# #----------------------






# # tkinter中的文本輸入框說明 https://shengyu7697.github.io/python-tkinter-entry/
# #-------entry-----------
# filenameGetText = StringVar()#建立tk文字變數物件
# entryFilename = Entry(window, textvariable=filenameGetText,width=25)#建立文字輸入框，命名為entryMain，將其中輸入的字指向filenameGetText
# entryFilename.grid(row=1, column=1)
# #------------------------





#------button-----------
# btn3 = Button(window,text = '確認',command = confirm ,width=10)#按下按鈕執行delete副程式:刪除最後一筆資料
# btn3.grid(row=4, column=0, ipadx=10, pady=30)
#-----------------------




window.mainloop()  #循環刷新視窗畫面
#--------------------------------------------------------