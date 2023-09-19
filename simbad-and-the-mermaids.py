#!/usr/bin/env python

import pyvo

simbadtap = pyvo.dal.TAPService("https://simbad.unistra.fr/simbad/sim-tap")

#------------
# Retrieving data
#------------

all_links = simbadtap.run_sync("select * from TAP_SCHEMA.key_columns").to_table()
columns = simbadtap.run_sync("select * from TAP_SCHEMA.columns WHERE table_name NOT LIKE 'TAP_SCHEMA%'")


#-------------
# Cleaning
#-------------

groups_by_table = columns.to_table().group_by('table_name')

# some tables have mes or not in their names
mes_tables = []
for key in groups_by_table.groups.keys:
    if "mes" == key["table_name"][0:3]:
        mes_tables += [key["table_name"][3:].upper()]

def add_mes(table, mes_tables):
    if table in mes_tables:
        return "MES" + table
    return table

#--------------
# Writing the mermaid
#--------------

with open("README.md", "w+") as out:
    # write a title
    out.write("# Simbad Entity Relation Diagram\n")
    # signal the start of the mermaid diagram
    out.write("```mermaid\nerDiagram\n")
    # first the relations
    for link in all_links['key_id']:
        ends = link.split('To')
        if len(ends) > 1:
            left_table = add_mes(ends[0].upper(), mes_tables)
            right_table = add_mes(ends[1].upper(), mes_tables)
            
            out.write(f"""    {left_table} }}o..o{{ {right_table} : ""\n""")
    # then the attributes
    for key, group in zip(groups_by_table.groups.keys, groups_by_table.groups):
        out.write(f'    {key["table_name"].upper()} {{\n')
        for line in group:
            out.write(f"""        {line["datatype"]} {line["column_name"]} {"PK" if line["principal"] else ""} "{line["description"]}"\n""")
        out.write("}\n")
    out.write("```")