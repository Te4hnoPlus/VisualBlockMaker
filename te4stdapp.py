import json, os, shutil
from tkinter import ttk, Tk, filedialog, Toplevel, Wm, PhotoImage, BooleanVar
import tkinter.messagebox as msgbox
from te4lib import *


class baseApp:
    def __init__(self, root: Wm, name="Std Te4hno Python APP", size=None) -> None:
        self.root = root
        self.config = None
        if size != None: self.root.geometry=size
        self.title = name
        self.root.title(name)
        self.frm = ttk.Frame(self.root, padding=20)
        self.frm.grid()
        self.cursor = 0
        self.__components__ = {}
        self.__components__["__onclose__"] = []
        self.__components__["__onstart__"] = []

        def onClose():
            cansel = None
            for func in self.__components__["__onclose__"]: func(self)
            if not (cansel == True): self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", onClose)

        self.addVarComp(var="title", funcGet=lambda:self.title, funcSet=self.setTitle)
        def setSize(val):self.root.size = val
        self.addVarComp(var="size", funcGet=lambda:self.root.size, funcSet=setSize)


    def ico(self, path="icon.png"):
        try:
            self.root.call("wm", "iconphoto", self.root._w, PhotoImage(file=path))
        except:
            print(f"Can't set icon [{path}]")
        return self


    def setTitle(self, title):
        self.title = title
        self.root.title(title)
            

    def text(self, text="Text", var:str=None, pos=None, padding=10):
        label = ttk.Label(self.frm, text=text, padding=padding)
        self.__onAddLabel__(label=label, var=var, pos=pos)
        return self
    

    def checkBtn(self, var, text=None, func=lambda app:None, pos=None, padding=10):
        if(text == None): text = var
        bVar = BooleanVar()
        def command(**kwargs):
           self.config[var] = bVar.get()
           func(self)

        label = ttk.Checkbutton(self.frm, text=text, padding=padding, command=command, variable=bVar)
        self.__onAddLabel__(label=label, pos=pos)

        self.addVarComp(var=var, 
            funcSet=lambda v:bVar.set(v), 
            funcGet=lambda  :bVar.get()
        )
        return self
    

    def onStart(self, task=lambda:None):
        self.__components__["__onstart__"].append(task)
        return self


    def onClose(self, task=lambda:None):
        self.__components__["__onclose__"].append(task)
        return self


    def __onAddLabel__(self, label, var=None, pos=None):
        column = 0
        row = self.cursor
        next = True
        if pos != None:
            column = pos["c"] if "c" in pos else 0
            row = pos["r"] if "r" in pos else self.cursor
            next = row == self.cursor
        label.grid(column=column, row=row)
        if next: self.cursor+=1
        if var == None: return
        self.addVarComp(var=var, 
            funcSet=lambda v:label.config(text=v), 
            funcGet=lambda  :label.cget("text")
        )
    

    def addVarComp(self, var:str, funcGet, funcSet):
        self.__components__[var]=(funcGet, funcSet)


    def buttom(self, func=lambda app:None, name="Buttom", var=None, style=None, pos=None, padding=10):
        label = ttk.Button(self.frm, text=name, command=lambda:func(self), padding=padding, style=style)
        self.__onAddLabel__(label=label, var=var, pos=pos)
        return self
    

    def nw(self):
        return self.text("")
    

    def input(self, var:str, default=None, focusTask=lambda app:None, unfocusTask=lambda app:None, width=30, height=1, pos=None):
        label, funcSet, funcGet = None, None, None
        if height > 1:
            from tkinter.scrolledtext import ScrolledText
            label = ScrolledText(self.frm, width=width, height=height, font = ("Times New Roman",11))
            self.__onAddLabel__(label=label, var=None, pos=pos)

            def funcSet(val):
                label.delete("1.0", 'end-1c')
                if val == None:return
                label.insert("1.0", val)
                
            funcGet = lambda: label.get("1.0", 'end-1c')
        else:
            label = ttk.Entry(self.frm, width=width, font = ("Times New Roman",11))

            def funcSet(val):
                label.delete(0, 'end')
                if val == None: return
                label.insert(0, val)

            funcGet = label.get

        self.__onAddLabel__(label, pos=pos)

        if type(default) == tuple:
            self.onStart(lambda a:funcSet(self[(default[0], default[0])]))
        else: 
            funcSet(default)

        def unfocus(event):
            self.config[var] = funcGet()
            unfocusTask(self)

        def focus(event):
            focusTask(self)

        label.bind("<FocusOut>", unfocus)
        label.bind("<FocusIn>", focus)

        self.addVarComp(var=var, funcGet=funcGet, funcSet=funcSet)
        return self
    

    def start(self):
        for task in self.__components__["__onstart__"]: task(self)
        del self.__components__["__onstart__"]
        self.root.mainloop()
        return self
    

    def congig(self, config=None):
        if(config==None):return self.config
        self.config = config
        return self


    def __getitem__(self, name):
        val = None
        if type(name) == tuple:
            val = name[1]
            name = name[0]
        if name in self.config:
            return self.config[name]
        if name in self.__components__:
            result = self.__components__[name][0]()
            if result != None: return result
        return val
    

    def __setitem__(self, name, val):
        if name in self.__components__:
            self.__components__[name][1](val)
        self.config[name] = val


    def __contains__(self, name):
        return name in self.config or name in self.__components__


    def __delitem__(self, name):
        del self.__components__[name]
    

    def visualGetDir(self, name:str=None):
        return filedialog.askdirectory(
            title=self.title if name == None else f"{self.title}: {name}"
        )
    

    def visualGetFile(self, name:str=None, default=None, filter=None, multi=False):
        openFunc = None
        if(multi):
            openFunc = filedialog.askopenfilenames
        else:
            openFunc = filedialog.askopenfilename

        return openFunc(
            title=self.title if name == None else f"{self.title}: {name}",
            defaultextension=filter, initialfile=default
        )
    

    def visualInfo(self, text:str, title:str=None):
        if title == None: title = self.title
        msg = msgbox.showinfo(title=title, message=text, parent=self.root)


    def visualError(self, text:str, title:str=None):
        if title == None: title = self.title
        msg = msgbox.showerror(title=title, message=text, parent=self.root)


    def visualWarning(self, text:str, title:str=None):
        if title == None: title = self.title
        msg = msgbox.showwarning(title=title, message=text, parent=self.root)


    def visualAsk(self, text:str, title:str=None):
        if title == None: title = self.title
        return msgbox.askyesno(title=title, message=text, parent=self.root)


    def __call__(self, *args, **kwds):
        return self.start()
    

def readJson(fileName:str, default={}):
    data = default
    if os.path.exists(fileName):
        with open(fileName, "r") as file: 
            data = json.load(file)
    return data
    

def clearDir(folder):
    if(not os.path.exists(folder)):return
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path): os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


class stdApp(baseApp): 
    def __init__(self, name="Std Te4hno Python APP", size=None, config={}):
        super().__init__(Tk(), name, size)

        if type(config) == str:
            self.config = {}
            def scanCfg(app: stdApp):
                for k, v in readJson(config).items():
                    self[k] = v

            def onClose0(app: stdApp):
                with open(config, "w+") as file: 
                    json.dump(self.config, file, indent=1)

            self.onStart(scanCfg)
            self.onClose(onClose0)
        else:
            self.config = config


class subWindow(baseApp):
    def __init__(self, parent: stdApp, name="Window", size=None):
        super().__init__(Toplevel(), name, size)
        self.config = parent.config

        def copyVars(app):
            for name in self.config:
                if name in self.__components__:
                    self.__components__[name][1](self.config[name])

        self.onStart(copyVars)


"""
Использование

def function(app:stdApp):
    var = app["var"]
    app["var2"] = var

stdApp("Имя").buttom("Кнопка", function).start()

"""