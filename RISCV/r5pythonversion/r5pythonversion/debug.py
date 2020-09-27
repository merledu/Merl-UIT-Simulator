from RISCV.r5pythonversion.r5pythonversion import views
from RISCV.r5pythonversion.r5pythonversion import C_views
from RISCV.r5pythonversion.r5pythonversion import instructions
str1 = 'c.addi x5,12\r\nc.addi x6,13\r\nc.bnez x5,label\r\nc.addi x7,14\r\nlabel:\r\n     c.mv x5,x6'
code_line = [line for line in str1.split('\n') if line.strip() != '']
for x in range(0,10):
    result = views.stepping(views.Base.vari)
print(result)
print(instructions.Instruction_type.val)
