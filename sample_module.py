from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta


class sample_module(ModelSQL, ModelView):
    # description (mandatory on first declaration)
    'Sample Module'

    # Internal class name. Always used as a reference inside Tryton
    # default: '<module_name>.<class_name>' on Tryton
    # becomes '<module_name>_<class_name>' in the database
    _VERSIONS = [('v3.8', '3.8')]
    __name__ = 'sample.module'
    _rec_name = 'title'
    
    name = fields.Char('Module Name', required=True)
    version = fields.Selection( _VERSIONS, 'Version', required=True)
    save_directory = fields.Char('Directory Path', help='Omit the slash at the back')
    depends = fields.Text('Depends', help='Depend Tryton Modules. Using comma (,) as separator.' )
    requires = fields.Text('Pre-prerequisite', help='Requirement external python module. Using comma (,) as separator.' )
    active = fields.Boolean('Active')
    date_generate = fields.DateTime('Generated On', readonly=True)
    
    @classmethod
    def __setup__(cls):
        super(sample_module, cls).__setup__()
        cls._buttons.update({
                'generate': {},
                })
                
    @classmethod
    @ModelView.button
    def generate(cls, samples):
        Date = Pool().get('ir.date')
        for sample in samples:
            cls.write([sample], {
                    'date_generate': Date.today(),
                    })

        pass
