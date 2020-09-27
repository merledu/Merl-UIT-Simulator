# import re
#
# whole_code1 = "0x00C00293\r\n0x00D00313"
# if re.match("^0x", whole_code1):
#     whole_code1 = whole_code1.replace('\r\n', '\n')
#
# code_line = [line for line in whole_code1.split('\n') if line.strip() != '']
# Bin = []
# for i in range(len(code_line)):
#     code_line[i] = re.sub(r"^0x", '', code_line[i])
#     Bin.append("{0:032b}".format(int(code_line[i], 16)))
#
# print(code_line)
# print(Bin)
#
# opcodeh = []
# desth = []
# funct3h = []
# source1h = []
# immh = []
# code = []
# for i in range(len(code_line)):
#     if Bin[i][25:32] == "0010011" and Bin[i][17:20] == "000":
#         opcodeh.append(Bin[i][25:32])
#         desth.append(int(Bin[i][20:25], 2))
#         funct3h.append(Bin[i][17:20])
#         source1h.append(int(Bin[i][12:17], 2))
#         immh.append(int(Bin[i][:12], 2))
#         code.append("addi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
# print(desth)
# print(source1h)
# print(immh)
#
# print(code)


from r5pythonversion.r5pythonversion import views
from r5pythonversion.r5pythonversion import Display_Info
from r5pythonversion.r5pythonversion import Simulator_buttons
from r5pythonversion.r5pythonversion.Simulator_buttons import stepping
# views.Base.code_line1 = ["addi x3,x2,12", "jal label", "add x2,x1,x1", "label:", "addi x4,x3,4", "jalr x0,x5,4"]
# answer = stepping(views.Base.code_line1[views.Base.vari])
views.Base.whole_code = "addi x1,x0,2\r\njal label\r\naddi x2,x0,4\r\nlabel1:\r\nslt x2,x1,x2\r\nadd x3,x2,x3\r\njal label1\r\nsub x3,x4,x5\r\nsw x2,5(x0)\r\nlabel:\r\nori x17,x14,4\r\nandi x16,x13,3\r\nxori x15,x12,2\r\nslli x14,x1,2\r\nsrli x13,x1,3\r\nsrai x12,x2,2\r\nlui x13,1\r\njalr x0,x5,20"
views.Base.whole_code = "addi x1,x0,2\r\naddi x2,x0,4\r\nslt x2,x1,x2\r\nadd x3,x2,x3\r\nsub x3,x4,x5\r\nsw x2,5(x0)\r\nori x17,x14,4\r\nandi x16,x13,3\r\nxori x15,x12,2\r\nslli x14,x1,2\r\nsrli x13,x1,3\r\nsrai x12,x2,2\r\nlui x13,1"
Simulator_buttons.execute(views.Base.whole_code)
# answer = stepping(views.Base.code_line1[views.Base.vari])
# Display_Info.Display_info_I("test")
