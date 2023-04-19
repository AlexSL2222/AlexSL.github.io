#自动按顺序做缓存
import random
rand = random.random()
color = hou.Color(rand,rand,rand)
endNode = list(hou.selectedNodes())[0]
allNode = list(endNode.inputAncestors())
mergelist = []
vlist = []

for node in allNode:                               #读取所有merge节点
    if node.type().name() == "merge":
        mergelist.append(node)
    elif len(node.outputs()) > 1:
        mergelist.append(node)

#print(mergelist)
for merge in mergelist:                            #获取所有merge节点的上游节点，判断每个merge上游的merge数量
    i = 0
    mergeup = list(merge.inputAncestors())    
    for count in mergeup:
        if count.type().name() == "merge":
            i += 1
    vlist.append(i)
mergedict = dict(zip(mergelist, vlist))

mergelist = sorted(mergedict.items(), key=lambda x:x[1], reverse=False)
mergedict = dict(mergelist)
mergelist = list(mergedict.keys())                  #根据merge数量对列表排序，判断cache节点的上下游关系
#print(mergelist)

names = locals()
for i in range(len(mergelist)):
    mlist = list(mergelist[i].inputAncestors())
    relist = list(reversed(mlist))
    names['merge' + str(i) ] = relist


for i in range(len(mergelist)):                     #根据merge节点的顺序对上游的cache进行缓存
    for node in names['merge' + str(i) ]:
        if node.type().name() == "filecache::2.0":
            oldcolor = node.color()
            if oldcolor != color:
                node.setColor(color)
                node.parm("basename").set("$OS")
                node.parm("enableversion").set(0)
                node.parm("loadfromdisk").set(1)
                node.parm("execute").pressButton()
                print(node)
            else:
                continue

reallNode = list(reversed(allNode))

for node in reallNode:
    oldcolor = node.color()
    if oldcolor != color and node.type().name() == "filecache::2.0":
        node.setColor(color)
        node.parm("basename").set("$OS")
        node.parm("enableversion").set(0)
        node.parm("loadfromdisk").set(1)
        node.parm("execute").pressButton()
        print(node)