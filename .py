import nbtlib
from collections import namedtuple

face=namedtuple("face","A B C D")
point=namedtuple("v","X Y Z")


nbtfile=nbtlib.load("skull_4.nbt").root
palettes=nbtfile["palette"]
blocks=nbtfile["blocks"]


def create_palette(palette):#现在只是判断是不是空气。将要改掉。
    if palette["Name"]=="minecraft:air":
        return []
    else:
        return [face(point(0,0,0),point(16,0,0),point(16,16,0),point(0,16,0)),
                face(point(0,0,16),point(16,0,16),point(16,16,16),point(0,16,16)),
                face(point(0,0,0),point(0,16,0),point(0,16,16),point(0,0,16)),
                face(point(16,0,0),point(16,16,0),point(16,16,16),point(16,0,16)),
                face(point(0,0,0),point(16,0,0),point(16,0,16),point(0,0,16)),
                face(point(0,16,0),point(16,16,0),point(16,16,16),point(0,16,16))]#一个立方体
def move(faces,pos):#把一串面统统移动 单位是1/16格。也就是原版游戏材质里的像素。
    x,y,z=pos
    x,y,z=16*x,16*y,16*z
    out=[]
    for f in faces:
        f_=[]
        for p in f:
            x_,y_,z_=p
            f_.append(point(x+x_,y+y_,z+z_))
        out.append(face(*f_))
    return out

palettes=tuple(map(create_palette,palettes))
out=[]
for block in blocks:
    out.extend(   move(palettes[block["state"]],block["pos"])   )

vlist=[]
flist=[]
for f in out:
    f_=[]
    for v in f:
        if v not in vlist:
            vlist.append(v)
            num=len(vlist)
        else:
            num=vlist.index(v)+1
        f_.append(num)
    flist.append(face(*f_))

for v in vlist:
    print ("v",*v)
for f in flist:
    print ("f",*f)

    
    
    
    
    
   
def ore(dict1,objdict):
	return all(objdict.get(i) in j.split("|") for i,j in dict1.items())
def when(when,obj):
	if isinstance(when.get("OR"),list):
		return any(ore(i,obj) for i in when["OR"])
	return ore(when,obj)
def multipart(mult,obj):
    for case in mult:
        if ("when" not in case) or when(case["when"],obj):
            if isinstance( case["apply"],list):
                yield case["apply"][0]
            else:
                yield case["apply"]
#multipart(j["multipart"],palettes[4]["Properties"])
t="eggs=1,hatch=1"
dict((j.strip() for j in i.split("=")) for i in t.split(","))
