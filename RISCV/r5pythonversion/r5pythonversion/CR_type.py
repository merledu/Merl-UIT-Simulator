from .instructions import Instruction_type

class CR_type(Instruction_type):
    And = False
    Or = False
    Xor = False
    sub = False
    subw = False
    addw = False
    add = False
    mv = False

    def getoperator(self, x):
        if "c.add" in x:
            y = "add"
            self.add = True
            x = x[len(y) + 3:]
            return x
        elif "c.addw" in x:
            y = "sub"
            self.addw = True
            x = x[len(y) + 3:]
            return x
        elif "c.mv" in x:
            y = "mv"
            self.mv = True
            x = x[len(y) + 3:]
            return x

        elif "c.sub" in x:
            y = "sub"
            self.sub = True
            x = x[len(y) + 3:]
            return x
        elif "c.subw" in x:
            y = "subw"
            self.subw = True
            x = x[len(y) + 3:]
            return x
        elif "c.or" in x:
            y = "or"
            self.Or = True
            x = x[len(y) + 3:]
            return x
        elif "c.and" in x:
            y = "and"
            self.And = True
            x = x[len(y) + 3:]
            return x
        elif "c.xor" in x:
            y = "xor"
            self.Xor = True
            x = x[len(y) + 3:]
            return x

        else:
            return x

    def getsd(self, x):
        x = x.replace(" ", "")
        self.dest, self.src1 = x.split(",")
        self.getexecute()

    def getexecute(self):

        print(self.val)

        self.src1 = self.src1[1:]
        self.dest = self.dest[1:]

        self.indexs1 = int(self.src1)
        self.indexd = int(self.dest)

        Instruction_type.indexs1 = self.indexs1
        Instruction_type.indexd = self.indexd

        if self.add:
            self.addOp()
        elif self.addw:
            self.addwOp()
        elif self.mv:
            self.moveOp()
        elif self.sub:
            self.subOp()
        elif self.subw:
            self.subwOp()
        elif self.Or:
            self.Oroperator()
        elif self.And:
            self.Andoperator()
        elif self.Xor:
            self.Xoroperator()

        else:
            print("wrong instruction")

    def addOp(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)

    def addwOp(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)

    def subOp(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp1 - temp
        self.val[self.indexd] = temp
        print(self.val)

    def subwOp(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp - temp1
        self.val[self.indexd] = temp
        print(self.val)

    def moveOp(self):
        temp = self.val[self.indexs1]
        #temp1 = self.val[self.indexs2]
        #temp = temp * temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Oroperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp | temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Andoperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp & temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Xoroperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexd]
        temp = temp ^ temp1
        self.val[self.indexd] = temp
        print(self.val)