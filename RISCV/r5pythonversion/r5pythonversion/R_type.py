from . import instructions


class R_type(instructions.Instruction_type):
    rem = False
    remu = False
    sub = False
    add = False
    div = False
    divu = False
    mul = False
    mulh = False
    mulhu = False
    mulhsu = False
    Or = False
    And = False
    Xor = False
    llshift = False  # left logical shift
    rlshift = False  # right logical shift
    rashift = False  # right arithmetic shift
    slt = False  # set less than
    sltu = False  # set less than unsigned

    def getoperator(self, x):
        print("This is get operator" + str(x))
        if "add" in x:
            y = "add"
            self.add = True
            x = x[len(y) + 1:]
            return x
        elif "sub" in x:
            y = "sub"
            self.sub = True
            x = x[len(y) + 1:]
            return x
        elif "mulhsu" in x:
            y = "mulhsu"
            self.mulhsu = True
            x = x[len(y) + 1:]
            return x
        elif "mulhu" in x:
            y = "mulhu"
            self.mulhu = True
            x = x[len(y) + 1:]
            return x
        elif "mulh" in x:
            print("In MULH")
            y = "mulh"
            self.mulh = True
            x = x[len(y) + 1:]
            return x
        elif "mul" in x:
            y = "mul"
            self.mul = True
            x = x[len(y) + 1:]
            return x
        elif "divu" in x:
            y = "divu"
            self.divu = True
            x = x[len(y) + 1:]
            return x
        elif "div" in x:
            y = "div"
            self.div = True
            x = x[len(y) + 1:]
            return x
        elif "remu" in x:
            y = "remu"
            self.remu = True
            x = x[len(y) + 1:]
            return x
        elif "rem" in x:
            y = "rem"
            self.rem = True
            x = x[len(y) + 1:]
            return x
        elif "or" in x:
            y = "or"
            self.Or = True
            x = x[len(y) + 1:]
            return x
        elif "and" in x:
            y = "and"
            self.And = True
            x = x[len(y) + 1:]
            return x
        elif "xor" in x:
            y = "xor"
            self.Xor = True
            x = x[len(y) + 1:]
            return x
        elif "sll" in x:
            y = "sll"
            self.llshift = True
            x = x[len(y) + 1:]
            return x
        elif "srl" in x:
            y = "srl"
            self.rlshift = True
            x = x[len(y) + 1:]
            return x
        elif "sra" in x:
            y = "sra"
            self.rashift = True
            x = x[len(y) + 1:]
            return x
        elif "sltu" in x:
            y = "sltu"
            self.sltu = True
            x = x[len(y) + 1:]
            return x
        elif "slt" in x:
            y = "slt"
            self.slt = True
            x = x[len(y) + 1:]
            return x
        else:
            return x

    def getsd(self, x):
        x = x.replace(" ", "")
        self.dest, self.src1, self.src2 = x.split(",")
        res = self.getexecute()
        print(res)
        if 'Divide by zero error encountered' in res:
            return res
        else:
            return res

    def getexecute(self):

        print(self.val)

        self.src1 = self.src1[1:]
        self.src2 = self.src2[1:]
        temp = self.dest.find("x")
        self.dest = self.dest[temp+1:]

        self.indexs1 = int(self.src1)
        self.indexs2 = int(self.src2)
        self.indexd = int(self.dest)

        instructions.Instruction_type.indexs1 = self.indexs1
        instructions.Instruction_type.indexs2 = self.indexs2
        instructions.Instruction_type.indexd = self.indexd

        if self.add:
            res = self.adder()
            return res
        elif self.sub:
            res = self.subtractor()
            return res
        elif self.mul:
            res = self.multi()
            return res
        elif self.mulh:
            res = self.multh()
            return res
        elif self.mulhu:
            res = self.multhu()
            return res
        elif self.mulhsu:
            res = self.multhsu()
            return res
        elif self.div:
            res = self.divide()
            if 'Divide by zero error encountered' in res:
                return res
            else:
                return res
        elif self.divu:
            print('This is DIVU')
            res = self.divideu()
            if 'Divide by zero error encountered' in res:
                return res
            else:
                return res
        elif self.rem:
            res = self.remainder()
            if 'Divide by zero error encountered' in res:
                return res
            else:
                return res
        elif self.remu:
            res = self.remainderu()
            if 'Divide by zero error encountered' in res:
                return res
            else:
                return res
        elif self.Or:
            res = self.Oroperator()
            return res
        elif self.And:
            res = self.Andoperator()
            return res
        elif self.Xor:
            res = self.Xoroperator()
            return res
        elif self.llshift:
            res = self.slloperator()
            return res
        elif self.rlshift:
            res = self.srloperator()
            return res
        elif self.rashift:
            res = self.sraoperator()
            return res
        elif self.slt:
            res = self.sltreg()
            return res
        elif self.sltu:
            res = self.sltunsigned()
            return res
        else:
            print("wrong instruction")

    def adder(self):
        temp = self.val[self.indexs1]
        print(temp)
        temp1 = self.val[self.indexs2]
        print(temp1)
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def subtractor(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp - temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def multi(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp * temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'
    def multh(self):
        print("In MULH")
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp * temp1
        if temp < 0:
            n = temp + 2 ** 64
            print(n)
            binary = '{0:064b}'.format(n)
            print(binary)
            binary = binary[0:32]
            temp = int(binary, 2)
            temp = temp - 2 ** 32
        else:
            binary = '{0:064b}'.format(temp)
            print(binary)
            binary = binary[0:32]
            temp = int(binary, 2)
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'
    def multhu(self):
        print("In MULHU")
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp < 0:
            temp = self.val[self.indexs1] + 2 ** 32
            print("This is temp unsigned " + str(temp))
        if temp1 < 0:
            temp1 = self.val[self.indexs2] + 2 ** 32
            print("This is temp1 unsigned " + str(temp1))
        temp = temp * temp1
        binary = '{0:064b}'.format(temp)
        print(binary)
        binary = binary[0:32]
        temp = int(binary, 2)
        print("This is temp " + str(temp))
        if temp > 2047:
            temp = temp - 2 ** 32
            print("This is temp1 " + str(temp))
            self.val[self.indexd] = temp
        else:
            print("This is temp2 " + str(temp))
            self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'
    def multhsu(self):
        print("In MULHU")
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp1 < 0:
            temp1 = self.val[self.indexs2] + 2 ** 32
        temp = temp * temp1
        if temp < 0:
            n = temp + 2 ** 64
            print(n)
            binary = '{0:064b}'.format(n)
            print(binary)
            print(len(binary))
            binary = binary[0:32]
            temp = int(binary, 2)
            temp = temp - 2 ** 32
            print(temp)
            self.val[self.indexd] = temp
        else:
            binary = '{0:064b}'.format(temp)
            print(binary)
            binary = binary[0:32]
            temp = int(binary, 2)
            if temp > 2047:
                temp = temp - 2 ** 32
                self.val[self.indexd] = temp
            else:
                self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def divide(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp1 != 0:
            temp = temp / temp1
            self.val[self.indexd] = int(temp)
            print(self.val)
            return 'No error'
        else:
            return 'Divide by zero error encountered in DIV'
    def divideu(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp < 0 or temp1 < 0:
            temp = self.val[self.indexs1] + 2 ** 32
            temp1 = self.val[self.indexs2] + 2 ** 32
        if temp1 != 0:
            temp = temp / temp1
            self.val[self.indexd] = int(temp)
            print(self.val)
            return 'No error'
        else:
            return 'Divide by zero error encountered in DIV'


    def remainder(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp1 != 0:
            temp = temp % temp1
            self.val[self.indexd] = temp
            print(self.val)
            return 'No Error'
        else:
            return 'Divide by zero error encountered in REM'
    def remainderu(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp < 0 or temp1 < 0:
            temp = self.val[self.indexs1] + 2 ** 32
            temp1 = self.val[self.indexs2] + 2 ** 32
        if temp1 != 0:
            temp = temp % temp1
            self.val[self.indexd] = int(temp)
            print(self.val)
            return 'No Error'
        else:
            return 'Divide by zero error encountered in REM'


    def Oroperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp | temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def Andoperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp & temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def Xoroperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp ^ temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def slloperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp << temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def srloperator(self):
        temp = self.val[self.indexs1]
        temp = temp + (2 ** 32)
        temp1 = self.val[self.indexs2]
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def sraoperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        # ones = ~temp
        # twos = ones + 1
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)
        return 'No Error'

    def sltreg(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp < temp1:
            self.val[self.indexd] = 1
        else:
            self.val[self.indexd] = 0
        print(self.val)
        return 'No Error'

    def sltunsigned(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        if temp1 < 0:
            temp1 = temp1 * (-1)
        if temp < temp1:
            self.val[self.indexd] = 1
        else:
            self.val[self.indexd] = 0
        print(self.val)
        return 'No Error'