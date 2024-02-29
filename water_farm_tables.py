from odbc_handler import *

# This function creates all of the tables in the database. It isn't finished yet.
def create_tables(odbc: ODBCHandler):
    odbc.create_table("documents",
        {"document_id": SHORT_CHAR,
        "PRIMARY KEY": "(document_id)",
        "document_type": LONG_CHAR
        })
  
    odbc.create_table("certifications",
        {"certification_id": SHORT_CHAR,
        "PRIMARY KEY": "(certification_id)",  
        "fwfp_id": SHORT_CHAR,
        "date_of_engagement": DATE,
        "status": LONG_CHAR,
        "certifier_id": SHORT_CHAR,
        "certification_requirements_met": BOOL,
        "certification_type": LONG_CHAR,
        "date_of_certification_decision": DATE,
        "has_conflict_of_interest": BOOL,
        "is_second_certifier": BOOL,
        "part_certification_description": LONG_CHAR,
        "document_id": SHORT_CHAR,
        "other_regulatory_requirements_included": BOOL,
        "other_regulatory_requirements_statement": LONG_CHAR,
        "next_certification_due_date": DATE,
        "reassignment_reason": LONG_CHAR,
        "recertification_reason": LONG_CHAR,
        "created_at": TIMESTAMP,
        "updated_at": TIMESTAMP,
        "completed_at": TIMESTAMP,
        "FOREIGN KEY": "(document_id) REFERENCES documents(document_id)"
        })
    
    odbc.create_table("audits",
        {"audit_id": SHORT_CHAR,
        "PRIMARY KEY": "(audit_id)",
        "fwfp_id": SHORT_CHAR,
        "date_of_engagement": DATE,
        "status": LONG_CHAR,
        "auditor_id": SHORT_CHAR,
        "audit_grade": LONG_CHAR,
        "audit_grade_summary": MED_CHAR,
        "date_of_audit_decision": DATE,
        "date_of_next_audit": DATE,
        "has_conflict_of_interest": BOOL,
        "document_id": SHORT_CHAR,
        "FOREIGN KEY": "(document_id) REFERENCES documents(document_id)"
        })
  
    odbc.create_table("fwfp",
        {"fwfp_id": SHORT_CHAR,
        "PRIMARY KEY": "(fwfp_id)",
        "created_at": TIMESTAMP,
        "certification_id": SHORT_CHAR,
        "audit_id": SHORT_CHAR,
        "FOREIGN KEY (audit_id)": "REFERENCES audits(audit_id)",
        "FOREIGN KEY (certification_id)": "REFERENCES certifications(certification_id)"
        })
  
    odbc.create_table("land_uses",
        {"land_uses_id": INT_ID,
        "category": LONG_CHAR,
        "land_use_code": LONG_CHAR,
        "land_use": LONG_CHAR
        })
  
    odbc.create_table("users",
        {"user_id": SHORT_CHAR,
        "first_name": LONG_CHAR,
        "last_name": LONG_CHAR,
        "email": LONG_CHAR
        })

    odbc.create_table("farm",
        {"farm_id": INT_ID,
        "name": LONG_CHAR,
        "total_area_ha": LONG_CHAR,
        "leased_licensed_area_ha": LONG_CHAR,
        "current_resource_consents": LONG_CHAR,
        "legal_land_titles_and_parcels": LONG_CHAR,
        "operator_id": SHORT_CHAR,
        "other_contacts_id": SHORT_CHAR,
        "fwfp_developer_id": SHORT_CHAR,
        "address_id": SHORT_CHAR,
        "regional_councils": SHORT_CHAR,
        "land_uses_id": "INT",
        "boundaries_id": "INT",
        })

    odbc.create_table("address",
        {"address_id": INT_ID,
        "street_address": LONG_CHAR,
         "suburb": LONG_CHAR,
         "city": LONG_CHAR,
         "postcode": LONG_CHAR,
         "country": LONG_CHAR
        })

    odbc.create_table("operator",
        {"operator_id": INT_ID,
        "first_name": LONG_CHAR,
        "last_name": LONG_CHAR,
        "nzbn": LONG_CHAR,
        "primary_phone": LONG_CHAR,
        "other_phone": LONG_CHAR,
        "email": MED_CHAR,
        "address_id": SHORT_CHAR
        })

    odbc.create_table("fwfp_developer",
        {"fwfp_developer_id": INT_ID,
        "first_name": LONG_CHAR,
        "last_name": LONG_CHAR,
        "business_name": LONG_CHAR
        })

    odbc.create_table("boundaries",
        {"boundary_id": INT_ID,
        "additionalProp1": MED_CHAR,
        "additionalProp2": MED_CHAR,
        "additionalProp3": MED_CHAR
        })