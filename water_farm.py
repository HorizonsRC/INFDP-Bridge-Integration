from odbc_handler import ODBCHandler
from common_functions import *
import logging
from water_farm_tables import create_tables
from infdp_normalizer import *

# Swap which one is in use by commenting it out. The real API doesn't exist yet and *will not* function!
from infdp_bridge_api_test import *
#from infdp_bridge_api import *

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

    odbc.big_insert("documents", get_document(1))

    cert = get_certification(1)

    odbc.big_insert("certifications", normalize_cert(cert))

    
    odbc.big_insert("land_uses", get_land_uses()[0])

    # Inserting user.
    odbc.big_insert("users", get_user(1))
    odbc.big_insert("audits", normalize_audit(get_audit(1)))
    odbc.big_insert("farm", normalize_farm(cert))
    odbc.big_insert("address", normalize_address(cert))
    odbc.big_insert("operator", normalize_operator(cert))
    odbc.big_insert("fwfp_developer", normalize_fwfp_dev(cert))
    odbc.big_insert("boundaries", normalize_boundaries(cert))
    odbc.big_insert("fwfp", normalize_fwfp(get_fwfps_by_id(1)))

    odbc.commit()

    print("\nDATA IN TABLES")
    for i in odbc.get_all_tables():
        print("\n" + i)
        print(odbc.select("*", i))
    print()

    logging.info("Exiting...")