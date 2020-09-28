from django.contrib import messages
from django.http import HttpResponse


from . import instructions
from . import views
import json
import re

def Display_info_I(request):
    print("This is Display")
    views.Base.status = "False"
    views.Base.base_address = 0
    views.Base.jal_imm = {}
    views.Base.j_count = 0
    views.Base.code_line1 = []
    views.Base.error = ""
    views.Base.lui_imm = 0
    views.Base.aui_imm = 0
    views.Base.label_address = {}
    views.Base.whole_code = ""
    views.Base.ins_type = []
    views.Base.destination = []
    views.Base.source1 = []
    views.Base.source2 = []
    views.Base.immediate1 = []
    views.Base.immediate2 = []
    views.Base.opcode = []
    views.Base.func7 = []
    views.Base.func3 = []
    views.Base.func2 = []
    views.Base.func4 = []
    views.Base.func6 = []
    views.Base.pc = []
    views.Base.next = 0
    views.Base.length = 0
    views.Base.data = []
    views.Base.list_column_1 = []
    views.Base.list_column_2 = []
    views.Base.list_column_3 = []
    views.Base.list_column_4 = []
    views.Base.listkey = []
    views.Base.hex = ""
    views.Base.vari = 0
    views.Base.nxt = 0
    views.Base.dump_bin = []

    request.session['session'] = 0
    views.Base.whole_code = request.POST.get("editline", "")
    #views.Base.whole_code = "addi x1,x0,2\r\njal label\r\naddi x2,x0,4\r\nlabel1:\r\nslt x2,x1,x2\r\nadd x3,x2,x3\r\njal label1\r\nsub x3,x4,x5\r\nsw x2,5(x0)\r\nlabel:\r\nori x17,x14,4\r\nandi x16,x13,3\r\nxori x15,x12,2\r\nslli x14,x1,2\r\nsrli x13,x1,3\r\nsrai x12,x2,2\r\nlui x13,1\r\njalr x0,x5,20"
    #views.Base.whole_code = " addi a5,zero,17\nstart:\naddi a1,zero,1\nupx:\nadd a0,a2,zero\nup:\naddi a3,a3,1\nadd a2,a0,a1\nbeq a5,a3,end\nandi a4,a3,1\nbeq a4,zero,upx\nadd a1,a2,zero\njal up\nend:"
    print(views.Base.whole_code)
    whole_code1 = views.Base.whole_code.replace('\r\n', '\n')
    print(whole_code1)
    for i in range(0, 32):
        instructions.Instruction_type.val[i] = 0
    if re.match("^0x", whole_code1):
        code_line_hex = [line for line in whole_code1.split('\n') if line.strip() != '']
        Bin = []
        for i in range(len(code_line_hex)):
            code_line_hex[i] = re.sub(r"^0x", '', code_line_hex[i])
            Bin.append("{0:032b}".format(int(code_line_hex[i], 16)))

        print(code_line_hex)
        print(Bin)

        opcodeh = []
        desth = []
        funct3h = []
        source1h = []
        immh = []
        code = []
        funct7h = []
        for i in range(len(code_line_hex)):
            if Bin[i][25:32] == "0010011" and Bin[i][17:20] == "000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("addi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "001" and Bin[i][:7] == "0000000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("slli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "010":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("slti" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "011":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("sltiu" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "100":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("xori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0000000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("srli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0100000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("srai" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "110":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("ori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "111":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("andi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))

        print(desth)
        print(source1h)
        print(immh)

        views.Base.data = code
        views.Base.code_line1 = code
    else:
        print("in else")
        error, views.Base.data = views.interpreter(whole_code1)
        print(error)
        if error:
            param123 = {'error': error}
            # views.Base.param.update({'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code, 'ctn': 1, 'data': zip(instructions.Instruction_type.val, views.Base.reg_name), 'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4)})
            messages.error(request, error)
            return HttpResponse(json.dumps(param123))
        print(views.Base.data)

        code_line = [line for line in whole_code1.split('\n') if line.strip() != '']
        print("Code Line =")
        print(code_line)

        views.Base.code_line1 = []
        for k in range(len(code_line)):
            if ':' not in code_line[k]:
                views.Base.code_line1.append(code_line[k])
            else:
                continue
    print(views.Base.code_line1)
    r_ins = ['add', 'sub', 'mul', 'div', 'rem', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
    i_ins = ['lw', 'lb', 'lh', 'lbu', 'lhu', 'slli', 'srli', 'srai', 'addi', 'subi', 'xori',
             'andi',
             'ori', 'slti', 'sltiu', 'fence', 'fence.i', 'scall', 'sbreak', 'jalr']
    sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
    s_ins = ['sb', 'sh', 'sw']
    u_ins = ['lui', 'auipc']
    uj_ins = ['jal']
    jal_immediate = []
    ins_mem = []
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    bits = []
    instruction_memory_uni_counter = 0
    print(views.Base.data)
    print("This is length " + str(len(views.Base.data)))

    print("Code Line1 =")
    print(views.Base.code_line1)
    c = 0
    p_counter = 0
    for i in range(len(views.Base.data)):
        if views.Base.data[i][0] in i_ins or views.Base.data[i][0] in uj_ins or views.Base.data[i][0] in u_ins or views.Base.data[i][0] in sb_ins or views.Base.data[i][0] in s_ins or views.Base.data[i][0] in r_ins:
            views.Base.pc.append('0x' + '{0:01X}'.format(p_counter * 4))
            print(views.Base.pc)
            bits.append(32)
            p_counter = p_counter + 1
        x = str(views.Base.data[i])
        x = x.lower()
        x = x.strip()
        m = re.search(r'\w+', x)
        m = m.group()
        half_ins = x[len(m) + 1:]
        half_ins = half_ins.replace(" ", "")
        if m in i_ins:
            views.Base.ins_type.append('I')
            if 'lw' in m or 'lh' in m or 'lb' in m or 'lbu' in m or 'lhu' in m:
                # half_ins = re.findall(r'\w\d+|\d+', x)
                half_ins = re.findall(r'[+-]?\d+', x)
                dest = half_ins[0]
                imm = half_ins[1]
                src1 = half_ins[2]
                imm_int = '{0:012b}'.format(int(imm))
                dest_int = '{0:05b}'.format(int(dest))
                src1_int = '{0:05b}'.format(int(src1))
                views.Base.destination.append(dest_int)
                views.Base.source1.append(src1_int)
                views.Base.immediate1.append(imm_int)
                views.Base.immediate2.append('X')
                views.Base.source2.append('X')
                views.Base.opcode.append('0000011')
                if 'lb' in m:
                    views.Base.func3.append('000')
                    views.Base.func7.append('X')
                elif 'lh' in m:
                    views.Base.func3.append('001')
                    views.Base.func7.append('X')
                elif 'lw' in m:
                    views.Base.func3.append('010')
                    views.Base.func7.append('X')
                elif 'lbu' in m:
                    views.Base.func3.append('100')
                    views.Base.func7.append('X')
                elif 'lhu' in m:
                    views.Base.func3.append('101')
                    views.Base.func7.append('X')

                ins_mem.append(
                    str(views.Base.immediate1[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(
                        views.Base.destination[c]) + str(views.Base.opcode[c]))
            elif 'jalr' in m:
                views.Base.ins_type.append('X')
                views.Base.opcode.append('X')
                views.Base.func7.append('X')
                views.Base.func3.append('X')
                views.Base.source1.append('X')
                views.Base.source2.append('X')
                views.Base.destination.append('X')
                views.Base.immediate2.append('X')
                views.Base.immediate1.append('X')
                ins_mem.append('00000000000000000000000000000000')
            else:
                half_ins = re.findall(r'[+-]?\d+', x)
                if re.match("^0x", whole_code1):
                    dest = half_ins[0]
                    src1 = half_ins[1]
                    imm = half_ins[2]
                else:
                    print(views.Base.data[i][1])
                    dest = views.Base.data[i][1]
                    dest = dest[1:]
                    imm = views.Base.data[i][3]
                    src1 = views.Base.data[i][2]
                    src1 = src1[1:]
                dest_int = '{0:05b}'.format(int(dest))
                src1_int = '{0:05b}'.format(int(src1))
                imm_int = ""
                if int(imm) < 0:
                    print("Negative")
                    print(imm)
                    n = int(imm) + 2 ** 32
                    imm_int = ''
                    binary = '{0:012b}'.format(n)
                    binary = binary[::-1]
                    imm_int = binary[:12]
                    imm_int = imm_int[::-1]
                    print(imm_int)
                else:
                    imm_int = '{0:012b}'.format(int(imm))
                views.Base.destination.append(dest_int)
                views.Base.source1.append(src1_int)
                views.Base.immediate2.append('X')
                views.Base.source2.append('X')
                views.Base.opcode.append('0010011')
                if 'addi' in m:
                    views.Base.func3.append('000')
                elif 'slli' in m:
                    views.Base.func3.append('001')
                elif 'sltiu' in m:
                    views.Base.func3.append('011')
                elif 'slti' in m:
                    views.Base.func3.append('010')
                elif 'xori' in m:
                    views.Base.func3.append('100')
                elif 'srli' in m or 'srai' in m:
                    views.Base.func3.append('101')
                elif 'ori' in m:
                    views.Base.func3.append('110')
                elif 'andi' in m:
                    views.Base.func3.append('111')
                if 'slli' in m or 'srli' in m:
                    imm_int = '{0:05b}'.format(int(imm))
                    views.Base.func7.append('0000000')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.func7[c]) + str(views.Base.immediate1[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(
                            views.Base.destination[c]) + str(views.Base.opcode[c]))

                elif 'srai' in m:
                    imm_int = '{0:05b}'.format(int(imm))
                    views.Base.func7.append('0100000')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.func7[c]) + str(views.Base.immediate1[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(
                            views.Base.destination[c]) + str(views.Base.opcode[c]))

                else:
                    views.Base.func7.append('X')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.immediate1[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(views.Base.destination[c]) + str(views.Base.opcode[c]))
            print(ins_mem)


        elif m in r_ins:
            views.Base.ins_type.append('R')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            src1 = half_ins[1]
            src2 = half_ins[2]
            dest_int = '{0:05b}'.format(int(dest))
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.destination.append(dest_int)
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('X')
            views.Base.immediate2.append('X')
            views.Base.opcode.append('0110011')
            if 'add' in m or 'sub' in m:
                views.Base.func3.append('000')
            elif 'sll' in m:
                views.Base.func3.append('001')
            elif 'sltu' in m:
                views.Base.func3.append('011')
            elif 'slt' in m:
                views.Base.func3.append('010')
            elif 'xor' in m:
                views.Base.func3.append('100')
            elif 'srl' in m or 'sra' in m:
                views.Base.func3.append('101')
            elif 'or' in m:
                views.Base.func3.append('110')
            elif 'and' in m:
                views.Base.func3.append('111')
            if 'sub' in m or 'sra' in m:
                views.Base.func7.append('0100000')
                ins_mem.append(
                    str(views.Base.func7[c]) + str(views.Base.source2[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(
                        views.Base.destination[c]) + str(
                        views.Base.opcode[c]))
            else:
                views.Base.func7.append('0000000')
                ins_mem.append(
                    str(views.Base.func7[c]) + str(views.Base.source2[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(
                        views.Base.destination[c]) + str(
                        views.Base.opcode[c]))

        elif m in sb_ins:
            views.Base.ins_type.append('SB')
            half_ins = re.findall(r'[+-]?\d+', x)
            src1 = half_ins[0]
            # imm = half_ins[2]
            src2 = half_ins[1]
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('0000000')
            views.Base.immediate2.append('10000')
            views.Base.destination.append('X')
            views.Base.opcode.append('1100011')
            views.Base.func7.append('X')
            if 'beq' in m:
                views.Base.func3.append('000')
            elif 'bne' in m:
                views.Base.func3.append('001')
            elif 'bltu' in m:
                views.Base.func3.append('110')
            elif 'blt' in m:
                views.Base.func3.append('100')
            elif 'bgeu' in m:
                views.Base.func3.append('111')
            elif 'bge' in m:
                views.Base.func3.append('101')
            #ins_mem.append('00000000000000000000000000000000')
            ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(views.Base.immediate2[i]) + str(views.Base.opcode[i]))


        elif m in s_ins:
            views.Base.ins_type.append('S')
            half_ins = re.findall(r'[+-]?\d+', x)
            src1 = half_ins[2]
            dest = half_ins[1]
            dest_int = int(dest) + views.Base.base_address
            imm = half_ins[1]
            src2 = half_ins[0]
            dest_int = '{0:05b}'.format(dest_int)
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            imm_int = '{0:07b}'.format(int(imm))
            views.Base.destination.append('X')
            views.Base.source1.append(src1_int)
            views.Base.immediate1.append(imm_int)
            views.Base.immediate2.append(dest_int)
            views.Base.source2.append(src2_int)
            views.Base.opcode.append('0100011')
            views.Base.func7.append('X')
            if 'sb' in m:
                views.Base.func3.append('000')
            elif 'sh' in m:
                views.Base.func3.append('001')
            elif 'sw' in m:
                views.Base.func3.append('010')
            ins_mem.append(
                str(views.Base.immediate1[c]) + str(views.Base.source2[c]) + str(views.Base.source1[c]) + str(views.Base.func3[c]) + str(
                    views.Base.immediate2[c]) + str(
                    views.Base.opcode[c]))

        elif m in u_ins:
            views.Base.ins_type.append('U')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            imm = half_ins[1]
            dest_int = '{0:05b}'.format(int(dest))
            if 'auipc' in m:
                views.Base.opcode.append('0010111')
                imm_int = '{0:020b}'.format(int(imm))
                views.Base.immediate1.append(imm_int)
            else:
                views.Base.opcode.append('0110111')
                imm_int = '{0:020b}'.format(int(imm))
                views.Base.immediate1.append(imm_int)
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.destination.append(dest_int)
            views.Base.immediate2.append('X')
            ins_mem.append(str(views.Base.immediate1[c]) + str(views.Base.destination[c]) + str(views.Base.opcode[c]))

        elif m in uj_ins:
            views.Base.ins_type.append('UJ')
            half_ins = re.findall(r'[+-]?\d+', x)
            # dest = half_ins[0]
            # dest_int = '{0.05b}'.format(int(dest))
            views.Base.destination.append('00001')
            views.Base.opcode.append('1101111')
            for key in views.Base.jal_imm:
                if key in x:
                    imm = views.Base.jal_imm[key]
            imm_int = '{0:020b}'.format(int(imm))
            views.Base.immediate1.append(imm_int)
            views.Base.j_count += 1
            # print("Value of JUMP : " + str(views.Base.jal_imm))
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.immediate2.append('X')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))
        elif 'ret' in m or 'ebreak' in m:
            views.Base.ins_type.append('X')
            views.Base.opcode.append('X')
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.destination.append('X')
            views.Base.immediate2.append('X')
            views.Base.immediate1.append('X')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))
        else:
            continue

        views.Base.func2.append('X')
        views.Base.func4.append('X')
        views.Base.func6.append('X')
        if views.Base.data[i][0] in i_ins or views.Base.data[i][0] in uj_ins or views.Base.data[i][0] in u_ins or views.Base.data[i][0] in sb_ins or views.Base.data[i][0] in s_ins or views.Base.data[i][0] in r_ins:
        ####### Transfering instruction bits into dump list #######
            views.Base.dump_bin.append([bits[c], ins_mem[c]])
            c = c + 1
        ###########################################################

    for k in ins_mem:
        l3.append(k[:8])
        l2.append(k[8:16])
        l1.append(k[16:24])
        l0.append(k[24:32])
    print(l3)
    print(l2)
    print(l1)
    print(l0)
    for k in range(len(ins_mem)):
        l3[k] = '{0:02X}'.format(int(l3[k], 2))
        l2[k] = '{0:02X}'.format(int(l2[k], 2))
        l1[k] = '{0:02X}'.format(int(l1[k], 2))
        l0[k] = '{0:02X}'.format(int(l0[k], 2))
    print(l3)
    print(l2)
    print(l1)
    print(l0)

    for i in range(0, len(views.Base.code_line1)):
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter)] = int(
            l0[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 1)] = int(l1[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 2)] = int(l2[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 3)] = int(l3[i], 16)

        instruction_memory_uni_counter += 4

    # print(views.Base.ins_type)

    ##### This Is Memory Block START
    ###When using Online web
    file_values=open("/home/merloxygen/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
    ###when using dedicated machine(PC)

    # file_values = open("templates\m.txt", "r")
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
    views.Base.listkey = []
    for x in range(0, 512):
        if (x == 512 / 4):
            break
        views.Base.listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
        counter_memory_address = counter_memory_address + 4

    #########################################################
    for i in range(0, 512 * 4):
        # memory_dictionary[hex(i)]=memory_value[i]
        instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(i)]
    #########################################################

    ########################################################## Memory  breaking For Views

    count_memory_break_view = 0
    for i in range(0, 514 * 4):
        if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
            break
        views.Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
        views.Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
        views.Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
        views.Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
        count_memory_break_view = count_memory_break_view + 4

    ########################################################## Memory  breaking For Views

    ########################################################## Address Division For Views

    ########################################################## Address Division For Views
    # views.Base.param.update({'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code, 'data': zip(instructions.Instruction_type.val, views.Base.reg_name), 'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4), 'data3': zip(views.Base.pc, views.Base.code_line1, views.Base.ins_type, views.Base.immediate1, views.Base.func7, views.Base.source2, views.Base.source1, views.Base.func3, views.Base.destination, views.Base.immediate2, views.Base.opcode), 'ctn': 1})
    # print(views.Base.param)
    # return render(request, 'index.html', views.Base.param)
    param123 = {'length': len(views.Base.code_line1), 'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code,
                'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
                'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4, 'pc': views.Base.pc, 'codes': views.Base.code_line1,
                'ins_type': views.Base.ins_type, 'imm1': views.Base.immediate1, 'f7': views.Base.func7, 'f6': views.Base.func6, 'f4': views.Base.func4,'s2': views.Base.source2,
                's1': views.Base.source1, 'f3': views.Base.func3, 'f2': views.Base.func2, 'dest': views.Base.destination, 'imm2': views.Base.immediate2,
                'opcode': views.Base.opcode, 'ctn': 1}
    print(param123)

    views.Base.stack_register.clear()
    views.Base.memory_list1.clear()
    views.Base.memory_list2.clear()
    views.Base.memory_list3.clear()
    views.Base.memory_list4.clear()
    views.Base.ins_number.clear()

    return HttpResponse(json.dumps(param123))


def Display_info_IM(request):
    print("This is IM Display")
    views.Base.status = "False"
    views.Base.base_address = 0
    views.Base.jal_imm = {}
    views.Base.j_count = 0
    views.Base.code_line1 = []
    views.Base.error = ""
    views.Base.lui_imm = 0
    views.Base.aui_imm = 0
    views.Base.label_address = {}
    views.Base.whole_code = ""
    views.Base.ins_type = []
    views.Base.destination = []
    views.Base.source1 = []
    views.Base.source2 = []
    views.Base.immediate1 = []
    views.Base.immediate2 = []
    views.Base.opcode = []
    views.Base.func7 = []
    views.Base.func3 = []
    views.Base.func2 = []
    views.Base.func4 = []
    views.Base.func6 = []
    views.Base.pc = []
    views.Base.next = 0
    views.Base.length = 0
    views.Base.data = []
    views.Base.list_column_1 = []
    views.Base.list_column_2 = []
    views.Base.list_column_3 = []
    views.Base.list_column_4 = []
    views.Base.listkey = []
    views.Base.hex = ""
    views.Base.vari = 0
    views.Base.nxt = 0
    views.Base.dump_bin = []
    Error = ''

    request.session['session'] = 0
    views.Base.whole_code = request.POST.get("editline1", "")
    # views.Base.whole_code = "addi x5,x0,12\r\naddi x6,x0,13"
    print(views.Base.whole_code)
    whole_code1 = views.Base.whole_code.replace('\r\n', '\n')
    print(whole_code1)
    for i in range(0, 32):
        instructions.Instruction_type.val[i] = 0
    if re.match("^0x", whole_code1):
        code_line_hex = [line for line in whole_code1.split('\n') if line.strip() != '']
        Bin = []
        for i in range(len(code_line_hex)):
            code_line_hex[i] = re.sub(r"^0x", '', code_line_hex[i])
            Bin.append("{0:032b}".format(int(code_line_hex[i], 16)))

        print(code_line_hex)
        print(Bin)

        opcodeh = []
        desth = []
        funct3h = []
        source1h = []
        immh = []
        code = []
        funct7h = []
        for i in range(len(code_line_hex)):
            if Bin[i][25:32] == "0010011" and Bin[i][17:20] == "000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("addi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "001" and Bin[i][:7] == "0000000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("slli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "010":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("slti" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "011":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("sltiu" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "100":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("xori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0000000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("srli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0100000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("srai" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "110":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("ori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "111":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("andi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))

        print(desth)
        print(source1h)
        print(immh)

        views.Base.data = code
        views.Base.code_line1 = code
    else:
        print("in else")
        error, views.Base.data = views.interpreterIM(whole_code1)
        print(error)
        if error:
            param123 = {'error': error}
            # views.Base.param.update({'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code, 'ctn': 1, 'data': zip(instructions.Instruction_type.val, views.Base.reg_name), 'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4)})
            messages.error(request, error)
            return HttpResponse(json.dumps(param123))
        print(views.Base.data)

        code_line = [line for line in whole_code1.split('\n') if line.strip() != '']
        print("Code Line =")
        print(code_line)

        views.Base.code_line1 = []
        for k in range(len(code_line)):
            if ':' not in code_line[k]:
                views.Base.code_line1.append(code_line[k])
            else:
                continue
    print(views.Base.code_line1)
    r_ins = ['add', 'sub', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
    i_ins = ['lw', 'lb', 'lh', 'lbu', 'lhu', 'slli', 'srli', 'srai', 'addi', 'subi', 'xori',
             'andi',
             'ori', 'slti', 'sltiu', 'fence', 'fence.i', 'scall', 'sbreak', 'jalr']
    sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
    s_ins = ['sb', 'sh', 'sw']
    u_ins = ['lui', 'auipc']
    uj_ins = ['jal']
    mr_ins = ['mul', 'mulh', 'mulhu', 'mulhsu', 'div', 'divu', 'rem', 'remu']
    jal_immediate = []
    ins_mem = []
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    bits = []
    instruction_memory_uni_counter = 0
    print(views.Base.data)
    print(len(views.Base.data))

    print("Code Line1 =")
    print(views.Base.code_line1)
    p_counter = 0
    for i in range(len(views.Base.code_line1)):
        if views.Base.data[i][0] in i_ins or views.Base.data[i][0] in uj_ins or views.Base.data[i][0] in u_ins or views.Base.data[i][0] in sb_ins or views.Base.data[i][0] in s_ins or views.Base.data[i][0] in r_ins or views.Base.data[i][0] in mr_ins:
            views.Base.pc.append('0x' + '{0:01X}'.format(p_counter * 4))
            print(views.Base.pc)
            bits.append(32)
            p_counter = p_counter + 1
        x = views.Base.code_line1[i]
        x = x.lower()
        x = x.strip()
        m = re.search(r'\w+', x)
        m = m.group()
        half_ins = x[len(m) + 1:]
        half_ins = half_ins.replace(" ", "")
        bits.append(32)
        if m in i_ins:
            views.Base.ins_type.append('I')
            if 'lw' in m or 'lh' in m or 'lb' in m or 'lbu' in m or 'lhu' in m:
                # half_ins = re.findall(r'\w\d+|\d+', x)
                half_ins = re.findall(r'[+-]?\d+', x)
                dest = half_ins[0]
                imm = half_ins[1]
                src1 = half_ins[2]
                imm_int = '{0:012b}'.format(int(imm))
                dest_int = '{0:05b}'.format(int(dest))
                src1_int = '{0:05b}'.format(int(src1))
                views.Base.destination.append(dest_int)
                views.Base.source1.append(src1_int)
                views.Base.immediate1.append(imm_int)
                views.Base.immediate2.append('X')
                views.Base.source2.append('X')
                views.Base.opcode.append('0000011')
                if 'lb' in m:
                    views.Base.func3.append('000')
                    views.Base.func7.append('X')
                elif 'lh' in m:
                    views.Base.func3.append('001')
                    views.Base.func7.append('X')
                elif 'lw' in m:
                    views.Base.func3.append('010')
                    views.Base.func7.append('X')
                elif 'lbu' in m:
                    views.Base.func3.append('100')
                    views.Base.func7.append('X')
                elif 'lhu' in m:
                    views.Base.func3.append('101')
                    views.Base.func7.append('X')

                ins_mem.append(
                    str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                        views.Base.destination[i]) + str(views.Base.opcode[i]))
            else:
                half_ins = re.findall(r'[+-]?\d+', x)
                if re.match("^0x", whole_code1):
                    dest = half_ins[0]
                    src1 = half_ins[1]
                    imm = half_ins[2]
                else:
                    # print(views.Base.data[i][1])
                    dest = views.Base.data[i][1]
                    dest = dest[1:]
                    imm = views.Base.data[i][3]
                    src1 = views.Base.data[i][2]
                    src1 = src1[1:]
                dest_int = '{0:05b}'.format(int(dest))
                src1_int = '{0:05b}'.format(int(src1))
                imm_int = ""
                if int(imm) < 0:
                    print("Negative")
                    print(imm)
                    n = int(imm) + 2 ** 32
                    imm_int = ''
                    binary = '{0:012b}'.format(n)
                    binary = binary[::-1]
                    imm_int = binary[:12]
                    imm_int = imm_int[::-1]
                    print(imm_int)
                else:
                    imm_int = '{0:012b}'.format(int(imm))
                views.Base.destination.append(dest_int)
                views.Base.source1.append(src1_int)
                views.Base.immediate2.append('X')
                views.Base.source2.append('X')
                views.Base.opcode.append('0010011')
                if 'addi' in m:
                    views.Base.func3.append('000')
                elif 'slli' in m:
                    views.Base.func3.append('001')
                elif 'sltiu' in m:
                    views.Base.func3.append('011')
                elif 'slti' in m:
                    views.Base.func3.append('010')
                elif 'xori' in m:
                    views.Base.func3.append('100')
                elif 'srli' in m or 'srai' in m:
                    views.Base.func3.append('101')
                elif 'ori' in m:
                    views.Base.func3.append('110')
                elif 'andi' in m:
                    views.Base.func3.append('111')
                if 'slli' in m or 'srli' in m:
                    imm_int = '{0:05b}'.format(int(imm))
                    views.Base.func7.append('0000000')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.func7[i]) + str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                            views.Base.destination[i]) + str(views.Base.opcode[i]))

                elif 'srai' in m:
                    imm_int = '{0:05b}'.format(int(imm))
                    views.Base.func7.append('0100000')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.func7[i]) + str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                            views.Base.destination[i]) + str(views.Base.opcode[i]))

                else:
                    views.Base.func7.append('X')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))
            print(ins_mem)

        elif m in r_ins:
            views.Base.ins_type.append('R')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            src1 = half_ins[1]
            src2 = half_ins[2]
            dest_int = '{0:05b}'.format(int(dest))
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.destination.append(dest_int)
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('X')
            views.Base.immediate2.append('X')
            views.Base.opcode.append('0110011')
            if 'add' in m or 'sub' in m:
                views.Base.func3.append('000')
            elif 'sll' in m:
                views.Base.func3.append('001')
            elif 'sltu' in m:
                views.Base.func3.append('011')
            elif 'slt' in m:
                views.Base.func3.append('010')
            elif 'xor' in m:
                views.Base.func3.append('100')
            elif 'srl' in m or 'sra' in m:
                views.Base.func3.append('101')
            elif 'or' in m:
                views.Base.func3.append('110')
            elif 'and' in m:
                views.Base.func3.append('111')
            if 'sub' in m or 'sra' in m:
                views.Base.func7.append('0100000')
                ins_mem.append(
                    str(views.Base.func7[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                        views.Base.destination[i]) + str(
                        views.Base.opcode[i]))
            else:
                views.Base.func7.append('0000000')
                ins_mem.append(
                    str(views.Base.func7[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                        views.Base.destination[i]) + str(views.Base.opcode[i]))
        elif m in sb_ins:
            views.Base.ins_type.append('SB')
            half_ins = re.findall(r'[+-]?\d+', x)
            src1 = half_ins[0]
            # imm = half_ins[2]
            src2 = half_ins[1]
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('0000000')
            views.Base.immediate2.append('10000')
            views.Base.destination.append('X')
            views.Base.opcode.append('1100011')
            views.Base.func7.append('X')
            if 'beq' in m:
                views.Base.func3.append('000')
            elif 'bne' in m:
                views.Base.func3.append('001')
            elif 'bltu' in m:
                views.Base.func3.append('110')
            elif 'blt' in m:
                views.Base.func3.append('100')
            elif 'bgeu' in m:
                views.Base.func3.append('111')
            elif 'bge' in m:
                views.Base.func3.append('101')
            #ins_mem.append('00000000000000000000000000000000')

            ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(views.Base.immediate2[i]) + str(views.Base.opcode[i]))


        elif m in s_ins:
            views.Base.ins_type.append('S')
            half_ins = re.findall(r'[+-]?\d+', x)
            src1 = half_ins[2]
            dest = half_ins[1]
            dest_int = int(dest) + views.Base.base_address
            imm = half_ins[1]
            src2 = half_ins[0]
            dest_int = '{0:05b}'.format(dest_int)
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            imm_int = '{0:07b}'.format(int(imm))
            views.Base.destination.append('X')
            views.Base.source1.append(src1_int)
            views.Base.immediate1.append(imm_int)
            views.Base.immediate2.append(dest_int)
            views.Base.source2.append(src2_int)
            views.Base.opcode.append('0100011')
            views.Base.func7.append('X')
            if 'sb' in m:
                views.Base.func3.append('000')
            elif 'sh' in m:
                views.Base.func3.append('001')
            elif 'sw' in m:
                views.Base.func3.append('010')
            ins_mem.append(
                str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                    views.Base.immediate2[i]) + str(
                    views.Base.opcode[i]))

        elif m in u_ins:
            views.Base.ins_type.append('U')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            imm = half_ins[1]
            dest_int = '{0:05b}'.format(int(dest))
            if 'auipc' in m:
                views.Base.opcode.append('0010111')
                imm_int = '{0:020b}'.format(int(imm))
                views.Base.immediate1.append(imm_int)
            else:
                views.Base.opcode.append('0110111')
                imm_int = '{0:020b}'.format(int(imm))
                views.Base.immediate1.append(imm_int)
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.destination.append(dest_int)
            views.Base.immediate2.append('X')
            ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif m in uj_ins:
            views.Base.ins_type.append('UJ')
            half_ins = re.findall(r'[+-]?\d+', x)
            # dest = half_ins[0]
            # dest_int = '{0.05b}'.format(int(dest))
            views.Base.destination.append('00001')
            views.Base.opcode.append('1101111')
            for key in views.Base.jal_imm:
                if key in x:
                    imm = views.Base.jal_imm[key]
            imm_int = '{0:020b}'.format(int(imm))
            views.Base.immediate1.append(imm_int)
            views.Base.j_count += 1
            # print("Value of JUMP : " + str(views.Base.jal_imm))
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.immediate2.append('X')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif 'ret' in m or 'ebreak' in m:
            views.Base.ins_type.append('X')
            views.Base.opcode.append('X')
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.destination.append('X')
            views.Base.immediate2.append('X')
            views.Base.immediate1.append('X')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif m in mr_ins:
            views.Base.ins_type.append('R')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            src1 = half_ins[1]
            src2 = half_ins[2]
            dest_int = '{0:05b}'.format(int(dest))
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.destination.append(dest_int)
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('X')
            views.Base.immediate2.append('X')
            views.Base.opcode.append('0110011')
            if m == 'mul':
                views.Base.func3.append('000')
            elif m == 'mulh':
                views.Base.func3.append('001')
            elif 'mulhsu' in m:
                views.Base.func3.append('010')
            elif 'mulhu' in m:
                views.Base.func3.append('011')
            elif m == 'div':
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in DIV'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('100')
            elif 'divu' in m:
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in DIVU'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('101')
            elif m == 'rem':
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in REM'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('110')
            elif 'remu' in m:
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in REMU'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('111')
            views.Base.func7.append('0000001')
            ins_mem.append(
                str(views.Base.func7[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                    views.Base.destination[i]) + str(views.Base.opcode[i]))
        else:
            continue

        views.Base.func2.append('X')
        views.Base.func4.append('X')
        views.Base.func6.append('X')

        ####### Transfering instruction bits into dump list #######
        views.Base.dump_bin.append([bits[i], ins_mem[i]])
        ###########################################################

    for k in ins_mem:
        l3.append(k[:8])
        l2.append(k[8:16])
        l1.append(k[16:24])
        l0.append(k[24:32])
    print(l3)
    print(l2)
    print(l1)
    print(l0)
    for k in range(len(ins_mem)):
        l3[k] = '{0:02X}'.format(int(l3[k], 2))
        l2[k] = '{0:02X}'.format(int(l2[k], 2))
        l1[k] = '{0:02X}'.format(int(l1[k], 2))
        l0[k] = '{0:02X}'.format(int(l0[k], 2))
    print(l3)
    print(l2)
    print(l1)
    print(l0)

    for i in range(0, len(views.Base.code_line1)):
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter)] = int(
            l0[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 1)] = int(l1[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 2)] = int(l2[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 3)] = int(l3[i], 16)

        instruction_memory_uni_counter += 4

    # print(views.Base.ins_type)

    ##### This Is Memory Block START
    ###When using Online web
    file_values=open("/home/merloxygen/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
    ###when using dedicated machine(PC)

    # file_values = open("templates\m.txt", "r")
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
    views.Base.listkey = []
    for x in range(0, 512):
        if (x == 512 / 4):
            break
        views.Base.listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
        counter_memory_address = counter_memory_address + 4

    #########################################################
    for i in range(0, 512 * 4):
        # memory_dictionary[hex(i)]=memory_value[i]
        instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(i)]
    #########################################################

    ########################################################## Memory  breaking For Views

    count_memory_break_view = 0
    for i in range(0, 514 * 4):
        if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
            break
        views.Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
        views.Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
        views.Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
        views.Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
        count_memory_break_view = count_memory_break_view + 4

    ########################################################## Memory  breaking For Views

    ########################################################## Address Division For Views

    ########################################################## Address Division For Views
    # views.Base.param.update({'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code, 'data': zip(instructions.Instruction_type.val, views.Base.reg_name), 'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4), 'data3': zip(views.Base.pc, views.Base.code_line1, views.Base.ins_type, views.Base.immediate1, views.Base.func7, views.Base.source2, views.Base.source1, views.Base.func3, views.Base.destination, views.Base.immediate2, views.Base.opcode), 'ctn': 1})
    # print(views.Base.param)
    # return render(request, 'index.html', views.Base.param)
    param123 = {'length': len(views.Base.code_line1), 'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code,
                'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
                'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4, 'pc': views.Base.pc, 'codes': views.Base.code_line1,
                'ins_type': views.Base.ins_type, 'imm1': views.Base.immediate1, 'f7': views.Base.func7, 'f6': views.Base.func6, 'f4': views.Base.func4,'s2': views.Base.source2,
                's1': views.Base.source1, 'f3': views.Base.func3, 'f2': views.Base.func2, 'dest': views.Base.destination, 'imm2': views.Base.immediate2,
                'opcode': views.Base.opcode, 'ctn': 1}
    print(param123)

    views.Base.stack_register.clear()
    views.Base.memory_list1.clear()
    views.Base.memory_list2.clear()
    views.Base.memory_list3.clear()
    views.Base.memory_list4.clear()
    views.Base.ins_number.clear()

    return HttpResponse(json.dumps(param123))


def Display_info_IMC(request):
    views.Base.status = "False"
    views.Base.base_address = 0
    views.Base.jal_imm = {}
    views.Base.j_count = 0
    views.Base.code_line1 = []
    views.Base.error = ""
    views.Base.lui_imm = 0
    views.Base.aui_imm = 0
    views.Base.label_address = {}
    views.Base.whole_code = ""
    views.Base.ins_type = []
    views.Base.destination = []
    views.Base.source1 = []
    views.Base.source2 = []
    views.Base.immediate1 = []
    views.Base.immediate2 = []
    views.Base.opcode = []
    views.Base.func7 = []
    views.Base.func3 = []
    views.Base.func2 = []
    views.Base.func4 = []
    views.Base.func6 = []
    views.Base.pc = []
    views.Base.next = 0
    views.Base.length = 0
    views.Base.data = []
    views.Base.list_column_1 = []
    views.Base.list_column_2 = []
    views.Base.list_column_3 = []
    views.Base.list_column_4 = []
    views.Base.listkey = []
    views.Base.dump_bin = []
    views.Base.hex = ""
    views.Base.vari = 0
    views.Base.nxt = 0
    bits = []
    Error = ''

    request.session['session'] = 0
    views.Base.whole_code = request.POST.get('editline2', '')
    #views.Base.whole_code = "addi x1,x0,-1"
    # views.Base.whole_code = views.Base.whole_code
    whole_code1 = views.Base.whole_code.replace('\r\n', '\n')
    for i in range(0, 32):
        instructions.Instruction_type.val[i] = 0
    if re.match("^0x", whole_code1):
        code_line_hex = [line for line in whole_code1.split('\n') if line.strip() != '']
        Bin = []
        for i in range(len(code_line_hex)):
            code_line_hex[i] = re.sub(r"^0x", '', code_line_hex[i])
            Bin.append("{0:032b}".format(int(code_line_hex[i], 16)))

        print(code_line_hex)
        print(Bin)

        opcodeh = []
        desth = []
        funct3h = []
        source1h = []
        immh = []
        code = []
        funct7h = []
        for i in range(len(code_line_hex)):
            if Bin[i][25:32] == "0010011" and Bin[i][17:20] == "000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("addi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "001" and Bin[i][:7] == "0000000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("slli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "010":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("slti" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "011":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("sltiu" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "100":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][:12], 2))
                code.append("xori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0000000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("srli" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "101" and Bin[i][:7] == "0100000":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("srai" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "110":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("ori" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))
            elif Bin[i][25:32] == "0010011" and Bin[i][17:20] == "111":
                opcodeh.append(Bin[i][25:32])
                desth.append(int(Bin[i][20:25], 2))
                funct3h.append(Bin[i][17:20])
                source1h.append(int(Bin[i][12:17], 2))
                immh.append(int(Bin[i][7:12], 2))
                funct7h.append(int(Bin[i][:7], 2))
                code.append("andi" + " x" + str(desth[i]) + ",x" + str(source1h[i]) + "," + str(immh[i]))

        print(desth)
        print(source1h)
        print(immh)

        views.Base.data = code
        views.Base.code_line1 = code
    else:
        print("in else")
        error, views.Base.data = views.interpreter(whole_code1)
        print(error)
        if error:
            param123 = {'error': error}
            # views.Base.param.update({'result': "True", 'status1': views.Base.status, 'code': views.Base.whole_code, 'ctn': 1, 'data': zip(instructions.Instruction_type.val, views.Base.reg_name), 'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4)})
            messages.error(request, error)
            return HttpResponse(json.dumps(param123))

        print(views.Base.data)
        code_line = [line for line in whole_code1.split('\n') if line.strip() != '']

        views.Base.code_line1 = []
        for k in range(len(code_line)):
            if ':' not in code_line[k]:
                views.Base.code_line1.append(code_line[k])
            else:
                continue

    r_ins = ['add', 'sub', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
    i_ins = ['lw', 'lb', 'lh', 'lbu', 'lhu', 'slli', 'srli', 'srai', 'addi', 'subi', 'muli', 'divi', 'remi', 'xori',
             'andi',
             'ori', 'slti', 'sltiu', 'fence', 'fence.i', 'scall', 'sbreak', 'jalr']
    sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
    s_ins = ['sb', 'sh', 'sw']
    u_ins = ['lui', 'auipc']
    uj_ins = ['jal']
    mr_ins = ['mul', 'mulh', 'mulhu', 'mulhsu', 'div', 'divu', 'rem', 'remu']
    ci_ins = ['c.addi', 'c.addiw', 'c.ldsp', 'c.lwsp', 'c.lqsp', 'c.addiw', 'c.addi16sp', 'c.li', 'c.lui', 'c.slli',
              'c.break', 'c.srli', 'c.srai']
    cl_ins = ['c.lw', 'c.ld', 'c.lq']
    cs_ins = ['c.sw', 'c.sd', 'c.sq']
    css_ins = ['c.swsp', 'c.sdsp', 's.sqsp']
    cr_ins = ['c.add', 'c.mv', 'c.jr', 'c.jalr', 'c.ebreak']
    ca_ins = ['c.and', 'c.or', 'c.sub', 'c.subw', 'c.xor', 'c.addw']
    ciw_ins = ['c.addi4sp']
    cb_ins = ['c.beqz', 'c.bnez', 'c.andi']
    cj_ins = ['c.j', 'c.jal']
    jal_immediate = []
    ins_mem = []
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    pc_count = 0
    views.Base.data = code_line
    instruction_memory_uni_counter = 0
    views.Base.pc.append('0x' + '{0:01X}'.format(0))
    for i in range(len(views.Base.data)):
        # x = views.Base.code_line1[i]
        x = code_line[i]
        x = x.lower()
        x = x.strip()
        m = re.search(r'^c.\w+|\w+', x)
        m = m.group()
        half_ins = x[len(m) + 1:]
        half_ins = half_ins.replace(" ", "")
        print(m)
        if i < len(views.Base.code_line1):
            if m in ci_ins or m in cr_ins or m in cs_ins or m in css_ins or m in cj_ins or m in cb_ins or m in cl_ins or m in ciw_ins or m in ca_ins:
                pc_count = pc_count + 2
                bits.append(16)
                views.Base.pc.append('0x' + '{0:01X}'.format(pc_count))
            elif m in i_ins or m in uj_ins or m in u_ins or m in sb_ins or m in s_ins or m in r_ins or m in mr_ins:
                pc_count = pc_count + 4
                views.Base.pc.append('0x' + '{0:01X}'.format(pc_count))
                bits.append(32)
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
        print(views.Base.pc)
        if m in i_ins:
            views.Base.ins_type.append('I')
            if 'lw' in m or 'lh' in m or 'lb' in m or 'lbu' in m or 'lhu' in m:
                # half_ins = re.findall(r'\w\d+|\d+', x)
                half_ins = re.findall(r'[+-]?\d+', x)
                dest = half_ins[0]
                imm = half_ins[1]
                src1 = half_ins[2]
                imm_int = '{0:012b}'.format(int(imm))
                dest_int = '{0:05b}'.format(int(dest))
                src1_int = '{0:05b}'.format(int(src1))
                views.Base.destination.append(dest_int)
                views.Base.source1.append(src1_int)
                views.Base.immediate1.append(imm_int)
                views.Base.immediate2.append('X')
                views.Base.source2.append('X')
                views.Base.opcode.append('0000011')
                if 'lb' in m:
                    views.Base.func3.append('000')
                    views.Base.func7.append('X')
                elif 'lh' in m:
                    views.Base.func3.append('001')
                    views.Base.func7.append('X')
                elif 'lw' in m:
                    views.Base.func3.append('010')
                    views.Base.func7.append('X')
                elif 'lbu' in m:
                    views.Base.func3.append('100')
                    views.Base.func7.append('X')
                elif 'lhu' in m:
                    views.Base.func3.append('101')
                    views.Base.func7.append('X')

                ins_mem.append(
                    str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                        views.Base.destination[i]) + str(views.Base.opcode[i]))
            else:
                half_ins = re.findall(r'[+-]?\d+', x)
                if re.match("^0x", whole_code1):
                    dest = half_ins[0]
                    src1 = half_ins[1]
                    imm = half_ins[2]
                else:
                    # print(views.Base.data[i][1])
                    # dest = views.Base.data[i][1]
                    # dest = dest[1:]
                    # imm = views.Base.data[i][3]
                    # src1 = views.Base.data[i][2]
                    # src1 = src1[1:]
                    dest = half_ins[0]
                    imm = half_ins[2]
                    src1 = half_ins[1]
                dest_int = '{0:05b}'.format(int(dest))
                src1_int = '{0:05b}'.format(int(src1))
                imm_int = ""
                if int(imm) < 0:
                    print("Negative")
                    print(imm)
                    n = int(imm) + 2 ** 32
                    imm_int = ''
                    binary = '{0:012b}'.format(n)
                    binary = binary[::-1]
                    imm_int = binary[:12]
                    imm_int = imm_int[::-1]
                    print(imm_int)
                else:
                    imm_int = '{0:012b}'.format(int(imm))
                views.Base.destination.append(dest_int)
                views.Base.source1.append(src1_int)
                views.Base.immediate2.append('X')
                views.Base.source2.append('X')
                views.Base.opcode.append('0010011')
                if 'addi' in m:
                    views.Base.func3.append('000')
                elif 'slli' in m:
                    views.Base.func3.append('001')
                elif 'sltiu' in m:
                    views.Base.func3.append('011')
                elif 'slti' in m:
                    views.Base.func3.append('010')
                elif 'xori' in m:
                    views.Base.func3.append('100')
                elif 'srli' in m or 'srai' in m:
                    views.Base.func3.append('101')
                elif 'ori' in m:
                    views.Base.func3.append('110')
                elif 'andi' in m:
                    views.Base.func3.append('111')
                if 'slli' in m or 'srli' in m:
                    imm_int = '{0:05b}'.format(int(imm))
                    views.Base.func7.append('0000000')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.func7[i]) + str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(
                            views.Base.func3[i]) + str(
                            views.Base.destination[i]) + str(views.Base.opcode[i]))

                elif 'srai' in m:
                    imm_int = '{0:05b}'.format(int(imm))
                    views.Base.func7.append('0100000')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.func7[i]) + str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(
                            views.Base.func3[i]) + str(
                            views.Base.destination[i]) + str(views.Base.opcode[i]))

                else:
                    views.Base.func7.append('X')
                    views.Base.immediate1.append(imm_int)
                    ins_mem.append(
                        str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                            views.Base.destination[i]) + str(views.Base.opcode[i]))
            print(ins_mem)


        elif m in r_ins:

            views.Base.ins_type.append('R')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            src1 = half_ins[1]
            src2 = half_ins[2]
            dest_int = '{0:05b}'.format(int(dest))
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.destination.append(dest_int)
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('X')
            views.Base.immediate2.append('X')
            views.Base.opcode.append('0110011')
            if 'add' in m or 'sub' in m:
                views.Base.func3.append('000')
            elif 'sll' in m:
                views.Base.func3.append('001')
            elif 'sltu' in m:
                views.Base.func3.append('011')
            elif 'slt' in m:
                views.Base.func3.append('010')
            elif 'xor' in m:
                views.Base.func3.append('100')
            elif 'srl' in m or 'sra' in m:
                views.Base.func3.append('101')
            elif 'or' in m:
                views.Base.func3.append('110')
            elif 'and' in m:
                views.Base.func3.append('111')
            if 'sub' in m or 'sra' in m:
                views.Base.func7.append('0100000')
                ins_mem.append(
                    str(views.Base.func7[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(
                        views.Base.func3[i]) + str(views.Base.destination[i]) + str(
                        views.Base.opcode[i]))
            else:
                views.Base.func7.append('0000000')
                ins_mem.append(
                    str(views.Base.func7[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(
                        views.Base.func3[i]) + str(views.Base.destination[i]) + str(
                        views.Base.opcode[i]))

        elif m in sb_ins:

            views.Base.ins_type.append('SB')
            half_ins = re.findall(r'[+-]?\d+', x)
            src1 = half_ins[0]
            # imm = half_ins[2]
            src2 = half_ins[1]
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('0000000')
            views.Base.immediate2.append('10100')
            views.Base.destination.append('X')
            views.Base.opcode.append('1100011')
            views.Base.func7.append('X')
            if 'beq' in m:
                views.Base.func3.append('000')
            elif 'bne' in m:
                views.Base.func3.append('001')
            elif 'bltu' in m:
                views.Base.func3.append('110')
            elif 'blt' in m:
                views.Base.func3.append('100')
            elif 'bgeu' in m:
                views.Base.func3.append('111')
            elif 'bge' in m:
                views.Base.func3.append('101')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(views.Base.immediate2[i]) + str(views.Base.opcode[i]))

        elif m in s_ins:

            views.Base.ins_type.append('S')
            half_ins = re.findall(r'[+-]?\d+', x)
            src1 = half_ins[2]
            dest = half_ins[1]
            dest_int = int(dest) + views.Base.base_address
            imm = half_ins[1]
            src2 = half_ins[0]
            dest_int = '{0:05b}'.format(dest_int)
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            imm_int = '{0:07b}'.format(int(imm))
            views.Base.destination.append('X')
            views.Base.source1.append(src1_int)
            views.Base.immediate1.append(imm_int)
            views.Base.immediate2.append(dest_int)
            views.Base.source2.append(src2_int)
            views.Base.opcode.append('0100011')
            views.Base.func7.append('X')
            if 'sb' in m:
                views.Base.func3.append('000')
            elif 'sh' in m:
                views.Base.func3.append('001')
            elif 'sw' in m:
                views.Base.func3.append('010')
            ins_mem.append(
                str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(
                    views.Base.func3[i]) + str(views.Base.immediate2[i]) + str(
                    views.Base.opcode[i]))

        elif m in u_ins:
            views.Base.ins_type.append('U')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            imm = half_ins[1]
            print("Imm")
            print(imm)
            dest_int = '{0:05b}'.format(int(dest))
            if 'auipc' in m:
                views.Base.opcode.append('0010111')
                imm_int = '{0:020b}'.format(int(imm))
                views.Base.immediate1.append(imm_int)
            else:
                print("Imm int")
                views.Base.opcode.append('0110111')
                imm_int = '{0:020b}'.format(int(imm))
                print(imm_int)
                views.Base.immediate1.append(imm_int)
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.destination.append(dest_int)
            views.Base.immediate2.append('X')
            ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif m in uj_ins:

            views.Base.ins_type.append('UJ')
            half_ins = re.findall(r'[+-]?\d+', x)
            # dest = half_ins[0]
            # dest_int = '{0.05b}'.format(int(dest))
            views.Base.destination.append('00001')
            views.Base.opcode.append('1101111')
            for key in views.Base.jal_imm:
                if key in x:
                    imm = views.Base.jal_imm[key]
            imm_int = '{0:020b}'.format(int(imm))
            views.Base.immediate1.append(imm_int)
            views.Base.j_count += 1
            # print("Value of JUMP : " + str(views.Base.jal_imm))
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.func2.append('X')
            views.Base.func4.append('X')
            views.Base.func6.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.immediate2.append('X')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif 'ret' in m or m == 'ebreak':

            views.Base.ins_type.append('X')
            views.Base.opcode.append('X')
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.func2.append('X')
            views.Base.func4.append('X')
            views.Base.func6.append('X')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.destination.append('X')
            views.Base.immediate2.append('X')
            views.Base.immediate1.append('X')
            ins_mem.append('00000000000000000000000000000000')
            # ins_mem.append(str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif m in mr_ins:
            views.Base.ins_type.append('R')
            half_ins = re.findall(r'[+-]?\d+', x)
            dest = half_ins[0]
            src1 = half_ins[1]
            src2 = half_ins[2]
            dest_int = '{0:05b}'.format(int(dest))
            src1_int = '{0:05b}'.format(int(src1))
            src2_int = '{0:05b}'.format(int(src2))
            views.Base.destination.append(dest_int)
            views.Base.source1.append(src1_int)
            views.Base.source2.append(src2_int)
            views.Base.immediate1.append('X')
            views.Base.immediate2.append('X')
            views.Base.opcode.append('0110011')
            if m == 'mul':
                views.Base.func3.append('000')
            elif m == 'mulh':
                views.Base.func3.append('001')
            elif 'mulhsu' in m:
                views.Base.func3.append('010')
            elif 'mulhu' in m:
                views.Base.func3.append('011')
            elif m == 'div':
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in DIV'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('100')
            elif 'divu' in m:
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in DIVU'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('101')
            elif m == 'rem':
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in REM'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('110')
            elif 'remu' in m:
                if int(src2) == 0:
                    Error = 'Source two Register should not be zero in REMU'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                views.Base.func3.append('111')
            views.Base.func7.append('0000001')
            ins_mem.append(
                str(views.Base.func7[i]) + str(views.Base.source2[i]) + str(views.Base.source1[i]) + str(views.Base.func3[i]) + str(
                    views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif m in cr_ins:
            views.Base.ins_type.append('CR')
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.immediate2.append('X')
            views.Base.immediate1.append('X')
            half_ins = re.findall(r'[+-]?\d+', x)
            if 'c.add' in m:
                src2 = half_ins[1]
                dest = half_ins[0]
                if int(dest) == 0 or int(src2) == 0:
                    Error = 'Destination Register and Source Register should not be x0(zero) in C.ADD'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func4.append('1001')
                    views.Base.opcode.append('10')
                    views.Base.func2.append('X')
                    views.Base.func6.append('X')
                    views.Base.source1.append('X')
                    views.Base.source2.append(src2_int)
                    views.Base.destination.append(dest_int)
                    print(i)
                    ins_mem.append("0000000000000000" + str(views.Base.func4[i]) + str(views.Base.destination[i]) + str(views.Base.source2[i]) + str(views.Base.opcode[i]))
            elif 'c.mv' in m:
                src2 = half_ins[1]
                dest = half_ins[0]
                if int(dest) == 0 or int(src2) == 0:
                    Error = 'Destination Register and Source Register should not be x0(zero) in C.MV'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func4.append('1000')
                    views.Base.opcode.append('10')
                    views.Base.func2.append('X')
                    views.Base.source1.append('X')
                    views.Base.func6.append('X')
                    views.Base.source2.append(src2_int)
                    views.Base.destination.append(dest_int)
                    print(i)
                    ins_mem.append("0000000000000000" + str(views.Base.func4[i]) + str(views.Base.destination[i]) + str(views.Base.source2[i]) + str(views.Base.opcode[i]))
            elif 'c.jr' in m:
                src1 = half_ins[2]
                src2 = half_ins[0]
                if int(src1) == 0 or int(src2) != 0:
                    Error = 'Source One Register should not be x0(zero) and Source two Register should be x0(zero) in C.JR'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    src1_int = '{0:05b}'.format(int(src1))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func4.append('1000')
                    views.Base.opcode.append('10')
                    views.Base.func2.append('X')
                    views.Base.func6.append('X')
                    views.Base.source2.append(src2_int)
                    views.Base.source1.append(src1_int)
                    views.Base.destination.append('X')
                    print(i)
                    ins_mem.append("0000000000000000" + str(views.Base.func4[i]) + str(views.Base.source1[i]) + str(views.Base.source2[i]) + str(views.Base.opcode[i]))
            elif 'c.jalr' in m:
                src1 = half_ins[2]
                src2 = half_ins[0]
                if int(src1) == 0 or int(src2) != 1:
                    Error = 'Source One Register should not be x0(zero) and Source two Register should be x1(ra) in C.JALR'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    src1_int = '{0:05b}'.format(int(src1))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func4.append('1001')
                    views.Base.opcode.append('10')
                    views.Base.func2.append('X')
                    views.Base.func6.append('X')
                    views.Base.source2.append(src2_int)
                    views.Base.source1.append(src1_int)
                    views.Base.destination.append('X')
                    print(i)
                    ins_mem.append("0000000000000000" + str(views.Base.func4[i]) + str(views.Base.source1[i]) + str(views.Base.source2[i]) + str(views.Base.opcode[i]))
            elif 'c.ebreak' in m:
                views.Base.func4.append('1001')
                views.Base.opcode.append('10')
                views.Base.func2.append('X')
                views.Base.func6.append('X')
                views.Base.source2.append('00000')
                views.Base.source1.append('00000')
                views.Base.destination.append('X')
                print(i)
                ins_mem.append("0000000000000000" + str(views.Base.func4[i]) + str(views.Base.source1[i]) + str(views.Base.source2[i]) + str(views.Base.opcode[i]))

        elif m in ca_ins:
            views.Base.ins_type.append('CA')
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.immediate2.append('X')
            views.Base.immediate1.append('X')
            views.Base.source1.append('X')
            half_ins = re.findall(r'[+-]?\d+', x)
            src2 = half_ins[1]
            dest = half_ins[0]
            if int(dest) < 8 or int(dest) > 15 or int(src2) < 8 or int(src2) > 15:
                Error = 'Destination and Source Register should be greater than x8(s0) and less than x15(a5) in ' + m.upper()
                dict1 = {'Error': Error, 'error': True}
                return HttpResponse(json.dumps(dict1))
            else:
                if 'c.sub' in m:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func6.append('100011')
                    views.Base.func2.append('00')
                    views.Base.func4.append('X')
                    views.Base.opcode.append('01')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.destination.append(dest_int[2:5])
                    ins_mem.append('0000000000000000' +
                        str(views.Base.func6[i]) + str(views.Base.destination[i]) + str(views.Base.func2[i]) + str(
                            views.Base.source2[i]) + str(views.Base.opcode[i]))
                elif 'c.subw' in m:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func6.append('100111')
                    views.Base.func2.append('00')
                    views.Base.func4.append('X')
                    views.Base.opcode.append('01')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.destination.append(dest_int[2:5])
                    ins_mem.append('0000000000000000' +
                        str(views.Base.func6[i]) + str(views.Base.destination[i]) + str(views.Base.func2[i]) + str(
                            views.Base.source2[i]) + str(views.Base.opcode[i]))
                elif 'c.addw' in m:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func6.append('100111')
                    views.Base.func2.append('01')
                    views.Base.func4.append('X')
                    views.Base.opcode.append('01')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.destination.append(dest_int[2:5])
                    ins_mem.append('0000000000000000' + str(views.Base.func6[i]) + str(views.Base.destination[i]) + str(views.Base.func2[i]) + str(
                        views.Base.source2[i]) + str(views.Base.opcode[i]))
                elif 'c.or' in m:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func6.append('100011')
                    views.Base.func2.append('10')
                    views.Base.func4.append('X')
                    views.Base.opcode.append('01')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.destination.append(dest_int[2:5])
                    ins_mem.append('0000000000000000' + str(views.Base.func6[i]) + str(views.Base.destination[i]) + str(views.Base.func2[i]) + str(
                        views.Base.source2[i]) + str(views.Base.opcode[i]))
                elif 'c.and' in m:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func6.append('100011')
                    views.Base.func2.append('11')
                    views.Base.func4.append('X')
                    views.Base.opcode.append('01')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.destination.append(dest_int[2:5])
                    ins_mem.append('0000000000000000' + str(views.Base.func6[i]) + str(views.Base.destination[i]) + str(views.Base.func2[i]) + str(
                        views.Base.source2[i]) + str(views.Base.opcode[i]))
                elif 'c.xor' in m:
                    dest_int = '{0:05b}'.format(int(dest))
                    src2_int = '{0:05b}'.format(int(src2))
                    views.Base.func6.append('100011')
                    views.Base.func2.append('01')
                    views.Base.func4.append('X')
                    views.Base.opcode.append('01')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.destination.append(dest_int[2:5])
                    ins_mem.append('0000000000000000' + str(views.Base.func6[i]) + str(views.Base.destination[i]) + str(views.Base.func2[i]) + str(
                        views.Base.source2[i]) + str(views.Base.opcode[i]))

        elif m in ci_ins:
            views.Base.ins_type.append('CI')
            half_ins = re.findall(r'[+-]?\d+', x)
            imm = half_ins[1]
            dest = half_ins[0]
            print("dest")
            print(dest)
            print("imm")
            print(imm)
            if m == "c.addi":
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if dest == "0" or imm == "0":
                    Error = 'Destination Register and immediate should not be zero in C.ADDI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    if int(imm) < 0:
                        print("Negative")
                        print(imm)
                        n = int(imm) + 2 ** 32
                        imm_int = ''
                        binary = '{0:06b}'.format(n)
                        binary = binary[::-1]
                        imm_int = binary[:6]
                        imm_int = imm_int[::-1]
                        print(imm_int)
                    else:
                        imm_int = '{0:06b}'.format(int(imm))
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    views.Base.func3.append('000')
                    views.Base.destination.append(dest_int)
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.addiw' in m:
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if dest == "0":
                    Error = 'Destination Register should not be x0(zero) in C.ADDIW'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:06b}'.format(int(imm))
                    views.Base.func3.append('001')
                    views.Base.destination.append(dest_int)
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.li' in m:
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if dest == "0":
                    Error = 'Destination Register should not be x0(zero) in C.LI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    if int(imm) < 0:
                        print("Negative")
                        print(imm)
                        n = int(imm) + 2 ** 32
                        imm_int = ''
                        binary = '{0:06b}'.format(n)
                        binary = binary[::-1]
                        imm_int = binary[:6]
                        imm_int = imm_int[::-1]
                        print(imm_int)
                    else:
                        imm_int = '{0:06b}'.format(int(imm))
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    views.Base.func3.append('010')
                    views.Base.destination.append(dest_int)
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.lui' in m:
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if dest == "0" or dest == "2" or imm == "0":
                    Error = 'Destination Register should not be x0(zero) or x2(sp) and immediate should not be zero in C.LUI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:06b}'.format(int(imm))
                    views.Base.func3.append('011')
                    views.Base.destination.append(dest_int)
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.slli' in m:
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if dest == "0" or int(imm) <= 0:
                    Error = 'Destination Register should not be x0(zero) and immediate should be greater than zero in C.SLLI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                elif int(imm) < 32:
                    views.Base.opcode.append('10')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:06b}'.format(int(imm))
                    views.Base.func3.append('000')
                    views.Base.destination.append(dest_int)
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.srli' in m:
                views.Base.source1.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if int(dest) < 8 or int(dest) > 15 or int(imm) < 0:
                    Error = 'Destination Register should be greater than x8(s0) and less than x15(a5) and immediate should be greater or equal to zero in C.SRLI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                elif int(imm) < 32:
                    views.Base.func2.append('00')
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:06b}'.format(int(imm))
                    views.Base.func3.append('100')
                    views.Base.destination.append(dest_int[2:5])
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.func2[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.srai' in m:
                views.Base.source1.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if int(dest) < 8 or int(dest) > 15 or int(imm) < 0:
                    Error = 'Destination Register should be greater than x8(s0) and less than x15(a5) and immediate should be greater or equal to zero in C.SRAI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                elif int(imm) < 32:
                    views.Base.func2.append('01')
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:06b}'.format(int(imm))
                    views.Base.func3.append('100')
                    views.Base.destination.append(dest_int[2:5])
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.func2[i]) + str(views.Base.destination[i]) + str(
                        views.Base.immediate2[i]) + str(views.Base.opcode[i]))
            elif 'c.addi16sp' in m:
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                dest = half_ins[1]
                print("dest")
                print(dest)
                if dest == "2":
                    imm = half_ins[2]
                    if int(imm) != 0:
                        views.Base.opcode.append('01')
                        dest_int = '{0:05b}'.format(int(dest))
                        imm_int = '{0:06b}'.format(int(imm))
                        views.Base.func3.append('011')
                        views.Base.destination.append(dest_int)
                        views.Base.immediate2.append(imm_int[1:6])
                        views.Base.immediate1.append(imm_int[0:1])
                        ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                            views.Base.immediate2[i]) + str(views.Base.opcode[i]))
                else:
                    Error = 'Destination Register should be x2(sp) in C.ADDI16SP'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
            elif 'c.lwsp' in m:
                views.Base.source1.append('X')
                views.Base.func2.append('X')
                views.Base.func4.append('X')
                views.Base.func6.append('X')
                views.Base.func7.append('X')
                views.Base.source2.append('X')
                if dest == "0" or int(imm) % 4 != 0:
                    Error = 'Destination Register should not be x0(zero) and immediate should be multiple of 4 in C.LWSP'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('10')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:032b}'.format(int(imm * 4))
                    views.Base.func3.append('010')
                    views.Base.destination.append(dest_int)
                    views.Base.immediate2.append(imm_int[27:30] + imm_int[24:26])
                    views.Base.immediate1.append(imm_int[26:27])
                    ins_mem.append('0000000000000000' +
                        str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
                            views.Base.immediate2[i]) + str(
                            views.Base.opcode[i]))
            # elif 'c.lqsp' in m:
            #     views.Base.source1.append('X')
            #     views.Base.func2.append('X')
            #     views.Base.func4.append('X')
            #     views.Base.func6.append('X')
            #     views.Base.func7.append('X')
            #     views.Base.source2.append('X')
            #     views.Base.opcode.append('10')
            #     dest_int = '{0:05b}'.format(int(dest))
            #     imm_int = '{0:032b}'.format(int(imm * 8))
            #     views.Base.func3.append('001')
            #     views.Base.destination.append(dest_int)
            #     views.Base.immediate2.append(imm_int[27:28] + imm_int[22:26])
            #     views.Base.immediate1.append(imm_int[26:27])
            #     ins_mem.append('0000000000000000' +
            #         str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
            #             views.Base.immediate2[i]) + str(
            #             views.Base.opcode[i]))
            # elif 'c.ldsp' in m:
            #     views.Base.source1.append('X')
            #     views.Base.func2.append('X')
            #     views.Base.func4.append('X')
            #     views.Base.func6.append('X')
            #     views.Base.func7.append('X')
            #     views.Base.source2.append('X')
            #     views.Base.opcode.append('10')
            #     dest_int = '{0:05b}'.format(int(dest))
            #     imm_int = '{0:032b}'.format(int(imm * 16))
            #     views.Base.func3.append('011')
            #     views.Base.destination.append(dest_int)
            #     views.Base.immediate2.append(imm_int[27:29] + imm_int[23:26])
            #     views.Base.immediate1.append(imm_int[26:27])
            #     ins_mem.append('0000000000000000' +
            #         str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.destination[i]) + str(
            #             views.Base.immediate2[i]) + str(views.Base.opcode[i]))

        elif m in css_ins:
            views.Base.ins_type.append('CSS')
            views.Base.func7.append('X')
            views.Base.func2.append('X')
            views.Base.func4.append('X')
            views.Base.func6.append('X')
            views.Base.source1.append('X')
            views.Base.immediate2.append('X')
            views.Base.destination.append('X')
            half_ins = re.findall(r'[+-]?\d+', x)
            imm = half_ins[1]
            src2 = half_ins[0]
            dest = half_ins[2]
            if 'c.swsp' in m:
                if dest != "2":
                    Error = 'Destination Register should not be x2(sp) in C.SWSP'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('10')
                    src2_int = '{0:05b}'.format(int(src2))
                    imm_int = '{0:032b}'.format(int(imm * 4))
                    views.Base.func3.append('110')
                    views.Base.source2.append(src2_int)
                    views.Base.immediate1.append(imm_int[26:30] + imm_int[24:26])
                    ins_mem.append('0000000000000000' +
                        str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(
                            views.Base.opcode[i]))
            # elif 'c.sqsp' in m:
            #     views.Base.opcode.append('10')
            #     src2_int = '{0:05b}'.format(int(src2))
            #     imm_int = '{0:032b}'.format(int(imm * 8))
            #     views.Base.func3.append('101')
            #     views.Base.source2.append(src2_int)
            #     views.Base.immediate1.append(imm_int[26:28] + imm_int[22:26])
            #     ins_mem.append('0000000000000000' +
            #         str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(
            #             views.Base.opcode[i]))
            # elif 'c.sdsp' in m:
            #     views.Base.opcode.append('10')
            #     src2_int = '{0:05b}'.format(int(src2))
            #     imm_int = '{0:032b}'.format(int(imm * 16))
            #     views.Base.func3.append('111')
            #     views.Base.source2.append(src2_int)
            #     views.Base.immediate1.append(imm_int[26:29] + imm_int[23:26])
            #     ins_mem.append('0000000000000000' +
            #         str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.source2[i]) + str(
            #             views.Base.opcode[i]))

        elif m in cs_ins:
            views.Base.ins_type.append('CS')
            views.Base.func7.append('X')
            views.Base.func2.append('X')
            views.Base.func6.append('X')
            views.Base.func4.append('X')
            views.Base.destination.append('X')
            half_ins = re.findall(r'[+-]?\d+', x)
            imm = half_ins[1]
            src2 = half_ins[0]
            src1 = half_ins[2]
            if 'c.sw' in m:
                if int(src1) < 8 or int(src1) > 15 or int(src2) < 8 or int(src2) > 15 or int(imm) < 0:
                    Error = 'Soruce one and Source two Register should be greater than x8(s0) and less than x15(a5) and immediate should be greater then or equal to zero in C.SW'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('00')
                    src2_int = '{0:05b}'.format(int(src2))
                    src1_int = '{0:05b}'.format(int(src1))
                    imm_int = '{0:032b}'.format(int(imm) * 4)
                    views.Base.func3.append('110')
                    views.Base.source2.append(src2_int[2:5])
                    views.Base.source1.append(src1_int[2:5])
                    views.Base.immediate1.append(imm_int[25:28])
                    views.Base.immediate2.append(imm_int[24:25] + imm_int[28:29])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.immediate2[i]) + str(views.Base.source2[i]) + str(
                            views.Base.opcode[i]))

        elif m in cl_ins:
            views.Base.ins_type.append('CL')
            views.Base.func7.append('X')
            views.Base.func2.append('X')
            views.Base.func6.append('X')
            views.Base.func4.append('X')
            views.Base.source2.append('X')
            half_ins = re.findall(r'[+-]?\d+', x)
            imm = half_ins[1]
            dest = half_ins[0]
            src1 = half_ins[2]
            if 'c.lw' in m:
                if int(src1) < 8 or int(src1) > 15 or int(dest) < 8 or int(dest) > 15 or int(imm) < 0:
                    Error = 'Destination and Source Register should be greater than x8(s0) and less than x15(a5) and immediate should be greater then or equal to zero in C.LW'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('00')
                    dest_int = '{0:05b}'.format(int(dest))
                    src1_int = '{0:05b}'.format(int(src1))
                    imm_int = '{0:032b}'.format(int(imm) * 4)
                    views.Base.func3.append('010')
                    views.Base.destination.append(dest_int[2:5])
                    views.Base.source1.append(src1_int[2:5])
                    views.Base.immediate1.append(imm_int[25:28])
                    views.Base.immediate2.append(imm_int[24:25] + imm_int[28:29])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.source1[i]) + str(views.Base.immediate2[i]) + str(views.Base.destination[i]) + str(
                            views.Base.opcode[i]))

        elif m in ciw_ins:
            half_ins = re.findall(r'[+-]?\d+', x)
            views.Base.ins_type.append('CIW')
            views.Base.func2.append('X')
            views.Base.func4.append('X')
            views.Base.func6.append('X')
            views.Base.func7.append('X')
            views.Base.source2.append('X')
            views.Base.source1.append('X')
            views.Base.immediate2.append('X')
            dest = half_ins[1]
            print("dest")
            print(dest)
            imm = half_ins[2]
            print("imm")
            print(imm)
            if int(dest) < 8 or int(dest) > 15 or int(imm) <= 0:
                Error = 'Destination Register should be greater than x8(s0) and less than x15(a5) and immediate should be greater then zero in C.ADDI4SP'
                dict1 = {'Error': Error, 'error': True}
                return HttpResponse(json.dumps(dict1))
            else:
                views.Base.opcode.append('00')
                dest_int = '{0:05b}'.format(int(dest))
                imm_int = '{0:032b}'.format(int(imm) * 4)
                views.Base.func3.append('000')
                views.Base.destination.append(dest_int[2:5])
                views.Base.immediate1.append(imm_int[25:27] + imm_int[29:25] + imm_int[28:29] + imm_int[27:28])
                ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) +
                               str(views.Base.destination[i]) + str(views.Base.opcode[i]))

        elif m in cb_ins:
            half_ins = re.findall(r'[+-]?\d+', x)
            views.Base.ins_type.append('CB')
            views.Base.source1.append('X')
            views.Base.source2.append('X')
            views.Base.func7.append('X')
            views.Base.func4.append('X')
            views.Base.func6.append('X')
            if 'c.andi' in m:
                dest = half_ins[0]
                imm = half_ins[1]
                if int(dest) < 8 or int(dest) > 15 or int(imm) <= 0:
                    Error = 'Destination Register should be greater than x8(s0) and less than x15(a5) and immediate should be greater then zero in C.ANDI'
                    dict1 = {'Error': Error, 'error': True}
                    return HttpResponse(json.dumps(dict1))
                else:
                    views.Base.opcode.append('01')
                    dest_int = '{0:05b}'.format(int(dest))
                    imm_int = '{0:06b}'.format(int(imm))
                    views.Base.func3.append('100')
                    views.Base.func2.append('10')
                    views.Base.destination.append(dest_int[2:5])
                    views.Base.immediate2.append(imm_int[1:6])
                    views.Base.immediate1.append(imm_int[0:1])
                    ins_mem.append('0000000000000000' + str(views.Base.func3[i]) + str(views.Base.immediate1[i]) + str(views.Base.func2[i]) + str(
                        views.Base.destination[i]) + str(views.Base.immediate2[i]) + str(views.Base.opcode[i]))

        else:  # NOP instruction
            views.Base.ins_type.append('X')
            views.Base.opcode.append('01')
            views.Base.func7.append('X')
            views.Base.func3.append('X')
            views.Base.func6.append('X')
            views.Base.func4.append('0000')
            views.Base.func2.append('X')
            views.Base.source1.append('00000')
            views.Base.source2.append('00000')
            views.Base.destination.append('X')
            views.Base.immediate2.append('X')
            views.Base.immediate1.append('X')
            ins_mem.append('00000000000000000000000000000001')
        print(bits)
        ####### Transfering instruction bits into dump list #######
        views.Base.dump_bin.append([bits[i], ins_mem[i]])
        print(len(views.Base.dump_bin))
        print(bits)
        print(len(ins_mem))
        ###########################################################


    print(views.Base.dump_bin)
    print(ins_mem)
    for k in ins_mem:
        l3.append(k[:8])
        l2.append(k[8:16])
        l1.append(k[16:24])
        l0.append(k[24:32])
    print(l3)
    print(l2)
    print(l1)
    print(l0)
    for k in range(len(ins_mem)):
        l3[k] = '{0:02X}'.format(int(l3[k], 2))
        l2[k] = '{0:02X}'.format(int(l2[k], 2))
        l1[k] = '{0:02X}'.format(int(l1[k], 2))
        l0[k] = '{0:02X}'.format(int(l0[k], 2))
    print(l3)
    print(l2)
    print(l1)
    print(l0)

    for i in range(0, len(views.Base.code_line1)):
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(instruction_memory_uni_counter)] = int(
            l0[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 1)] = int(l1[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 2)] = int(l2[i], 16)
        instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(instruction_memory_uni_counter + 3)] = int(l3[i], 16)

        instruction_memory_uni_counter += 4

    # print(views.Base.ins_type)

    ##### This Is Memory Block START
    ###When using Online web
    file_values=open("/home/merloxygen/Merl-UIT-Simulator/RISCV/r5pythonversion/templates/m.txt","r")
    ###when using dedicated machine(PC)

    # file_values = open("templates\m.txt", "r")
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
    views.Base.listkey = []
    for x in range(0, 512):
        if (x == 512 / 4):
            break
        views.Base.listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
        counter_memory_address = counter_memory_address + 4

    #########################################################
    for i in range(0, 512 * 4):
        # memory_dictionary[hex(i)]=memory_value[i]
        instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(i)]
    #########################################################

    ########################################################## Memory  breaking For Views

    count_memory_break_view = 0
    for i in range(0, 514 * 4):
        if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
            break
        views.Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
        views.Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
        views.Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
        views.Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
        count_memory_break_view = count_memory_break_view + 4

    ########################################################## Memory  breaking For Views

    ########################################################## Address Division For Views

    ########################################################## Address Division For Views
    print(whole_code1)
    # param.update({'result': "True", 'status1': views.Base.status, 'code2': views.Base.whole_code,
    #               'data': zip(instructions.Instruction_type.val, views.Base.reg_name),
    #               'data1': zip(listkey, list_column_1, list_column_2, list_column_3, list_column_4),
    #               'data3': zip(views.Base.pc, views.Base.code_line1, views.Base.ins_type, views.Base.immediate1,
    #                            views.Base.func7, views.Base.func6, views.Base.func4, views.Base.source2,
    #                            views.Base.source1, views.Base.func3, views.Base.func2, views.Base.destination,
    #                            views.Base.immediate2, views.Base.opcode), 'ctn': 1})
    # # views.Base.code_line1 = views.Base.code_line1
    # print(param)

    param123 = {'length': len(views.Base.code_line1), 'result': "True", 'status1': views.Base.status,
                'code': views.Base.whole_code,
                'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1,
                'list2': views.Base.list_column_2,
                'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4, 'pc': views.Base.pc,
                'codes': views.Base.code_line1,
                'ins_type': views.Base.ins_type, 'imm1': views.Base.immediate1, 'f7': views.Base.func7,
                'f6': views.Base.func6, 'f4': views.Base.func4, 's2': views.Base.source2,
                's1': views.Base.source1, 'f3': views.Base.func3, 'f2': views.Base.func2,
                'dest': views.Base.destination, 'imm2': views.Base.immediate2,
                'opcode': views.Base.opcode, 'ctn': 1}
    print(param123)

    views.Base.stack_register.clear()
    views.Base.memory_list1.clear()
    views.Base.memory_list2.clear()
    views.Base.memory_list3.clear()
    views.Base.memory_list4.clear()
    views.Base.ins_number.clear()
    return HttpResponse(json.dumps(param123))




