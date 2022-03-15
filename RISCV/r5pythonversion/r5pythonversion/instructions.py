import random


class Instruction_type(object):
    src1 = ""
    src2 = ""
    dest = ""
    indexs1 = 0
    indexs2 = 0
    indexd = 0
    val = []
    offset = ""
    offset_val = 0
    offset_shitf = 1

    memory_addresses_view = []
    memory_value_view = []
    memory_value = []
    memory_dictionary = {}
    # memory_dictionary_fetch is the Dictionary from where the Actual Transfer and Recieving of Data Occurs
    memory_dictionary_fetch = {}

    ### 8 Digit Memory Address View with 4 byte memory Occupation
    ###############################################################

    ###Generating Memory Address For View

    for i in range(0, 512):
        j = i * 4 + 4
        # memory_addresses.append(hex(j))
        memory_addresses_view.append('0x' + '{0:08X}'.format(j))

    ###Working Memory value Initialization

    for i in range(0, 512 * 4):
        memory_value.append(0)

    ###Generating values in Hex of Memory For View

    for i in range(0, 512):
        memory_value_view.append('0x' + '{0:08X}'.format(memory_value[i]))

    for i in range(0, 512):
        # memory_dictionary[hex(i)]=memory_value[i]
        memory_dictionary[memory_addresses_view[i]] = memory_value[i]

    for i in range(0, 512 * 4):
        # memory_dictionary[hex(i)]=memory_value[i]
        memory_dictionary_fetch['{0:08X}'.format(i)] = memory_value[i]

    ###############################################################

    ####################################################################################
    print("Print Check Start Here")
    ##Check VIA PRINT
    print("Memory Address")
    # print(memory_addresses_view)
    print("Memory Initialization")
    # print(memory_value)
    print("Memory Hex value")
    # print(memory_value_view)

    print("Memory Dictionary Value")
    # print(memory_dictionary)

    print("Memory Dictionary To Fetch")
    # print(memory_dictionary_fetch)

    print("Print check END Here")
    ################################################################

    val.append(0)
    for i in range(1, 32):
        val.append(0)
        # val.append(random.randint(1, 100))
    memory_block = []

    list = []
    for y in range(0, 512):
        list.append(random.randint(3, 9))

    mydix = {}

    for x in range(0, 512):
        # key=input('Enter Key ')
        mydix[hex(x)] = list[x]
        # print(mydix)

    # Need To Be Update
    listkey = []
    # *mydix

    listvalue = []

    # *mydix.values()

    # print(mydix)
    # print(listkey)
    # for x in range(0, 512):
    # memory_block.append(random.randint(1, 7000))


# class I_type(Instruction_type):
#     remi = False
#     subi = False
#     addi = False
#     divi = False
#     muli = False
#     load = False
#     Ori = False
#     Andi = False
#     Xori = False
#     llshifti = False  # left logical immediate shift
#     rlshifti = False  # right logical immediate shift
#     rashifti = False  # right arithmetic immediate shift
#     sltimm = False  # Set less than immediate
#     sltimmu = False  # Set less than immediate unsigned
#
#     def getoperatori(self, x):
#         if "addi" in x:
#             y = "addi"
#             self.addi = True
#             x = x[len(y) + 1:]
#             return x
#         elif "subi" in x:
#             y = "subi"
#             self.subi = True
#             x = x[len(y) + 1:]
#             return x
#         elif "muli" in x:
#             y = "muli"
#             self.muli = True
#             x = x[len(y) + 1:]
#             return x
#         elif "divi" in x:
#             y = "divi"
#             self.divi = True
#             x = x[len(y) + 1:]
#             return x
#         elif "remi" in x:
#             y = "remi"
#             self.remi = True
#             x = x[len(y) + 1:]
#             return x
#         elif "lw" in x:
#             y = "lw"
#             self.load = True
#             x = x[len(y) + 1:]
#             return x
#         elif "ori" in x:
#             y = "ori"
#             self.Ori = True
#             x = x[len(y) + 1:]
#             return x
#         elif "andi" in x:
#             y = "andi"
#             self.Andi = True
#             x = x[len(y) + 1:]
#             return x
#         elif "xori" in x:
#             y = "xor"
#             self.Xori = True
#             x = x[len(y) + 1:]
#             return x
#         elif "slli" in x:
#             y = "slli"
#             self.llshifti = True
#             x = x[len(y) + 1:]
#             return x
#         elif "srli" in x:
#             y = "srli"
#             self.rlshifti = True
#             x = x[len(y) + 1:]
#             return x
#         elif "srai" in x:
#             y = "srai"
#             self.rashifti = True
#             x = x[len(y) + 1:]
#             return x
#         elif "sltiu" in x:
#             y = "sltiu"
#             self.sltimmu = True
#             x = x[len(y) + 1:]
#             return x
#         elif "slti" in x:
#             y = "slti"
#             self.sltimm = True
#             x = x[len(y) + 1:]
#             return x
#         else:
#             return x
#
#     def getsdi(self, x):
#         x = x.replace(" ", "")
#         self.dest, self.src1, self.src2 = x.split(",")
#         print(self.dest)
#         print(self.src1)
#         print(self.src2)
#         self.getexecute()
#
#     def getsdl(self, x):
#         x = x.replace(" ", "")
#         x = x.replace("(", "")
#         x = x.replace(")", "")
#
#         self.dest, self.src1 = x.split(",")
#
#         #
#         counter = 0
#         a = self.src1
#         # print(a)
#
#         for x1 in a:
#             if (x1 == 'x' or counter == 1):
#                 counter = 1
#                 break
#             else:
#                 # Problem
#                 a = a[1:]
#                 # problem END
#                 self.offset_shitf = self.offset_shitf + 1
#                 self.offset = self.offset + x1
#         #
#         print(self.offset)
#         print(self.src1)
#         print(self.dest)
#         self.getexecute()
#
#     def getexecute(self):
#
#         print(self.val)
#         # self.src1 = self.src1[1:]
#         # self.src1 = self.src1[2:]
#         # print(self.src1)
#
#         self.src1 = self.src1[self.offset_shitf:]
#         self.dest = self.dest[1:]
#
#         if self.load:
#             self.offset_val = int(self.offset)
#             print(self.offset_val)
#             self.indexs1 = int(self.src1)
#             # self.indexs1 = int(self.src1)
#             self.indexd = int(self.dest)
#         else:
#             self.indexs1 = int(self.src1)
#             self.indexs2 = int(self.src2)
#             self.indexd = int(self.dest)
#
#         Instruction_type.indexs1 = self.indexs1
#         Instruction_type.indexs2 = self.indexs2
#         Instruction_type.indexd = self.indexd
#
#         if self.addi:
#             self.adderi()
#         elif self.subi:
#             self.subtractori()
#         elif self.muli:
#             self.multii()
#         elif self.divi:
#             self.dividei()
#         elif self.remi:
#             self.remainderi()
#         elif self.load:
#             self.loadd(self.val[self.indexs1] + self.offset_val)
#             # self.loadd(self.val[self.indexs1])
#         elif self.Ori:
#             self.Oroperatori()
#         elif self.Andi:
#             self.Andoperatori()
#         elif self.Xori:
#             self.Xoroperatori()
#         elif self.llshifti:
#             self.slloperatori()
#         elif self.rlshifti:
#             self.srloperatori()
#         elif self.rashifti:
#             self.sraoperatori()
#         elif self.sltimm:
#             self.sltimmediate()
#         elif self.sltimmu:
#             self.sltimmediateunsigned()
#         else:
#             print("wrong instruction")
#
#     def adderi(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def subtractori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp - temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def multii(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp * temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def dividei(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp / temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def remainderi(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp % temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def loadd(self, res):
#         # print(self.mydix)
#
#         ###When using Online web
#         # file_values = open("/home/OxygenUIT/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
#         ###when using dedicated machine(PC)
#         file_values = open("templates\m.txt", "r")
#         # print(file_values.readable())
#
#         list = []
#         for x in range(0, 512):
#             list.append(file_values.readline())
#         file_values.close()
#         # print(list)
#         list1 = []
#         for x in list:
#             list1.append(x.replace('\n', ''))
#         # new_set = {x.replace('\n', '') for x in list}
#         # print(list1)
#         memory_block = {}
#         for x in range(0, 512):
#             memory_block[hex(x)] = list1[x]
#
#         value = int(memory_block.get(hex(res)))
#         # mydix.get up
#         # value =self.memory_block[res]
#         self.val[self.indexd] = value
#         print(self.val[self.indexd])
#         print(self.val)
#         print(self.indexd)
#
#         # self.updatememory()
#         # print(self.memory_block)
#         # print(self.memory_block[self.val[self.indexs1]])
#         # print(self.val)
#
#     # Call This Function On Source Operation In Code
#
#     def Oroperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp | temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Andoperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp & temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Xoroperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp ^ temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def slloperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp << temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def srloperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         temp = temp >> temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def sraoperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         # ones = ~temp
#         # twos = ones + 1
#         temp = temp >> temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def sltimmediate(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         if temp < temp1:
#             self.val[self.indexd] = 1
#         else:
#             self.val[self.indexd] = 0
#         print(self.val)
#
#     def sltimmediateunsigned(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexs2
#         if temp1 < 0:
#             temp1 = temp1 * (-1)
#         if temp < temp1:
#             self.val[self.indexd] = 1
#         else:
#             self.val[self.indexd] = 0
#         print(self.val)


# class R_type(Instruction_type):
#     rem = False
#     sub = False
#     add = False
#     div = False
#     mul = False
#     Or = False
#     And = False
#     Xor = False
#     llshift = False  # left logical shift
#     rlshift = False  # right logical shift
#     rashift = False  # right arithmetic shift
#     slt = False  # set less than
#     sltu = False  # set less than unsigned
#
#     def getoperator(self, x):
#         if "add" in x:
#             y = "add"
#             self.add = True
#             x = x[len(y) + 1:]
#             return x
#         elif "sub" in x:
#             y = "sub"
#             self.sub = True
#             x = x[len(y) + 1:]
#             return x
#         elif "mul" in x:
#             y = "mul"
#             self.mul = True
#             x = x[len(y) + 1:]
#             return x
#         elif "div" in x:
#             y = "div"
#             self.div = True
#             x = x[len(y) + 1:]
#             return x
#         elif "rem" in x:
#             y = "rem"
#             self.rem = True
#             x = x[len(y) + 1:]
#             return x
#         elif "or" in x:
#             y = "or"
#             self.Or = True
#             x = x[len(y) + 1:]
#             return x
#         elif "and" in x:
#             y = "and"
#             self.And = True
#             x = x[len(y) + 1:]
#             return x
#         elif "xor" in x:
#             y = "xor"
#             self.Xor = True
#             x = x[len(y) + 1:]
#             return x
#         elif "sll" in x:
#             y = "sll"
#             self.llshift = True
#             x = x[len(y) + 1:]
#             return x
#         elif "srl" in x:
#             y = "srl"
#             self.rlshift = True
#             x = x[len(y) + 1:]
#             return x
#         elif "sra" in x:
#             y = "sra"
#             self.rashift = True
#             x = x[len(y) + 1:]
#             return x
#         elif "sltu" in x:
#             y = "sltu"
#             self.sltu = True
#             x = x[len(y) + 1:]
#             return x
#         elif "slt" in x:
#             y = "slt"
#             self.slt = True
#             x = x[len(y) + 1:]
#             return x
#         else:
#             return x
#
#     def getsd(self, x):
#         x = x.replace(" ", "")
#         self.dest, self.src1, self.src2 = x.split(",")
#         self.getexecute()
#
#     def getexecute(self):
#
#         print(self.val)
#
#         self.src1 = self.src1[1:]
#         self.src2 = self.src2[1:]
#         self.dest = self.dest[1:]
#
#         self.indexs1 = int(self.src1)
#         self.indexs2 = int(self.src2)
#         self.indexd = int(self.dest)
#
#         Instruction_type.indexs1 = self.indexs1
#         Instruction_type.indexs2 = self.indexs2
#         Instruction_type.indexd = self.indexd
#
#         if self.add:
#             self.adder()
#         elif self.sub:
#             self.subtractor()
#         elif self.mul:
#             self.multi()
#         elif self.div:
#             self.divide()
#         elif self.rem:
#             self.remainder()
#         elif self.Or:
#             self.Oroperator()
#         elif self.And:
#             self.Andoperator()
#         elif self.Xor:
#             self.Xoroperator()
#         elif self.llshift:
#             self.slloperator()
#         elif self.rlshift:
#             self.srloperator()
#         elif self.rashift:
#             self.sraoperator()
#         elif self.slt:
#             self.sltreg()
#         elif self.sltu:
#             self.sltunsigned()
#         else:
#             print("wrong instruction")
#
#     def adder(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def subtractor(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp - temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def multi(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp * temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def divide(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp / temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def remainder(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp % temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Oroperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp | temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Andoperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp & temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Xoroperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp ^ temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def slloperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp << temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def srloperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         temp = temp >> temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def sraoperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         ones = ~temp
#         twos = ones + 1
#         temp = twos >> temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def sltreg(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         if temp < temp1:
#             self.val[self.indexd] = 1
#         else:
#             self.val[self.indexd] = 0
#         print(self.val)
#
#     def sltunsigned(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexs2]
#         if temp1 < 0:
#             temp1 = temp1 * (-1)
#         if temp < temp1:
#             self.val[self.indexd] = 1
#         else:
#             self.val[self.indexd] = 0
#         print(self.val)

#
# class S_type(Instruction_type):
#     storew = False
#
#     def getoperators(self, x):
#
#         if "sw" in x:
#             y = "sw"
#             self.storew = True
#             x = x[len(y) + 1:]
#             return x
#         else:
#             return x
#
#     def getsds(self, x):
#         x = x.replace(" ", "")
#         x = x.replace("(", "")
#         x = x.replace(")", "")
#
#         self.dest, self.src1 = x.split(",")
#
#         ###########################
#         counter = 0
#         a = self.src1
#         print(a)
#
#         for x1 in a:
#             if (x1 == 'x' or counter == 1):
#                 counter = 1
#                 break
#             else:
#                 # Problem
#                 a = a[1:]
#                 # problem END
#                 self.offset_shitf = self.offset_shitf + 1
#                 self.offset = self.offset + x1
#         #
#         print(self.offset)
#         ###########################
#         self.getexecute()
#
#     def getexecute(self):
#
#         print(self.val)
#         self.src1 = self.src1[self.offset_shitf:]
#         self.offset_val = int(self.offset)
#         self.dest = self.dest[1:]
#
#         print(self.src1)
#         print(self.dest)
#         print(self.offset_val)
#
#         if self.storew:
#             self.indexs1 = int(self.src1)
#             self.indexd = int(self.dest)
#         else:
#             self.indexs1 = int(self.src1)
#             self.indexs2 = int(self.src2)
#             self.indexd = int(self.dest)
#
#         Instruction_type.indexs1 = self.indexs1
#         Instruction_type.indexs2 = self.indexs2
#         Instruction_type.indexd = self.indexd
#
#         if self.storew:
#             self.stored(self.val[self.indexd] + self.offset_val)
#         else:
#             print("wrong instruction")
#
#     def stored(self, res):
#         print("result", res)
#         print(self.indexs1)
#         # self.memory_block[self.val[self.indexd]] = self.val[self.indexs1]
#         # self.mydix[hex(self.val[self.indexd])]=(self.val[self.indexs1])
#         # self.mydix[hex(self.val[self.indexd])]=int(self.val[self.indexs1])
#
#         self.mydix[hex(self.val[self.indexs1] + self.offset_val)] = int(self.val[self.indexd])
#
#         ###When using Online web
#         # filevalue1=open("/home/OxygenUIT/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","w")
#
#         filevalue1 = open("templates\m.txt", "w")
#         for x in range(0, 512):
#             filevalue1.writelines(str(self.mydix.get(hex(x))) + '\n')
#         filevalue1.close()
#
#         print(self.val)
#         print(self.mydix)
#         print(self.mydix.get(hex(self.val[self.indexs1])))
#         print("##############################")
#         # print(self.memory_block[self.val[self.indexs1]])
#         # print(self.val)
#
# class CR_type(Instruction_type):
#     And = False
#     Or = False
#     Xor = False
#     sub = False
#     subw = False
#     addw = False
#     add = False
#     mv = False
#
#     def getoperator(self, x):
#         if "c.add" in x:
#             y = "add"
#             self.add = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.addw" in x:
#             y = "sub"
#             self.addw = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.mv" in x:
#             y = "mv"
#             self.mv = True
#             x = x[len(y) + 3:]
#             return x
#
#         elif "c.sub" in x:
#             y = "sub"
#             self.sub = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.subw" in x:
#             y = "subw"
#             self.subw = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.or" in x:
#             y = "or"
#             self.Or = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.and" in x:
#             y = "and"
#             self.And = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.xor" in x:
#             y = "xor"
#             self.Xor = True
#             x = x[len(y) + 3:]
#             return x
#
#         else:
#             return x
#
#     def getsd(self, x):
#         x = x.replace(" ", "")
#         self.dest, self.src1 = x.split(",")
#         self.getexecute()
#
#     def getexecute(self):
#
#         print(self.val)
#
#         self.src1 = self.src1[1:]
#         self.dest = self.dest[1:]
#
#         self.indexs1 = int(self.src1)
#         self.indexd = int(self.dest)
#
#         Instruction_type.indexs1 = self.indexs1
#         Instruction_type.indexd = self.indexd
#
#         if self.add:
#             self.addOp()
#         elif self.addw:
#             self.addwOp()
#         elif self.mv:
#             self.moveOp()
#         elif self.sub:
#             self.subOp()
#         elif self.subw:
#             self.subwOp()
#         elif self.Or:
#             self.Oroperator()
#         elif self.And:
#             self.Andoperator()
#         elif self.Xor:
#             self.Xoroperator()
#
#         else:
#             print("wrong instruction")
#
#     def addOp(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def addwOp(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def subOp(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp1 - temp
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def subwOp(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp - temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def moveOp(self):
#         temp = self.val[self.indexs1]
#         #temp1 = self.val[self.indexs2]
#         #temp = temp * temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Oroperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp | temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Andoperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp & temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def Xoroperator(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.val[self.indexd]
#         temp = temp ^ temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
# class CI_type(Instruction_type):
#     addi = False
#     addiw = False
#     addiw4spn = False
#     li = False
#     lui = False
#     slli = False
#     cberak = False
#     lqsp = False
#     lwsp = False
#     ldsp = False
#     rlshifti = False  # right logical immediate shift
#     rashifti = False  # right arithmetic immediate shift
#     andi=False
#
#     def getoperatori(self, x):
#         if "c.addiw4spn" in x:
#             y = "addiw4spn"
#             self.addiw4spn = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.addiw" in x:
#             y = "addiw"
#             self.addiw = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.addi" in x:
#             y = "addi"
#             self.addi = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.li" in x:
#             y = "li"
#             self.li = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.lui" in x:
#             y = "lui"
#             self.lui = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.slli" in x:
#             y = "slli"
#             self.slli = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.srli" in x:
#             y = "srli"
#             self.rashifti = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.andi" in x:
#             y = "andi"
#             self.andi = True
#             x = x[len(y) + 3:]
#             return x
#         elif "c.srai" in x:
#             y = "srai"
#             self.rashifti = True
#             x = x[len(y) + 3:]
#             return x
#
#         else:
#             return x
#
# #src1 is Immediate
#
#     def getsdi(self, x):
#         x = x.replace(" ", "")
#         self.dest, self.src1 = x.split(",")
#         print(self.dest)
#         print(self.src1)
#         #print(self.src2)
#         self.getexecute()
#
#     def getsdl(self, x):
#         x = x.replace(" ", "")
#         x = x.replace("(", "")
#         x = x.replace(")", "")
#
#         self.dest, self.src1 = x.split(",")
#
#         #
#         counter = 0
#         a = self.src1
#         # print(a)
#
#         for x1 in a:
#             if (x1 == 'x' or counter == 1):
#                 counter = 1
#                 break
#             else:
#                 # Problem
#                 a = a[1:]
#                 # problem END
#                 self.offset_shitf = self.offset_shitf + 1
#                 self.offset = self.offset + x1
#         #
#         print(self.offset)
#         print(self.src1)
#         print(self.dest)
#         self.getexecute()
#
#
#
#     def getexecute(self):
#
#         print(self.val)
#         # self.src1 = self.src1[1:]
#         # self.src1 = self.src1[2:]
#         # print(self.src1)
#
#         #self.src1 = self.src1[self.offset_shitf:]
#         self.dest = self.dest[1:]
#
#
#
#         self.indexs1 = int(self.src1)
#         self.indexd = int(self.dest)
#
#
#         Instruction_type.indexs1 = self.indexs1
#         #Instruction_type.indexs2 = self.indexs2
#         Instruction_type.indexd = self.indexd
#
#         if self.addi:
#             self.addiOp()
#         elif self.addiw:
#             self.addiwOp()
#         elif self.addiw4spn:
#             self.addiw4spnOp()
#         elif self.li:
#             self.liOp()
#         elif self.lui:
#             self.luiOp()
#         elif self.lqsp:
#             self.lqspOp()
#             # self.loadd(self.val[self.indexs1])
#         elif self.lwsp:
#             self.lwspOp()
#         elif self.andi:
#             self.andiOp()
#         elif self.slli:
#             self.slliOp()
#         elif self.rlshifti:
#             self.srloperatori()
#         elif self.rashifti:
#             self.sraoperatori()
#
#         else:
#             print("wrong instruction")
#
#     def addiOp(self):
#         temp = self.indexs1
#         temp1 = self.val[self.indexd]
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#     def addiwOp(self):
#         temp = self.indexs1
#         temp1 = self.val[self.indexd]
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#     def addiw4spnOp(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexd
#         temp = temp + temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def liOp(self):
#         print("Li")
#         temp = self.indexs1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def luiOp(self):
#         print("Lui")
#         Instruction_type.src1 = int(self.src1)
#         Instruction_type.dest = int(self.dest)
#         print(self.src1)
#         print(self.dest)
#
#         Instruction_type.val[Instruction_type.dest] = Instruction_type.src1 * 4096
#
#     def lqspOp(self):
#         print("Lqsp")
#
#     def lwspOp(self):
#         print("Lwsp")
#
#     def ldspOp(self):
#         print("Ldsp")
#
#     # Call This Function On Source Operation In Code
#     def andiOp(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexd
#         temp = temp & temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#
#     def slliOp(self):
#         temp = self.val[self.indexd]
#         temp1 = self.indexs1
#         temp = temp << temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def srloperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexd
#         temp = temp >> temp1
#         self.val[self.indexd] = temp
#         print(self.val)
#
#     def sraoperatori(self):
#         temp = self.val[self.indexs1]
#         temp1 = self.indexd
#         # ones = ~temp
#         # twos = ones + 1
#         temp = temp >> temp1
#         self.val[self.indexd] = temp
#         print(self.val)
