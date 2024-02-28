from odbc_handler import ODBCHandler
from common_functions import *
import logging
from water_farm_tables import create_tables

# Swap which one is in use by commenting it out. The real API doesn't exist yet and *will not* function!
import infdp_bridge_api_test as infdp_bridge_api
#import infdp_bridge_api

config = load_config("water_farm.cfg")

LOG_LEVEL = config["logging"]["LogLevel"]
NAME = config["logging"]["LogName"]
SERVER = config["server_info"]["ServerName"]
DATABASE = config["server_info"]["Database"]
DRIVER = config["server_info"]["Driver"]

init_logger(LOG_LEVEL, NAME)

if __name__ == "__main__":
    # Initialise the ODBC class.
    odbc = ODBCHandler(SERVER, DRIVER, DATABASE)

    # Deleting foreign keys so the tables can be dropped.
    odbc.delete_fk_constraint("fwfp", "certification_id")
    odbc.delete_fk_constraint("fwfp", "audit_id")
    odbc.delete_fk_constraint("certifications", "document_id")
    odbc.delete_fk_constraint("audits", "document_id")

    # Dropping all tables.
    for i in odbc.get_all_tables():
        odbc.drop_table(i)

    # Make tables.
    create_tables(odbc)

    # Inserting the document.
    odbc.big_insert("documents", infdp_bridge_api.get_document(1))

    # Inserting the certification.
    data = infdp_bridge_api.get_certification(1)
    data["document_id"] = data["documents"][0]["document_id"]
    odbc.big_insert("certifications", data)

    # Inserting land uses, whatever that is. It is for some unknown reason a list, unlike everything else, so we have to retrieve the dictionary from that list.
    odbc.big_insert("land_uses", infdp_bridge_api.get_land_uses()[0])

    # Inserting user.
    odbc.big_insert("users", infdp_bridge_api.get_user(1))

    # Inserting audit.
    data = infdp_bridge_api.get_audit(1)
    data["document_id"] = data["documents"][0]["document_id"]
    odbc.big_insert("audits", data)

    cert = infdp_bridge_api.get_certification(1)

    odbc.big_insert("farm", cert["farm"])
    odbc.big_insert("address", cert["farm"]["address"])
    odbc.big_insert("operator", cert["farm"]["operator"])
    
    odbc.big_insert("fwfp_developer", cert["farm"]["fwfp_developer"])
    odbc.big_insert("boundaries", cert["farm"]["boundaries"])

    # Inserting the fresh water farm plan. It looks funky because we have to get the ID of the foreign keys, that's just how the data is returned.
    data = infdp_bridge_api.get_fwfps_by_id(1)
    data["certification_id"] = data["certifications"][0]["certification_id"]
    data["audit_id"] = data["audits"][0]["audit_id"]
    odbc.big_insert("fwfp", data)

    odbc.commit()

    print("\nDATA IN TABLES")
    for i in odbc.get_all_tables():
        print("\n" + i)
        print(odbc.select("*", i))
    print()

    logging.info("Exiting...")