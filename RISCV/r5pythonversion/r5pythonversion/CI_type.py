from .instructions import Instruction_type


class CI_type(Instruction_type):
    addi = False
    addiw = False
    addiw4spn = False
    li = False
    lui = False
    slli = False
    cberak = False
    lqsp = False
    lwsp = False
    ldsp = False
    rlshifti = False  # right logical immediate shift
    rashifti = False  # right arithmetic immediate shift
    andi=False

    def getoperatori(self, x):
        if "c.addiw4spn" in x:
            y = "addiw4spn"
            self.addiw4spn = True
            x = x[len(y) + 3:]
            return x
        elif "c.addiw" in x:
            y = "addiw"
            self.addiw = True
            x = x[len(y) + 3:]
            return x
        elif "c.addi" in x:
            y = "addi"
            self.addi = True
            x = x[len(y) + 3:]
            return x
        elif "c.li" in x:
            y = "li"
            self.li = True
            x = x[len(y) + 3:]
            return x
        elif "c.lui" in x:
            y = "lui"
            self.lui = True
            x = x[len(y) + 3:]
            return x
        elif "c.slli" in x:
            y = "slli"
            self.slli = True
            x = x[len(y) + 3:]
            return x
        elif "c.srli" in x:
            y = "srli"
            self.rlshifti = True
            x = x[len(y) + 3:]
            return x
        elif "c.andi" in x:
            y = "andi"
            self.andi = True
            x = x[len(y) + 3:]
            return x
        elif "c.srai" in x:
            y = "srai"
            self.rashifti = True
            x = x[len(y) + 3:]
            return x

        else:
            return x

#src1 is Immediate

    def getsdi(self, x):
        x = x.replace(" ", "")
        self.dest, self.src1 = x.split(",")
        print(self.dest)
        print(self.src1)
        #print(self.src2)
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

        #self.src1 = self.src1[self.offset_shitf:]
        self.dest = self.dest[1:]



        self.indexs1 = int(self.src1)
        self.indexd = int(self.dest)


        Instruction_type.indexs1 = self.indexs1
        #Instruction_type.indexs2 = self.indexs2
        Instruction_type.indexd = self.indexd

        if self.addi:
            self.addiOp()
        elif self.addiw:
            self.addiwOp()
        elif self.addiw4spn:
            self.addiw4spnOp()
        elif self.li:
            self.liOp()
        elif self.lui:
            self.luiOp()
        elif self.lqsp:
            self.lqspOp()
            # self.loadd(self.val[self.indexs1])
        elif self.lwsp:
            self.lwspOp()
        elif self.andi:
            self.andiOp()
        elif self.slli:
            self.slliOp()
        elif self.rlshifti:
            self.srloperatori()
        elif self.rashifti:
            self.sraoperatori()

        else:
            print("wrong instruction")

    def addiOp(self):
        temp = self.indexs1
        temp1 = self.val[self.indexd]
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)
    def addiwOp(self):
        temp = self.indexs1
        temp1 = self.val[self.indexd]
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)
    def addiw4spnOp(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexd
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)

    def liOp(self):
        print("Li")
        temp = self.indexs1
        self.val[self.indexd] = temp
        print(self.val)

    def luiOp(self):
        print("Lui")
        Instruction_type.src1 = int(self.src1)
        Instruction_type.dest = int(self.dest)
        print(self.src1)
        print(self.dest)

        Instruction_type.val[Instruction_type.dest] = Instruction_type.src1 * 4096

    def lqspOp(self):
        print("Lqsp")

    def lwspOp(self):
        print("Lwsp")

    def ldspOp(self):
        print("Ldsp")

    # Call This Function On Source Operation In Code
    def andiOp(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexd
        temp = temp & temp1
        self.val[self.indexd] = temp
        print(self.val)


    def slliOp(self):
        temp = self.val[self.indexd]
        temp1 = self.indexs1
        temp = temp << temp1
        self.val[self.indexd] = temp
        print(self.val)

    def srloperatori(self):
        temp = self.val[self.indexd]
        temp = temp + (2 ** 32)
        temp1 = self.indexs1
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)

    def sraoperatori(self):
        temp = self.val[self.indexd]
        temp1 = self.indexs1
        # ones = ~temp
        # twos = ones + 1
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)