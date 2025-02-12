# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:25:23 2025

@author: Kiman Park, Ph.D.
"""
from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    url_prefix=''
)
