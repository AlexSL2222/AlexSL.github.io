#houdini批量导入文件
import os
geoname = hou.ui.readInput("Import File Name",buttons = ["Ok","Cancle"])[1] #输入文件名
node = hou.node("/obj").createNode("geo",geoname) #创建geo节点

path = hou.ui.selectFile(file_type=hou.fileType.Directory) #输入路径
fileList = os.listdir(path)   #列出文件夹内文件


mergeNode = node.createNode('merge')   #创建merge节点
 
for name in fileList:        #遍历文件夹内文件，并对每一个执行
    fileNode = node.createNode('file')      #创建节点
    fileNode.parm('file').set(path + name)   #设置文件读取的路径
    namelist = name.split(".")
    parmname = namelist[0]
    attNode = node.createNode('attribcreate')  #创建名字属性，用于循环
    attNode.parm('name1').set('name')          #设置节点参数
    attNode.parm('class1').set(1)
    attNode.parm('type1').set(3)
    attNode.parm('string1').set(parmname)
    
    attNode.setInput(0,fileNode)     #连接节点
    
    mergeNode.setInput(1100,attNode)  #需要设置一个比较大的输入口数字
    
nullNode = node.createNode("null","OUT" + "_" + geoname) #创建null节点
nullNode.setInput(0,mergeNode) #连接节点

nullNode.setDisplayFlag(True) #设置显示
node.layoutChildren()    #整理节点