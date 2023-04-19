import os
import sys
import shlex
from pathlib import Path
import hou

# 获取用户选择的文件
files = hou.ui.selectFile(title="Select ABC or FBX Files", file_type=hou.fileType.Geometry, multiple_select=True)
if not files:
    hou.ui.displayMessage(text="No files selected!", severity=hou.severityType.Error)
    sys.exit()

# 替换分号并拆分文件路径字符串
files = files.replace(";", " ")
files = shlex.split(files)

# 展开文件路径中的环境变量
files = [hou.expandString(file) for file in files]

# 创建一个新的 null 节点
obj = hou.node("/obj")
scaleSop = obj.createNode("null", "Scale")
scaleSop.parm("scale").set(0.01)

# 创建一个新的 geo 节点并重命名为 ImpMod
geo = obj.createNode("geo", "ImpMod")
geo.setInput(0, scaleSop)
geo.setDisplayFlag(False)

mergeSop = geo.createNode("merge")

fileIndex = 1
for file in files:
    fileName = os.path.splitext(os.path.basename(file))[0]
    if Path(file).exists():
        if "cam" in fileName.lower():
            # 创建 alembicarchive 节点并导入相机 abc 文件
            camSop = obj.createNode("alembicarchive", fileName)
            camSop.parm("fileName").set(file)
            # 将 alembicarchive 节点与 Scale 节点连接
            camSop.setInput(0, scaleSop)
        else:
            fileExt = os.path.splitext(file)[1].lower()
            if fileExt == ".abc":
                fileSop = geo.createNode("alembic", fileName)
                fileSop.parm("fileName").set(file)
                outSuffix = "abc"
            elif fileExt == ".fbx":
                fileSop = geo.createNode("fbxskinimport", fileName)
                fileSop.parm("fbxfile").set(file)
                fileSop.parm("convertunits").set(False)
                outSuffix = "fbx"
            else:
                continue

            fileSop.setDisplayFlag(False)
            mergeSop.setNextInput(fileSop)

            # 在 my_geo 节点中创建一个新的 null 节点并重命名为 Out_abc_1 或 Out_fbx_1
            outNull = geo.createNode("null", "Out_" + outSuffix + "_" + str(fileIndex))
            outNull.setInput(0, fileSop)
            fileIndex += 1
    else:
        hou.ui.displayMessage(text="file not exist: " + file, severity=hou.severityType.Error)

nullSop = geo.createNode("null")
nullSop.setDisplayFlag(True)

# 创建一个新的 geo 节点并重命名为 Sim
sim = obj.createNode("geo", "Sim")
sim.setColor(hou.Color((1, 0, 0)))
sim.setDisplayFlag(False)

# 在 Sim 节点内部，将 "my_geo" 节点内，导入 abc 或 fbx 的文件节点以 objectMerge 的形式导入到 Sim 中
fileIndex = 1
for file in files:
    if Path(file).exists():
        fileName = os.path.splitext(os.path.basename(file))[0]
        if "cam" not in fileName.lower():
            objMerge = sim.createNode("object_merge", fileName)
            fileExt = os.path.splitext(file)[1].lower()
            if fileExt == ".abc":
                outSuffix = "abc"
            elif fileExt == ".fbx":
                outSuffix = "fbx"
            else:
                continue

            objMerge.parm("objpath1").set(geo.path() + "/Out_" + outSuffix + "_" + str(fileIndex))
            objMerge.parm("xformtype").set(1)
            fileIndex += 1

sim.layoutChildren()
geo.layoutChildren()
obj.layoutChildren()

hou.ui.displayMessage(text="success")