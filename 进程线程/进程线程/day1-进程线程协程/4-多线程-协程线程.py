import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showerror("提示", "下载完成")
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数蒋贤成设置为守护线程（主程退出就不在保留执行序）
        DownloadTaskHandler(daemon=True).start()
        pass

    def show_about():
        tkinter.messagebox.showinfo("关于", "作者：刘欢(v1.0)")
        pass

    top = tkinter.Tk()
    top.title("单线程")
    top.geometry("200x150")
    top.wm_attributes("-topmost", 1)

    pane1 = tkinter.Frame(top)
    button1 = tkinter.Button(pane1, text="下载", command=download)
    button1.pack(side="left")
    buttone2 = tkinter.Button(pane1, text="关于", command=show_about)
    buttone2.pack(side="right")
    pane1.pack(side="bottom")

    tkinter.mainloop()


if __name__ == '__main__':
    main()
