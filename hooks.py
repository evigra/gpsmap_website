from odoo import SUPERUSER_ID

"""
def pre_load_hook(env):
    load_es_mx_lang(env)

def post_load_hook(env):
    load_es_mx_lang(env)
"""

def pre_init_hook(cr):
    load_update_website(cr)


def load_update_website(cr):
    cr.execute("""
        UPDATE ir_model_data
           SET noupdate = FALSE
         WHERE module = 'website'
           AND name = 'default_website'
           AND model = 'website'
    """)