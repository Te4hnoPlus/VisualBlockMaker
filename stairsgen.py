

def stairsState(id: str, nms: str = "minecraft"):
    return {
    "variants": {
        "facing=east,half=bottom,shape=straight"    :  { "model": f"{nms}:{id}_stairs"                                           },
        "facing=west,half=bottom,shape=straight"    :  { "model": f"{nms}:{id}_stairs"      , "y": 180          , "uvlock": True },
        "facing=south,half=bottom,shape=straight"   :  { "model": f"{nms}:{id}_stairs"      , "y": 90           , "uvlock": True },
        "facing=north,half=bottom,shape=straight"   :  { "model": f"{nms}:{id}_stairs"      , "y": 270          , "uvlock": True },
        "facing=east,half=bottom,shape=outer_right" :  { "model": f"{nms}:{id}_outer_stairs"                                     },
        "facing=west,half=bottom,shape=outer_right" :  { "model": f"{nms}:{id}_outer_stairs", "y": 180          , "uvlock": True },
        "facing=south,half=bottom,shape=outer_right":  { "model": f"{nms}:{id}_outer_stairs", "y": 90           , "uvlock": True },
        "facing=north,half=bottom,shape=outer_right":  { "model": f"{nms}:{id}_outer_stairs", "y": 270          , "uvlock": True },
        "facing=east,half=bottom,shape=outer_left"  :  { "model": f"{nms}:{id}_outer_stairs", "y": 270          , "uvlock": True },
        "facing=west,half=bottom,shape=outer_left"  :  { "model": f"{nms}:{id}_outer_stairs", "y": 90           , "uvlock": True },
        "facing=south,half=bottom,shape=outer_left" :  { "model": f"{nms}:{id}_outer_stairs"                                     },
        "facing=north,half=bottom,shape=outer_left" :  { "model": f"{nms}:{id}_outer_stairs", "y": 180          , "uvlock": True },
        "facing=east,half=bottom,shape=inner_right" :  { "model": f"{nms}:{id}_inner_stairs"                                     },
        "facing=west,half=bottom,shape=inner_right" :  { "model": f"{nms}:{id}_inner_stairs", "y": 180          , "uvlock": True },
        "facing=south,half=bottom,shape=inner_right":  { "model": f"{nms}:{id}_inner_stairs", "y": 90           , "uvlock": True },
        "facing=north,half=bottom,shape=inner_right":  { "model": f"{nms}:{id}_inner_stairs", "y": 270          , "uvlock": True },
        "facing=east,half=bottom,shape=inner_left"  :  { "model": f"{nms}:{id}_inner_stairs", "y": 270          , "uvlock": True },
        "facing=west,half=bottom,shape=inner_left"  :  { "model": f"{nms}:{id}_inner_stairs", "y": 90           , "uvlock": True },
        "facing=south,half=bottom,shape=inner_left" :  { "model": f"{nms}:{id}_inner_stairs"                                     },
        "facing=north,half=bottom,shape=inner_left" :  { "model": f"{nms}:{id}_inner_stairs", "y": 180          , "uvlock": True },
        "facing=east,half=top,shape=straight"       :  { "model": f"{nms}:{id}_stairs"      , "x": 180          , "uvlock": True },
        "facing=west,half=top,shape=straight"       :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 180, "uvlock": True },
        "facing=south,half=top,shape=straight"      :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 90 , "uvlock": True },
        "facing=north,half=top,shape=straight"      :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 270, "uvlock": True },
        "facing=east,half=top,shape=outer_right"    :  { "model": f"{nms}:{id}_outer_stairs", "x": 180, "y": 90 , "uvlock": True },
        "facing=west,half=top,shape=outer_right"    :  { "model": f"{nms}:{id}_outer_stairs", "x": 180, "y": 270, "uvlock": True },
        "facing=south,half=top,shape=outer_right"   :  { "model": f"{nms}:{id}_outer_stairs", "x": 180, "y": 180, "uvlock": True },
        "facing=north,half=top,shape=outer_right"   :  { "model": f"{nms}:{id}_outer_stairs", "x": 180,           "uvlock": True },
        "facing=east,half=top,shape=outer_left"     :  { "model": f"{nms}:{id}_outer_stairs", "x": 180,           "uvlock": True },
        "facing=west,half=top,shape=outer_left"     :  { "model": f"{nms}:{id}_outer_stairs", "x": 180, "y": 180, "uvlock": True },
        "facing=south,half=top,shape=outer_left"    :  { "model": f"{nms}:{id}_outer_stairs", "x": 180, "y": 90 , "uvlock": True },
        "facing=north,half=top,shape=outer_left"    :  { "model": f"{nms}:{id}_outer_stairs", "x": 180, "y": 270, "uvlock": True },
        "facing=east,half=top,shape=inner_right"    :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 90 , "uvlock": True },
        "facing=west,half=top,shape=inner_right"    :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 270, "uvlock": True },
        "facing=south,half=top,shape=inner_right"   :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 180, "uvlock": True },
        "facing=north,half=top,shape=inner_right"   :  { "model": f"{nms}:{id}_stairs"      , "x": 180,           "uvlock": True },
        "facing=east,half=top,shape=inner_left"     :  { "model": f"{nms}:{id}_stairs"      , "x": 180,           "uvlock": True },
        "facing=west,half=top,shape=inner_left"     :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 180, "uvlock": True },
        "facing=south,half=top,shape=inner_left"    :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 90 , "uvlock": True },
        "facing=north,half=top,shape=inner_left"    :  { "model": f"{nms}:{id}_stairs"      , "x": 180, "y": 270, "uvlock": True }
        }
    }


def stairsBlock(id: str, inner: bool = None, nms: str = "minecraft"):
    parent = "block/inner_stairs" if inner == True else ("block/outer_stairs" if inner == False else "block/stairs") 
    return {
        "parent": "block/stairs",
        "textures": {
            "bottom": f"{nms}:blocks/{id}",
            "top"   : f"{nms}:blocks/{id}",
            "side"  : f"{nms}:blocks/{id}"
        }
    }