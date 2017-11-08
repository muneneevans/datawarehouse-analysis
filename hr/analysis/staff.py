from common.analysis import connection
from maps.analysis import counties, constituencies, wards
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import json


#get all job types
def get_job_types(in_json=False):
    ''' return a list of all job types
        returns a dataframe or json string in record orientation '''
    query = ''' SELECT dataelementname as name, dataelementid as id, uid, cadreid as cadreId FROM dim_ihris_dataelement '''
    all_job_types = pd.read_sql(query, connection.get_connection())
    
    if in_json:
        return all_job_types.to_json(orient='records')
    else:
        return all_job_types


#get all cadres
def get_cadres(in_json=False):
    ''' return a list of all job types
        returns a dataframe or json string in record orientation '''
    query = ''' SELECT cadreid as id, cadrename as name FROM dim_ihris_cadre '''
    all_cadres = pd.read_sql(query, connection.get_connection())
    
    if in_json:
        return all_cadres.to_json(orient='records')
    else:
        return all_cadres

def get_facility_staff(facility_id, in_json=False):
    ''' Return a list of all products that have been ordered by the facility'''
    query = """ SELECT a.value, b.dataelementname, c.name 
                FROM fact_ihris_datavalue a, dim_ihris_dataelement b, facilities_facility c
                WHERE a.mflcode = c.code 
                    AND a.dataelementid = b.uid
                    AND c.id = '%s' """%(facility_id)
    staff = pd.read_sql(query, connection.get_connection())

    if in_json:
        return staff.to_json(orient='records')
    else:
        return staff