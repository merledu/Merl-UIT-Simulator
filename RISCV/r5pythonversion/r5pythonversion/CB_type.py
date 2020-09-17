from .instructions import Instruction_type

class CB_type(Instruction_type):
    ins_word = []
    op1 = 0
    rs1 = ''
    track = False

    def CB_split_inst(self,ins):
        ins = ins.replace(',', ' ')
        self.ins_word = ins.split()
        return self.ins_word
    def CB_op_select(self):
        #self.ins_word = self.split_inst(ins)
        self.rs1 = self.ins_word[1]
        self.op1 = int(self.rs1[1:])
        if self.ins_word[0] == 'c.beqz':
            self.track = self.cb_beqz_op()
        elif self.ins_word[0] == 'c.bnez':
            self.track = self.cb_bnez_op()
        return self.track, self.ins_word[2]
    def cb_beqz_op(self):
        if self.val[self.op1] == 0:
            return True
        return False
    def cb_bnez_op(self):
        if self.val[self.op1] != 0:
            return True
        return False
