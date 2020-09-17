
from django.shortcuts import render
from . import instructions
from . import Interpreter
from . import InterpreterIM

class Base:
    param = {}
    param1 = {}
    param12 = {}
    stack_register = []
    memory_list1 = []
    memory_list2 = []
    memory_list3 = []
    memory_list4 = []
    ins_number = []
    status = "False"
    base_address = 0
    jal_imm = {}
    j_count = 0
    code_line1 = []
    error = ""
    lui_imm = 0
    aui_imm = 0
    label_address = {}
    whole_code = ""
    ins_type = []
    destination = []
    source1 = []
    source2 = []
    immediate1 = []
    immediate2 = []
    opcode = []
    func7 = []
    func3 = []
    func2 = []
    func4 = []
    func6 = []
    ##### List for Dump Functionality  #####
    dump_bin = []
    vari = 0
    pc = []
    nxt = 0
    next = 0
    length = 0
    data = []
    reg_name = ['x0(zero)', 'x1(ra)', 'x2(sp)', 'x3(gp)', 'x4(tp)',
                'x5(t0)', 'x6(t1)', 'x7(t2)', 'x8(s0)', 'x9(s1)', 'x10(a0)', 'x11(a1)', 'x12(a2)', 'x13(a3)', 'x14(a4)',
                'x15(a5)', 'x16(a6)', 'x17(a7)', 'x18(s2)', 'x19(s3)', 'x20(s4)', 'x21(s5)', 'x22(s6)', 'x23(s7)',
                'x24(s8)',
                'x25(s9)', 'x26(s10)', 'x27(s11)', 'x28(t3)', 'x29(t4)', 'x30(t5)', 'x31(t6)']

    list_column_1 = []
    list_column_2 = []
    list_column_3 = []
    list_column_4 = []
    listkey = []
    hex=""

def home(request):
    request.session['session'] = 0

    ##### This Is Memory Block START
    ###When using Online web
    # file_values=open("/home/OxygenUIT/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
    ###when using dedicated machine(PC)

    file_values = open("templates\m.txt", "r")
    # print(file_values.readable())
    list = []
    for x in range(0, 512):
        list.append(file_values.readline())
    # file_values.close()
    # print(list)
    list1 = []
    for x in list:
        list1.append(x.replace('\n', ''))
        # new_set = {x.replace('\n', '') for x in list}
        # print(list1)

    counter_memory_address = 0
    for x in range(0, 512):
        if (x == 512 / 4):
            break
        Base.listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
        counter_memory_address = counter_memory_address + 4

    #########################################################
    for i in range(0, 512 * 4):
        # memory_dictionary[hex(i)]=memory_value[i]
        instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(i)]
    #########################################################


    ########################################################## Memory  breaking For Views



    count_memory_break_view = 0
    for i in range(0, 514 * 4):
        if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
            break
        Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
        Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
        Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
        Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
        count_memory_break_view = count_memory_break_view + 4

    ########################################################## Memory  breaking For Views

    ########################################################## Address Division For Views
    Base.param.update({'result': "False", 'status': Base.status, 'data': zip(instructions.Instruction_type.val, Base.reg_name), 'data1': zip(Base.listkey, Base.list_column_1, Base.list_column_2, Base.list_column_3, Base.list_column_4)})

    return render(request, 'index.html', Base.param)

def interpreter(whole_code):
    code_line = [line for line in whole_code.split('\n') if line.strip() != '']
    print(code_line)
    tokens = []
    label_list = []
    single_ins = []
    code = []
    count = 0
    err = None
    err_p = None
    lexer = Interpreter.Lexer1(code_line, len(code_line))
    if len(whole_code) > 0:
        for i in range(len(code_line)):
            tok, err, label_list, single_ins = lexer.tokenize(code_line[i].strip(), i + 1)
            if err:
                print(err)
                # messages.error(request,err)
                #return 0, err, []
                return err, []

            else:
                #print(tok)
                tokens.append(tok)
                code.append(single_ins)
        parser = Interpreter.Parser(tokens, label_list, code)
        err_p, code = parser.grammer_selection()
        if err_p:
            print(err_p)
            # messages.error(request,err)
            return err_p, code
        else:
            return None, code
def interpreterIM(whole_code):
    code_line = [line for line in whole_code.split('\n') if line.strip() != '']
    print(code_line)
    tokens = []
    label_list = []
    single_ins = []
    code = []
    count = 0
    err = None
    err_p = None
    lexer = InterpreterIM.Lexer1(code_line, len(code_line))
    if len(whole_code) > 0:
        for i in range(len(code_line)):
            tok, err, label_list, single_ins = lexer.tokenize(code_line[i].strip(), i + 1)
            if err:
                print(err)
                # messages.error(request,err)
                #return 0, err, []
                return err, []

            else:
                #print(tok)
                tokens.append(tok)
                code.append(single_ins)
        parser = InterpreterIM.Parser(tokens, label_list, code)
        err_p, code = parser.grammer_selection()
        if err_p:
            print(err_p)
            # messages.error(request,err)
            return err_p, code
        else:
            return None, code

# def Display_info(request):
#     print("This is Display")
#     Base.status = "False"
#     Base.base_address = 0
#     Base.jal_imm = {}
#     Base.j_count = 0
#     Base.code_line1 = []
#     Base.error = ""
#     Base.lui_imm = 0
#     Base.aui_imm = 0
#     Base.label_address = {}
#     Base.whole_code = ""
#     Base.ins_type = []
#     Base.destination = []
#     Base.source1 = []
#     Base.source2 = []
#     Base.immediate1 = []
#     Base.immediate2 = []
#     Base.opcode = []
#     Base.func7 = []
#     Base.func3 = []
#     Base.func2 = []
#     Base.func4 = []
#     Base.func6 = []
#     Base.pc = []
#     Base.next = 0
#     Base.length = 0
#     Base.data = []
#     Base.list_column_1 = []
#     Base.list_column_2 = []
#     Base.list_column_3 = []
#     Base.list_column_4 = []
#     Base.listkey = []
#     Base.hex = ""
#     Base.vari = 0
#     Base.nxt = 0
#
#
#     request.session['session'] = 0
#     Base.whole_code = request.POST.get("editline", "")
#     #Base.whole_code = "addi x5,x0,12\r\naddi x6,x0,13"
#     print(Base.whole_code)
#     whole_code1 = Base.whole_code.replace('\r\n', '\n')
#     print(whole_code1)
#     for i in range(0, 32):
#         instructions.Instruction_type.val[i] = 0
#     if re.match("^0x", whole_code1):
#         code_line_hex = [line for line in whole_code1.split('\n') if line.strip() != '']
#         Bin = []
#         for i in range(len(code_line_hex)):
#             code_line_hex[i] = re.sub(r"^0x", '', code_line_hex[i])
#             Bin.append("{0:032b}".format(int(code_line_hex[i], 16)))
#
#         print(code_line_hex)
#         print(Bin)
#
#         opcodeh = []
#         desth = []
#         funct3h = []
#         source1h = []
#         immh = []
#         code = []
#         funct7h = []
#         for i in range(len(code_line_hex)):
#             if Bin[i][25:32] == "0010011" and Bin[i][17:20] == "000":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][:12], 2))
#                 code.append("addi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "001" and Bin[i][:7] == "0000000":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][7:12], 2))
#                 funct7h.append(int(Bin[i][:7], 2))
#                 code.append("slli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "010":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][:12], 2))
#                 code.append("slti" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "011":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][:12], 2))
#                 code.append("sltiu" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "100":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][:12], 2))
#                 code.append("xori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0000000":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][7:12], 2))
#                 funct7h.append(int(Bin[i][:7], 2))
#                 code.append("srli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0100000":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][7:12], 2))
#                 funct7h.append(int(Bin[i][:7], 2))
#                 code.append("srai" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "110":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][7:12], 2))
#                 funct7h.append(int(Bin[i][:7], 2))
#                 code.append("ori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#             elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "111":
#                 opcodeh.append(Bin[i][25:32])
#                 desth.append(int(Bin[i][20:25], 2))
#                 funct3h.append(Bin[i][17:20])
#                 source1h.append(int(Bin[i][12:17], 2))
#                 immh.append(int(Bin[i][7:12], 2))
#                 funct7h.append(int(Bin[i][:7], 2))
#                 code.append("andi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
#
#         print(desth)
#         print(source1h)
#         print(immh)
#
#         Base.data = code
#         Base.code_line1 = code
#     else:
#         print("in else")
#         error, Base.data = interpreter(whole_code1)
#         print(error)
#         if error:
#             param123 = {'error': error}
#             #Base.param.update({'result': "True", 'status1': Base.status, 'code': Base.whole_code, 'ctn': 1, 'data': zip(instructions.Instruction_type.val, Base.reg_name), 'data1': zip(Base.listkey, Base.list_column_1, Base.Base.list_column_2, Base.list_column_3, Base.list_column_4)})
#             messages.error(request, error)
#             return HttpResponse(json.dumps(param123))
#         print(Base.data)
#
#         code_line = [line for line in whole_code1.split('\n') if line.strip() != '']
#         print("Code Line =")
#         print(code_line)
#
#         Base.code_line1 = []
#         for k in range(len(code_line)):
#             if ':' not in code_line[k]:
#                 Base.code_line1.append(code_line[k])
#             else:
#                 continue
#     print(Base.code_line1)
#     r_ins = ['add', 'sub', 'mul', 'div', 'rem', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
#     i_ins = ['lw', 'lb', 'lh', 'lbu', 'lhu', 'slli', 'srli', 'srai', 'addi', 'subi', 'muli', 'divi', 'remi', 'xori',
#              'andi',
#              'ori', 'slti', 'sltiu', 'fence', 'fence.i', 'scall', 'sbreak', 'jalr']
#     sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
#     s_ins = ['sb', 'sh', 'sw']
#     u_ins = ['lui', 'auipc']
#     uj_ins = ['jal']
#     jal_immediate = []
#     ins_mem = []
#     l0 = []
#     l1 = []
#     l2 = []
#     l3 = []
#     instruction_memory_uni_counter = 0
#     print(Base.data)
#     print(len(Base.data))
#
#     print("Code Line1 =")
#     print(Base.code_line1)
#
#     for i in range(len(Base.code_line1)):
#         Base.pc.append('0x' + '{0:01X}'.format(i * 4))
#         x = Base.code_line1[i]
#         x = x.lower()
#         x = x.strip()
#         m = re.search(r'\w+', x)
#         m = m.group()
#         half_ins = x[len(m) + 1:]
#         half_ins = half_ins.replace(" ", "")
#
#         if m in i_ins:
#             Base.ins_type.append('I')
#             if 'lw' in m or 'lh' in m or 'lb' in m or 'lbu' in m or 'lhu' in m:
#                 # half_ins = re.findall(r'\w\d+|\d+', x)
#                 half_ins = re.findall(r'\d+', x)
#                 dest = half_ins[0]
#                 imm = half_ins[1]
#                 src1 = half_ins[2]
#                 imm_int = '{0:012b}'.format(int(imm))
#                 dest_int = '{0:05b}'.format(int(dest))
#                 src1_int = '{0:05b}'.format(int(src1))
#                 Base.destination.append(dest_int)
#                 Base.source1.append(src1_int)
#                 Base.immediate1.append(imm_int)
#                 Base.immediate2.append('X')
#                 Base.source2.append('X')
#                 Base.opcode.append('0000011')
#                 if 'lb' in m:
#                     Base.func3.append('000')
#                     Base.func7.append('X')
#                 elif 'lh' in m:
#                     Base.func3.append('001')
#                     Base.func7.append('X')
#                 elif 'lw' in m:
#                     Base.func3.append('010')
#                     Base.func7.append('X')
#                 elif 'lbu' in m:
#                     Base.func3.append('100')
#                     Base.func7.append('X')
#                 elif 'lhu' in m:
#                     Base.func3.append('101')
#                     Base.func7.append('X')
#
#
#
#                 ins_mem.append(
#                     str(Base.immediate1[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(Base.destination[i]) + str(Base.opcode[i]))
#             else:
#                 half_ins = re.findall(r'\d+', x)
#                 if re.match("^0x", whole_code1):
#                     dest = half_ins[0]
#                     src1 = half_ins[1]
#                     imm = half_ins[2]
#                 else:
#                     # print(Base.data[i][1])
#                     dest = Base.data[i][1]
#                     dest = dest[1:]
#                     imm = Base.data[i][3]
#                     src1 = Base.data[i][2]
#                     src1 = src1[1:]
#                 dest_int = '{0:05b}'.format(int(dest))
#                 src1_int = '{0:05b}'.format(int(src1))
#                 Base.destination.append(dest_int)
#                 Base.source1.append(src1_int)
#                 Base.immediate2.append('X')
#                 Base.source2.append('X')
#                 Base.opcode.append('0010011')
#                 if 'addi' in m:
#                     Base.func3.append('000')
#                 elif 'slli' in m:
#                     Base.func3.append('001')
#                 elif 'sltiu' in m:
#                     Base.func3.append('011')
#                 elif 'slti' in m:
#                     Base.func3.append('010')
#                 elif 'xori' in m:
#                     Base.func3.append('100')
#                 elif 'srli' in m or 'srai' in m:
#                     Base.func3.append('101')
#                 elif 'ori' in m:
#                     Base.func3.append('110')
#                 elif 'andi' in m:
#                     Base.func3.append('111')
#                 if 'slli' in m or 'srli' in m:
#                     imm_int = '{0:05b}'.format(int(imm))
#                     Base.func7.append('0000000')
#                     Base.immediate1.append(imm_int)
#                     ins_mem.append(str(Base.func7[i]) + str(Base.immediate1[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(
#                         Base.destination[i]) + str(Base.opcode[i]))
#
#                 elif 'srai' in m:
#                     imm_int = '{0:05b}'.format(int(imm))
#                     Base.func7.append('0100000')
#                     Base.immediate1.append(imm_int)
#                     ins_mem.append(str(Base.func7[i]) + str(Base.immediate1[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(
#                         Base.destination[i]) + str(Base.opcode[i]))
#
#                 else:
#                     imm_int = '{0:012b}'.format(int(imm))
#                     Base.func7.append('X')
#                     Base.immediate1.append(imm_int)
#                     ins_mem.append(
#                         str(Base.immediate1[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(Base.destination[i]) + str(Base.opcode[i]))
#             print(ins_mem)
#
#         elif m in r_ins:
#             Base.ins_type.append('R')
#             half_ins = re.findall(r'\d+', x)
#             dest = half_ins[0]
#             src1 = half_ins[1]
#             src2 = half_ins[2]
#             dest_int = '{0:05b}'.format(int(dest))
#             src1_int = '{0:05b}'.format(int(src1))
#             src2_int = '{0:05b}'.format(int(src2))
#             Base.destination.append(dest_int)
#             Base.source1.append(src1_int)
#             Base.source2.append(src2_int)
#             Base.immediate1.append('X')
#             Base.immediate2.append('X')
#             Base.opcode.append('0110011')
#             if 'add' in m or 'sub' in m:
#                 Base.func3.append('000')
#             elif 'sll' in m:
#                 Base.func3.append('001')
#             elif 'sltu' in m:
#                 Base.func3.append('011')
#             elif 'slt' in m:
#                 Base.func3.append('010')
#             elif 'xor' in m:
#                 Base.func3.append('100')
#             elif 'srl' in m or 'sra' in m:
#                 Base.func3.append('101')
#             elif 'or' in m:
#                 Base.func3.append('110')
#             elif 'and' in m:
#                 Base.func3.append('111')
#             if 'sub' in m or 'sra' in m:
#                 Base.func7.append('0100000')
#                 ins_mem.append(
#                     str(Base.func7[i]) + str(Base.source2[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(Base.destination[i]) + str(
#                         Base.opcode[i]))
#             else:
#                 Base.func7.append('0000000')
#                 ins_mem.append(
#                     str(Base.func7[i]) + str(Base.source2[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(Base.destination[i]) + str(
#                         Base.opcode[i]))
#         elif m in sb_ins:
#             Base.ins_type.append('SB')
#             half_ins = re.findall(r'\d+', x)
#             src1 = half_ins[0]
#             # imm = half_ins[2]
#             src2 = half_ins[1]
#             src1_int = '{0:05b}'.format(int(src1))
#             src2_int = '{0:05b}'.format(int(src2))
#             Base.source1.append(src1_int)
#             Base.source2.append(src2_int)
#             Base.immediate1.append('not labeled yet')
#             Base.immediate2.append('not labeled yet')
#             Base.destination.append('X')
#             Base.opcode.append('1100011')
#             Base.func7.append('X')
#             if 'beq' in m:
#                 Base.func3.append('000')
#             elif 'bne' in m:
#                 Base.func3.append('001')
#             elif 'bltu' in m:
#                 Base.func3.append('110')
#             elif 'blt' in m:
#                 Base.func3.append('100')
#             elif 'bgeu' in m:
#                 Base.func3.append('111')
#             elif 'bge' in m:
#                 Base.func3.append('101')
#             ins_mem.append('00000000000000000000000000000000')
#             # ins_mem.append(str(Base.immediate1[i]) + str(Base.source2[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(Base.immediate2[i]) + str(Base.opcode[i]))
#
#
#         elif m in s_ins:
#             Base.ins_type.append('S')
#             half_ins = re.findall(r'\d+', x)
#             src1 = half_ins[2]
#             dest = half_ins[1]
#             dest_int = int(dest) + Base.base_address
#             imm = half_ins[1]
#             src2 = half_ins[0]
#             dest_int = '{0:05b}'.format(dest_int)
#             src1_int = '{0:05b}'.format(int(src1))
#             src2_int = '{0:05b}'.format(int(src2))
#             imm_int = '{0:07b}'.format(int(imm))
#             Base.destination.append('X')
#             Base.source1.append(src1_int)
#             Base.immediate1.append(imm_int)
#             Base.immediate2.append(dest_int)
#             Base.source2.append(src2_int)
#             Base.opcode.append('0100011')
#             Base.func7.append('X')
#             if 'sb' in m:
#                 Base.func3.append('000')
#             elif 'sh' in m:
#                 Base.func3.append('001')
#             elif 'sw' in m:
#                 Base.func3.append('010')
#             ins_mem.append(
#                 str(Base.immediate1[i]) + str(Base.source2[i]) + str(Base.source1[i]) + str(Base.func3[i]) + str(Base.immediate2[i]) + str(
#                     Base.opcode[i]))
#
#         elif m in u_ins:
#             Base.ins_type.append('U')
#             half_ins = re.findall(r'\d+', x)
#             dest = half_ins[0]
#             dest_int = '{0:05b}'.format(int(dest))
#             if 'auipc' in m:
#                 Base.opcode.append('0010111')
#                 imm_int = '{0:020b}'.format(Base.aui_imm)
#                 Base.immediate1.append(imm_int)
#             else:
#                 Base.opcode.append('0110111')
#                 imm_int = '{0:020b}'.format(Base.lui_imm)
#                 Base.immediate1.append(imm_int)
#             Base.func7.append('X')
#             Base.func3.append('X')
#             Base.source1.append('X')
#             Base.source2.append('X')
#             Base.destination.append(dest_int)
#             Base.immediate2.append('X')
#             ins_mem.append(str(Base.immediate1[i]) + str(Base.destination[i]) + str(Base.opcode[i]))
#
#         elif m in uj_ins:
#             Base.ins_type.append('UJ')
#             half_ins = re.findall(r'\d+', x)
#             # dest = half_ins[0]
#             # dest_int = '{0.05b}'.format(int(dest))
#             Base.destination.append('00001')
#             Base.opcode.append('1101111')
#             for key in Base.jal_imm:
#                 if key in x:
#                     imm = Base.jal_imm[key]
#             imm_int = '{0:020b}'.format(int(imm))
#             Base.immediate1.append(imm_int)
#             Base.j_count += 1
#             # print("Value of JUMP : " + str(Base.jal_imm))
#             Base.func7.append('X')
#             Base.func3.append('X')
#             Base.source1.append('X')
#             Base.source2.append('X')
#             Base.immediate2.append('X')
#             ins_mem.append('00000000000000000000000000000000')
#             # ins_mem.append(str(Base.immediate1[i]) + str(Base.destination[i]) + str(Base.opcode[i]))
#
#         elif 'ret' in m or 'ebreak' in m:
#             Base.ins_type.append('X')
#             Base.opcode.append('X')
#             Base.func7.append('X')
#             Base.func3.append('X')
#             Base.source1.append('X')
#             Base.source2.append('X')
#             Base.destination.append('X')
#             Base.immediate2.append('X')
#             Base.immediate1.append('X')
#             ins_mem.append('00000000000000000000000000000000')
#             # ins_mem.append(str(Base.immediate1[i]) + str(Base.destination[i]) + str(Base.opcode[i]))
#         else:
#             continue
#
#
#     for k in ins_mem:
#         l3.append(k[:8])
#         l2.append(k[8:16])
#         l1.append(k[16:24])
#         l0.append(k[24:32])
#     print(l3)
#     print(l2)
#     print(l1)
#     print(l0)
#     for k in range(len(ins_mem)):
#         l3[k] = '{0:02X}'.format(int(l3[k], 2))
#         l2[k] = '{0:02X}'.format(int(l2[k], 2))
#         l1[k] = '{0:02X}'.format(int(l1[k], 2))
#         l0[k] = '{0:02X}'.format(int(l0[k], 2))
#     print(l3)
#     print(l2)
#     print(l1)
#     print(l0)
#
#     for i in range(0, len(Base.code_line1)):
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter)] = int(l0[i], 16)
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter + 1)] = int(l1[i], 16)
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter + 2)] = int(l2[i], 16)
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter + 3)] = int(l3[i], 16)
#
#         instruction_memory_uni_counter += 4
#
#     # print(Base.ins_type)
#
#     ##### This Is Memory Block START
#     ###When using Online web
#     # file_values=open("/home/OxygenUIT/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
#     ###when using dedicated machine(PC)
#
#     file_values = open("templates\m.txt", "r")
#     # print(file_values.readable())
#     list = []
#     for x in range(0, 512):
#         list.append(file_values.readline())
#     # file_values.close()
#     # print(list)
#     list1 = []
#     for x in list:
#         list1.append(x.replace('\n', ''))
#         # new_set = {x.replace('\n', '') for x in list}
#         # print(list1)
#
#     counter_memory_address = 0
#     Base.listkey = []
#     for x in range(0, 512):
#         if (x == 512 / 4):
#             break
#         Base.listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
#         counter_memory_address = counter_memory_address + 4
#
#     #########################################################
#     for i in range(0, 512 * 4):
#         # memory_dictionary[hex(i)]=memory_value[i]
#         instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(i)]
#     #########################################################
#
#     ########################################################## Memory  breaking For Views
#
#     count_memory_break_view = 0
#     for i in range(0, 514 * 4):
#         if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
#             break
#         Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
#         Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
#         Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
#         Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
#         count_memory_break_view = count_memory_break_view + 4
#
#     ########################################################## Memory  breaking For Views
#
#     ########################################################## Address Division For Views
#
#     ########################################################## Address Division For Views
#     # Base.param.update({'result': "True", 'status1': Base.status, 'code': Base.whole_code, 'data': zip(instructions.Instruction_type.val, Base.reg_name), 'data1': zip(Base.listkey, Base.list_column_1, Base.list_column_2, Base.list_column_3, Base.list_column_4), 'data3': zip(Base.pc, Base.code_line1, Base.ins_type, Base.immediate1, Base.func7, Base.source2, Base.source1, Base.func3, Base.destination, Base.immediate2, Base.opcode), 'ctn': 1})
#     # print(Base.param)
#     # return render(request, 'index.html', Base.param)
#     param123 = {'length': len(Base.code_line1), 'result': "True", 'status1': Base.status, 'code': Base.whole_code,
#                 'data': instructions.Instruction_type.val, 'list1': Base.list_column_1, 'list2': Base.list_column_2,
#                 'list3': Base.list_column_3, 'list4': Base.list_column_4, 'pc': Base.pc, 'codes': Base.code_line1,
#                 'ins_type': Base.ins_type, 'imm1': Base.immediate1, 'f7': Base.func7, 's2': Base.source2,
#                 's1': Base.source1, 'f3': Base.func3, 'dest': Base.destination, 'imm2': Base.immediate2,
#                 'opcode': Base.opcode, 'ctn': 1}
#     print(param123)
#
#     Base.stack_register.clear()
#     Base.memory_list1.clear()
#     Base.memory_list2.clear()
#     Base.memory_list3.clear()
#     Base.memory_list4.clear()
#     Base.ins_number.clear()
#
#
#     return HttpResponse(json.dumps(param123))
#
#
# def interpreter(whole_code):
#     code_line = [line for line in whole_code.split('\n') if line.strip() != '']
#     print(code_line)
#     tokens = []
#     label_list = []
#     single_ins = []
#     code = []
#     count = 0
#     err = None
#     err_p = None
#     lexer = Interpreter.Lexer1(code_line, len(code_line))
#     if len(whole_code) > 0:
#         for i in range(len(code_line)):
#             tok, err, label_list, single_ins = lexer.tokenize(code_line[i].strip(), i + 1)
#             if err:
#                 print(err)
#                 # messages.error(request,err)
#                 #return 0, err, []
#                 return err, []
#
#             else:
#                 #print(tok)
#                 tokens.append(tok)
#                 code.append(single_ins)
#         parser = Interpreter.Parser(tokens, label_list, code)
#         err_p, code = parser.grammer_selection()
#         if err_p:
#             print(err_p)
#             # messages.error(request,err)
#             return err_p, code
#         else:
#             return None, code
# def index(request):
#     result = 0
#     at_last = ''
#     whole_code = Base.whole_code
#     print(whole_code)
#     result, success = execute(whole_code)
#     if success:
#         messages.success(request, message='Code exited with 0 error!')
#         at_last = 'Code exited with 0 error!'
#
#
#     #Base.param.update({'ctn': len(Base.code_line1) + 1, 'result': "off", 'fresult': result, 'data': zip(instructions.Instruction_type.val, Base.reg_name), 'data1': zip(Base.listkey, Base.list_column_1, Base.list_column_2, Base.list_column_3, Base.list_column_4), 'data3': zip(Base.pc, Base.code_line1, Base.ins_type, Base.immediate1, Base.func7, Base.source2, Base.source1, Base.func3, Base.destination, Base.immediate2, Base.opcode)})
#     print(Base.param)
#     #Base.param1 = {'fresult': result,'data': zip(instructions.Instruction_type.val,Base.reg_name), 'data1': zip(Base.listkey,Base.list_column_1,Base.list_column_2,Base.list_column_3,Base.list_column_4)}
#     param123 = {'success': str(success), 'atlast': at_last, 'fresult': result, 'ctn': len(Base.code_line1) + 1, 'result': "off", 'status1': Base.status, 'code': Base.whole_code,
#                 'data': instructions.Instruction_type.val, 'list1': Base.list_column_1, 'list2': Base.list_column_2,
#                 'list3': Base.list_column_3, 'list4': Base.list_column_4}
#     print(param123)
#     #return render(request, 'index.html', Base.param)
#     return HttpResponse(json.dumps(param123))
#
# def execute(whole_code):
#     code_line = []
#     whole_code = whole_code.replace('\r\n', '\n')
#     code_line = [line for line in whole_code.split('\n') if line.strip() != '']
#     for i in range(0, 32):
#         instructions.Instruction_type.val[i] = 0
#
#     Base.stack_register.clear()
#     Base.memory_list1.clear()
#     Base.memory_list2.clear()
#     Base.memory_list3.clear()
#     Base.memory_list4.clear()
#     Base.ins_number.clear()
#
#     r_type = []
#     i_type = []
#     s_type = []
#     sb_type = []
#     jump_type = []
#     count_jump = 0
#     count_i = 0
#     count_r = 0
#     count_s = 0
#     count_sb = 0
#     Base.vari = 0
#     Base.nxt = 0
#     pc = 0
#     success = False
#     r_ins = ['add', 'sub', 'mul','div','rem','xor','or','and','sll','srl','sra','sltu','slt']
#     i_ins = ['slli','srli','srai','addi','subi','muli','divi','remi','xori','andi','ori','slti','sltiu','fence','fence.i','scall','sbreak']
#     sb_ins = ['beq','bne','blt','bge','bltu','bgeu']
#     jump_ins = ['jal', 'jalr']
#
#     for i in range(len(code_line)):
#         if ':' in code_line[i]:
#             Base.label_address[code_line[i]] = i
#
#     for i in range(Base.vari, len(code_line)):
#         mainting_stack(instructions.Instruction_type.val, Base.list_column_1, Base.list_column_2, Base.list_column_3,
#                        Base.list_column_4, Base.vari)
#         if Base.vari == len(code_line):
#             break
#         x = code_line[Base.vari]
#         x = x.lower()
#         x = x.strip()
#         m = re.search(r'^c.\w+|\w+', x)
#         m = m.group()
#         temp = False
#         #print(m)
#         if m in i_ins:
#             i_type.append(instructions.I_type())
#             print(len(i_type))
#             # i_type[i].val = instructions.Instruction_type.val
#             x = i_type[count_i].getoperatori(x)
#             #i_type[count_i].getsdi(x)
#             x = Base.data[i][0]
#             i_type[count_i].dest = Base.data[i][1]
#             i_type[count_i].src1 = Base.data[i][2]
#             i_type[count_i].src2 = Base.data[i][3]
#             i_type[count_i].getexecute()
#             count_i += 1
#             pc += 4
#             if Base.vari < len(code_line)-1:
#                 Base.vari += 1
#             #instructions.Instruction_type.val = i_type[i].val
#
#         elif "lw" in x:
#            i_type.append(instructions.I_type())
#            print(len(i_type))
#
#            register_num_list=re.findall(r'\d+',x)
#            print(register_num_list)
#            dest=int(register_num_list[0])
#            src1=int(register_num_list[1])
#            src2=int(register_num_list[2])
#            src2=instructions.Instruction_type.val[src2]
#            offset_for_register=src1+src2
#
#            print(offset_for_register)
#            offset_temp='{0:08X}'.format(offset_for_register)
#            offset_temp1='{0:08X}'.format(offset_for_register+1)
#            offset_temp2='{0:08X}'.format(offset_for_register+2)
#            offset_temp3='{0:08X}'.format(offset_for_register+3)
#            tem_value=[]
#            tem_value_register=0
#            #tem_value Should Be in Register
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp2))
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp3))
#
#            print(tem_value)
#
#            for values in tem_value:
#                (tem_value_register) = int(tem_value_register) + int(values)
#            instructions.Instruction_type.val[dest] = tem_value_register
#            print(instructions.Instruction_type.val)
#
#
#
#             # i_type[i].val = instructions.Instruction_type.val
#            x = i_type[count_i].getoperatori(x)
#            #i_type[count_i].getsdl(x)
#            #Stopping From Other Load
#            count_i += 1
#            pc += 4
#            if Base.vari < len(code_line)-1:
#                 Base.vari += 1
#
#         elif "lhu" in x:
#            i_type.append(instructions.I_type())
#            print(len(i_type))
#
#            register_num_list=re.findall(r'\d+',x)
#            print(register_num_list)
#            dest=int(register_num_list[0])
#            src1=int(register_num_list[1])
#            src2=int(register_num_list[2])
#            src2=instructions.Instruction_type.val[src2]
#            offset_for_register=src1+src2
#
#            offset_temp='{0:08X}'.format(offset_for_register)
#            offset_temp1='{0:08X}'.format(offset_for_register+1)
#            #tem_value Should Be in Register
#            tem_value=[]
#            tem_value_register=0
#            #tem_value Should Be in Register
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
#            print(tem_value)
#            print("Unsigned")
#            for values in tem_value:
#                tem_value_register=tem_value_register+int(values)
#                print(tem_value_register)
#                if(tem_value_register<0):
#                    instructions.Instruction_type.val[dest]= tem_value_register * -1
#                else:
#                    instructions.Instruction_type.val[dest]=tem_value_register
#                print(instructions.Instruction_type.val)
#
#
#
#
#             # i_type[i].val = instructions.Instruction_type.val
#            x = i_type[count_i].getoperatori(x)
#            #i_type[count_i].getsdl(x)
#            #Stopping From Other Load
#            count_i += 1
#            pc += 4
#            if Base.vari < len(code_line)-1:
#                 Base.vari += 1
#
#         elif "lbu" in x:
#            i_type.append(instructions.I_type())
#            print(len(i_type))
#
#            register_num_list=re.findall(r'\d+',x)
#            print(register_num_list)
#            dest=int(register_num_list[0])
#            src1=int(register_num_list[1])
#            src2=int(register_num_list[2])
#            src2=instructions.Instruction_type.val[src2]
#            offset_for_register=src1+src2
#
#            offset_temp='{0:08X}'.format(offset_for_register)
#            #tem_value Should Be in Register
#            tem_value=instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
#            print(tem_value)
#            if(int(tem_value)<0):
#                instructions.Instruction_type.val[dest]= int(tem_value) * -1
#            else:
#                instructions.Instruction_type.val[dest]=int(tem_value)
#            print(instructions.Instruction_type.val)
#
#            # i_type[i].val = instructions.Instruction_type.val
#            x = i_type[count_i].getoperatori(x)
#            #i_type[count_i].getsdl(x)
#            #Stopping From Other Load
#            count_i += 1
#            pc += 4
#            if Base.vari < len(code_line)-1:
#                 Base.vari += 1
#
#         elif "lb" in x:
#            i_type.append(instructions.I_type())
#            print(len(i_type))
#
#            register_num_list=re.findall(r'\d+',x)
#            print(register_num_list)
#            dest=int(register_num_list[0])
#            src1=int(register_num_list[1])
#            src2=int(register_num_list[2])
#            src2=instructions.Instruction_type.val[src2]
#            offset_for_register=src1+src2
#
#            offset_temp='{0:08X}'.format(offset_for_register)
#            #tem_value Should Be in Register
#            tem_value=instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
#            print(tem_value)
#            instructions.Instruction_type.val[dest]=int(tem_value)
#            print(instructions.Instruction_type.val)
#            # i_type[i].val = instructions.Instruction_type.val
#            x = i_type[count_i].getoperatori(x)
#            #i_type[count_i].getsdl(x)
#            #Stopping From Other Load
#            count_i += 1
#            pc += 4
#            if Base.vari < len(code_line)-1:
#                 Base.vari += 1
#
#         elif "lh" in x:
#            i_type.append(instructions.I_type())
#            print(len(i_type))
#
#            register_num_list=re.findall(r'\d+',x)
#            print(register_num_list)
#            dest=int(register_num_list[0])
#            src1=int(register_num_list[1])
#            src2=int(register_num_list[2])
#            src2=instructions.Instruction_type.val[src2]
#            offset_for_register=src1+src2
#
#            offset_temp='{0:08X}'.format(offset_for_register)
#            offset_temp1='{0:08X}'.format(offset_for_register+1)
#            tem_value_register=0
#            tem_value=[]
#            #tem_value Should Be in Register
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
#            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
#            print(tem_value)
#            for values in tem_value:
#                tem_value_register=tem_value_register+int(values)
#            instructions.Instruction_type.val[dest]=tem_value_register
#            print(instructions.Instruction_type.val)
#            # i_type[i].val = instructions.Instruction_type.val
#            x = i_type[count_i].getoperatori(x)
#            #i_type[count_i].getsdl(x)
#            #Stopping From Other Load
#            count_i += 1
#            pc += 4
#            if Base.vari < len(code_line)-1:
#                 Base.vari += 1
#
#         elif m in sb_ins:
#             Base.error = ""
#             sb_type.append(Branch.SB_type())
#             sb_type[count_sb].split_inst(x)
#             temp, label = sb_type[count_sb].op_select()
#             count_sb += 1
#             Base.nxt = Base.vari + 1
#             pc += 4
#             if temp:
#                # instructions.Instruction_type.val[1] = Base.nxt * 4
#                 for j in range(len(code_line)):
#                     if label in code_line[j]:
#                         Base.vari = j+1
#             elif Base.vari < len(code_line)-1:
#                 Base.vari+=1
#
#         elif "sw" in x:
#             Base.error = ""
#             s_type.append(instructions.S_type())
#             print(len(s_type))
#
#             ######################################################
#             # Content
#             register_num_list = re.findall(r'\d+', x)
#             print(register_num_list)
#             dest = int(register_num_list[0])
#             src1 = int(register_num_list[1])
#             src2 = int(register_num_list[2])
#             src2 = instructions.Instruction_type.val[src2]
#             Base.base_address = src2
#             offset_for_register = src1 + src2
#
#             byte1 = 255 & instructions.Instruction_type.val[dest]
#             byte2 = 65280 & instructions.Instruction_type.val[dest]
#             byte3 = 16711680 & instructions.Instruction_type.val[dest]
#             byte4 = 4278190080 & instructions.Instruction_type.val[dest]
#             print("byte1", byte1)
#             print("byte2", byte2)
#             print("byte3", byte3)
#             print("byte4", byte4)
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 2)] = byte3
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 3)] = byte4
#             #########################################################################
#             # Filling portion
#             print(instructions.Instruction_type.memory_dictionary_fetch)
#             #########################################################################
#
#             ######################################################
#
#             x = s_type[count_s].getoperators(x)
#             # s_type[count_s].getsds(x)
#             count_s += 1
#             pc += 4
#             if Base.vari < len(code_line) - 1:
#                 Base.vari += 1
#
#         elif "sh" in x:
#             Base.error = ""
#             s_type.append(instructions.S_type())
#             print(len(s_type))
#
#             ######################################################
#             # Content
#             register_num_list = re.findall(r'\d+', x)
#             print(register_num_list)
#             dest = int(register_num_list[0])
#             src1 = int(register_num_list[1])
#             src2 = int(register_num_list[2])
#             src2 = instructions.Instruction_type.val[src2]
#             Base.base_address = src2
#             offset_for_register = src1 + src2
#
#             byte1 = 255 & instructions.Instruction_type.val[dest]
#             byte2 = 65280 & instructions.Instruction_type.val[dest]
#
#             print("byte1", byte1)
#             print("byte2", byte2)
#
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
#
#             #########################################################################
#             # Filling portion
#             print(instructions.Instruction_type.memory_dictionary_fetch)
#             #########################################################################
#
#             ######################################################
#
#             x = s_type[count_s].getoperators(x)
#             # s_type[count_s].getsds(x)
#             count_s += 1
#             pc += 4
#             if Base.vari < len(code_line) - 1:
#                 Base.vari += 1
#
#         elif "sb" in x:
#             s_type.append(instructions.S_type())
#             print(len(s_type))
#
#             ######################################################
#             # Content
#             register_num_list = re.findall(r'\d+', x)
#             print(register_num_list)
#             dest = int(register_num_list[0])
#             src1 = int(register_num_list[1])
#             src2 = int(register_num_list[2])
#             src2 = instructions.Instruction_type.val[src2]
#             Base.base_address = src2
#             offset_for_register = src1 + src2
#
#             byte1 = 255 & instructions.Instruction_type.val[dest]
#
#             print("byte1", byte1)
#
#             instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
#
#             #########################################################################
#             # Filling portion
#             print(instructions.Instruction_type.memory_dictionary_fetch)
#             #########################################################################
#
#             ######################################################
#
#             x = s_type[count_s].getoperators(x)
#             # s_type[count_s].getsds(x)
#             count_s += 1
#             pc += 4
#             if Base.vari < len(code_line) - 1:
#                 Base.vari += 1
#
#             Base.error = ""
#
#         elif "lui" in x:
#             print("Lui is Running")
#             register_num_list = re.findall(r'\d+', x)
#             print(register_num_list)
#             dest = int(register_num_list[0])
#             src1 = int(register_num_list[1])
#             Base.lui_imm = src1 * 4096
#
#             # For 16 bit Load
#             # print(src1)
#             byte2 = 65280 & src1
#             # print(byte2)
#             instructions.Instruction_type.val[dest] = src1 * 4096
#             print(instructions.Instruction_type.val)
#
#             # x = i_type[count_i].getoperatori(x)
#             # i_type[count_i].getsdl(x)
#             # Stopping From Other Load
#             count_i += 1
#             pc += 4
#             if Base.vari < len(code_line) - 1:
#                 Base.vari += 1
#
#         elif "auipc" in x:
#             print("I am Running")
#             # print(pc1)
#             register_num_list = re.findall(r'\d+', x)
#             print(register_num_list)
#             dest = int(register_num_list[0])
#             src1 = int(register_num_list[1])
#             Base.aui_imm = src1
#             print(Base.vari)
#             instructions.Instruction_type.val[dest] = Base.vari * 4 + src1
#             # x = i_type[count_i].getoperatori(x)
#             # i_type[count_i].getsdl(x)
#             # Stopping From Other Load
#             count_i += 1
#             pc += 4
#             if Base.vari < len(code_line) - 1:
#                 Base.vari += 1
#
#             # UJ Type Instruction
#
#         elif m in jump_ins:
#             # l_count = 0
#             # label_add = 0
#             # y = x[4:]
#             # nxt = vari + 1
#             # track = vari
#             # instructions.Instruction_type.val[1] = nxt * 4
#             # jal_c = 0
#             # for key in Base.label_address:
#             #     if y in key:
#             #         label_add = Base.label_address[key]
#             # print("value of x1: " + str(nxt))
#             # if label_add > track:
#             #     while track != label_add:
#             #         if ':' not in code_line[track]:
#             #             l_count += 1
#             #         track += 1
#             #     jal_c = l_count
#             # elif label_add < track:
#             #     while track != label_add:
#             #         if ':' not in code_line[track]:
#             #             l_count -= 1
#             #         track -= 1
#             #     jal_c = l_count + 1
#
#             '''for j in range(len(code_line)):
#                 if j > vari and ':' in code_line[j]:
#                     l_count += 1
#                 if y in code_line[j] and (not ('jal' in code_line[j])):
#                     # code_line[j] = code_line[j].split(":")
#                     if j
#                     vari = j + 1
#                     jal_c = (vari + 1) - (nxt + l_count)'''
#             jump_type.append(Jump.JumpIns(x, Base.vari, code_line, Base.label_address))
#             jump_type[count_jump].split_inst()
#             if 'jal' in x:
#                 y = x[4:]
#                 track, jal_c = jump_type[count_jump].jal_op()
#                 Base.jal_imm[y] = jal_c
#                 print("jal list", Base.jal_imm)
#                 Base.vari = track + 1
#                 print("Vari = " + str(Base.vari))
#             if 'jalr' in x:
#                 Base.vari = jump_type[count_jump].jalr_op()
#             # Base.jal_imm[y] = jal_c
#             # print("jal list", Base.jal_imm)
#             # vari = track + 1
#             Base.error = ""
#             pc += 4
#         elif "ret" in x:
#             Base.vari = int((instructions.Instruction_type.val[1]) / 4)
#             print("value of x1(1): " + str(Base.nxt))
#             Base.error = ""
#         elif "ebreak" in x:
#             Base.error = ""
#             break
#         elif m in r_ins:
#             r_type.append(instructions.R_type())
#             print(len(r_type))
#             # r_type[i].val = instructions.Instruction_type.val
#             x = r_type[count_r].getoperator(x)
#             r_type[count_r].getsd(x)
#             count_r += 1
#             pc += 4
#             if Base.vari < len(code_line) - 1:
#                 Base.vari += 1
#             Base.error = ""
#             # instructions.Instruction_type.val = r_type[i].val
#
#         else:
#             break
#         instructions.Instruction_type.val[0] = 0
#     final_result = instructions.Instruction_type.val[instructions.Instruction_type.indexd]
#     print(final_result)
#     success = True
#     return final_result, success
#
# def step_by_step(request):
#     session = request.session.get('session', 0) + 1
#     print("Session = " + str(session))
#     request.session['session'] = session
#     Base.next = session
#     print("Base.next = " + str(Base.next))
#     print('length of codeline1')
#     print(len(Base.code_line1))
#     answer = stepping(Base.code_line1[Base.vari])
#
#
#
#     # prev_data = {'fresult': answer, 'success': "False", 'ctn': Base.vari + 1, 'result': "on", 'code': Base.whole_code,
#     #              'data': instructions.Instruction_type.val, 'list1': Base.list_column_1, 'list2': Base.list_column_2,
#     #              'list3': Base.list_column_3, 'list4': Base.list_column_4}
#
#     count = request.session['session']
#     print(count)
#     #Base.param1.update({'result': "on", 'fresult': answer, 'ctn': Base.vari + 1, 'code': Base.whole_code})
#     Base.param12.update({'fresult': answer, 'success': "False", 'ctn': Base.vari + 1, 'result': "on", 'code': Base.whole_code})
#
#     print("step1 :" + str(Base.param12))
#     print(request.session['session'])
#     print("Value of Vari = ")
#     print(Base.vari)
#     if Base.vari >= len(Base.code_line1):
#         messages.success(request, message="Code exited with 0 error")
#         del(request.session['session'])
#         Base.next = 0
#         session = 0
#         Base.param12.update({'result': "off", 'success': "True", 'atlast': "Code exited with 0 error"})
#     #return render(request, 'index.html', Base.param1)
#     return HttpResponse(json.dumps(Base.param12))
#
# def stepping(x):
#     whole_code = Base.whole_code.replace('\r\n', '\n')
#     code_line = [line for line in whole_code.split('\n') if line.strip() != '']
#     r_type = []
#     i_type = []
#     s_type = []
#     sb_type = []
#     jump_type = []
#     count_jump = 0
#     count_i = 0
#     count_r = 0
#     count_s = 0
#     count_sb = 0
#     pc = 0
#
#     mainting_stack(instructions.Instruction_type.val, Base.list_column_1, Base.list_column_2, Base.list_column_3,
#                    Base.list_column_4, Base.vari)
#
#     r_ins = ['add', 'sub', 'mul', 'div', 'rem', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
#     i_ins = ['slli', 'srli', 'srai', 'addi', 'subi', 'muli', 'divi', 'remi', 'xori', 'andi', 'ori', 'slti', 'sltiu',
#              'fence', 'fence.i', 'scall', 'sbreak']
#     sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
#     jump_ins = ['jal', 'jalr']
#
#     x = x.lower()
#     x = x.strip()
#     m = re.search(r'^c.\w+|\w+', x)
#     m = m.group()
#     temp = False
#
#     if m in i_ins:
#         Base.error = ""
#         i_type.append(instructions.I_type())
#         print(len(i_type))
#         # i_type[i].val = instructions.Instruction_type.val
#         x = i_type[count_i].getoperatori(x)
#         i_type[count_i].getsdi(x)
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             print("i am in condition huraahh!")
#             Base.vari += 1
#         # instructions.Instruction_type.val = i_type[i].val
#
#     elif "lw" in x:
#         Base.error = ""
#         i_type.append(instructions.I_type())
#         print(len(i_type))
#
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         offset_for_register = src1 + src2
#
#         print(offset_for_register)
#         offset_temp = '{0:08X}'.format(offset_for_register)
#         offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
#         offset_temp2 = '{0:08X}'.format(offset_for_register + 2)
#         offset_temp3 = '{0:08X}'.format(offset_for_register + 3)
#         tem_value = []
#         tem_value_register = 0
#         # tem_value Should Be in Register
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp2))
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp3))
#
#         print(tem_value)
#
#         for values in tem_value:
#             (tem_value_register) = int(tem_value_register) + int(values)
#         instructions.Instruction_type.val[dest] = tem_value_register
#         print(instructions.Instruction_type.val)
#
#         # i_type[i].val = instructions.Instruction_type.val
#         x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "lhu" in x:
#         Base.error = ""
#         i_type.append(instructions.I_type())
#         print(len(i_type))
#
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         offset_for_register = src1 + src2
#
#         offset_temp = '{0:08X}'.format(offset_for_register)
#         offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
#         # tem_value Should Be in Register
#         tem_value = []
#         tem_value_register = 0
#         # tem_value Should Be in Register
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
#         print(tem_value)
#         print("Unsigned")
#         for values in tem_value:
#             tem_value_register = tem_value_register + int(values)
#             print(tem_value_register)
#             if (tem_value_register < 0):
#                 instructions.Instruction_type.val[dest] = tem_value_register * -1
#             else:
#                 instructions.Instruction_type.val[dest] = tem_value_register
#             print(instructions.Instruction_type.val)
#
#         # i_type[i].val = instructions.Instruction_type.val
#         x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "lbu" in x:
#         Base.error = ""
#         i_type.append(instructions.I_type())
#         print(len(i_type))
#
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         offset_for_register = src1 + src2
#
#         offset_temp = '{0:08X}'.format(offset_for_register)
#         # tem_value Should Be in Register
#         tem_value = instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
#         print(tem_value)
#         if (int(tem_value) < 0):
#             instructions.Instruction_type.val[dest] =int(tem_value)  * -1
#         else:
#             instructions.Instruction_type.val[dest] = int(tem_value)
#         print(instructions.Instruction_type.val)
#
#         # i_type[i].val = instructions.Instruction_type.val
#         x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "lb" in x:
#         Base.error = ""
#         i_type.append(instructions.I_type())
#         print(len(i_type))
#
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         offset_for_register = src1 + src2
#
#         offset_temp = '{0:08X}'.format(offset_for_register)
#         # tem_value Should Be in Register
#         tem_value = instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
#         print(tem_value)
#         instructions.Instruction_type.val[dest] = int(tem_value)
#         print(instructions.Instruction_type.val)
#         # i_type[i].val = instructions.Instruction_type.val
#         x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "lh" in x:
#
#         Base.error = ""
#         i_type.append(instructions.I_type())
#         print(len(i_type))
#
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         offset_for_register = src1 + src2
#
#         offset_temp = '{0:08X}'.format(offset_for_register)
#         offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
#         tem_value_register = 0
#         tem_value = []
#         # tem_value Should Be in Register
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
#         tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
#         print(tem_value)
#         for values in tem_value:
#             tem_value_register = tem_value_register + int(values)
#         instructions.Instruction_type.val[dest] = tem_value_register
#         print(instructions.Instruction_type.val)
#         # i_type[i].val = instructions.Instruction_type.val
#         x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif m in sb_ins:
#         Base.error = ""
#         sb_type.append(Branch.SB_type())
#         sb_type[count_sb].split_inst(x)
#         temp, label = sb_type[count_sb].op_select()
#         count_sb += 1
#         Base.nxt = Base.vari + 1
#         pc += 4
#         if temp:
#             # instructions.Instruction_type.val[1] = Base.nxt * 4
#             for j in range(len(code_line)):
#                 if label in code_line[j]:
#                     Base.vari = j
#         elif Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "sw" in x:
#         Base.error = ""
#         s_type.append(instructions.S_type())
#         print(len(s_type))
#
#         ######################################################
#         # Content
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         Base.base_address = src2
#         offset_for_register = src1 + src2
#
#         byte1 = 255 & instructions.Instruction_type.val[dest]
#         byte2 = 65280 & instructions.Instruction_type.val[dest]
#         byte3 = 16711680 & instructions.Instruction_type.val[dest]
#         byte4 = 4278190080 & instructions.Instruction_type.val[dest]
#         print("byte1", byte1)
#         print("byte2", byte2)
#         print("byte3", byte3)
#         print("byte4", byte4)
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 2)] = byte3
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 3)] = byte4
#         #########################################################################
#         # Filling portion
#         print(instructions.Instruction_type.memory_dictionary_fetch)
#         #########################################################################
#
#         ######################################################
#
#         x = s_type[count_s].getoperators(x)
#         # s_type[count_s].getsds(x)
#         count_s += 1
#         pc += 4
#         if Base.vari < len(code_line) :
#             Base.vari += 1
#
#     elif "sh" in x:
#         Base.error = ""
#         s_type.append(instructions.S_type())
#         print(len(s_type))
#
#         ######################################################
#         # Content
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         Base.base_address = src2
#         offset_for_register = src1 + src2
#
#         byte1 = 255 & instructions.Instruction_type.val[dest]
#         byte2 = 65280 & instructions.Instruction_type.val[dest]
#
#         print("byte1", byte1)
#         print("byte2", byte2)
#
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
#
#         #########################################################################
#         # Filling portion
#         print(instructions.Instruction_type.memory_dictionary_fetch)
#         #########################################################################
#
#         ######################################################
#
#         x = s_type[count_s].getoperators(x)
#         # s_type[count_s].getsds(x)
#         count_s += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "sb" in x:
#         s_type.append(instructions.S_type())
#         print(len(s_type))
#
#         ######################################################
#         # Content
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         src2 = int(register_num_list[2])
#         src2 = instructions.Instruction_type.val[src2]
#         Base.base_address = src2
#         offset_for_register = src1 + src2
#
#         byte1 = 255 & instructions.Instruction_type.val[dest]
#
#         print("byte1", byte1)
#
#         instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
#
#         #########################################################################
#         # Filling portion
#         print(instructions.Instruction_type.memory_dictionary_fetch)
#         #########################################################################
#
#         ######################################################
#
#         x = s_type[count_s].getoperators(x)
#         # s_type[count_s].getsds(x)
#         count_s += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#         Base.error = ""
#
#     elif "lui" in x:
#         print("Lui is Running")
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         Base.lui_imm = src1
#
#         # For 16 bit Load
#         # print(src1)
#         byte2 = 65280 & src1
#         # print(byte2)
#         instructions.Instruction_type.val[dest] = src1
#         print(instructions.Instruction_type.val)
#
#         # x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#     elif "auipc" in x:
#         print("I am Running")
#         # print(pc1)
#         register_num_list = re.findall(r'\d+', x)
#         print(register_num_list)
#         dest = int(register_num_list[0])
#         src1 = int(register_num_list[1])
#         Base.aui_imm = src1
#         print(Base.vari)
#         instructions.Instruction_type.val[dest] = Base.vari * 4 + src1
#         # x = i_type[count_i].getoperatori(x)
#         # i_type[count_i].getsdl(x)
#         # Stopping From Other Load
#         count_i += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#
#         # UJ Type Instruction
#     elif m in jump_ins:
#         jump_type.append(Jump.JumpIns(x, Base.vari, code_line, Base.label_address))
#         jump_type[count_jump].split_inst()
#         if 'jal' in x:
#             y = x[4:]
#             track, jal_c = jump_type[count_jump].jal_op()
#             Base.jal_imm[y] = jal_c
#             print("jal list", Base.jal_imm)
#             Base.vari = track + 1
#             print("Vari = " + str(Base.vari))
#         if 'jalr' in x:
#             Base.vari = jump_type[count_jump].jalr_op()
#             # Base.jal_imm[y] = jal_c
#             # print("jal list", Base.jal_imm)
#             # vari = track + 1
#         Base.error = ""
#         pc += 4
#     elif "ret" in x:
#         Base.vari = int((instructions.Instruction_type.val[1]) / 4)
#         print("value of x1(1): " + str(Base.nxt))
#         Base.error = ""
#     elif m in r_ins:
#         r_type.append(instructions.R_type())
#         print(len(r_type))
#         # r_type[i].val = instructions.Instruction_type.val
#         x = r_type[count_r].getoperator(x)
#         r_type[count_r].getsd(x)
#         count_r += 1
#         pc += 4
#         if Base.vari < len(code_line):
#             Base.vari += 1
#         Base.error = ""
#         # instructions.Instruction_type.val = r_type[i].val
#
#     instructions.Instruction_type.val[0] = 0
#     final_result = instructions.Instruction_type.val[instructions.Instruction_type.indexd]
#
#
#
#     print("This is Stack")
#     print(Base.stack_register)
#     # Base.param1.update({'data': zip(instructions.Instruction_type.val, Base.reg_name),
#     #                'data1': zip(Base.listkey, Base.list_column_1, Base.list_column_2, Base.list_column_3, Base.list_column_4),
#     #                'data3': zip(Base.pc, Base.code_line1, Base.ins_type, Base.immediate1, Base.func7, Base.source2, Base.source1, Base.func3, Base.destination, Base.immediate2, Base.opcode)})
#
#     Base.param12.update({'data': instructions.Instruction_type.val, 'list1': Base.list_column_1, 'list2': Base.list_column_2,
#                     'list3': Base.list_column_3, 'list4': Base.list_column_4})
#     print(final_result)
#
#     #request.session['session'] = Base.param1
#     return final_result
#
# def reseting(request):
#
#     for i in range(0, 32):
#         instructions.Instruction_type.val[i] = 0
#
#     # counter_memory_address = 0
#     # Base.listkey = []
#     # for x in range(0, 512):
#     #     if (x == 512 / 4):
#     #         break
#     #     Base.listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
#     #     counter_memory_address = counter_memory_address + 4
#     #
#     # #########################################################
#     # for i in range(0, 512 * 4):
#     #     # memory_dictionary[hex(i)]=memory_value[i]
#     #     instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(i)]
#     # #########################################################
#     #
#     # Base.list_column_1 = []
#     # Base.list_column_2 = []
#     # Base.list_column_3 = []
#     # Base.list_column_4 = []
#     #
#     # count_memory_break_view = 0
#     # for i in range(0, 514 * 4):
#     #     if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
#     #         break
#     #     Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
#     #     Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
#     #     Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
#     #     Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
#     #     count_memory_break_view = count_memory_break_view + 4
#
#     # Base.param1.update({'result': "True", 'ctn': 0 + 1, 'code': Base.whole_code,
#     #                'data': zip(instructions.Instruction_type.val, Base.reg_name),
#     #                'data1': zip(Base.listkey, Base.list_column_1, Base.list_column_2, Base.list_column_3, Base.list_column_4),
#     #                'data3': zip(Base.pc, Base.code_line1, Base.ins_type, Base.immediate1, Base.func7, Base.source2,
#     #                             Base.source1, Base.func3, Base.destination, Base.immediate2, Base.opcode)})
#     Base.vari = 0
#     Base.param12.update({'success': "False", 'result': "True", 'ctn': Base.vari + 1, 'data': instructions.Instruction_type.val, 'list1': Base.list_column_1, 'list2': Base.list_column_2,
#                     'list3': Base.list_column_3, 'list4': Base.list_column_4})
#     request.session['session'] = 0
#     print(Base.param1)
#     #return render(request, 'index.html', Base.param1)
#     return HttpResponse(json.dumps(Base.param12))
#
# def prev(request):
#     instructions.Instruction_type.val = Base.stack_register.pop()
#     Base.list_column_1 = Base.memory_list1.pop()
#     Base.list_column_2 = Base.memory_list2.pop()
#     Base.list_column_3 = Base.memory_list3.pop()
#     Base.list_column_4 = Base.memory_list4.pop()
#     Base.vari = Base.ins_number.pop()
#
#     print("This is Prev")
#     print(instructions.Instruction_type.val)
#     print(Base.vari)
#     Base.param12.update({'data': instructions.Instruction_type.val, 'list1': Base.list_column_1, 'list2': Base.list_column_2,
#                     'list3': Base.list_column_3, 'list4': Base.list_column_4, 'ctn': Base.vari + 1})
#
#     return HttpResponse(json.dumps(Base.param12))
#
# def mainting_stack(register, list1, list2, list3, list4, ins_num):
#     print("In stack function")
#     if Base.vari + 1 <= len(Base.code_line1):
#
#         print("In stack condition")
#         ######### For Registers #########
#         file1 = open("file1.txt", "w")
#         file1.write(str(register))
#         file1.close()
#         file1 = open("file1.txt", "r")
#         x = file1.read()
#         Base.stack_register.append(json.loads(x))
#         file1.close()
#         #################################
#
#
#         ######### For Memory ############
#         file1 = open("file1.txt", "w")
#         file1.write(str(list1))
#         file1.close()
#         file1 = open("file1.txt", "r")
#         x = file1.read()
#         Base.memory_list1.append(json.loads(x))
#         file1.close()
#
#         file1 = open("file1.txt", "w")
#         file1.write(str(list2))
#         file1.close()
#         file1 = open("file1.txt", "r")
#         x = file1.read()
#         Base.memory_list2.append(json.loads(x))
#         file1.close()
#
#         file1 = open("file1.txt", "w")
#         file1.write(str(list3))
#         file1.close()
#         file1 = open("file1.txt", "r")
#         x = file1.read()
#         Base.memory_list3.append(json.loads(x))
#         file1.close()
#
#         file1 = open("file1.txt", "w")
#         file1.write(str(list4))
#         file1.close()
#         file1 = open("file1.txt", "r")
#         x = file1.read()
#         Base.memory_list4.append(json.loads(x))
#         file1.close()
#         #################################
#
#         ######### For Instructions Number #########
#         file1 = open("file1.txt", "w")
#         file1.write(str(ins_num))
#         file1.close()
#         file1 = open("file1.txt", "r")
#         x = file1.read()
#         Base.ins_number.append(int(x))
#         file1.close()
#         #################################
#
#         print(Base.stack_register)