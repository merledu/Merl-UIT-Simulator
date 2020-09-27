from django.http import HttpResponse
from . import instructions
from . import views
import json


def decimal(request):
    print("This is Decimal")
    dec_dict = {'val': instructions.Instruction_type.val, 'list1': views.Base.list_column_1, 'list2': views.Base.list_column_2,
                'list3': views.Base.list_column_3, 'list4': views.Base.list_column_4}
    return HttpResponse(json.dumps(dec_dict))


def hex(request):
    print("This is Hex")
    hex_val = []
    mem1_hex = []
    mem2_hex = []
    mem3_hex = []
    mem4_hex = []
    for j in range(len(instructions.Instruction_type.val)):
        if instructions.Instruction_type.val[j] < 0:
            hex_val.append('0x' + '{0:08X}'.format((instructions.Instruction_type.val[j] + (1 << 32)) % (1 << 32)))
        else:
            hex_val.append('0x' + '{0:08X}'.format(instructions.Instruction_type.val[j]))
    for j in range(len(views.Base.list_column_1)):
        if views.Base.list_column_1[j] < 0:
            mem1_hex.append('{0:02X}'.format((views.Base.list_column_1[j] + (1 << 32)) % (1 << 32)))
        else:
            mem1_hex.append('{0:02X}'.format(views.Base.list_column_1[j]))


        if views.Base.list_column_2[j] < 0:
            mem2_hex.append('{0:02X}'.format((views.Base.list_column_2[j] + (1 << 32)) % (1 << 32)))
        else:
            mem2_hex.append('{0:02X}'.format(views.Base.list_column_2[j]))


        if views.Base.list_column_3[j] < 0:
            mem3_hex.append('{0:02X}'.format((views.Base.list_column_3[j] + (1 << 32)) % (1 << 32)))
        else:
            mem3_hex.append('{0:02X}'.format(views.Base.list_column_3[j]))


        if views.Base.list_column_4[j] < 0:
            mem4_hex.append('{0:02X}'.format((views.Base.list_column_4[j] + (1 << 32)) % (1 << 32)))
        else:
            mem4_hex.append('{0:02X}'.format(views.Base.list_column_4[j]))


    hex_dict = {'val1': hex_val, 'list1': mem1_hex, 'list2': mem2_hex,
                'list3': mem3_hex, 'list4': mem4_hex}
    return HttpResponse(json.dumps(hex_dict))


def ascii(request):
    mem1_ascii = []
    mem2_ascii = []
    mem3_ascii = []
    mem4_ascii = []
    print("This is ASCII")
    ascii_val = []
    for j in range(len(instructions.Instruction_type.val)):
        if instructions.Instruction_type.val[j] < 0:
            ascii_val.append('0x' + '{0:08X}'.format((instructions.Instruction_type.val[j] + (1 << 32)) % (1 << 32)))
        elif instructions.Instruction_type.val[j] < 32:
            ascii_val.append('0x' + '{0:08X}'.format(instructions.Instruction_type.val[j]))
        else:
            ascii_val.append(chr(instructions.Instruction_type.val[j]))
    for j in range(len(views.Base.list_column_1)):
        if views.Base.list_column_1[j] < 0:
            mem1_ascii.append('0x' + '{0:02x}'.format((views.Base.list_column_1[j] + (1 << 32)) % (1 << 32)))
        elif views.Base.list_column_1[j] < 32:
            mem1_ascii.append('0x' + '{0:02x}'.format(views.Base.list_column_1[j]))
        else:
            mem1_ascii.append(chr(views.Base.list_column_1[j]))


        if views.Base.list_column_2[j] < 0:
            mem2_ascii.append('0x' + '{0:02x}'.format((views.Base.list_column_2[j] + (1 << 32)) % (1 << 32)))
        elif views.Base.list_column_2[j] < 32:
            mem2_ascii.append('0x' + '{0:02x}'.format(views.Base.list_column_2[j]))
        else:
            mem2_ascii.append(chr(views.Base.list_column_2[j]))


        if views.Base.list_column_3[j] < 0:
            mem3_ascii.append('0x' + '{0:02x}'.format((views.Base.list_column_3[j] + (1 << 32)) % (1 << 32)))
        elif views.Base.list_column_3[j] < 32:
            mem3_ascii.append('0x' + '{0:02x}'.format(views.Base.list_column_3[j]))
        else:
            mem3_ascii.append(chr(views.Base.list_column_3[j]))


        if views.Base.list_column_4[j] < 0:
            mem4_ascii.append('0x' + '{0:02x}'.format((views.Base.list_column_4 + (1 << 32)) % (1 << 32)))
        elif views.Base.list_column_4[j] < 32:
            mem4_ascii.append('0x' + '{0:02x}'.format(views.Base.list_column_4[j]))
        else:
            mem4_ascii.append(chr(views.Base.list_column_4[j]))

    ascii_dict = {'val2': ascii_val, 'list1': mem1_ascii, 'list2': mem2_ascii,
                  'list3': mem3_ascii, 'list4': mem4_ascii}
    return HttpResponse(json.dumps(ascii_dict))


def unsigned(request):
    mem1_unsign = []
    mem2_unsign = []
    mem3_unsign = []
    mem4_unsign = []
    print("This is Unsigned")
    unsign_val = []
    for j in range(len(instructions.Instruction_type.val)):
        if instructions.Instruction_type.val[j] < 0:
            unsign_val.append(instructions.Instruction_type.val[j] + 2 ** 32)
        else:
            unsign_val.append(instructions.Instruction_type.val[j])
    for j in range(len(views.Base.list_column_1)):
        if views.Base.list_column_1[j] < 0:
            mem1_unsign.append(views.Base.list_column_1[j] + 2 ** 32)
        else:
            mem1_unsign.append(views.Base.list_column_1[j])


        if views.Base.list_column_2[j] < 0:
            mem2_unsign.append(views.Base.list_column_2[j] + 2 ** 32)
        else:
            mem2_unsign.append(views.Base.list_column_2[j])


        if views.Base.list_column_3[j] < 0:
            mem3_unsign.append(views.Base.list_column_3[j] + 2 ** 32)
        else:
            mem3_unsign.append(views.Base.list_column_3[j])


        if views.Base.list_column_4[j] < 0:
            mem4_unsign.append(views.Base.list_column_4[j] + 2 ** 32)
        else:
            mem4_unsign.append(views.Base.list_column_4[j])
    un_dict = {'val3': unsign_val, 'list1': mem1_unsign, 'list2': mem2_unsign,
               'list3': mem3_unsign, 'list4': mem4_unsign}
    return HttpResponse(json.dumps(un_dict))
