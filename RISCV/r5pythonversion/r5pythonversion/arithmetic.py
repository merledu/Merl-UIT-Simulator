import random


class Arithmetic(object):
    src1 = ""
    src2 = ""
    dest = ""
    indexs1 = 0
    indexs2 = 0
    indexd = 0
    val = []
    offset=""
    offset_val=0
    offset_shitf=1
    for i in range(0, 32):
        val.append(random.randint(1, 100))
    memory_block = []

    list=[]
    for y in range(0, 512):
        list.append(random.randint(3, 9))

    mydix = {}

    for x in range(0, 512):
        # key=input('Enter Key ')
        mydix[hex(x)] = list[x]
        # print(mydix)

    #Need To Be Updat
    listkey = []
    #*mydix

    listvalue = []
    listvalue = []

    #*mydix.values()


    #print(mydix)
    #print(listkey)
    #for x in range(0, 512):
        #memory_block.append(random.randint(1, 7000))


class R_type(Arithmetic):



    rem = False
    sub = False
    add = False
    div = False
    mul = False
    Or = False
    And = False
    Xor = False
    llshift = False   #left logical shift
    rlshift = False    #right logical shift
    rashift = False    #right arithmetic shift





    def getoperator(self, x):
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
        elif "mul" in x:
            y = "mul"
            self.mul = True
            x = x[len(y) + 1:]
            return x
        elif "div" in x:
            y = "div"
            self.div = True
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
        else:
            return x

    def getsd(self, x):
        x = x.replace(" ", "")
        self.dest, self.src1, self.src2 = x.split(",")
        self.getexecute()

    def getexecute(self):

        print(self.val)

        self.src1 = self.src1[1:]
        self.src2 = self.src2[1:]
        self.dest = self.dest[1:]

        self.indexs1 = int(self.src1)
        self.indexs2 = int(self.src2)
        self.indexd = int(self.dest)

        Arithmetic.indexs1 = self.indexs1
        Arithmetic.indexs2 = self.indexs2
        Arithmetic.indexd = self.indexd


        if self.add:
            self.adder()
        elif self.sub:
            self.subtractor()
        elif self.mul:
            self.multi()
        elif self.div:
            self.divide()
        elif self.rem:
            self.remainder()
        elif self.Or:
            self.Oroperator()
        elif self.And:
            self.Andoperator()
        elif self.Xor:
            self.Xoroperator()
        elif self.llshift:
            self.slloperator()
        elif self.rlshift:
            self.srloperator()
        elif self.rashift:
            self.sraoperator()
        else:
            print("wrong instruction")

    def adder(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp + temp1
        self.val[self.indexd] = temp
        print(self.val)

    def subtractor(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp - temp1
        self.val[self.indexd] = temp
        print(self.val)

    def multi(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp * temp1
        self.val[self.indexd] = temp
        print(self.val)

    def divide(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp / temp1
        self.val[self.indexd] = temp
        print(self.val)

    def remainder(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp % temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Oroperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp | temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Andoperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp & temp1
        self.val[self.indexd] = temp
        print(self.val)

    def Xoroperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp ^ temp1
        self.val[self.indexd] = temp
        print(self.val)

    def slloperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp << temp1
        self.val[self.indexd] = temp
        print(self.val)

    def srloperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)

    def sraoperator(self):
        temp = self.val[self.indexs1]
        temp1 = self.val[self.indexs2]
        ones = ~temp
        twos = ones + 1
        temp = twos >> temp1
        self.val[self.indexd] = temp
        print(self.val)


class I_type(Arithmetic):



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
    rashifti = False    # right arithmetic immediate shift



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
        elif "ld" in x:
            y = "ld"
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
        else:
            return x

    def getsdi(self, x):
        x = x.replace(" ", "")
        self.dest, self.src1, self.src2 = x.split(",")
        self.getexecute()

    def getsdl(self,x):
        x = x.replace(" ","")
        x = x.replace("[","")
        x = x.replace("]", "")

        self.dest, self.src1 = x.split(",")

        #
        counter=0
        a=self.src1
        #print(a)

        for x1 in a:
            if(x1=='x' or counter==1):
                counter=1
                break
            else:
                #Problem
                a=a[1:]
                #problem END
                self.offset_shitf=self.offset_shitf+1
                self.offset=self.offset+x1
        #
        print(self.offset)
        print(self.src1)
        print(self.dest)
        self.getexecute()


    def getexecute(self):

        print(self.val)
        #self.src1 = self.src1[1:]
        #self.src1 = self.src1[2:]
        #print(self.src1)

        self.src1 = self.src1[self.offset_shitf:]
        self.dest = self.dest[1:]

        if self.load:
            self.offset_val = int(self.offset)
            print(self.offset_val)
            self.indexs1 = int(self.src1)
            #self.indexs1 = int(self.src1)
            self.indexd = int(self.dest)
        else:
            self.indexs1 = int(self.src1)
            self.indexs2 = int(self.src2)
            self.indexd = int(self.dest)

        Arithmetic.indexs1 = self.indexs1
        Arithmetic.indexs2 = self.indexs2
        Arithmetic.indexd = self.indexd


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
            self.loadd(self.val[self.indexs1]+self.offset_val)
            #self.loadd(self.val[self.indexs1])
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

    def loadd(self,res):
    #print(self.mydix)

        file_values=open("templates/m.txt","r")
        #print(file_values.readable())

        list=[]
        for x in range(0,512):
            list.append(file_values.readline())
        file_values.close()
        #print(list)
        list1=[]
        for x in list:
            list1.append(x.replace('\n',''))
        #new_set = {x.replace('\n', '') for x in list}
        #print(list1)
        memory_block={}
        for x in range(0,512):
            memory_block[hex(x)]=list1[x]



        value=int(memory_block.get(hex(res)))
        #mydix.get up
        #value =self.memory_block[res]
        self.val[self.indexd] = value
        print(self.val[self.indexd])
        print(self.val)
        print(self.indexd)

        #self.updatememory()
        #print(self.memory_block)
        #print(self.memory_block[self.val[self.indexs1]])
        #print(self.val)

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
        temp1 = self.indexs2
        temp = temp >> temp1
        self.val[self.indexd] = temp
        print(self.val)

    def sraoperatori(self):
        temp = self.val[self.indexs1]
        temp1 = self.indexs2
        ones = ~temp
        twos = ones + 1
        temp = twos >> temp1
        self.val[self.indexd] = temp
        print(self.val)


class S_type(Arithmetic):

    storew = False

    def getoperators(self, x):

        if "sw" in x:
            y = "sw"
            self.storew = True
            x = x[len(y) + 1:]
            return x
        else:
            return x

    def getsds(self, x):
        x = x.replace(" ", "")
        x = x.replace("[", "")
        x = x.replace("]", "")

        self.dest, self.src1 = x.split(",")

        ###########################
        counter=0
        a=self.src1
        print(a)

        for x1 in a:
            if(x1=='x' or counter==1):
                counter=1
                break
            else:
                #Problem
                a=a[1:]
                #problem END
                self.offset_shitf=self.offset_shitf+1
                self.offset=self.offset+x1
        #
        print(self.offset)
        ###########################
        self.getexecute()

    def getexecute(self):

        print(self.val)
        self.src1 = self.src1[self.offset_shitf:]
        self.offset_val=int(self.offset)
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

        Arithmetic.indexs1 = self.indexs1
        Arithmetic.indexs2 = self.indexs2
        Arithmetic.indexd = self.indexd

        if self.storew:
            self.stored(self.val[self.indexd]+self.offset_val)
        else:
            print("wrong instruction")

    def stored(self,res):
        print("result",res)
        print(self.indexs1)
        #self.memory_block[self.val[self.indexd]] = self.val[self.indexs1]
        #self.mydix[hex(self.val[self.indexd])]=(self.val[self.indexs1])
        #self.mydix[hex(self.val[self.indexd])]=int(self.val[self.indexs1])

        self.mydix[hex(self.val[self.indexs1]+self.offset_val)] = int(self.val[self.indexd])


        filevalue1=open("templates\m.txt","w")
        for x in range(0,512):
            filevalue1.writelines(str(self.mydix.get(hex(x)))+'\n')
        filevalue1.close()



        print(self.val)
        print(self.mydix)
        print(self.mydix.get(hex(self.val[self.indexs1])))
        print("##############################")
        #print(self.memory_block[self.val[self.indexs1]])
        #print(self.val)

