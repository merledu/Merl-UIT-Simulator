
from django.shortcuts import render
from . import instructions
from . import Interpreter
from . import InterpreterIM
import os

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
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, '..', 'templates/m.txt')
    # file_path = os.path.join(templates_path, "m.txt")
    file_values=open(file_path,"r")
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
