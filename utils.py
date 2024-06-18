from te4lib import *;
import json
import stairsgen as stg


def state(id: str, nms = "minecraft"):
    return {"variants":{"normal":{"model": nms+":"+id}}}


def block(id: str, nms = "minecraft"):
    return {"parent":"minecraft:block/cube_all","textures":{"all":nms+":"+id}}


def blockSlabState(id: str, nms = "minecraft"):
    return {
        "variants": {
            "half=bottom": {"model": nms+":half_" +id },
            "half=top"   : {"model": nms+":upper_"+id }
        }
    }


def blockSlab(id: str, nms = "minecraft", upper = False):
    return {
        "parent": "block/upper_slab" if upper else "block/half_slab",
        "textures": {
            "bottom": nms+":blocks/"+id,
            "top"   : nms+":blocks/"+id,
            "side"  : nms+":blocks/"+id
        }
    }


def blockItem(id: str, nms = "minecraft"):
    return {"parent": nms+":block/"+id}


def __makeDirFor__(filepath: str):
    dir = "/".join(filepath.split("/")[:-1])
    if not os.path.exists(dir):
        os.makedirs(dir)


def recipieShapedFor(id: str, nms = "minecraft"):
    return {
        "type": "minecraft:crafting_shaped",
        "pattern": [
            "   ",
            " V ",
            "   "
        ],
        "key": {
            "V": {"item": nms+":"+id}
        },
        "result": {
            "item": {"item": nms+":"+id},
            "count": 1
        }
    }


def recipieShapelessFor(id: str, nms = "minecraft"):
    return {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            {"item": nms+":"+id}
        ],
        "result": {
            "item": {"item": nms+":"+id},
            "count": 1
        }
    }


class BlockCreator:
    def __init__(self, nms = "minecraft", dir = "assets") -> None:
        self.nms = nms
        self.dir = dir


    def setNms(self, nms: str):
        self.nms = nms

    
    def setDir(self, dir: str):
        self.dir = dir


    def save(self, path: str, data: dict, indent=None, separators=(',',':')):
        filepath = f"{self.dir}/{path}"
        __makeDirFor__(filepath)

        with open(filepath, "w+") as file:
            json.dump(data, file, indent=indent, separators=separators)


    def saveReadable(self, path: str, data: dict):
        self.save(path, data, indent=4, separators=None)


    def path(self, path: str):
        return f"{self.nms}/{path}"
    

    def path(self, path: str, id: str):
        return f"{self.nms}/{path}/{id}.json"

    
    def makeBlockItem(self, id: str):
        self.save(self.path("blockstates" , id),     state(id=id, nms=self.nms))
        self.save(self.path("models/block", id),     block(id=id, nms=self.nms))
        self.save(self.path("models/item" , id), blockItem(id=id, nms=self.nms))


    def makeBlockSlab(self, id: str):
        id += "_slab"
        self.save(self.path("blockstates" ,          id), blockSlabState(id=id, nms=self.nms             ))
        
        self.save(self.path("models/block", "half_"+ id),      blockSlab(id=id, nms=self.nms, upper=False))
        self.save(self.path("models/block", "upper_"+id),      blockSlab(id=id, nms=self.nms, upper=True ))
        
        self.save(self.path("models/item" ,          id),      blockItem(id="half_" + id, nms=self.nms   ))


    def makeBlockStairs(self, id: str):
        self.save(self.path("blockstates",  id+"_stairs")      , stg.stairsState(id=id, nms=self.nms))

        self.save(self.path("models/block", id+"_stairs")      , stg.stairsBlock(id=id, nms=self.nms))
        self.save(self.path("models/block", id+"_inner_stairs"), stg.stairsBlock(id=id, nms=self.nms, inner=True))
        self.save(self.path("models/block", id+"_outer_stairs"), stg.stairsBlock(id=id, nms=self.nms, inner=False))

        self.save(self.path("models/item" , id+"_stairs")      , blockItem(id=id+"_stairs", nms=self.nms))


    def makeRecipie(self, id: str, shaped: bool = False):
        data = None
        if shaped:
            data =    recipieShapedFor(id, nms=self.nms)
        else:
            data = recipieShapelessFor(id, nms=self.nms)

        self.saveReadable(self.path("recipes", id), data)