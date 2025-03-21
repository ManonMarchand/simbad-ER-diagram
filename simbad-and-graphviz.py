#!/usr/bin/env python

import pyvo
import graphviz
from itertools import cycle

simbadtap = pyvo.dal.TAPService("https://simbad.unistra.fr/simbad/sim-tap")
colors = cycle(["#9EADC8", "#C7FFDA", "#FEC1A7", "#4CE0B3", "#F0A8ED", "#FDD791", "#F4B6C2", "#FE9599", "#FFF196"])

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
simbad_er.attr('graph', splines="polyline", overlap="false", mode='major', esep='+0', sep='0')
simbad_er.attr('edge', color='lightgray', penwidth='7', labelOverlay='100%')

#----------------------------------------
# Add the subgraph for measurement tables
#----------------------------------------

fontsize = "16"
mes_html_table = "{" + ' | '.join(measurement_tables['table_name']) + " }"

simbad_er.node("Measurement tables", label=mes_html_table, shape="record", fontsize=fontsize)
simbad_er.edge("basic", "Measurement tables", tooltip="oid:oidref", color=next(colors))

#--------------------------------
# Add the normal tables and nodes
#--------------------------------

for table in tables:
    simbad_er.node(str(table["table_name"]), tooltip=str(table["description"]), fontsize=fontsize)

for link in links:
    c = next(colors)
    simbad_er.edge(link["from_table"], link["target_table"],
                   tooltip=f"{link["from_column"]}:{link["target_column"]}",
                   color=c,
                   #headlabel=f"<<table border='0' cellborder='0'><tr><td bgcolor='white'>{link["from_column"]}:{link["target_column"]}</td></tr></table>>"
                   )

#----------------
# Generate output
#----------------

simbad_er.render("./simbad-er")
