from te4stdapp import stdApp, subWindow, baseApp
from utils import BlockCreator


if __name__ == "__main__":
    creator = BlockCreator()
    
    def setDir(app: stdApp):
        recheckDir(app, app.visualGetDir("Выберите целевую папку"))

    def recheckDir(app: stdApp, dir: str):
        if dir != None and dir != "": 
            creator.setDir(dir)
            app["dir"] = dir
        else: 
            app["dir"] = "assets"
            creator.setDir("assets")


    def onStart(app: stdApp):
        recheckDir(app, app["dir"])
        creator.setNms(app["nms"])


    def makeBlockGui(app: stdApp):
        def makeBlockBtn(app: baseApp):
            id = app["id"]
            flag = False

            if(app["make_base"]):
                flag = True
                creator.makeBlockItem(id)
            if(app["make_slab"]):
                flag = True
                creator.makeBlockSlab(id)
            if(app["make_stairs"]):
                flag = True
                creator.makeBlockStairs(id)

            if not flag:
                app.visualError("Ничего не создано")
            else:
                app.visualInfo("Успешно создано")


        wi = subWindow(app, "Создать"
            ).text("Пространство имен", var="nms"
            ).input("id"
            ).checkBtn("make_base"  , "Создать блок"     , pos={"c":1, "r":0}, padding=3
            ).checkBtn("make_slab"  , "Создать плиту"    , pos={"c":1, "r":1}, padding=3
            ).checkBtn("make_stairs", "Создать ступеньки", pos={"c":1, "r":2}, padding=3
            ).buttom(makeBlockBtn, name="Создать"
            ).ico().start()

        pass
    

    stdApp("Блокоделка", config="config.json"
           ).input("nms", "minecraft", unfocusTask=lambda app: creator.setNms(app["nms"])
           ).buttom(setDir, "Выбрать целевую папку"
           ).text(text="Папка не определена", var="dir",
           ).buttom(makeBlockGui, "Создать блок"
           ).onStart(onStart
           ).ico().start()

