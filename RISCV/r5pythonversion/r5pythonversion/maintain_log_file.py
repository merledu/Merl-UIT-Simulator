import logging
from . import views
from . import instructions
from . import Simulator_buttons

logging.basicConfig(filename='instructions.log', level=logging.INFO,
                        format='%(levelname)s:%(message)s')

with open('instructions.log', 'w'):
    pass

def log_file():
    logging.info('Instructions: {}'.format(views.Base.code_line1))
    logging.info('Registers: {}'.format(instructions.Instruction_type.val))
    logging.info('Memory +0: {}'.format(views.Base.list_column_1))
    logging.info('Memory +1: {}'.format(views.Base.list_column_2))
    logging.info('Memory +2: {}'.format(views.Base.list_column_3))
    logging.info('Memory +3: {}'.format(views.Base.list_column_4))


def log_dump(dump_hex):
    logging.info('Dumped Hex: {}'.format(dump_hex))