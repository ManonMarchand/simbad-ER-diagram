#!/usr/bin/env python

import pyvo
import graphviz

simbadtap = pyvo.dal.TAPService("https://simbad.unistra.fr/simbad/sim-tap")

#------------
# Retrieving data
#------------

query = """SELECT * FROM TAP_SCHEMA.key_columns JOIN TAP_SCHEMA.keys USING(key_id)
        WHERE from_table NOT LIKE 'mes%'
        """
links = simbadtap.run_sync(query).to_table()

query = """select * from TAP_SCHEMA.tables WHERE (table_name NOT LIKE 'TAP_SCHEMA%')
AND (table_name not like 'mes%')
"""
tables = simbadtap.run_sync(query).to_table()
tables.sort("table_name")

query = """select * from TAP_SCHEMA.tables WHERE (table_name NOT LIKE 'TAP_SCHEMA%')
AND (table_name like 'mes%')
"""
measurement_tables = simbadtap.run_sync(query).to_table()

#-----------------
# Create the graph
#-----------------

simbad_er = graphviz.Graph("Simbad Relational Database", format='svg', engine="neato")
simbad_er.attr('node', shape='box', penwidth='6', style='filled', color='lightgray')
simbad_er.attr('graph', splines="curved", overlap="false", mode='major', esep='+4', sep='3')
simbad_er.attr('edge', color='lightgray', penwidth='7')

# Add the subgraph for measurement tables

mes_html_table = "{"

for table in measurement_tables:
    mes_html_table += f'{table["table_name"]} | '


mes_html_table = mes_html_table[:-2]
mes_html_table += "}"

simbad_er.node("Measurement tables", label=mes_html_table, shape="record")
simbad_er.edge("basic", "Measurement tables", tooltip="oid:oidref")


for table in tables:
    simbad_er.node(str(table["table_name"]), tooltip=str(table["description"]))

for link in links:
    simbad_er.edge(link["from_table"], link["target_table"],
                   tooltip=f"{link["from_column"]}:{link["target_column"]}")

simbad_er.render("./simbad-er")