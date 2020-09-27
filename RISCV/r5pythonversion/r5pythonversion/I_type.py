from .instructions import Instruction_type


class I_type(Instruction_type):
    remi = False
    subi = False
    addi = False
    divi = False
    muli = False
    load = False
    Ori = False
    Andi = False
    Xori = False
    llshifti = False  # left logical immediate shift
    rlshifti = False  # right logical immediate shift
    rashifti = False  # right arithmetic immediate shift
    sltimm = False  # Set less than immediate
    sltimmu = False  # Set less than immediate unsigned

    def getoperatori(self, x):
        if "addi" in x:
            y = "addi"
            self.addi = True
            x = x[len(y) + 1:]
            return x
        elif "subi" in x:
            y = "subi"
            self.subi = True
            x = x[len(y) + 1:]
            return x
        elif "muli" in x:
            y = "muli"
            self.muli = True
            x = x[len(y) + 1:]
            return x
        elif "divi" in x:
            y = "divi"
            self.divi = True
            x = x[len(y) + 1:]
            return x
        elif "remi" in x:
            y = "remi"
            self.remi = True
            x = x[len(y) + 1:]
            return x
        elif "lw" in x:
            y = "lw"
            self.load = True
            x = x[len(y) + 1:]
            return x
        elif "ori" in x:
            y = "ori"
            self.Ori = True
            x = x[len(y) + 1:]
            return x
        elif "andi" in x:
            y = "andi"
            self.Andi = True
            x = x[len(y) + 1:]
            return x
        elif "xori" in x:
            y = "xor"
            self.Xori = True
            x = x[len(y) + 1:]
            return x
        elif "slli" in x:
            y = "slli"
            self.llshifti = True
            x = x[len(y) + 1:]
            return x
        elif "srli" in x:
            y = "srli"
            self.rlshifti = True
            x = x[len(y) + 1:]
            return x
        elif "srai" in x:
            y = "srai"
            self.rashifti = True
            x = x[len(y) + 1:]
            return x
        elif "sltiu" in x:
            y = "sltiu"
            self.sltimmu = True
            x = x[len(y) + 1:]
            return x
        elif "slti" in x:
            y = "slti"
            self.sltimm = True
            x = x[len(y) + 1:]
            return x
        else:
            return x

    def getsdi(self, x):
        x = x.replace(" ", "")
        self.dest, self.src1, self.src2 = x.split(",")
        print(self.dest)
        print(self.src1)
        print(self.src2)
        self.getexecute()

    def getsdl(self, x):
        x = x.replace(" ", "")
        x = x.replace("(", "")
        x = x.replace(")", "")

        self.dest, self.src1 = x.split(",")

        #
        counter = 0
        a = self.src1
        # print(a)

        for x1 in a:
            if (x1 == 'x' or counter == 1):
                counter = 1
                break
            else:
                # Problem
                a = a[1:]
                # problem END
                self.offset_shitf = self.offset_shitf + 1
                self.offset = self.offset + x1
        #
        print(self.offset)
        print(self.src1)
        print(self.dest)
        self.getexecute()

    def getexecute(self):

        print(self.val)
        # self.src1 = self.src1[1:]
        # self.src1 = self.src1[2:]
        # print(self.src1)

        self.src1 = self.src1[self.offset_shitf:]
        self.dest = self.dest[1:]

        if self.load:
            self.offset_val = int(self.offset)
            print(self.offset_val)
            self.indexs1 = int(self.src1)
            # self.indexs1 = int(self.src1)
            self.indexd = int(self.dest)
        else:
            self.indexs1 = int(self.src1)
            self.indexs2 = int(self.src2)
            self.indexd = int(self.dest)

        Instruction_type.indexs1 = self.indexs1
        Instruction_type.indexs2 = self.indexs2
        Instruction_type.indexd = self.indexd

        if self.addi:
            self.adderi()
        elif self.subi:
            self.subtractori()
        elif self.muli:
            self.multii()
        elif self.divi:
            self.dividei()
        elif self.remi:
            self.remainderi()
        elif self.load:
            self.loadd(self.val[self.indexs1] + self.offset_val)
            # self.loadd(self.val[self.indexs1])
        elif self.Ori:
            self.Oroperatori()
        elif self.Andi:
            self.Andoperatori()
        elif self.Xori:
            self.Xoroperatori()
        elif self.llshifti:
            self.slloperatori()
        elif self.rlshifti:
            self.srloperatori()
        elif self.rashifti:
            self.sraoperatori()
        elif self.sltimm:
            self.sltimmediate()
        elif self.sltimmu:
            self.sltimmediateunsigned()
        else:
            print("wrong instruction")

    def adderi(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)

    def subtractori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp - temp1
        self.val[self.indexd] = temp
        print(self.val)

    def multii(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp * temp1
        self.val[self.indexd] = temp
        print(self.val)

    def dividei(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp / temp1
        self.val[self.indexd] = temp
        print(self.val)

    def remainderi(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp % temp1
        self.val[self.indexd] = temp
        print(self.val)

    def loadd(self, res):
        # print(self.mydix)

        ###When using Online web
        # file_values = open("/home/OxygenUIT/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
        ###when using dedicated machine(PC)
        file_values = open("templates\m.txt", "r")
        # print(file_values.readable())

        list = []
        for x in range(0, 512):
            list.append(file_values.readline())
        file_values.close()
        # print(list)
        list1 = []
        for x in list:
            list1.append(x.replace('\n', ''))
        # new_set = {x.replace('\n', '') for x in list}
        # print(list1)
        memory_block = {}
        for x in range(0, 512):
            memory_block[hex(x)] = list1[x]

        value = int(memory_block.get(hex(res)))
        # mydix.get up
        # value =self.memory_block[res]
        self.val[self.indexd] = value
        print(self.val[self.indexd])
        print(self.val)
        print(self.indexd)

        # self.updatememory()
        # print(self.memory_block)
        # print(self.memory_block[self.val[self.indexs1]])
        # print(self.val)

    # Call This Function On Source Operation In Code

    def Oroperatori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp | temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Andoperatori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp & temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Xoroperatori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp ^ temp1
        self.val[self.indexd] = temp
        print(self.val)

    def slloperatori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        temp = temp << temp1
        self.val[self.indexd] = temp
        print(self.val)

    def srloperatori(self):
        temp = self.val[self.indexs1]
        temp = temp + (2 ** 32)
        temp1 = self.indexs2
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)

    def sraoperatori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        # ones = ~temp
        # twos = ones + 1
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)

    def sltimmediate(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        if temp < temp1:
            self.val[self.indexd] = 1
        else:
            self.val[self.indexd] = 0
        print(self.val)

    def sltimmediateunsigned(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        if temp1 < 0:
            temp1 = temp1 * (-1)
        if temp < temp1:
            self.val[self.indexd] = 1
        else:
            self.val[self.indexd] = 0
        print(self.val)