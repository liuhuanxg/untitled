import time
import tkinter
import tkinter.messagebox

def download():
    #模拟下载需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showerror("提示","下载完成！")
    pass

def show_about():
    tkinter.messagebox.showinfo("关于","作者：刘欢(v1.0)")

def main():
    top =  tkinter.Tk()
    top.title("单线程")
    top.geometry("200x150")
    top.wm_attributes("-topmost", True)

    pane1 = tkinter.Frame(top)
    button1 = tkinter.Button(pane1, text="下载", command=download)
    button1.pack(side="left")
    button2 = tkinter.Button(pane1, text="关于", command=show_about)
    button2.pack(side="right")
    pane1.pack(side="bottom")

    tkinter.mainloop()

if __name__ == '__main__':
    main()