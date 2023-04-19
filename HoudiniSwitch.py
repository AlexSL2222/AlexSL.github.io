#switch自动连接
color = hou.Color(0.5,0.5,0.5)
#设置输入框
def input_Name():
    inputName = hou.ui.readInput("Input Name",buttons = ["ok","Cancle"])[1] #输入内容
    inputName = inputName.replace(" ","_")
    return inputName

try:
    nodes = hou.selectedNodes()
    
    if len(nodes) != 0:
        pan = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor) #获取NetworkEditor面板中鼠标点击的位置
        pos = pan.selectPosition()
    
    switch = nodes[0].parent().createNode("switch") #在选中的node层级创建switch节点
    switch.setName(input_Name()) #设置节点参数
    switch.setColor(color)
    switch.setPosition(pos)
    switch.setRenderFlag(1)
    switch.setDisplayFlag(1)

#设置节点链接
    for i in range(len(nodes)):
#        nodes[i].setSelected(0)
        switch.setInput(i,nodes[i])
#设置切换参数
        inputnode = switch.inputs()
        inputcount = len(inputnode)
        switchparm = switch.parm("input").set(inputcount - 1)
except:
    pass