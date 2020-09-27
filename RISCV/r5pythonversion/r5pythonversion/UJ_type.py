from .instructions import Instruction_type

import sys


class JumpIns(Instruction_type):
    def __init__(self, ins, next_pc, code_line, whole_code, label_address):
        self.ins = ins
        self.next_pc = next_pc
        self.code_line = code_line
        self.ins_list = code_line
        self.whole_code = whole_code
        self.ins_split = []
        self.label_address = label_address

    def split_inst(self):
        self.code_line = self.ins.replace(',', ' ')
        # self.code_line = self.code_line.replace('(', ' ')
        # self.code_line = self.code_line.replace(')', ' ')
        self.ins_split = self.code_line.split()

    def jal_op(self):
        l_count = 0
        label_add = 0
        y = self.ins[4:]  # ins = x
        nxt = self.next_pc + 1  # next_pc = vari
        track = self.next_pc
        if len(self.ins_split) == 2:
            Instruction_type.val[1] = nxt * 4
        else:
            ret_add = self.ins_split[1]  # register in which the return address will be saved
            ret_add = int(ret_add[1:])
            Instruction_type.val[ret_add] = nxt * 4

        jal_c = 0
        print("label address")
        print(self.label_address)
        for key in self.label_address:
            if y in key:
                label_add = self.label_address[key]
        print("value of x1: " + str(nxt))
        print("track:", track)
        if label_add > track:
            while track != label_add:
                if ':' not in self.ins_list[track]:
                    print("instruction : ", self.ins_list[track])
                    l_count += 1
                track += 1
            jal_c = l_count
        elif label_add < track:       #not working properly
            while track != label_add:
                if ':' not in self.code_line[track]:
                    l_count -= 1
                track -= 1
            jal_c = l_count

        '''for j in range(len(code_line)):
            if j > vari and ':' in code_line[j]:
                l_count += 1
            if y in code_line[j] and (not ('jal' in code_line[j])):
                # code_line[j] = code_line[j].split(":")
                if j
                vari = j + 1
                jal_c = (vari + 1) - (nxt + l_count)'''
        return track, jal_c

    def jalr_op(self):
        # offset = int(self.ins_split[2])
        print(self.ins_split)
        source_reg = self.ins_split[2]
        source_reg = int(source_reg[1:])  # source register
        print("Source Register is " + str(source_reg))
        jump_add = (int(self.ins_split[3]) + Instruction_type.val[source_reg]) / 4  # calculating jump address

        nxt = self.next_pc + 1  # next_pc = vari
        ret_add = self.ins_split[1]  # register in which the return address will be saved
        ret_add = int(ret_add[-1])
        Instruction_type.val[ret_add] = nxt * 4
        if jump_add > len(self.code_line) - 1:
            sys.exit()
        else:
            return int(jump_add)
