#houdini添加自定义参数
nodeL = list(hou.selectedNodes())

tuple = {"float"     : hou.FloatParmTemplate,
         "int"       : hou.IntParmTemplate,
         "string"    : hou.StringParmTemplate,
         "rampcolor" : hou.RampParmTemplate,
         "rampfloat" : hou.RampParmTemplate}

def input_Window():
#设置输入框    
    inputWindow = hou.ui.readMultiInput("Input your Info",["inputTuple","inputName","inputLable"],buttons = ["Ok","Cancle"])[1]
    return inputWindow

    
def AddPram(node):
    
    if split[0] == "rampcolor":
        addPram = tuple[split[0]](split[1],split[2],hou.rampParmType.Color)
        print(split[0])
   
    elif split[0] == "rampfloat":
        addPram = tuple[split[0]](split[1],split[2],hou.rampParmType.Float)
        print(split[0])
        
    else:
        addPram = tuple[split[0]](split[1],split[2],1)

#设置添加参数在面板中的位置        
    group = node.parmTemplateGroup()
    
    if a == "group":
        group.insertBefore("group",addPram)
    else:
        group.insertBefore(b,addPram)
    
    node.setParmTemplateGroup(group)
    return
        
for selNode in nodeL:
#获得节点中所有参数的列表    
    num = selNode.parms()
#a是第一个参数的名字，b为第二个参数的名字
    a = num[0].name()
    b = num[1].name()
    
    split = list(input_Window())
    AddPram(selNode)