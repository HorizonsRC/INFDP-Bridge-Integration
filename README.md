# INFDP Bridge Integration
This project is for pulling the data from [https://bridge-infdp.teurukahika.govt.nz/api/v1/docs/](bridge-infdp) and making the database for it.

## water_farm.py
This is the file you want to run. It expects a config file.

## odbc_handler.py
A way of using an ODBC database programatically in Python instead of having to write SQL code in the cursor manually.

## infdp_bridge_api.py and infdp_bridge_api_test.py
These two files are for interacting with the API, it's just the endpoints put into functions for ease of use. the test version is the example data put into functions for obvious testing purposes.

## water_farm_tables.py
Makes tables, expects the ODBC class to be passed to it.

## common_functions.py
Just some useful functions, needs expanding.
