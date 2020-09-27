import re

#######################################
# OPCODES
#######################################
lex_tok = set()
# I EXTENSION OPCODES:
r_ins = ['add', 'sub', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
i_ins = ['slli', 'srli', 'srai', 'addi', 'subi', 'muli', 'divi', 'remi', 'xori', 'andi', 'ori', 'slti', 'sltiu',
         'fence', 'fence.i', 'scall', 'sbreak', 'jalr']
sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
s_ins = ['sb', 'sh', 'sw']
load = ['lw', 'lb', 'lh', 'lbu', 'lhu']
u_ins = ['lui', 'auipc']
uj_ins = ['jal']
# C EXTENSION OPCODES:
cr_ins = ['c.add', 'c.addw', 'c.mv', 'c.sub', 'c.jr', 'c.jalr']
ci_ins = ['c.addi', 'c.addiw', 'c.addi16sp', 'c.addi4spn', 'c.li', 'c.lui', 'c.slli']
c_load = ['c.lw', 'c.lwsp', 'c.ld', 'c.ldsp', 'c.lq', 'c.lqsp']
cs_ins = ['c.sw', 'c.sd', 'c.sq']
css_ins = ['c.swsp', 'c.sdsp', 'c.sqsp']
cb_ins = ['c.beqe', 'c.bnez']
c_jump = ['c.j', 'c.jr', 'c.jal', 'c.jalr']
c_system = ['c.ebreak']
#######################
f_label = r'(^([a-zA-Z])([a-zA-Z0-9]+)?)'
num_label = r'[0-9]+(b|f)'
label = r'(^([a-zA-Z])([a-zA-Z0-9]+)?):'
lparen = "("
rparen = ")"

reg = []
for i in range(0, 32):
    reg.append('x' + str(i))
IMM = r'^-?[0-9]\d*(\.\d+)?$'

#######################################
# TOKENS
#######################################
TT_RTYPE = 'RTYPE'
TT_ITYPE = 'ITYPE'
TT_UJTYPE = 'UJTYPE'
TT_SBTYPE = 'SBTYPE'
TT_STYPE = 'STYPE'
TT_LOAD = 'LOAD'
TT_UTYPE = 'UTYPE'
TT_CRTYPE = 'C_RTYPE'
TT_CITYPE = 'C_ITYPE'
TT_CIWTYPE = 'C_IWTYPE'
TT_CJTYPE = 'C_JTYPE'
TT_CBTYPE = 'C_BTYPE'
TT_CSTYPE = 'C_STYPE'
TT_CSSTYPE = 'C_SSTYPE'
TT_CLOAD = 'C_LOAD'
TT_FLABEL = 'FLABEL'
TT_REG = 'REG'
TT_IMM = 'IMM'
TT_LABEL = 'LABEL'
TT_ERROR = 'ERROR'
TT_LPAREN = '('
TT_RPAREN = ')'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'


#######################################
# Lexer
#######################################


class Lexer1:
    def __init__(self, text, end):
        self.text = text
        self.label_rec = []
        self.flabel_rec = []
        self.count = []
        self.data = []
        self.temp = ''
        self.line_no = 0
        self.end = end
        self.track = 0
        self.error = None
        self.code = []
        self.reg_name = {'x0': 'zero', 'x1': 'ra', 'x2': 'sp', 'x3': 'gp', 'x4': 'tp', 'x5': 't0'
            , 'x6': 't1', 'x7': 't2', 'x8': ('s0', 'fp'), 'x9': 's1', 'x10': 'a0'
            , 'x11': 'a1', 'x12': 'a2', 'x13': 'a3', 'x14': 'a4', 'x15': 'a5', 'x16': 'a6',
                         'x17': 'a7', 'x18': 's2', 'x19': 's3', 'x20': 's4', 'x21': 's5', 'x22': 's6', 'x23': 's7'
            , 'x24': 's8', 'x25': 's9', 'x26': 's10', 'x27': 's11', 'x28': 't3', 'x29': 't4', 'x30': 't5', 'x31': 't6'}

    def tokenize(self, text, line_no):
        token = []
        self.line_no = line_no
        self.data = []

        temp_word = ''
        '''self.temp = text.replace(',', ' ')
        self.temp = self.temp.replace('(', ' ')
        self.temp = self.temp.replace(')', ' ')
        self.data = self.temp.split()'''
        text.strip()
        for i in range(len(text)):
            if text[i] == ' ':
                self.data.append(temp_word)
                temp_word = ''
                # print(temp_word)
            elif text[i] == ',':
                self.data.append(temp_word)
                temp_word = ''
                # print(temp_word)
            elif text[i] == '(':
                self.data.append(temp_word)
                self.data.append(text[i])
                # print(temp_word)
                temp_word = ''
                # print(temp_word)
            elif text[i] == ')':
                self.data.append(temp_word)
                self.data.append(text[i])
                temp_word = ''
                # print(temp_word)
            elif i == (len(text) - 1):
                temp_word = temp_word + text[i]
                self.data.append(temp_word)
                # print(temp_word)
            else:
                temp_word = temp_word + text[i]

        token, self.error, self.label_rec, self.code = self.build_tokens()
        return token, self.error, self.label_rec, self.code

    def build_tokens(self):
        token = []
        tok = ''

        for i in range(len(self.data)):
            imm_pattern = re.match(IMM, self.data[i])
            label_pattern = re.match(label, self.data[i])
            flabel_pattern = re.match(f_label, self.data[i])
            if self.data[i] in self.reg_name.values():
                self.data[i] = list(self.reg_name.keys())[list(self.reg_name.values()).index(self.data[i])]

            if self.data[i] == ' \n':
                pass
            elif self.data[i] == lparen:
                token.append(Token(TT_LPAREN))
            elif self.data[i] == rparen:
                token.append(Token(TT_RPAREN))
            # TOKENS FOR I EXTENSION
            elif self.data[i] in i_ins:
                token.append(Token(TT_ITYPE))
            elif self.data[i] in r_ins:
                token.append(Token(TT_RTYPE))
            elif self.data[i] in reg:
                token.append(Token(TT_REG, self.data[i]))
            elif imm_pattern:
                token.append(Token(TT_IMM, self.data[i]))
            elif self.data[i] in load:
                token.append(Token(TT_LOAD))
            elif self.data[i] in s_ins:
                token.append(Token(TT_STYPE))
            elif self.data[i] in u_ins:
                token.append(Token(TT_UTYPE))
            elif self.data[i] in uj_ins:
                token.append(Token(TT_UJTYPE))
            elif self.data[i] in s_ins:
                token.append(Token(TT_STYPE))
            # TOKENS FOR C EXTENSION #####################
            elif self.data[i] in cr_ins:
                token.append(Token(TT_CRTYPE))
            elif self.data[i] in ci_ins:
                token.append(Token(TT_CITYPE))
            elif self.data[i] in c_load:
                token.append(Token(TT_CLOAD))
            elif self.data[i] in cs_ins:
                token.append(Token(TT_CSTYPE))
            elif self.data[i] in css_ins:
                token.append(Token(TT_CSSTYPE))
            elif self.data[i] in cb_ins:
                token.append(Token(TT_CBTYPE))
            elif self.data[i] in c_jump:
                token.append(Token(TT_CJTYPE))

            elif label_pattern:
                token.append(Token(TT_LABEL))
                latex = self.data[i]
                self.label_rec.append(latex[:-1])
            elif flabel_pattern:
                token.append(Token(TT_FLABEL, self.data[i]))
                self.flabel_rec.append(self.data[i])
                self.count.append(self.line_no)
            ##############################################
            else:
                return [], InvalidInstruction(self.line_no).as_string(), None, None
        self.track += 1

        return token, None, self.label_rec, self.data


#######################################
# ERROR
#######################################
class Error:
    def __init__(self, err_msg, line_no):
        self.err_msg = err_msg
        self.line_no = line_no

    def as_string(self):
        result = f'{self.err_msg} in Line Number {self.line_no}'
        return result


class InvalidInstruction(Error):
    def __init__(self, line_no):
        super().__init__('Invalid Instruction', line_no)


class LabelNotFound(Error):
    def __init__(self, line_no, track):
        super().__init__(f'(Label: "{track}") not found ', line_no)


class InvalidSyntax(Error):
    def __init__(self, line_no):
        super().__init__('Invalid Syntax', line_no)


class ImmediateOutOfRange(Error):
    def __init__(self, line_no, track):
        super().__init__(f'Immediate Value("{track}") is out of range. '
                         f'Value should be in between -2048 and 2047', line_no)


####################################
# PARSER
####################################
class Parser:
    def __init__(self, data, label_list, code):
        self.data = data
        self.code = code
        self.label_list = label_list
        self.errorp = None

    def grammer_selection(self):
        for i in range(len(self.data)):
            # I EXTENSION #######################################################################
            if self.data[i][0].type == TT_RTYPE:
                self.errorp = self.RType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_ITYPE:
                self.errorp = self.IType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_UJTYPE:
                self.errorp = self.UJType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_UTYPE:
                self.errorp = self.UType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_SBTYPE:
                self.errorp = self.SBType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_STYPE or self.data[i][0] == TT_LOAD:
                self.errorp = self.SType_grammar(self.data[i], i + 1)
            # C EXTENSION #######################################################################
            elif self.data[i][0].type == TT_CSTYPE or self.data[i][0] == TT_CLOAD:
                self.errorp = self.CSType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_CRTYPE:
                self.errorp = self.CRType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_CITYPE:
                self.errorp = self.CIType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_CBTYPE:
                self.errorp = self.CBType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_CSSTYPE:
                self.errorp = self.CSSType_grammar(self.data[i], i + 1)
            elif self.data[i][0].type == TT_CJTYPE:
                self.errorp = self.CJType_grammar(self.data[i], i + 1)
            #######################################################################################
            elif self.data[i][0].type == TT_LABEL:
                self.errorp = self.Label_grammer(self.data[i], i + 1)
            elif self.data[i][0].type == TT_REG or self.data[i][0].type == TT_IMM:
                self.errorp = InvalidSyntax(i + 1).as_string()
            elif self.data[i][0].type == TT_FLABEL:
                self.errorp = InvalidInstruction(i + 1).as_string()
            elif self.errorp:
                return self.errorp, self.code
        return self.errorp, self.code

    # RV32I INSTRUCTIONS : ##################################################################

    def RType_grammar(self, inst, line_no):
        if len(inst) < 4:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 4:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_REG or inst[3].type != TT_REG:
            return InvalidSyntax(line_no).as_string()

    def IType_grammar(self, inst, line_no):
        if len(inst) < 4:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 4:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_REG or inst[3].type != TT_IMM:
            return InvalidSyntax(line_no).as_string()
        elif inst[3].type == TT_IMM and (-2048 > int(inst[3].value) or int(inst[3].value) > 2047):
            return ImmediateOutOfRange(line_no, inst[3].value).as_string()

    def UJType_grammar(self, inst, line_no):
        if len(inst) < 2:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 3:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) == 2:
            if inst[1].type != TT_FLABEL:
                return InvalidSyntax(line_no).as_string()
            elif inst[1].value not in self.label_list:
                return [], LabelNotFound(line_no, inst[1].value).as_string()
        elif len(inst) == 3:
            if inst[1].type != TT_REG or inst[2].type != TT_FLABEL:
                return InvalidSyntax(line_no).as_string()
            elif inst[2].value not in self.label_list:
                return [], LabelNotFound(line_no, inst[2].value).as_string()

    def SBType_grammar(self, inst, line_no):
        if len(inst) < 4:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 4:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_REG or inst[3].type != TT_FLABEL:
            return InvalidSyntax(line_no).as_string()

    def SType_grammar(self, inst, line_no):
        if len(inst) < 6:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 6:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_IMM or inst[3].type != TT_LPAREN or inst[4].type != TT_REG or \
                inst[5].type != TT_RPAREN:
            return InvalidSyntax(line_no).as_string()

    def UType_grammar(self, inst, line_no):
        if len(inst) < 3:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 3:
            return InvalidSyntax(line_no).as_string()
        if inst[1].type != TT_REG or inst[2].type != TT_IMM:
            return InvalidSyntax(line_no).as_string()

    # RV32E INSTRUCTIONS ###################################################################################
    def CRType_grammar(self, inst, line_no):
        if len(inst) < 3:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 3:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_REG:
            return InvalidSyntax(line_no).as_string()

    def CIType_grammar(self, inst, line_no):
        if len(inst) < 3:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 3:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_IMM:
            return InvalidSyntax(line_no).as_string()
        elif inst[2].type == TT_IMM and (-2048 > int(inst[2].value) or int(inst[2].value) > 2047):
            return ImmediateOutOfRange(line_no, inst[2].value).as_string()

    def CSType_grammar(self, inst, line_no):
        if len(inst) < 6:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 6:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_IMM or inst[3].type != TT_LPAREN or inst[4].type != TT_REG or \
                inst[5].type != TT_RPAREN:
            return InvalidSyntax(line_no).as_string()

    def CSSType_grammar(self, inst, line_no):
        if len(inst) < 3:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 3:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_IMM:
            return InvalidSyntax(line_no).as_string()
        elif inst[2].type == TT_IMM and (-2048 > int(inst[3].value) or int(inst[3].value) > 2047):
            return ImmediateOutOfRange(line_no, inst[3].value).as_string()

    def CBType_grammar(self, inst, line_no):
        if len(inst) < 3:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 3:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_REG or inst[2].type != TT_FLABEL:
            return InvalidSyntax(line_no).as_string()

    def CJType_grammar(self, inst, line_no, label_list):
        if len(inst) < 2:
            return InvalidSyntax(line_no).as_string()
        elif len(inst) > 2:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].type != TT_FLABEL:
            return InvalidSyntax(line_no).as_string()
        elif inst[1].value not in self.label_list:
            return [], LabelNotFound(line_no, inst[1].value).as_string()

    def Label_grammer(self, inst, line_no):
        if len(inst) > 1:
            return InvalidSyntax(line_no).as_string()


####################################
# RUN
####################################
# text = 'addi x3,x0,12\n' \
#        'addi x5,x0,13\n' \
#        'jal label\n' \
#        'addi x7,x0,14\n' \
#        'label:\n' \
#        'addi x2,x5,13'
# tokens = []
# count = 0
# data = text.split('\n')
# err_p = None
# lexer = Lexer1(data, len(data))
# label_list = []
#
# for i in range(len(data)):
#     tok, err, label_list, single_ins = lexer.tokenize(data[i], i + 1)
#     if err:
#         print(err)
#         break
#     else:
#         print(tok)
#         tokens.append(tok)
#         parser = Parser(tokens, label_list, single_ins)
#         err_p = parser.grammer_selection()
#         if err_p:
#             print(err_p)

# print(res)'''
