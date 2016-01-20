from trytond.pool import Pool
from sample_module import *

def register():
    Pool.register(
        'sample_module',
        module='demo_trytond', type_='model')
    Pool.register(
        module='demo_trytond', type_='report')
    Pool.register(
        module='demo_trytond', type_='wizard')