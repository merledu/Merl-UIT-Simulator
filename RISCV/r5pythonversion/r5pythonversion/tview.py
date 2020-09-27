import json

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from . import instructions
from django.shortcuts import render

class Base:
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
    pc = []
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

val = []
val1 = []
val2 = []
val3 = []
for i in range(0, 32):
    val.append(0)

def home(request):

    reg_name = ['x0(zero)', 'x1(ra)', 'x2(sp)', 'x3(gp)', 'x4(tp)',
                'x5(t0)', 'x6(t1)', 'x7(t2)', 'x8(s0)', 'x9(s1)', 'x10(a0)', 'x11(a1)', 'x12(a2)', 'x13(a3)', 'x14(a4)',
                'x15(a5)', 'x16(a6)', 'x17(a7)', 'x18(s2)', 'x19(s3)', 'x20(s4)', 'x21(s5)', 'x22(s6)', 'x23(s7)',
                'x24(s8)',
                'x25(s9)', 'x26(s10)', 'x27(s11)', 'x28(t3)', 'x29(t4)', 'x30(t5)', 'x31(t6)']

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
        instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch[
            '{0:08X}'.format(i)]
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

    return render(request, 't.html', {'data1': zip(reg_name, val), 'data2': zip(Base.listkey, Base.list_column_1, Base.list_column_2, Base.list_column_3, Base.list_column_4)})



def test_view(request):
    for i in range(0, 32):
        val[i] = 0
    print("hello")
    reg_name = ['x0(zero)', 'x1(ra)', 'x2(sp)', 'x3(gp)', 'x4(tp)',
                'x5(t0)', 'x6(t1)', 'x7(t2)', 'x8(s0)', 'x9(s1)', 'x10(a0)', 'x11(a1)', 'x12(a2)', 'x13(a3)', 'x14(a4)',
                'x15(a5)', 'x16(a6)', 'x17(a7)', 'x18(s2)', 'x19(s3)', 'x20(s4)', 'x21(s5)', 'x22(s6)', 'x23(s7)',
                'x24(s8)',
                'x25(s9)', 'x26(s10)', 'x27(s11)', 'x28(t3)', 'x29(t4)', 'x30(t5)', 'x31(t6)']

    c = 2+3

    for i in range(0, 32):
        val[i] = i
    dict1 = {'c': c, 'b': 'hey', 'data': val}
    print(val)
    return HttpResponse(json.dumps(dict1))


def decimal(request):
    print("This is Decimal")
    dec_dict = {'val': val}
    return HttpResponse(json.dumps(dec_dict))


def hex(request):
    print("This is Hex")
    for j in range(len(val)):
        val1.append('0x' + '{0:08X}'.format(val[j]))
    hex_dict = {'val1': val1}
    return HttpResponse(json.dumps(hex_dict))


def ascii(request):
    print("This is ASCII")
    for j in range(len(val)):
        if j < 32:
            val2.append('0x' + '{0:08X}'.format(val[j]))
        else:
            val2.append(chr(j))
    ascii_dict = {'val2': val2}
    return HttpResponse(json.dumps(ascii_dict))


def unsigned(request):
    print("This is Unsigned")
    for j in range(len(val)):
        if j < 0:
            val3.append(j + 2 ** 32)
        else:
            val3.append(j)
    un_dict = {'val3': val3}
    return HttpResponse(json.dumps(un_dict))

