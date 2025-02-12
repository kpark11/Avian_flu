# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:25:23 2025

@author: Kiman Park, Ph.D.
"""

from apps import db


class Avian_flu(db.Model):
    
    __tablename__ = 'avian_flu'
    
    id = db.Column('id', db.Integer, primary_key=True)
    county = db.Column('County', db.Text)
    state = db.Column('State', db.Text)
    outbreak_date = db.Column('Outbreak Date', db.DateTime)
    flock_type = db.Column('Flock Type', db.Text)
    flock_size = db.Column('Flock Size', db.Integer)
    
    def __init__(self, id, county, state, outbreak_date, flock_type, flock_size):
        self.id = id
        self.county = county
        self.state = state
        self.outbreak_date = outbreak_date
        self.flock_type = flock_type
        self.flock_size = flock_size
    
    def __repr__(self):
        return f"({self.id}, {self.county}, {self.state}, {self.outbreak_date}, {self.flock_type}, {self.flock_size})"
    
    def json(self):
        return {'id': self.id, 'County': self.county, 'State': self.state,
                'Outbreak Date': self.outbreak_date, 'Flock type': self.flock_type, 
                'Flock size': self.flock_size}
    
    def stringify(self):
        return {'id': str(self.id), 'County': str(self.county), 'State': str(self.state),
                'Outbreak Date': str(self.outbreak_date), 'Flock type': str(self.flock_type), 
                'Flock size': str(self.flock_size)}
