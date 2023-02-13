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

        'views/blood_connect_request_view.xml',
        'views/blood_connect_donor.xml',
        'views/blood_connect_patient.xml',
        'views/blood_connect_hospital.xml',
        'views/blood_connect_donation.xml',
        'views/blood_connect_order.xml',
        'views/blood_connect_donation_center.xml',
        'views/blood_connect_blood_type.xml',
        # 'views/blood_connect_donation_request.xml',
        # 'views/blood_connect_blood_inventory.xml',
        'views/blood_connect_menu.xml',
    ],
}