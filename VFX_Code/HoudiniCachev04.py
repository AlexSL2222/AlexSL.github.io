#自动按顺序做缓存
import random
rand = random.random()
color = hou.Color(rand,rand,rand)
endNode = list(hou.selectedNodes())[0]
allNode = list(endNode.inputAncestors())
mergelist = []
vlist = []

def setCache(node):                                 #缓存节点的参数设置
    node.setColor(color)
    node.parm("basename").set("$OS")
    node.parm("enableversion").set(0)
    node.parm("loadfromdisk").set(1)
    node.parm("execute").pressButton()
    print(node)
    return node


for node in allNode:                                #读取所有merge节点,并且如果节点有两个输出将这个节点视为merge
    if node.type().name() == "merge":
        mergelist.append(node)
    elif len(node.outputs()) > 1:
        mergelist.append(node)

#print(mergelist)
for merge in mergelist:                             #获取所有merge节点上游的merge节点数量，创建字典，包含数量越多的流程中越靠下
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
    mlist = list(mergelist[i].inputAncestors())     #获取每个merge节点的上游节点，并反转顺序
    relist = list(reversed(mlist))
    names['merge' + str(i) ] = relist


for i in range(len(mergelist)):                     #根据merge节点的顺序对上游的cache进行缓存
    for node in names['merge' + str(i) ]:
        if node.type().name() == "filecache::2.0":  #用节点颜色作为判断颜色相同的表示已缓存并跳过
            oldcolor = node.color()
            if oldcolor != color:
                setCache(node)
            else:
                continue

reallNode = list(reversed(allNode))                 #对最后一个merge节点下游的cache节点进行缓存

for node in reallNode:
    oldcolor = node.color()
    if oldcolor != color and node.type().name() == "filecache::2.0":
        setCache(node)