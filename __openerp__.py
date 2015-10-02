# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Contact Snippet',
    'category': 'Website',
    'version': '0.1',
    'author': 'bloopark systems GmbH & Co. KG, Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['website_partner','crm'],
    'description': """
Contact Snippet
===============
  * Adds two contact form snippets, a big one in <section> tag, and a smaller one to be used inside bootstrap columns.
  * Submitting the form creates a new lead to Odoo back-end
  * Based on work by Bloopark Systems, available at https://github.com/blooparksystems/bp_contact_snippet
""",
    'data': [
        'views/form.xml'
    ],
}
