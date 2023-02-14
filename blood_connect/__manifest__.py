# -*- coding: utf-8 -*-
{
    'name':'Blood Connect',
    'author':'Kashyap Patel',
    'depends':['base'],
    'application':True,
    'installable':True,
    'license':'LGPL-3',
    'data':[
        'security/ir.model.access.csv',

        'views/blood_request.xml',
        'views/donor.xml',
        'views/patient.xml',
        'views/hospital.xml',
        'views/blood_donation.xml',
        'views/blood_order.xml',
        'views/donation_center.xml',
        'views/blood_type.xml',
        # 'views/donation_request.xml',
        # 'views/blood_inventory.xml',
        'views/blood_connect_menu.xml',
    ],
}