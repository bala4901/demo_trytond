from trytond.pool import Pool

def register():
    Pool.register(
        module='demo_trytond', type_='model')
    Pool.register(
        module='demo_trytond', type_='report')
    Pool.register(
        module='demo_trytond', type_='wizard')