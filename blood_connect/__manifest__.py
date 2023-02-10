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
        'views/blood_connect_menu.xml',
    ],
}