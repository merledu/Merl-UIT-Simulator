from django.shortcuts import render
from . import arithmetic

def read(request):
    return render(request, 'test.html')


def simulator(request):
    return render(request, 'simulator.html')

def index(request):
    result = 0
    whole_code = request.GET.get('editor', '')
    instruction = ['add','sub','div','mul','rem','addi','subi','divi','muli','remi',
    'and','or','xor','andi','ori','xori','sll','srl','sra','slli','srli','srai',
                   'ld','sw','jal']

    result = execute(whole_code)
    reg_name=['x0','x1','x2','x3','x4',
              'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14',
              'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 'x21', 'x22', 'x23', 'x24',
              'x25','x26','x27','x28','x29','x30','x31']

    ##### This Is Memory Block START
    file_values=open("templates\m.txt","r")
        #print(file_values.readable())
    list=[]
    for x in range(0,512):
        list.append(file_values.readline())
    file_values.close()
        #print(list)
    list1=[]
    for x in list:
        list1.append(x.replace('\n',''))
        #new_set = {x.replace('\n', '') for x in list}
        #print(list1)


    listkey=[]
    for x in range(0,512):
        listkey.append(hex(x))

    #print(len(list1))
    #print(len(listkey))
    #for x in range(0,512):
        #memory_block[hex(x)]=list1[x]

    ####This Is Memory Block END
    param = {'fresult': result, 'code': whole_code,'data':zip(arithmetic.Arithmetic.val,reg_name),'data1':zip(listkey,list1)}
    return render(request, 'index.html', param)


def execute(whole_code):
    code_line = []
    #code_line = whole_code.split(':')
    #code_line = code_line.split(';')
    whole_code=whole_code.replace('\r\n', '')
    whole_code= whole_code.replace(';', ':')
    code_line = whole_code.split(':')


    code_line = code_line[:-1]
    r_type = []
    i_type = []
    s_type = []
    count_i = 0
    count_r = 0
    count_s = 0
    vari = 0
    for i in range(vari, len(code_line)):
        x = code_line[vari]
        x = x.strip()
        if "addi" in x or "subi" in x or "muli" in x or "divi" in x or "remi" in x or "ori" in x or "andi" in x or "xori" in x or "slli" in x or "srli" in x or "srai" in x:
            i_type.append(arithmetic.I_type())
            print(len(i_type))
            # i_type[i].val = arithmetic.Arithmetic.val
            x = i_type[count_i].getoperatori(x)
            i_type[count_i].getsdi(x)
            count_i+=1
            if vari < len(code_line)-1:
                vari+=1
            #arithmetic.Arithmetic.val = i_type[i].val
        elif "ld" in x:
            i_type.append(arithmetic.I_type())
            print(len(i_type))
            # i_type[i].val = arithmetic.Arithmetic.val
            x = i_type[count_i].getoperatori(x)
            i_type[count_i].getsdl(x)
            count_i += 1
            if vari < len(code_line)-1:
                vari += 1

        elif "sw" in x:
            s_type.append(arithmetic.S_type())
            print(len(s_type))
            x = s_type[count_s].getoperators(x)
            s_type[count_s].getsds(x)
            count_s += 1
            if vari < len(code_line)-1:
                vari += 1


        # UJ Type Instruction
        elif "jal" in x:
            x = x[5:]
            for j in range(len(code_line)):
                if x in code_line[j] and (not ("jump" in code_line[j])):
                    code_line[j] = code_line[j].split(":")
                    vari = j+1
        else:
            r_type.append(arithmetic.R_type())
            print(len(r_type))
            # r_type[i].val = arithmetic.Arithmetic.val
            x = r_type[count_r].getoperator(x)
            r_type[count_r].getsd(x)
            count_r+=1
            if vari < len(code_line)-1:
                vari+=1
            #arithmetic.Arithmetic.val = r_type[i].val

    final_result = arithmetic.Arithmetic.val[arithmetic.Arithmetic.indexd]
    print(final_result)
    return final_result

def showmemory(request):
    #data = zip(arithmetic.Arithmetic.listkey, arithmetic.Arithmetic.listvalue)
    #print(arithmetic.Arithmetic.listkey)
    #print(arithmetic.Arithmetic.listvalue)

    file_values=open("templates\m.txt","r")
        #print(file_values.readable())
    list=[]
    for x in range(0,512):
        list.append(file_values.readline())
    file_values.close()
        #print(list)
    list1=[]
    for x in list:
        list1.append(x.replace('\n',''))
        #new_set = {x.replace('\n', '') for x in list}
        #print(list1)


    listkey=[]
    for x in range(0,512):
        listkey.append(hex(x))

    #print(len(list1))
    #print(len(listkey))
    #for x in range(0,512):
        #memory_block[hex(x)]=list1[x]

    return render(request,'table.html',{'data':zip(listkey,list1)})
