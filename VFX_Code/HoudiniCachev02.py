#按顺序做缓存
color = hou.Color(1,0.5,0.5)
endNode = list(hou.selectedNodes())[0]
allNode = list(endNode.inputAncestors())
mergelist = []
vlist = []
for node in allNode:
    if node.type().name() == "merge":
        mergelist.append(node)

#print(mergelist)
for merge in mergelist:
    i = 0
    mergeup = list(merge.inputAncestors())    
    for count in mergeup:
        if count.type().name() == "merge":
            i += 1
    vlist.append(i)
mergedict = dict(zip(mergelist, vlist))

mergelist = sorted(mergedict.items(), key=lambda x:x[1], reverse=False)
mergedict = dict(mergelist)
mergelist = list(mergedict.keys())
#print(mergelist)

names = locals()
for i in range(len(mergelist)):
    mlist = list(mergelist[i].inputAncestors())
    relist = list(reversed(mlist))
    names['merge' + str(i) ] = relist
print(merge0)
##    exec('merge{} = {}'.format(i,list(mergelist[i].inputAncestors())))
##    exec('n{} = {}'.format(i, i))
##print(merge0)
for i in range(len(mergelist)):
    for node in names['merge' + str(i) ]:
        if node.type().name() == "filecache::2.0":
            node.setColor(color)
            node.parm("basename").set("$OS")
            node.parm("enableversion").set(0)
            node.parm("loadfromdisk").set(1)
            node.parm("execute").pressButton()