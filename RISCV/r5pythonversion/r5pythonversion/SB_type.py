from .instructions import Instruction_type


class SB_type(Instruction_type):
    ins_word = []
    op1 = 0
    op2 = 0
    rs1 = ''
    rs2 = ''
    track = False

    def split_inst(self,ins):
        ins = ins.replace(',', ' ')
        self.ins_word = ins.split()
        return self.ins_word
    def op_select(self):
        #self.ins_word = self.split_inst(ins)
        self.rs1 = self.ins_word[1]
        self.op1 = int(self.rs1[1:])
        self.rs2 = self.ins_word[2]
        self.op2 = int(self.rs2[1:])
        if self.ins_word[0] == 'beq':
            track = self.beq_op()
        elif self.ins_word[0] == 'bne':
            track = self.bne_op()
        elif self.ins_word[0] == 'blt':
            track = self.blt_op()
        elif self.ins_word[0] == 'bge':
            track = self.bge_op()
        elif self.ins_word[0] == 'bltu':
            track = self.bltu_op()
        elif self.ins_word[0] == 'bgeu':
            track = self.bgeu_op()
        return track, self.ins_word[3]
    def beq_op(self):
        if self.val[self.op1] == self.val[self.op2]:
            return True
        return False
    def bne_op(self):
        if self.val[self.op1] != self.val[self.op2]:
            return True
        return False
    def blt_op(self):
        if self.val[self.op1] < self.val[self.op2]:
            return True
        return False
    def bge_op(self):
        if self.val[self.op1] >= self.val[self.op2]:
            return True
        return False
    def bltu_op(self):
        if self.val[self.op1] < abs(self.val[self.op2]):
            return True
        return False
    def bgeu_op(self):
        if self.val[self.op1] >= abs(self.val[self.op2]):
            return True
        return False

