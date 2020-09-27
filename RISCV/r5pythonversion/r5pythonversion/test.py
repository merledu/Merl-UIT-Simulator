# # # # from RISCV.r5pythonversion.r5pythonversion import instructions
# # # # #
# # # # # val = 0
# # # # # nbits = 32
# # # # # print('{0:02X}'.format((val + (1 << 32)) % (1 << 32)))
# # # # # t = hex((val + (1 << nbits)) % (1 << nbits))
# # # # # t = chr(93)
# # # # # print(t)
# # # # # print(t)
# # # # #
# # # # # list_column_1 = []
# # # # # list_column_2 = []
# # # # # list_column_3 = []
# # # # # list_column_4 = []
# # # # # listkey = []
# # # # #
# # # # # counter_memory_address = 0
# # # # # for x in range(0, 512):
# # # # #     if (x == 512 / 4):
# # # # #         break
# # # # #     listkey.append('0x' + '{0:08X}'.format(counter_memory_address))
# # # # #     counter_memory_address = counter_memory_address + 4
# # # # #
# # # # # #########################################################
# # # # # for i in range(0, 512 * 4):
# # # # #     # memory_dictionary[hex(i)]=memory_value[i]
# # # # #     instructions.Instruction_type.memory_value[i] = instructions.Instruction_type.memory_dictionary_fetch['{0:08X}'.format(i)]
# # # # # #########################################################
# # # # #
# # # # #
# # # # # ########################################################## Memory  breaking For Views
# # # # #
# # # # #
# # # # #
# # # # # count_memory_break_view = 0
# # # # # for i in range(0, 514 * 4):
# # # # #     if (count_memory_break_view == len(instructions.Instruction_type.memory_value)):
# # # # #         break
# # # # #     list_column_1.append('{0:02X}'.format(instructions.Instruction_type.memory_value[count_memory_break_view]))
# # # # #     list_column_2.append('{0:02X}'.format(instructions.Instruction_type.memory_value[count_memory_break_view + 1]))
# # # # #     list_column_3.append('{0:02X}'.format(instructions.Instruction_type.memory_value[count_memory_break_view + 2]))
# # # # #     list_column_4.append('{0:02X}'.format(instructions.Instruction_type.memory_value[count_memory_break_view + 3]))
# # # # #     count_memory_break_view = count_memory_break_view + 4
# # # # #
# # # # #
# # # # # print(list_column_1)
# # # #
# # # # # stack = []
# # # # # a2 = []
# # # # # a1 = [1, 2, 3]
# # # # # new = {}
# # # # # dict1 = {'a1': a1}
# # # # # stack.append(dict1)
# # # # # print(stack)
# # # # # a1 = [9, 5, 6]
# # # # # dict1 = ({'a1': a1})
# # # # # stack.append(dict1)
# # # # # a1 = [7, 8, 9]
# # # # # for i in range(len(a1)):
# # # # #     a2.append(i+8)
# # # # # a1 = a2
# # # # # dict1 = ({'a1': a1})
# # # # # stack.append(dict1)
# # # # # print(stack)
# # # # # new = stack.pop()
# # # # # print(new)
# # # # # new = stack.pop()
# # # # # print(new)
# # # # # new = stack.pop()
# # # # # print(new)
# # # # # if not stack:
# # # # #     print("Empty")
# # # #
# # # # # import json
# # # # #
# # # # # a2 = []
# # # # # stack = []
# # # # # dict1 = {}
# # # # # dict2 = {}
# # # # #
# # # # #
# # # # # import numpy as geek
# # # # # a1 = [1, 2, 3]
# # # # # def test(a1):
# # # # #     file1 = open("file1.txt", "w")
# # # # #     file1.write(str(a1))
# # # # #     file1.close()
# # # # #
# # # # #     file1 = open("file1.txt", "r")
# # # # #     x = file1.read()
# # # # #     # dict1 = {"a1": x}
# # # # #     stack.append(json.loads(x))
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # for i in range(len(a1)):
# # # # #     a1 = [i+5, i+5, i+5]
# # # # #     test(a1)
# # # # #
# # # # #
# # # # # print(dict1)
# # # # # print(stack)
# # # # #
# # # # # # for i in range(len(stack)):
# # # # # #     stack[i] = json.loads(stack[i])
# # # # # #
# # # # # # print(stack)
# # # # # #
# # # # # # print(stack.pop())
# # # # #
# # # # t = 4 & 65280
# # # #
# # # # print(t)
# # # #
# # # #
# # # # bin = '00000000000000001111011101110000'
# # # #
# # # #
# # # # hex = '{0:08X}'.format(int(bin, 2))
# # # #
# # # # print(hex)
# # # import networkx as nx
# # # import matplotlib.pyplot as plt
# # #
# # # G = nx.path_graph(4)
# # # cities = {0: "Toronto", 1: "London", 2: "Berlin", 3: "New York"}
# # #
# # # H = nx.relabel_nodes(G, cities)
# # #
# # # print("Nodes of graph: ")
# # # print(H.nodes())
# # # print("Edges of graph: ")
# # # print(H.edges())
# # # nx.draw(H)
# # # plt.savefig("path_graph_cities.png")
# # # plt.show()
# #
# #
# #
# # ############################# GRAPH FOR DISPLAY INFO ####################################
# # from graphviz import Digraph
# #
# # f = Digraph('finite_state_machine', filename='fsm.gv')
# # f.attr(rankdir='LR', size='100,5')
# #
# # f.attr('node', shape='doublecircle')
# # f.node('Simulator with Execution')
# # f.node('Simulator with Dump')
# # f.node('Simulator with Single step forward')
# #
# # f.attr('node', shape='circle')
# # f.edge('', 'Initial State')
# # f.edge('Initial State', 'Home', label='request')
# # f.edge('Home', 'Editor', label='Start Button')
# # f.edge('Editor', 'Interpreter', label='Start Simulation Button with Instructions')
# # f.edge('Interpreter', 'Editor', label='Error')
# # f.edge('Interpreter', 'Bits Division', label='Instructions')
# # f.edge('Bits Division', 'Simulator', label='Bits divided Instructions')
# # f.edge('Simulator', 'Simulator with Execution', label='Run', shape='doublecircle')
# # f.edge('Simulator', 'Simulator with Single step forward', label='Step')
# # f.edge('Simulator', 'Simulator with Dump', label='Dump', shape='doublecircle')
# # f.edge('Simulator with Dump', 'Simulator with Execution', label='Run')
# # f.edge('Simulator with Execution', 'Simulator with Single step backward', label='Prev')
# # f.edge('Simulator with Execution', 'Simulator with Reset', label='Reset')
# # f.edge('Simulator with Execution', 'Simulator with Dump', label='Dump', shape='doublecircle')
# # f.edge('Simulator with Dump', 'Simulator with Single step forward', label='Step')
# # f.edge('Simulator with Dump', 'Simulator with Single step backward', label='Prev')
# # f.edge('Simulator with Dump', 'Simulator with Reset', label='Reset')
# # f.edge('Simulator with Single step forward', 'Simulator with Single step forward', label='Step')
# # f.edge('Simulator with Single step forward', 'Simulator with Dump', label='Dump', shape='doublecircle')
# # f.edge('Simulator with Single step forward', 'Simulator with Single step backward', label='Prev')
# # f.edge('Simulator with Single step forward', 'Simulator with Reset', label='Reset')
# # f.edge('Simulator with Single step forward', 'Simulator with Execution', label='Run')
# # f.edge('Simulator with Single step backward', 'Simulator with Single step backward', label='Prev')
# # f.edge('Simulator with Single step backward', 'Simulator with Single step forward', label='Step')
# # f.edge('Simulator with Single step backward', 'Simulator with Execution', label='Run')
# # f.edge('Simulator with Single step backward', 'Simulator with Dump', label='Dump', shape='doublecircle')
# # f.edge('Simulator with Single step backward', 'Simulator with Reset', label='Reset')
# # f.edge('Simulator with Reset', 'Simulator with Single step forward', label='Step')
# # f.edge('Simulator with Reset', 'Simulator with Execution', label='Run')
# # f.edge('Simulator with Reset', 'Simulator with Dump', label='Dump', shape='doublecircle')
# # f.edge('Registers Values', 'Memory Values', label='Memory')
# # f.edge('Memory Values', 'Registers Values', label='Register')
# # f.edge('Simulator with Reset', 'Memory Values', label='Memory')
# # f.edge('Simulator with Execution', 'Memory Values', label='Memory')
# # f.edge('Simulator with Single step forward', 'Memory Values', label='Memory')
# # f.edge('Simulator with Single step backward', 'Memory Values', label='Memory')
# # f.edge('Simulator with Dump', 'Memory Values', label='Memory')
# # f.edge('Simulator', 'Memory Values', label='Memory')
# # f.edge('Simulator with Reset', 'Registers Values', label='Register')
# # f.edge('Simulator with Execution', 'Registers Values', label='Register')
# # f.edge('Simulator with Single step forward', 'Registers Values', label='Register')
# # f.edge('Simulator with Single step backward', 'Registers Values', label='Register')
# # f.edge('Simulator with Dump', 'Registers Values', label='Register')
# # f.edge('Simulator', 'Registers Values', label='Register')
# # f.view()
# #
# #
# # ############################# GRAPH FOR DISPLAY INFO ####################################
# # # f.edge('8', '10')
# # # f.edge('10', '12')
# # # f.edge('10', '11')
# # # f.edge('11', '20')
# # # f.edge('12', '14')
# # # f.edge('12', '13')
# # # f.edge('13', '20')
# # # f.edge('14', '16')
# # # f.edge('14', '15')
# # # f.edge('15', '20')
# # # f.edge('16', '18')
# # # f.edge('16', '17')
# # # f.edge('17', '20')
# # # f.edge('18', '20')
# # # f.edge('18', '19')
# # # f.edge('19', '20')
# # # f.edge('20', '5,6')
# # # f.edge('5,6', '21')
# # # f.edge('21', '22')
# # # f.edge('21', '23')
# # # f.edge('22', '21')
# # # f.edge('23', '24')
# # # f.edge('24', '23')
# # # f.edge('23', '25')
# # # f.edge('25', '26')
# # # f.edge('26', '25')
# # # f.edge('25', '27')
# # # f.edge('27', '28')
# # # f.edge('28', '27')
# # # f.edge('27', '29,30,31')
# # #
# # # f.view()
# #
# # ############################# GRAPH FOR DISPLAY INFO ####################################
# #
# # # ############################### GRAPH FOR DUMP ###############################
# # #
# # # from graphviz import Digraph
# # #
# # # f = Digraph('finite_state_machine', filename='fsm.gv')
# # # f.attr(rankdir='LR', size='100,5')
# # #
# # # f.attr('node')
# # # f.node('0')
# # # f.node('1,2')
# # # f.node('3,4,5')
# # # f.node('6,7,8')
# # #
# # # f.attr('node', shape='circle')
# # # f.edge('0', '1,2')
# # # f.edge('1,2', '6,7,8')
# # # f.edge('1,2', '3,4,5')
# # # f.edge('3,4,5', '1,2')
# # #
# # # f.view()
# # #
# # # ############################### GRAPH FOR DUMP ###############################
# # from django import forms
# # #
# # # from django.shortcuts import render
# # #
# # # class FormFood(forms.Form):
# # #     CHOICES = [(1, 'Yes'), (2, 'No')]
# # #     response = forms.ChoiceField(widget=forms.RadioSelect,
# # #               label = 'Would you like:' + '\n' + 'test'  , choices=CHOICES)
# # #
# # #
# # #
# # #
# # # def home_view(request):
# # #     context = {}
# # #     context['form'] = FormFood()
# # #     return render(request, "home.html", context)
# # import pandas as pd
# # df = pd.DataFrame({'1': [14561,'X store','Sales Quantity',1],
# #                    '2': [14561,'X store','Net Sales',2],
# #                    '3': [16534,'Y store','Sales Quantity',2],
# #                    '4': [16534,'Y store','Net Sales',1]})
# #
# # df = df.transpose()
# # print('store_code' + str(df[0].unique()))
# # print('store_name' + str(df[1].unique()))
# # print('sales_total' + str(df[2].unique()))
# # print('net_sales_total' + str(df[3].unique()))
# #
# # Function to demonstrate printing pattern triangle
# #
# # import matplotlib.pyplot as plt
# #
# # def drawline(inches):
# #     x1, y1 = [0, inches], [0, 0] # horizontal line
# #     x2, y2 = [0, 0], [0, inches] # vertical line
# #
# #     plt.plot(x1, y1, x2, y2, marker='o')
# #     plt.show()
# #
#
# # drawline(8)
#
# # def encrypt(text, s):
# #     result = ""
# #
# #     # traverse text
# #     for i in range(len(text)):
# #         char = text[i]
# #
# #         # Encrypt uppercase characters
# #         if (char.isupper()):
# #             result += chr((ord(char) + s - 65) % 26 + 65)
# #
# #             # Encrypt lowercase characters
# #         else:
# #             result += chr((ord(char) + s - 97) % 26 + 97)
# #
# #     return result
# #
# #
# # # check the above function
# # text = "abcd"
# # s = 1
# # print("Text  : " + text)
# # print("Shift : " + str(s))
# # print("Cipher: " + encrypt(text, s))
# #
# # text = "CEASER CIPHER DEMO"
# # s = 4
# # import csv
# # import pprint
# # import pandas as pd
# #
# #
# #
# # input_file = pd.read_csv('country.csv', header = None)
# #
# # input_file = input_file.to_dict()
# # print(input_file)
# # print(type(input_file))
#
# # import mmap
# # import re
# # status = False
# # username = input("username: ")
# # names_file = open("names_file.txt", "a")
# #
# # paste = bytes(username, 'utf-8')
# # with open("names_file.txt", "rb", 0) as file, \
# #     mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
# #     for f in file:
# #         f = f.strip()
# #         if f == paste:
# #             print("true")
# #             status = True
# #     if status == False:
# #         names_file.write("\n" + username)
# #         print(username + " got added to the list")
# #
# #
# #
# # names_file.close()
#
# # import random
# # students = int(input("How many students do you want to enter? \n Students: "))
# #
# # Student_Count =  [([0] * 4) for i in range(students)]
# # for a in range(students):
# #     for b in range(4):
# #         Student_Count[a][b] = random.randint(1,100)
# # Max = (list(map(max,Student_Count)))
# # Min = (list(map(min,Student_Count)))
# # print("MAX")
# # print(Max)
# # print("MIN")
# # print(Min)
# #
# # for a in range(students):
# #     print("Student", a + 1 , end = "\t\t\t")
# #     for b in range (4):
# #         print(Student_Count[a][b], end = "\t\t\t ") # the print of Random numbers
# #     print()
# # print("_____________________________________________________________")
# # print("Highest", end = "\t\t\t\t")
# # for c in range(students):
# #     print(Max[c], end = "\t\t\t ")
# # print()
# # print("Lowest", end = "\t\t\t\t ")
# # for c in range(students):
# #     print(Min[c], end = "\t\t\t ")
#
# # mylist = [[[2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0],
# #            [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0],
# #            [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0]],
# #           [[2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0],
# #            [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0],
# #            [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0],
# #            [2.67, 2.67, 2.0, 2.0], [2.67, 2.67, 2.0, 2.0]]]
# # allGPA = []
# # myaverage = mylist
# # c = 0
# # count = 0
# # gpa = [0]
# # for list in mylist:
# #     for i in range(len(list)):
# #         gpa[0] = sum(mylist[c][i]) / len(mylist[c][i])
# #         allGPA.append(gpa)
# #         myaverage[c][i] = gpa
# #
# #     c = c + 1
# # print(myaverage)
#
# # import pyautogui as pyautogui
# #
# # pyautogui.write(r'C:\Users\Alex\Dropbox\PythonDev\Instagram\imagename.jpg', interval=0.1)
# #
#
# #
# # daftar = ["K","H","S"]
# # kiri = daftar
# # kanan = []
# # petani = []
# #
# # def kirikekanan():
# #     global daftar, kiri, kanan, petani, naonweh
# #     petani = list(next(naonweh))
# #     kiri_sementara = list(set(kiri).difference(petani)) #mengurangkan isi himpunan yang ada di kiri dengan yg dibawa petani
# #     if set(kiri_sementara) == {"K","H"} or set(kiri_sementara) == {"K","S"}:
# #         kirikekanan()
# #     else:
# #         kiri = kiri_sementara
# #         kanan = list(set(daftar).difference(kiri))
# #         print("yang dibawa petani = {}, sehingga kiri = {}, kanan = {}y".format(petani, kiri, kanan))
# #
# # def kanankekiri():
# #     global daftar, kiri, kanan, petani, naonweh2
# #     if kanan == {"K","H"} or kanan == {"K","S"}:
# #         petani = list(next(naonweh2))
# #         kanan = list(set(kanan).difference(petani))
# #         kiri = list(set(daftar).difference(kanan))
# #         print("yang dibawa petani = {}, sehingga kiri = {}, kanan = {}g".format(petani, kiri, kanan))
# #     else:
# #         petani = []
# #         print("yang dibawa petani = {}, sehingga kiri = {}, kanan = {}g".format(petani, kiri, kanan))
# #
# #
# # while set(kanan) != set(daftar):
# #     naonweh = iter(kiri)
# #     naonweh2 = iter(kanan)
# #     kirikekanan()
# #     kanankekiri()
#
# # arq = open("output.txt", "w")
# # count = 0
# # file = open("names_file.txt", "r")
# # t = []
# # for line in file.readlines():
# #     line = line.strip()
# #     t.append(line)
# # for i in range(len(t)):
# #     if 'AS' in t[i]:
# #         count = count + 1
# #         print("set policy", t[i], "then accept", t[i+1])
# # print("\n Display return", count, "lines")
#
#
# # def pre_word(word):
# #     if word.startswith("pre") and word.isalpha():
# #         return True
# #     else:
# #         return False
# #
# # word = input("enter a word that starts with \"pre\": ")
# #
# # word = pre_word(word)
# #
# # if word == False:
# #     print('this is not a \"pre\" word')
# #
# # else:
# #     print('this is a valid \"pre\" word')
#
# # import random
# # count = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # dice1 = random.randrange(1,7)
# # freq = 12
# # def probabilities_sum():
# #     print('\nprobability for 2 dices:')
# #     for j in range(1, 12):
# #         percentage_2 = (count[j - 1] / freq) * 100
# #         procent_2 = str(percentage_2)
# #         print('this is J', j)
# #         print(j + 1, ':', procent_2)
# #
# # probabilities_sum()
# #
#
#
# # batch_id = input("enter your product ID: ")
# # IDs = []
# # temp = ''
# # for i in batch_id:
# #     if i == '-':
# #         IDs.append(temp)
# #         temp = ''
# #     else:
# #         temp += i
# # if temp:
# #     IDs.append(temp)
# #
# # print("Your Country code is =", IDs[0])
# # print("Your product code is =", IDs[1])
# # print("Your Batch Number is =", IDs[2])
#
# # arq = open("output.txt", "w")
# # # count = 0
# # # file = open("/homescript/ASN.txt", "r")
# # # t = []
# # # for line in file.readlines():
# # #     line = line.strip()
# # #     t.append(line)
# # # for i in range(len(t)):
# # #     if 'AS' in t[i]:
# # #         count = count + 1
# # #         print("set policy", t[i], "then accept", t[i+1])
# # #         print("set policy", t[i], "then accept", t[i+2])
# # # print("\n Display return", count, "lines")
# #
# # list = ['4', '1', '3', '9', 'Z', 'P', 'V', 'A']
# # number = []
# # alphabet = []
# # for l in list:
# #     if l.isnumeric():
# #         number.append(l)
# #     else:
# #         alphabet.append(l)
# #
# # number = sorted(number)
# # alphabet = sorted(alphabet)
# # list = alphabet + number
# # print(list)
# #
#
# # def bubbleSort(arr):
# #     n = len(arr)
# #     for i in range(n):
# #         print(arr[i])
# #         for j in range(0, n - i - 1):
# #             if arr[j] > arr[j + 1]:
# #                 print(arr[j], arr[j+1])
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# #             print(arr)
# #
# #             # Driver code to test above
# #
# #
# # arr = [5, 2, 3, 7, 10, 1, 8]
# # bubbleSort(arr)
# # print("Sorted array")
# # print(arr)
#
# # def octal_to_string(octal):
# #     permission = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
# #     result = ""
# #     # Iterate over each of the digits in octal
# #     for ___ in [int(n) for n in str(octal)]:
# #         result += permission[___]
# #     return result
# #
# # print(octal_to_string(755)) # Should be rwxr-xr-x
# # print(octal_to_string(644)) # Should be rw-r--r--
# # print(octal_to_string(750)) # Should be rwxr-x---
# # print(octal_to_string(600)) # Should be rw-------
# # def octal_to_string(octal):
# #     result = ""
# #     value_letters = [(4,"r"),(2,"w"),(1,"x")]
# #     # Iterate over each of the digits in octal
# #     for ___ in [int(n) for n in str(octal)]:
# #         # Check for each of the permissions values
# #         for value, letter in value_letters:
# #             if ___ >= value:
# #                  result += letter
# #                  ___ -= value
# #             else:
# #                 result += "-"
# #     return result
# #
# # print(octal_to_string(755)) # Should be rwxr-xr-x
# # print(octal_to_string(644)) # Should be rw-r--r--
# # print(octal_to_string(750)) # Should be rwxr-x---
# # print(octal_to_string(600)) # Should be rw-------
#
# #
# # def Reverse(Pattern):
# #     rev = []
# #     n = len(Pattern)
# #     for i in range(n):
# #         n = n-1
# #     rev.append(Pattern[::-1])
# #     return rev[0]
# #
# # def Complement(Pattern):
# #   complements = {"A":"T", "T":"A", "G":"C", "C":"G"}
# #   nucleotides = []
# #   for i in Pattern:
# #       nucleotides += complements[i]
# #   return "".join(nucleotides)
# #
# # print(Reverse("ACACAC"))
# # print(Complement("ACACAC"))
# #
# #
# # def ReverseComplement(Pattern):
# #     rev = []
# #     n = len(Pattern)
# #     for i in range(n):
# #         n = n-1
# #     rev.append(Pattern[::-1])
# #     complements = {"A":"T", "T":"A", "G":"C", "C":"G"}
# #     nucleotides = []
# #     for i in Pattern:
# #         nucleotides += complements[i]
# #     return "".join(nucleotides)
# #
# # print(ReverseComplement("ACACAC"))
# # secret_number = 9
# # guess_count = 0
# # guess_limit = 3
# # status = False
# # while guess_count < guess_limit:
# #     guess = int(input('Guess: '))
# #     guess_count += 1
# #     if guess == secret_number:
# #         print('You Won!')
# #         status = True
# #         break
# # if status == False:
# #     print('You Lose!')
#
# # def streamdata(var, message_var):
# #     print(var, message_var)
# #
# # def messages_var1():
# #     print("message1")
# # def messages_var2():
# #     print("message2")
# # def messages_var3():
# #     print("message3")
# # var1 = 'abc'
# # var2 = 'abcd'
# # var3 = 'abcde'
# #
# # list1 = [var1, var2, var3]
# # message = [messages_var1, messages_var2, messages_var3]
# # run_data_for_all = []
# # for i in range(len(list1)):
# #     run_data_for_all.append(streamdata(list1[i], message[i]))
#
# #
# # class A(object):
# #     a = None
# #     def b(cls):
# #         print("A class")
# #
# # a = A()
# # print(a.a is a.a)
# # print(a.b)
# # print()
# # class B(object):
# #     a = None
# #     @staticmethod
# #     def b():
# #         print("B class")
# # B.b()
# # b = B()
# #
# # print(b.a is b.a)
# # print(b.b)
# # print()
# #
# # class C(object):
# #     a = None
# #     @classmethod
# #     def b(self):
# #         print("C class")
# # C.b()
# # c = C()
# # print(c.a is c.a)
# # print(c.b)
# # print()
#
# # name = input('>>>')
# # ascending_order = name.split(',')
# # ascending_order = sorted(ascending_order, reverse=True)
# # print(ascending_order)
#
# # l1 = [1, 2, 3]
# # s = 2
# # new_list = []
# # all_combination = []
# # def combination(numbers, n, subset):
# #     if len(subset) == n:
# #         all_combination.append(subset)
# #     else:
# #         for i in range(len(numbers)):
# #             combination(numbers, n, subset + [numbers[i]])
# #
# #
# # combination(l1, s, new_list)
# # print(all_combination)
#
# # a = [-2,1,5,3,8,5,6]
# # b = [1,2,5]
# # def getvalues(original_list, indexes_list):
# #     new_list = []
# #     for i in indexes_list:
# #         new_list.append(original_list[i])
# #     return new_list
# # result = getvalues(a, b)
# # print(result)
#
# # import re
# # file1 = open("names_file.txt", "r")
# # l = file1.readlines()
# # new_list = []
# # for i in l:
# #     m = re.findall(r'\d+', i)
# #     new_list.append(m)
# # print(new_list)
# # for j in range(len(new_list)):
# #     for k in range(2):
# #         new_list[j][k] = int(new_list[j][k])
# # print(new_list)
#
# # import itertools
# #
# # lst1=[1, 2, 3, 5, 6, 3, 9, 5, 1, 2]
# # k = int(input())
# # lst = [i for j in range(1,k+1) for i in itertools.combinations(lst1, j)]
# # set1 = set(lst)
# # print(lst)
# # print(set1)
# # set1 = list(set1)
# # new = []
#
# #
# # l1 = [1, 2, 3, 5, 6, 3, 9, 5, 1, 2]
# # s = 3
# # new_list = []
# # all_combination = []
# # def combination(numbers, n, subset):
# #     if len(subset) == n:
# #         all_combination.append(subset)
# #     else:
# #         for i in range(len(numbers)):
# #             combination(numbers, n, subset + [numbers[i]])
# # combination(l1, s, new_list)
# # print(all_combination)
# # unique = []
# # status = False
# # for i in all_combination:
# #     for j in range(len(i)):
# #         l = j+1
# #         for k in range(l, len(i)):
# #             if i[j] == i[k] and i[j]:
# #                 status = True
# #                 break
# #             else:
# #                 status = False
# #         if status == True:
# #             break
# #
# #     if status == False:
# #         unique.append(i)
# # print(unique)
#
# # team = {'a': 6, 'b': 8, 'c': 2, 'k': 23, 'd': 18, 'r': 13, 'w': 4, 'h': 9}
# #
# # team = sorted(team.items(), key =
# #              lambda kv:(kv[1], kv[0]), reverse=True)
# # print(team)
# # print("Top 3 Bands")
# # print(team[:3])
# # print("Bottom 3 Bands")
# # print(team[-3:])
#
# # A = [[['m', 'b'], ['f', 'g']], [['g', 'h'], ['f', 'b']], [['f', 'g'], ['m', 'b']], [['l', 'k'], ['d', 'c']]]
# # B = []
# # C = []
# # for i in A:
# #     for j in i:
# #         if j not in B:
# #             B = B + [j]
# #
# # c = 0
# # c1 = 1
# # counter = int(len(B) / 2)
# # for k in range(counter):
# #     C.append([B[k+c], B[k+c1]])
# #     c = c + 1
# #     c1 = c + 1
# # print(C)
#
#
# # t = ["bla bla bla", "yada yada yada","foo boo, foo", "yoo no you are not in list"]
# # # words = ["test", "bla", "yoo"]
# # # negation = ["no","not","none"]
# # # unmatched = []
# # # matched = []
# # # for i in words:
# # #     for j in t:
# # #         if i in j:
# # #             matched.append(j)
# # #
# # # for l in t:
# # #     if l not in matched and l not in unmatched:
# # #         unmatched.append(l)
# # #
# # # for m in negation:
# # #     for k in matched:
# # #         if m in k:
# # #             matched.remove(k)
# # #
# # # print(unmatched)
# # # print(matched)
#
#
# # import scipy.stats as s
# # import matplotlib.pyplot as plt
# # x = []
# # for i in range(0,50):
# #     x.append(s.poisson.pmf(i, 10))
# # print(x)
# #
# # for i in range(len(x)):
# #     x[i] = format(x[i], '')
# #
# # print(x)
# # plt.plot(x)
# #
#
# # import random
# # nwb = 5     # number of winning balls
# # rwb = 10    # range of winning balls
# # npb = 2     # number of powerballs
# # rpb = 20    # range of powerballs
# #
# # # randomly draw a list of winning balls
# # actual = []
# # while nwb > 0:
# #     x = random.randint(1, rwb)
# #     if x not in actual:
# #         actual.append(x)
# #         nwb = nwb - 1
# #         actual.sort()
# #
# # # randomly draw a list of winning powerballs
# # pbactual = []
# # while npb > 0:
# #     x = (random.randint(1, rpb))
# #     if x not in pbactual:
# #         pbactual.append(x)
# #         npb = npb - 1
# #         pbactual.sort()
# #
# #
# # win = False
# # run = True
# # count = 0
# # nwb2 = len(actual)
# # npb2 = len(pbactual)
# # wb = []     # list of randomly choosen balls
# # pbsim = []  # list of randomly choosen powerballs
# #
# # while win == False:
# #     while run:
# #         x = random.randint(1, rwb)
# #         if x not in wb:
# #             wb.append(x)
# #             pbactual.sort()
# #
# #         if len(wb) == nwb2:
# #             while npb2 > 0:
# #                 x = random.randint(1, rpb)
# #                 if x not in pbsim:
# #                     pbsim.append(x)
# #                     npb2 = npb2 - 1
# #             run = False
# #             win = True
# #
# #
# #
# #     actual.sort()
# #     wb.sort()
# #     pbactual.sort()
# #     pbsim.sort()
# #     count += 1
# #     print(actual, wb, pbactual, pbsim)
#
#
# # import bs4
# # import requests
# # from bs4 import BeautifulSoup
# #
# # result = requests.get("http://m.eredmenyek.com/?d=-1")
# # src = result.content
# # soup = BeautifulSoup(src)
# #
# # scores = []
# # match = []
# #
# # for final in soup.find_all("a",class_="fin"):
# #     scores.append(final.text)
# #
# # for span in soup.find(id="score-data").find_all('span'):
# #     if span.next_sibling != None:
# #         match.append(span.next_sibling)
# #
# # print(scores)
# # print(match)
# #
# # file = open("list.txt", "w")
# #
# # for index in range(len(match)):
# #     file.write(str(match[index].encode("utf-8")) + "\t" + str(scores[index].encode("utf-8")) + "\n")
# # file.close()
# #
#
#
# # T = np.array([137, 145, 150, 152, 159, 160, 184])
# # Di = np.array([1, 0, 1, 1, 1, 0, 1])
# # r = 5.0
# # def lnL(mu, sigma):
# #     return np.log(sigma) - (1 / 2) * np.sum(Di * ((T - mu) / sigma) ** 2) + np.sum(1 - Di) * -r
# # sol = lnL(15.0, 258.0)
# # print(sol)
# # from math import sqrt
# # from scipy.optimize import fsolve
# # import numpy as np
# #
# # T = np.array([137, 145, 150, 152, 159, 160, 184])
# # Di = np.array([1, 0, 1, 1, 1, 0, 1])
# # r = 5.0
# #
# #
# # def lnL(P):
# #     mu, sigma = P
# #     f1 = -r * np.log(sigma) - (1 / 2) * np.sum(Di * ((T - mu) / sigma) ** 2) + np.sum(1 - Di)
# #     return [f1]
# #
# #
# # sol = fsolve(lnL, (15.0, 258.0))
# # print(sol)
#
#
# # from threading import Thread
# #
# #
# # class First:
# #     def __init__(self):
# #         self.var1 = 'hello'
# #     def myfunc(self,event):
# #         Second(self.var1)
# #
# #
# # class Second(Thread):
# #     def __init__(self, var1):
# #         self.var1 = var1
# #         self.my_list = []
# #         Thread.__init__(self)
# #         self.start()    # start the thread i.e. run()
# #
# #     #----------------------------------------------------------------------
# #     def run(self):
# #         self.my_list.append(self.var1)
# #
# # class Third:
# #     var = 1
# #     obj = Second(var)
# #     print(obj.my_list)
#
# # str_var = 'host = "s" port = "d" service_name = "a" pass = "b" user = "c"'
# # list1 = str_var.split(" ")
# # for i in list1:
# #     if i == '=':
# #         list1.remove(i)
# # print(list1)
# # dict1 = {}
# # for i in range(int(len(list1) / 2)):
# #     dict1[list1[i]] = list1[i+1]
# # print(dict1)
#
# # class Reader:
# #
# #   def read(self, list1):
# #     s = "The list reads as such:"
# #     for index, value in enumerate(list1, start=1):
# #       s = s + "\n  element number {} is:  {}".format(index, value)
# #     print(s)
# #
# #
# # Obj = Reader()
# #
# # Obj.read(["haii", "my", "name", "is", "Jhon"])
#
# # height = int(input("Enter the height of the triangle: \n"))
# # #
# # # array = [1]
# # #
# # # for ch in range(height):
# # #     t = (str(array)[1:-1])
# # #     t = t.replace(',', ' ')
# # #     print(t)
# # #     newarray = []
# # #     newarray.append(array[0])
# # #     for ch in range(len(array) - 1):
# # #         (newarray.append(array[ch] + array[ch+1]))
# # #     t = str(newarray.append(array[-1]))[1:-1]
# # #
# # #     array = (newarray)
#
# # def list(L):
# #     L = []
# #     n = int(input('how many times?'))
# #     for i in lisca:
# #         if i not in L:
# #             L.append(i)
# #     L.sort()
# #     return L
# #
# #
# # lisca = [1, 2, 3, 2, 5, 6, 7, 2, 1, 7, 1, 7]
# # lisca = list(lisca)
# # print(lisca)
#
#
# # l1 = [1, 2, 3]
# # s = 2
# # unique = []
# # def subsets(set):
# #     if set == []:
# #         return [[]]
# #
# #     sub = subsets(set[1:])
# #     # This will give you all the subsets of given list and This is also the return variable of the function.
# #     all_combination = (sub + [[set[0]] + x for x in sub])
# #     ########################################################
# #     # This for loop will give you a subsets of desire length.
# #     for i in range(len(all_combination)):
# #         if int(len(all_combination[i])) == s and all_combination[i] not in unique:
# #             unique.append(all_combination[i])
# #     #########################################################
# #     return all_combination
# #
# # print(subsets(l1))
# # print(unique)
#
#
# temp = 2047
# temp1 = -2047 + 2 ** 32
# temp = temp * temp1
# if temp < 0:
#     n = temp + 2 ** 64
#     print(n)
#     binary = '{0:064b}'.format(n)
#     print(binary)
#     print(len(binary))
#     binary = binary[0:32]
#     temp = int(binary, 2)
#     temp = temp - 2 ** 32
#     print(temp)
# else:
#     binary = '{0:064b}'.format(temp)
#     print(binary)
#     length = len(binary)
#     binary = binary[0:32]
#     temp = int(binary, 2)
#     if temp > 2047:
#         temp = temp - 2 ** 32
#     print(len(binary))
#     print(temp)
#     print(binary)

#
#from RISCV.r5pythonversion.r5pythonversion import Simulator_buttons as s
# from RISCV.r5pythonversion.r5pythonversion import views as v
# from RISCV.r5pythonversion.r5pythonversion import Display_Info as d
# # #
# # # v.interpreter("beq a5,a3,end")
# # #s.stepping('mulhu x7,x5,x6')
# # whole = " addi a5,zero,17\nstart:\naddi a1,zero,1\nupx:\nadd a0,a2,zero\nup:\naddi a3,a3,1\nadd a2,a0,a1\nbeq a5,a3,end\nandi a4,a3,1\nbeq a4,zero,upx\nadd a1,a2,zero\njal up\nend:"
# whole = 0
# d.Display_info_IMC(whole)



dict1 = {}
code = ['addi x5,x0,12', 'c.addi x6,1', 'l1:', 'c.li x7,1', 'beq x6,x7,end', 'c.add x7,x6', 'end:', 'add x8,x5,x7', 'c.jal l1', 'sub x9,x8,x6']
a = hex(12)
pc_count = 0
pc = '0x' + '{0:01X}'.format(pc_count)
for i in code:
    if ':' not in i:
        if '.' in i:
            dict1[pc] = i
            pc_count = pc_count + 2
            pc = '0x' + '{0:01X}'.format(pc_count)
        else:
            dict1[pc] = i
            pc_count = pc_count + 4
            pc = '0x' + '{0:01X}'.format(pc_count)
    else:
        continue
print(dict1)
vari = 0




pc_to = ''
pc_from = ''
label = 'l1'
for i in range(len(code)):
    if pc_to == '' or pc_from == '':
        if code[i] == label+':':
            pc_to = code[i+1]
        if "jal" in code[i] and label in code[i]:
            pc_from = code[i]

print(pc_to)
print(pc_from)


for key in dict1:
    if dict1[key] == pc_to:
        pc_to = key
    if dict1[key] == pc_from:
        pc_from = key

print("This is pc_To " + str(pc_to))
print("This is pc_From " + str(pc_from))
pc_current = pc_from

pc_next = int(pc_current, 16) + (int(pc_to, 16) - int(pc_from, 16))
pc_next = '0x' + '{0:01X}'.format(pc_next)
pc_new = pc_next

print("This is next instruction address " + str(pc_new))

label_value = int((int(pc_to, 16) - int(pc_from, 16))/2)
print("This is label value " + str(label_value))



