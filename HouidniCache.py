#自动缓存
nodelist = list(hou.selectedNodes())
node = nodelist[0]
i=0
while i<100:
    pre = node.input(0)
    if  pre != None:
        
        node = pre
        i += 1
    else:
        break


while i<100:
    if len(node.outputs()) != 0:
        next = list(node.outputs())[0]
        if next.type().name() == "filecache::2.0":
            next.setColor(color)
            next.parm("basename").set("$OS")
            next.parm("enableversion").set(0)
            next.parm("loadfromdisk").set(1)
            next.parm("execute").pressButton()
            node = next
            i += 1
        else: 
            node = next
            i += 1
    else:
        break 