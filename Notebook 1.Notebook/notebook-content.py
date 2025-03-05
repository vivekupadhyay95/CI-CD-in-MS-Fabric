# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

import pandas as pd

df = pd.read_csv("abfss://e73c99c3-0f3f-42b0-9001-29a2ebdbff87@onelake.dfs.fabric.microsoft.com/6a3805f8-1e88-462f-ae72-1f129766658b/Files/hospital_readmissions.csv")
df.head()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
