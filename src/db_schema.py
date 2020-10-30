#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import Session, relationship, backref, joinedload_all
from sqlalchemy.orm.collections import attribute_mapped_collection
import itertools

from db_base import DECLARATIVE_BASE

class repr_table:
    """Metodos base para representar las clases de tabla"""
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)

class Currencies(DECLARATIVE_BASE, repr_table):
    __tablename__ = 'currencies'

    name = Column(String)
    symbol = Column(String, primary_key=True)
    precision = Column(Integer)
    type = Column(String)


class Accounts(DECLARATIVE_BASE, repr_table):
    __tablename__ = 'Accounts'

    id = Column(String, primary_key=True)
    name = Column(String)
    # custom, depository, credit_card, loan, mortgage, brokerage, investment, savings, other
    type = Column(String)
    currency_id = Column(String)
    # active, inactive, archived
    status = Column(String)
    order = Column(Integer)


class Categories(DECLARATIVE_BASE, repr_table):
    __tablename__ = 'categories'

    id = Column(String, primary_key=True)
    name = Column(String)
    # expense, income, system
    type = Column(String)


class Tags(DECLARATIVE_BASE, repr_table):
    __tablename__ = 'tags'

    id = Column(String, primary_key=True)
    name = Column(String)
    # expense, income
    type = Column(String)
    category_id = Column(String)


class Entries(DECLARATIVE_BASE, repr_table):
    __tablename__ = 'entries'

    id = Column(String, primary_key=True)
    amount = Column(Float)
    currency_id = Column(String)
    date = Column(String)
    desc = Column(String)
    account_id = Column(String)
    category_id  = Column(String)
    tags = Column(String)
