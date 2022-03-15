from .instructions import Instruction_type


class S_type(Instruction_type):
    storew = False

    def getoperators(self, x):
        print(x)
        if "sw" in x:
            y = "sw"
            self.storew = True
            x = x[len(y) + 1:]
            return x
        else:
            return x

    def getsds(self, x):
        x = x.replace(" ", "")
        x = x.replace("(", "")
        x = x.replace(")", "")

        self.dest, self.src1 = x.split(",")

        ###########################
        counter = 0
        a = self.src1
        print(a)

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
        ###########################
        self.getexecute()

    def getexecute(self):

        print(self.val)
        self.src1 = self.src1[self.offset_shitf:]
        self.offset_val = int(self.offset)
        self.dest = self.dest[1:]

        print(self.src1)
        print(self.dest)
        print(self.offset_val)

        if self.storew:
            self.indexs1 = int(self.src1)
            self.indexd = int(self.dest)
        else:
            self.indexs1 = int(self.src1)
            self.indexs2 = int(self.src2)
            self.indexd = int(self.dest)

        Instruction_type.indexs1 = self.indexs1
        Instruction_type.indexs2 = self.indexs2
        Instruction_type.indexd = self.indexd

        if self.storew:
            self.stored(self.val[self.indexd] + self.offset_val)
        else:
            print("wrong instruction")

    def stored(self, res):
        print("result", res)
        print(self.indexs1)
        # self.memory_block[self.val[self.indexd]] = self.val[self.indexs1]
        # self.mydix[hex(self.val[self.indexd])]=(self.val[self.indexs1])
        # self.mydix[hex(self.val[self.indexd])]=int(self.val[self.indexs1])

        self.mydix[hex(self.val[self.indexs1] + self.offset_val)] = int(self.val[self.indexd])

        ###When using Online web
        # filevalue1=open("/home/OxygenUIT/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","w")

        filevalue1 = open("templates\m.txt", "w")
        for x in range(0, 512):
            filevalue1.writelines(str(self.mydix.get(hex(x))) + '\n')
        filevalue1.close()

        print(self.val)
        print(self.mydix)
        print(self.mydix.get(hex(self.val[self.indexs1])))
        print("##############################")
        # print(self.memory_block[self.val[self.indexs1]])
        # print(self.val)