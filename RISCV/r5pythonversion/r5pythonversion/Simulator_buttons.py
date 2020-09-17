from django.contrib import messages
from django.http import HttpResponse

from . import I_type
from . import R_type
from . import S_type
from . import CR_type
from . import CI_type
from . import CB_type
from . import SB_type
from . import UJ_type
from . import views
from . import instructions
from . import maintain_log_file as log
import re
import json


def index(request):
    result = 0
    at_last = ''
    whole_code = views.Base.whole_code
    print(whole_code)
    
    result, success = execute(whole_code)
    
    if success:
        messages.success(request, message = 'Code exited with 0 error!')
        at_last = 'Code exited with 0 error!'
        log.log_file()
    else:
        views.Base.stack_register.pop()
        views.Base.memory_list1.pop()
        views.Base.memory_list2.pop()
        views.Base.memory_list3.pop()
        views.Base.memory_list4.pop()
        views.Base.ins_number.pop()
        views.Base.vari = 0
        dict1 = {'Error': result, 'error': success}
        return HttpResponse(json.dumps(dict1))

    # views.Base.param.update({'ctn': len(views.Base.code_line1) + 1, 'result': "off", 'fresult': result, 'data': zip(instructions.Instruction_type.val, views.Base.reg_name), 'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4), 'data3': zip(views.Base.pc, views.Base.code_line1, views.Base.ins_type, views.Base.immediate1, views.Base.func7, views.Base.source2, views.Base.source1, views.Base.func3, views.Base.destination, views.Base.immediate2, views.Base.opcode)})
    print(views.Base.param)
    count_memory_break_view = 0
    views.Base.list_column_1.clear()
    views.Base.list_column_2.clear()
    views.Base.list_column_3.clear()
    views.Base.list_column_4.clear()

    for i in range(0, 514 * 4):
        if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
            break
        views.Base.list_column_1.append(instructions.Instruction_type.memory_value[count_memory_break_view])
        views.Base.list_column_2.append(instructions.Instruction_type.memory_value[count_memory_break_view + 1])
        views.Base.list_column_3.append(instructions.Instruction_type.memory_value[count_memory_break_view + 2])
        views.Base.list_column_4.append(instructions.Instruction_type.memory_value[count_memory_break_view + 3])
        count_memory_break_view = count_memory_break_view + 4


    # views.Base.param1 = {'fresult': result,'data': zip(instructions.Instruction_type.val,views.Base.reg_name), 'data1': zip(views.Base.listkey,views.Base.list_column_1,views.Base.list_column_2,views.Base.list_column_3,views.Base.list_column_4)}
    param123 = {'success': str(success), 'atlast': at_last, 'fresult': result, 'ctn': len(views.Base.code_line1) + 1, 'result': "off", 'status1': views.Base.status, 'code': views.Base.whole_code,
                'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
                'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4}
    print(param123)
    # return render(request, 'index.html', views.Base.param)
    return HttpResponse(json.dumps(param123))


def execute(whole_code):
    code_line = []
    whole_code = whole_code.replace('\r\n', '\n')
    code_line = [line for line in whole_code.split('\n') if line.strip() != '']
    for i in range(0, 32):
        instructions.Instruction_type.val[i] = 0

    views.Base.stack_register.clear()
    views.Base.memory_list1.clear()
    views.Base.memory_list2.clear()
    views.Base.memory_list3.clear()
    views.Base.memory_list4.clear()
    views.Base.ins_number.clear()

    r_type = []
    i_type = []
    s_type = []
    sb_type = []
    ci_type = []
    cr_type = []
    cb_type = []
    jump_type = []
    count_jump = 0
    count_i = 0
    count_r = 0
    count_s = 0
    count_sb = 0
    count_ci = 0
    count_cr = 0
    count_cb = 0
    views.Base.vari = 0
    views.Base.nxt = 0
    pc = 0
    success = False
    r_ins = ['add', 'sub', 'mul', 'mulh', 'mulhu', 'mulhsu', 'div', 'divu', 'rem', 'remu', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
    i_ins = ['slli', 'srli', 'srai','addi', 'subi', 'muli', 'divi', 'remi', 'xori', 'andi', 'ori', 'slti', 'sltiu', 'fence' ,'fence.i' ,'scall' ,'sbreak']
    sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
    jump_ins = ['jal', 'jalr']
    ci_ins = ['c.addi', 'c.addiw', 'c.ldsp', 'c.lwsp', 'c.lqsp', 'c.addiw', 'c.addi16sp', 'c.li', 'c.lui', 'c.slli',
              'c.break', 'c.srli', 'c.srai', 'c.andi']
    cl_ins = ['c.lw', 'c.ld', 'c.lq']
    cs_ins = ['c.sw', 'c.sd', 'c.sq']
    css_ins = ['c.swsp', 'c.sdsp', 's.sqsp']
    cr_ins = ['c.add', 'c.addw', 'c.mv', 'c.sub', 'c.jr', 'c.jalr', 'c.xor', 'subw', 'c.or']
    ciw_ins = ['c.addi4spn']
    cb_ins = ['c.beqz', 'c.bnez']
    cj_ins = ['c.j', 'c.jal']

    for i in range(len(code_line)):
        if ':' in code_line[i]:
            views.Base.label_address[code_line[i]] = i

    for i in range(views.Base.vari, len(code_line)):
        mainting_stack(instructions.Instruction_type.val, views.Base.list_column_1, views.Base.list_column_2, views.Base.list_column_3,
                       views.Base.list_column_4, views.Base.vari)
        if views.Base.vari == len(code_line):
            break
        x = code_line[views.Base.vari]
        x = x.lower()
        x = x.strip()
        m = re.search(r'^c.\w+|\w+', x)
        m = m.group()
        temp = False
        # print(m)
        if m in i_ins:
            i_type.append(I_type.I_type())
            print(len(i_type))
            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdi(x)
            x = views.Base.data[i][0]
            i_type[count_i].dest = views.Base.data[i][1]
            i_type[count_i].src1 = views.Base.data[i][2]
            i_type[count_i].src2 = views.Base.data[i][3]
            i_type[count_i].getexecute()
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
            # instructions.Instruction_type.val = i_type[i].val

        #LW and LWSP for C extension
        elif "c.lwsp" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            print(offset_for_register)
            offset_temp = '{0:08X}'.format(offset_for_register)
            offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
            offset_temp2 = '{0:08X}'.format(offset_for_register + 2)
            offset_temp3 = '{0:08X}'.format(offset_for_register + 3)
            tem_value = []
            tem_value_register = 0
            # tem_value Should Be in Register
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp2))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp3))

            print(tem_value)

            for values in tem_value:
                (tem_value_register) = int(tem_value_register) + int(values)
            instructions.Instruction_type.val[dest] = tem_value_register
            print(instructions.Instruction_type.val)



            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
        elif "c.lw" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            print(offset_for_register)
            offset_temp = '{0:08X}'.format(offset_for_register)
            offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
            offset_temp2 = '{0:08X}'.format(offset_for_register + 2)
            offset_temp3 = '{0:08X}'.format(offset_for_register + 3)
            tem_value = []
            tem_value_register = 0
            # tem_value Should Be in Register
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp2))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp3))

            print(tem_value)

            for values in tem_value:
                (tem_value_register) = int(tem_value_register) + int(values)
            instructions.Instruction_type.val[dest] = tem_value_register
            print(instructions.Instruction_type.val)



            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
        elif "lw" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            print(offset_for_register)
            offset_temp = '{0:08X}'.format(offset_for_register)
            offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
            offset_temp2 = '{0:08X}'.format(offset_for_register + 2)
            offset_temp3 = '{0:08X}'.format(offset_for_register + 3)
            tem_value = []
            tem_value_register = 0
            # tem_value Should Be in Register
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp2))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp3))

            print(tem_value)

            for values in tem_value:
                (tem_value_register) = int(tem_value_register) + int(values)
            instructions.Instruction_type.val[dest] = tem_value_register
            print(instructions.Instruction_type.val)



            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
        elif "lhu" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            offset_temp = '{0:08X}'.format(offset_for_register)
            offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
            # tem_value Should Be in Register
            tem_value = []
            tem_value_register = 0
            # tem_value Should Be in Register
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
            print(tem_value)
            print("Unsigned")
            for values in tem_value:
                tem_value_register = tem_value_register + int(values)
                print(tem_value_register)
                if tem_value_register < 0:
                    instructions.Instruction_type.val[dest] = tem_value_register * -1
                else:
                    instructions.Instruction_type.val[dest] = tem_value_register
                print(instructions.Instruction_type.val)




            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
        elif "lbu" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+' ,x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            offset_temp = '{0:08X}'.format(offset_for_register)
            # tem_value Should Be in Register
            tem_value = instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
            print(tem_value)
            
            if int(tem_value) < 0:
                instructions.Instruction_type.val[dest] = int(tem_value) * -1
            else:
                instructions.Instruction_type.val[dest] = int(tem_value)
            print(instructions.Instruction_type.val)

            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
        elif "lb" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            offset_temp = '{0:08X}'.format(offset_for_register)
            # tem_value Should Be in Register
            tem_value = instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
            print(tem_value)
            instructions.Instruction_type.val[dest] = int(tem_value)
            print(instructions.Instruction_type.val)
            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) -1:
                views.Base.vari += 1
        elif "lh" in x:
            i_type.append(I_type.I_type())
            print(len(i_type))

            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            offset_for_register = src1 + src2

            offset_temp = '{0:08X}'.format(offset_for_register)
            offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
            tem_value_register = 0
            tem_value = []
            
            # tem_value Should Be in Register
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
            tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
            print(tem_value)
            for values in tem_value:
                tem_value_register = tem_value_register + int(values)
            instructions.Instruction_type.val[dest] = tem_value_register
            print(instructions.Instruction_type.val)
            # i_type[i].val = instructions.Instruction_type.val
            x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

        elif m in sb_ins:
            views.Base.error = ""
            sb_type.append(SB_type.SB_type())
            sb_type[count_sb].split_inst(x)
            temp, label = sb_type[count_sb].op_select()
            count_sb += 1
            views.Base.nxt = views.Base.vari + 1
            pc += 4
            if temp:
                # instructions.Instruction_type.val[1] = views.Base.nxt * 4
                for j in range(len(code_line)):
                    if label in code_line[j]:
                        views.Base.vari = j + 1
            elif views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1


    #SW for C extension
        elif "c.swsp" in x:
            views.Base.error = ""
            s_type.append(S_type.S_type())
            print(len(s_type))

            ######################################################
            # Content
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            views.Base.base_address = src2
            offset_for_register = src1 + src2

            byte1 = 255 & instructions.Instruction_type.val[dest]
            byte2 = 65280 & instructions.Instruction_type.val[dest]
            byte3 = 16711680 & instructions.Instruction_type.val[dest]
            byte4 = 4278190080 & instructions.Instruction_type.val[dest]
            print("byte1", byte1)
            print("byte2", byte2)
            print("byte3", byte3)
            print("byte4", byte4)
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 2)] = byte3
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 3)] = byte4
            #########################################################################
            # Filling portion
            print(instructions.Instruction_type.memory_dictionary_fetch)
            #########################################################################

            #########################################################################
            instructions.Instruction_type.memory_value[offset_for_register]=byte1
            instructions.Instruction_type.memory_value[offset_for_register+1]=byte2
            instructions.Instruction_type.memory_value[offset_for_register+2]=byte3
            instructions.Instruction_type.memory_value[offset_for_register+3]=byte4
            print(instructions.Instruction_type.memory_value)
            ######################################################

            x = s_type[count_s].getoperators(x)
            # s_type[count_s].getsds(x)
            count_s += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
        elif "c.sw" in x:
            views.Base.error = ""
            s_type.append(S_type.S_type())
            print(len(s_type))

            ######################################################
            # Content
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            views.Base.base_address = src2
            offset_for_register = src1 + src2

            byte1 = 255 & instructions.Instruction_type.val[dest]
            byte2 = 65280 & instructions.Instruction_type.val[dest]
            byte3 = 16711680 & instructions.Instruction_type.val[dest]
            byte4 = 4278190080 & instructions.Instruction_type.val[dest]
            print("byte1", byte1)
            print("byte2", byte2)
            print("byte3", byte3)
            print("byte4", byte4)
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 2)] = byte3
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 3)] = byte4
            #########################################################################
            # Filling portion
            print(instructions.Instruction_type.memory_dictionary_fetch)
            #########################################################################

            #########################################################################
            instructions.Instruction_type.memory_value[offset_for_register]=byte1
            instructions.Instruction_type.memory_value[offset_for_register+1]=byte2
            instructions.Instruction_type.memory_value[offset_for_register+2]=byte3
            instructions.Instruction_type.memory_value[offset_for_register+3]=byte4
            print(instructions.Instruction_type.memory_value)
            ######################################################

            x = s_type[count_s].getoperators(x)
            # s_type[count_s].getsds(x)
            count_s += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1


        elif "sw" in x:
            views.Base.error = ""
            s_type.append(S_type.S_type())
            print(len(s_type))

            ######################################################
            # Content
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            views.Base.base_address = src2
            offset_for_register = src1 + src2

            byte1 = 255 & instructions.Instruction_type.val[dest]
            byte2 = 65280 & instructions.Instruction_type.val[dest]
            byte3 = 16711680 & instructions.Instruction_type.val[dest]
            byte4 = 4278190080 & instructions.Instruction_type.val[dest]
            print("byte1", byte1)
            print("byte2", byte2)
            print("byte3", byte3)
            print("byte4", byte4)
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 2)] = byte3
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 3)] = byte4
            #########################################################################
            # Filling portion
            print(instructions.Instruction_type.memory_dictionary_fetch)
            #########################################################################

            #########################################################################
            instructions.Instruction_type.memory_value[offset_for_register]=byte1
            instructions.Instruction_type.memory_value[offset_for_register+1]=byte2
            instructions.Instruction_type.memory_value[offset_for_register+2]=byte3
            instructions.Instruction_type.memory_value[offset_for_register+3]=byte4
            print(instructions.Instruction_type.memory_value)
            ######################################################

            x = s_type[count_s].getoperators(x)
            # s_type[count_s].getsds(x)
            count_s += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

        elif "sh" in x:
            views.Base.error = ""
            s_type.append(S_type.S_type())
            print(len(s_type))

            ######################################################
            # Content
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            views.Base.base_address = src2
            offset_for_register = src1 + src2

            byte1 = 255 & instructions.Instruction_type.val[dest]
            byte2 = 65280 & instructions.Instruction_type.val[dest]

            print("byte1", byte1)
            print("byte2", byte2)

            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2

            #########################################################################
            # Filling portion
            print(instructions.Instruction_type.memory_dictionary_fetch)
            #########################################################################
            #########################################################################
            instructions.Instruction_type.memory_value[offset_for_register]=byte1
            instructions.Instruction_type.memory_value[offset_for_register+1]=byte2
            print(instructions.Instruction_type.memory_value)
            ######################################################
            ######################################################

            x = s_type[count_s].getoperators(x)
            # s_type[count_s].getsds(x)
            count_s += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

        elif "sb" in x:
            s_type.append(S_type.S_type())
            print(len(s_type))

            ######################################################
            # Content
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            src2 = int(register_num_list[2])
            src2 = instructions.Instruction_type.val[src2]
            views.Base.base_address = src2
            offset_for_register = src1 + src2

            byte1 = 255 & instructions.Instruction_type.val[dest]

            print("byte1", byte1)

            instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1

            #########################################################################
            instructions.Instruction_type.memory_value[offset_for_register]=byte1
            print(instructions.Instruction_type.memory_value)
            # Filling portion
            print(instructions.Instruction_type.memory_dictionary_fetch)
            #########################################################################

            ######################################################

            x = s_type[count_s].getoperators(x)
            # s_type[count_s].getsds(x)
            count_s += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

            views.Base.error = ""

        elif m == "lui":
            print("Lui is Running")
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            views.Base.lui_imm = src1 * 4096

            # For 16 bit Load
            # print(src1)
            byte2 = 65280 & src1
            # print(byte2)
            instructions.Instruction_type.val[dest] = src1 * 4096
            print(instructions.Instruction_type.val)

            # x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

        elif "auipc" in x:
            print("I am Running")
            # print(pc1)
            register_num_list = re.findall(r'\d+', x)
            print(register_num_list)
            dest = int(register_num_list[0])
            src1 = int(register_num_list[1])
            views.Base.aui_imm = src1
            print(views.Base.vari)
            instructions.Instruction_type.val[dest] = views.Base.vari * 4 + src1
            # x = i_type[count_i].getoperatori(x)
            # i_type[count_i].getsdl(x)
            # Stopping From Other Load
            count_i += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

            # UJ Type Instruction

        elif m in jump_ins:
            # l_count = 0
            # label_add = 0
            # y = x[4:]
            # nxt = vari + 1
            # track = vari
            # instructions.Instruction_type.val[1] = nxt * 4
            # jal_c = 0
            # for key in views.Base.label_address:
            #     if y in key:
            #         label_add = views.Base.label_address[key]
            # print("value of x1: " + str(nxt))
            # if label_add > track:
            #     while track != label_add:
            #         if ':' not in code_line[track]:
            #             l_count += 1
            #         track += 1
            #     jal_c = l_count
            # elif label_add < track:
            #     while track != label_add:
            #         if ':' not in code_line[track]:
            #             l_count -= 1
            #         track -= 1
            #     jal_c = l_count + 1

            '''for j in range(len(code_line)):
                if j > vari and ':' in code_line[j]:
                    l_count += 1
                if y in code_line[j] and (not ('jal' in code_line[j])):
                    # code_line[j] = code_line[j].split(":")
                    if j
                    vari = j + 1
                    jal_c = (vari + 1) - (nxt + l_count)'''
            jump_type.append(UJ_type.JumpIns(x, views.Base.vari, code_line, views.Base.label_address))
            jump_type[count_jump].split_inst()
            if 'jal' in x:
                y = x[4:]
                track, jal_c = jump_type[count_jump].jal_op()
                views.Base.jal_imm[y] = jal_c
                print("jal list", views.Base.jal_imm)
                views.Base.vari = track + 1
                print("Vari = " + str(views.Base.vari))
            if 'jalr' in x:
                views.Base.vari = jump_type[count_jump].jalr_op()
            # views.Base.jal_imm[y] = jal_c
            # print("jal list", views.Base.jal_imm)
            # vari = track + 1
            views.Base.error = ""
            pc += 4
        elif "ret" in x:
            views.Base.vari = int((instructions.Instruction_type.val[1]) / 4)
            print("value of x1(1): " + str(views.Base.nxt))
            views.Base.error = ""
        elif "ebreak" in x:
            views.Base.error = ""
            break
        elif m in r_ins:
            r_type.append(R_type.R_type())
            print(len(r_type))
            # r_type[i].val = instructions.Instruction_type.val
            x = r_type[count_r].getoperator(x)
            res = r_type[count_r].getsd(x)
            print(res)
            if 'Divide by zero error encountered' in res:
                return res, False
            count_r += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
            views.Base.error = ""
            # instructions.Instruction_type.val = r_type[i].val
        elif m in cr_ins:
            cr_type.append(CR_type.CR_type())
            print(len(cr_type))
            # r_type[i].val = instructions.Instruction_type.val
            x = cr_type[count_cr].getoperator(x)
            cr_type[count_cr].getsd(x)
            count_cr += 1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1
            # instructions.Instruction_type.val = r_type[i].val


        elif m in ci_ins:
            ci_type.append(CI_type.CI_type())
            print(len(ci_type))
            # i_type[i].val = instructions.Instruction_type.val
            x = ci_type[count_ci].getoperatori(x)
            ci_type[count_ci].getsdi(x)
            # byte2 = 65280 & src1
            # ci_type[count_ci].src2 = Base.data[i][3]
            # ci_type[count_ci].getexecute()
            count_ci += 1
            # Base.lui_imm = src1
            pc += 4
            if views.Base.vari < len(code_line) - 1:
                views.Base.vari += 1

            # instructions.Instruction_type.val = i_type[i].val
        elif m in cb_ins:
            cb_type.append(CB_type.CB_type())
            cb_type[count_cb].CB_split_inst(x)
            temp, label = cb_type[count_cb].CB_op_select()
            count_sb += 1
            views.Base.nxt = views.Base.vari + 1
            pc += 4
            if temp:
               # instructions.Instruction_type.val[1] = Base.nxt * 4
                for j in range(len(code_line)):
                    if label in code_line[j]:
                        views.Base.vari = j+1
            elif views.Base.vari < len(code_line)-1:
                views.Base.vari += 1
        else:
            break
        instructions.Instruction_type.val[0] = 0
    final_result = instructions.Instruction_type.val[instructions.Instruction_type.indexd]
    print(final_result)
    success = True
    return final_result, success


def step_by_step(request):
    session = request.session.get('session', 0) + 1
    print("Session = " + str(session))
    request.session['session'] = session
    views.Base.next = session
    print("views.Base.next = " + str(views.Base.next))
    print('length of codeline1')
    print(len(views.Base.code_line1))
    answer = stepping(views.Base.code_line1[views.Base.vari])
    if 'Divide by zero error encountered' in str(answer):
        views.Base.stack_register.pop()
        views.Base.memory_list1.pop()
        views.Base.memory_list2.pop()
        views.Base.memory_list3.pop()
        views.Base.memory_list4.pop()
        views.Base.ins_number.pop()
        dict1 = {'Error': answer, 'error': False}
        return HttpResponse(json.dumps(dict1))
    else:
        print("This is log file")
        log.log_file()

    # prev_data = {'fresult': answer, 'success': "False", 'ctn': views.Base.vari + 1, 'result': "on", 'code': views.Base.whole_code,
    #              'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
    #              'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4}

    count = request.session['session']
    print(count)
    # views.Base.param1.update({'result': "on", 'fresult': answer, 'ctn': views.Base.vari + 1, 'code': views.Base.whole_code})
    views.Base.param12.update(
        {'fresult': answer, 'success': "False", 'ctn': views.Base.vari + 1, 'result': "on", 'code': views.Base.whole_code})

    print("step1 :" + str(views.Base.param12))
    print(request.session['session'])
    print("Value of Vari = ")
    print(views.Base.vari)
    if views.Base.vari >= len(views.Base.code_line1):
        messages.success(request, message= "Code exited with 0 error")
        del (request.session['session'])
        views.Base.next = 0
        session = 0
        views.Base.param12.update({'result': "off", 'success': "True", 'atlast': "Code exited with 0 error"})
    # return render(request, 'index.html', views.Base.param1)
    return HttpResponse(json.dumps(views.Base.param12))


def stepping(x):
    whole_code = views.Base.whole_code.replace('\r\n', '\n')
    code_line = [line for line in whole_code.split('\n') if line.strip() != '']
    r_type = []
    i_type = []
    s_type = []
    sb_type = []
    ci_type = []
    cr_type = []
    cb_type = []
    jump_type = []
    count_jump = 0
    count_i = 0
    count_r = 0
    count_s = 0
    count_sb = 0
    count_ci = 0
    count_cr = 0
    count_cb = 0
    pc = 0

    mainting_stack(instructions.Instruction_type.val, views.Base.list_column_1, views.Base.list_column_2, views.Base.list_column_3,
                   views.Base.list_column_4, views.Base.vari)

    r_ins = ['add', 'sub', 'mul', 'mulh', 'mulhu', 'mulhsu', 'div', 'divu', 'rem', 'remu', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'sltu', 'slt']
    i_ins = ['slli', 'srli', 'srai', 'addi', 'subi', 'muli', 'divi', 'remi', 'xori', 'andi', 'ori', 'slti', 'sltiu',
             'fence', 'fence.i', 'scall', 'sbreak']
    sb_ins = ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']
    jump_ins = ['jal', 'jalr']
    ci_ins = ['c.addi', 'c.addiw', 'c.ldsp', 'c.lwsp', 'c.lqsp', 'c.addiw', 'c.addi16sp', 'c.li', 'c.lui', 'c.slli',
              'c.break', 'c.srli', 'c.srai', 'c.andi']
    cl_ins = ['c.lw', 'c.ld', 'c.lq']
    cs_ins = ['c.sw', 'c.sd', 'c.sq']
    css_ins = ['c.swsp', 'c.sdsp', 's.sqsp']
    cr_ins = ['c.add', 'c.addw', 'c.mv', 'c.sub', 'c.jr', 'c.jalr', 'c.xor', 'subw', 'c.or']
    ciw_ins = ['c.addi4spn']
    cb_ins = ['c.beqz', 'c.bnez']
    cj_ins = ['c.j', 'c.jal']

    x = x.lower()
    x = x.strip()
    m = re.search(r'^c.\w+|\w+', x)
    m = m.group()
    temp = False

    if m in i_ins:
        views.Base.error = ""
        i_type.append(I_type.I_type())
        print(len(i_type))
        # i_type[i].val = instructions.Instruction_type.val
        x = i_type[count_i].getoperatori(x)
        i_type[count_i].getsdi(x)
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            print("i am in condition huraahh!")
            views.Base.vari += 1
        # instructions.Instruction_type.val = i_type[i].val

    elif "lw" in x:
        views.Base.error = ""
        i_type.append(I_type.I_type())
        print(len(i_type))

        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        offset_for_register = src1 + src2

        print(offset_for_register)
        offset_temp = '{0:08X}'.format(offset_for_register)
        offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
        offset_temp2 = '{0:08X}'.format(offset_for_register + 2)
        offset_temp3 = '{0:08X}'.format(offset_for_register + 3)
        tem_value = []
        tem_value_register = 0
        # tem_value Should Be in Register
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp2))
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp3))

        print(tem_value)

        for values in tem_value:
            (tem_value_register) = int(tem_value_register) + int(values)
        instructions.Instruction_type.val[dest] = tem_value_register
        print(instructions.Instruction_type.val)

        # i_type[i].val = instructions.Instruction_type.val
        x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif x == "lhu":
        views.Base.error = ""
        i_type.append(I_type.I_type())
        print(len(i_type))

        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        offset_for_register = src1 + src2

        offset_temp = '{0:08X}'.format(offset_for_register)
        offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
        # tem_value Should Be in Register
        tem_value = []
        tem_value_register = 0
        # tem_value Should Be in Register
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
        print(tem_value)
        print("Unsigned")
        for values in tem_value:
            tem_value_register = tem_value_register + int(values)
            print(tem_value_register)
            if (tem_value_register < 0):
                instructions.Instruction_type.val[dest] = tem_value_register * -1
            else:
                instructions.Instruction_type.val[dest] = tem_value_register
            print(instructions.Instruction_type.val)

        # i_type[i].val = instructions.Instruction_type.val
        x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif "lbu" in x:
        views.Base.error = ""
        i_type.append(I_type.I_type())
        print(len(i_type))

        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        offset_for_register = src1 + src2

        offset_temp = '{0:08X}'.format(offset_for_register)
        # tem_value Should Be in Register
        tem_value = instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
        print(tem_value)
        if (int(tem_value) < 0):
            instructions.Instruction_type.val[dest] = int(tem_value) * -1
        else:
            instructions.Instruction_type.val[dest] = int(tem_value)
        print(instructions.Instruction_type.val)

        # i_type[i].val = instructions.Instruction_type.val
        x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif "lb" in x:
        views.Base.error = ""
        i_type.append(I_type.I_type())
        print(len(i_type))

        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        offset_for_register = src1 + src2

        offset_temp = '{0:08X}'.format(offset_for_register)
        # tem_value Should Be in Register
        tem_value = instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp)
        print(tem_value)
        instructions.Instruction_type.val[dest] = int(tem_value)
        print(instructions.Instruction_type.val)
        # i_type[i].val = instructions.Instruction_type.val
        x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif x == "lh":

        views.Base.error = ""
        i_type.append(I_type.I_type())
        print(len(i_type))

        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        offset_for_register = src1 + src2

        offset_temp = '{0:08X}'.format(offset_for_register)
        offset_temp1 = '{0:08X}'.format(offset_for_register + 1)
        tem_value_register = 0
        tem_value = []
        # tem_value Should Be in Register
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp))
        tem_value.append(instructions.Instruction_type.memory_dictionary_fetch.get(offset_temp1))
        print(tem_value)
        for values in tem_value:
            tem_value_register = tem_value_register + int(values)
        instructions.Instruction_type.val[dest] = tem_value_register
        print(instructions.Instruction_type.val)
        # i_type[i].val = instructions.Instruction_type.val
        x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif m in sb_ins:
        views.Base.error = ""
        sb_type.append(SB_type.SB_type())
        sb_type[count_sb].split_inst(x)
        temp, label = sb_type[count_sb].op_select()
        count_sb += 1
        views.Base.nxt = views.Base.vari + 1
        pc += 4
        if temp:
            # instructions.Instruction_type.val[1] = views.Base.nxt * 4
            for j in range(len(code_line)):
                if label in code_line[j]:
                    views.Base.vari = j
        elif views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif "sw" in x:
        views.Base.error = ""
        s_type.append(S_type.S_type())
        print(len(s_type))

        ######################################################
        # Content
        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        views.Base.base_address = src2
        offset_for_register = src1 + src2

        byte1 = 255 & instructions.Instruction_type.val[dest]
        byte2 = 65280 & instructions.Instruction_type.val[dest]
        byte3 = 16711680 & instructions.Instruction_type.val[dest]
        byte4 = 4278190080 & instructions.Instruction_type.val[dest]
        print("byte1", byte1)
        print("byte2", byte2)
        print("byte3", byte3)
        print("byte4", byte4)
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 2)] = byte3
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 3)] = byte4
        #########################################################################
        # Filling portion
        print(instructions.Instruction_type.memory_dictionary_fetch)
        #########################################################################

        ######################################################

        x = s_type[count_s].getoperators(x)
        # s_type[count_s].getsds(x)
        count_s += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif "sh" in x:
        views.Base.error = ""
        s_type.append(S_type.S_type())
        print(len(s_type))

        ######################################################
        # Content
        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        views.Base.base_address = src2
        offset_for_register = src1 + src2

        byte1 = 255 & instructions.Instruction_type.val[dest]
        byte2 = 65280 & instructions.Instruction_type.val[dest]

        print("byte1", byte1)
        print("byte2", byte2)

        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1
        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register + 1)] = byte2

        #########################################################################
        # Filling portion
        print(instructions.Instruction_type.memory_dictionary_fetch)
        #########################################################################

        ######################################################

        x = s_type[count_s].getoperators(x)
        # s_type[count_s].getsds(x)
        count_s += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif "sb" in x:
        s_type.append(S_type.S_type())
        print(len(s_type))

        ######################################################
        # Content
        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        src2 = int(register_num_list[2])
        src2 = instructions.Instruction_type.val[src2]
        views.Base.base_address = src2
        offset_for_register = src1 + src2

        byte1 = 255 & instructions.Instruction_type.val[dest]

        print("byte1", byte1)

        instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(offset_for_register)] = byte1

        #########################################################################
        # Filling portion
        print(instructions.Instruction_type.memory_dictionary_fetch)
        #########################################################################

        ######################################################

        x = s_type[count_s].getoperators(x)
        # s_type[count_s].getsds(x)
        count_s += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

        views.Base.error = ""

    elif m == "lui":
        print("Lui is Running")
        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        views.Base.lui_imm = src1

        # For 16 bit Load
        # print(src1)
        byte2 = 65280 & src1
        # print(byte2)
        instructions.Instruction_type.val[dest] = src1 * 4096
        print(instructions.Instruction_type.val[dest])
        print(instructions.Instruction_type.val)

        # x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

    elif "auipc" in x:
        print("I am Running")
        # print(pc1)
        register_num_list = re.findall(r'\d+', x)
        print(register_num_list)
        dest = int(register_num_list[0])
        src1 = int(register_num_list[1])
        views.Base.aui_imm = src1
        print(views.Base.vari)
        instructions.Instruction_type.val[dest] = views.Base.vari * 4 + src1
        # x = i_type[count_i].getoperatori(x)
        # i_type[count_i].getsdl(x)
        # Stopping From Other Load
        count_i += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1

        # UJ Type Instruction
    elif m in jump_ins:
        jump_type.append(UJ_type.JumpIns(x, views.Base.vari, code_line, views.Base.label_address))
        jump_type[count_jump].split_inst()
        if 'jal' in x:
            y = x[4:]
            track, jal_c = jump_type[count_jump].jal_op()
            views.Base.jal_imm[y] = jal_c
            print("jal list", views.Base.jal_imm)
            views.Base.vari = track + 1
            print("Vari = " + str(views.Base.vari))
        if 'jalr' in x:
            views.Base.vari = jump_type[count_jump].jalr_op()
            # views.Base.jal_imm[y] = jal_c
            # print("jal list", views.Base.jal_imm)
            # vari = track + 1
        views.Base.error = ""
        pc += 4
    elif "ret" in x:
        views.Base.vari = int((instructions.Instruction_type.val[1]) / 4)
        print("value of x1(1): " + str(views.Base.nxt))
        views.Base.error = ""
    elif m in r_ins:
        print("We are in R Type")
        r_type.append(R_type.R_type())
        print(len(r_type))
        # r_type[i].val = instructions.Instruction_type.val
        x = r_type[count_r].getoperator(x)
        print('This is get operator' + str(x))
        res = r_type[count_r].getsd(x)
        print(res)
        if 'Divide by zero error encountered' in res:
            return res, False
        count_r += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1
        views.Base.error = ""
        # instructions.Instruction_type.val = r_type[i].val

    elif m in cr_ins:
        cr_type.append(CR_type.CR_type())
        print(len(cr_type))
        # r_type[i].val = instructions.Instruction_type.val
        x = cr_type[count_cr].getoperator(x)
        cr_type[count_cr].getsd(x)
        count_cr += 1
        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1
        # instructions.Instruction_type.val = r_type[i].val

    elif m in ci_ins:
        ci_type.append(CI_type.CI_type())
        print(len(ci_type))
        # i_type[i].val = instructions.Instruction_type.val
        x = ci_type[count_ci].getoperatori(x)
        ci_type[count_ci].getsdi(x)
        # byte2 = 65280 & src1
        # ci_type[count_ci].src2 = Base.data[i][3]
        # ci_type[count_ci].getexecute()
        count_ci += 1
        # Base.lui_imm = src1

        pc += 4
        if views.Base.vari < len(code_line):
            views.Base.vari += 1
        # instructions.Instruction_type.val = i_type[i].val

    elif m in cb_ins:
        print("CB INS")
        cb_type.append(CB_type.CB_type())
        cb_type[count_cb].CB_split_inst(x)
        temp, label = cb_type[count_cb].CB_op_select()
        count_sb += 1
        views.Base.nxt = views.Base.vari + 1
        pc += 4
        print(temp)
        print(views.Base.data)
        if temp:
           # instructions.Instruction_type.val[1] = Base.nxt * 4
            for j in range(len(code_line)):
                if label in code_line[j]:
                    views.Base.vari = j
                    print("After condition" + str(views.Base.vari))
        elif views.Base.vari < len(code_line):
            views.Base.vari += 1

    instructions.Instruction_type.val[0] = 0
    final_result = instructions.Instruction_type.val[instructions.Instruction_type.indexd]

    print("This is Stack")
    print(views.Base.stack_register)
    # views.Base.param1.update({'data': zip(instructions.Instruction_type.val, views.Base.reg_name),
    #                'data1': zip(views.Base.listkey, views.Base.list_column_1, views.Base.list_column_2, views.Base.list_column_3, views.Base.list_column_4),
    #                'data3': zip(views.Base.pc, views.Base.code_line1, views.Base.ins_type, views.Base.immediate1, views.Base.func7, views.Base.source2, views.Base.source1, views.Base.func3, views.Base.destination, views.Base.immediate2, views.Base.opcode)})

    views.Base.param12.update(
        {'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
         'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4})
    print(final_result)

    # request.session['session'] = views.Base.param1
    return final_result


def reseting(request):
    for i in range(0, 32):
        instructions.Instruction_type.val[i] = 0

    views.Base.vari = 0
    views.Base.param12.update(
        {'success': "False", 'result': "True", 'ctn': views.Base.vari + 1, 'data': instructions.Instruction_type.val,
         'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
         'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4})
    request.session['session'] = 0
    print(views.Base.param1)
    # return render(request, 'index.html', views.Base.param1)
    return HttpResponse(json.dumps(views.Base.param12))


def prev(request):
    instructions.Instruction_type.val = views.Base.stack_register.pop()
    views.Base.list_column_1 = views.Base.memory_list1.pop()
    views.Base.list_column_2 = views.Base.memory_list2.pop()
    views.Base.list_column_3 = views.Base.memory_list3.pop()
    views.Base.list_column_4 = views.Base.memory_list4.pop()
    views.Base.vari = views.Base.ins_number.pop()

    print("This is Prev")
    print(instructions.Instruction_type.val)
    print(views.Base.vari)
    views.Base.param12.update(
        {'data': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
         'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4, 'ctn': views.Base.vari + 1})

    return HttpResponse(json.dumps(views.Base.param12))


def dump(request):
    dump_hex = []
    for k, l in views.Base.dump_bin:
        if k == 16:
            temp = '0x' + '{0:04X}'.format(int(l, 2))
            dump_hex.append(temp)
        else:
            temp = '0x' + '{0:08X}'.format(int(l, 2))
            dump_hex.append(temp)
    log.log_dump(dump_hex
                 )
    print(dump_hex)
    param123 = {'ins_hex': dump_hex}
    return HttpResponse(json.dumps(param123))


def mainting_stack(register, list1, list2, list3, list4, ins_num):
    print("In stack function")
    if views.Base.vari + 1 <= len(views.Base.code_line1):
        print("In stack condition")
        ######### For Registers #########
        file1 = open("file1.txt", "w")
        file1.write(str(register))
        file1.close()
        file1 = open("file1.txt", "r")
        x = file1.read()
        views.Base.stack_register.append(json.loads(x))
        file1.close()
        #################################

        ######### For Memory ############
        file1 = open("file1.txt", "w")
        file1.write(str(list1))
        file1.close()
        file1 = open("file1.txt", "r")
        x = file1.read()
        views.Base.memory_list1.append(json.loads(x))
        file1.close()

        file1 = open("file1.txt", "w")
        file1.write(str(list2))
        file1.close()
        file1 = open("file1.txt", "r")
        x = file1.read()
        views.Base.memory_list2.append(json.loads(x))
        file1.close()

        file1 = open("file1.txt", "w")
        file1.write(str(list3))
        file1.close()
        file1 = open("file1.txt", "r")
        x = file1.read()
        views.Base.memory_list3.append(json.loads(x))
        file1.close()

        file1 = open("file1.txt", "w")
        file1.write(str(list4))
        file1.close()
        file1 = open("file1.txt", "r")
        x = file1.read()
        views.Base.memory_list4.append(json.loads(x))
        file1.close()
        #################################

        ######### For Instructions Number #########
        file1 = open("file1.txt", "w")
        file1.write(str(ins_num))
        file1.close()
        file1 = open("file1.txt", "r")
        x = file1.read()
        views.Base.ins_number.append(int(x))
        file1.close()
        #################################

        print(views.Base.stack_register)
