#houdini按组将模型拆分
nodeL = list(hou.selectedNodes())

for node in nodeL:
    
    group = {"point" : node.geometry().pointGroups(),
             "prim"  : node.geometry().primGroups(),
             "edge"  : node.geometry().edgeGroups()}
    
    keylist = group.keys()
    
    for key in keylist:
        
        allgroups = group[key]

        for subgroup in allgroups:
           name = subgroup.name()
           
           blast = node.createOutputNode("blast")
           blast.parm("group").set(name)
           blast.parm("negate").set(1)
           blast.parm("removegrp").set(1)
            
           null = blast.createOutputNode("null","OUT_" + name)