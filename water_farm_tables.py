from odbc_handler import ODBCHandler

# This function creates all of the tables in the database. It isn't finished yet.
def create_tables(odbc: ODBCHandler):
    odbc.create_table("documents",
        {"document_id": "VARCHAR(100)",
        "PRIMARY KEY": "(document_id)",
        "document_type": "VARCHAR(300)"
        })
  
    odbc.create_table("certifications",
        {"certification_id": "VARCHAR(100)",
        "PRIMARY KEY": "(certification_id)",  
        "fwfp_id": "VARCHAR(100)",
        "date_of_engagement": "DATE",
        "status": "VARCHAR(300)",
        "certifier_id": "VARCHAR(100)",
        "certification_requirements_met": "BIT",
        "certification_type": "VARCHAR(300)",
        "date_of_certification_decision": "DATE",
        "has_conflict_of_interest": "BIT",
        "is_second_certifier": "BIT",
        "part_certification_description": "VARCHAR(300)",
        "document_id": "VARCHAR(100)",
        "other_regulatory_requirements_included": "BIT",
        "other_regulatory_requirements_statement": "VARCHAR(300)",
        "next_certification_due_date": "DATE",
        "reassignment_reason": "VARCHAR(300)",
        "recertification_reason": "VARCHAR(300)",
        "created_at": "VARCHAR(25)",
        "updated_at": "VARCHAR(25)",
        "completed_at": "VARCHAR(25)",
        "FOREIGN KEY": "(document_id) REFERENCES documents(document_id)"
        })
    
    odbc.create_table("audits",
        {"audit_id": "VARCHAR(100)",
        "PRIMARY KEY": "(audit_id)",
        "fwfp_id": "VARCHAR(100)",
        "date_of_engagement": "DATE",
        "status": "VARCHAR(300)",
        "auditor_id": "VARCHAR(100)",
        "audit_grade": "VARCHAR(300)",
        "audit_grade_summary": "VARCHAR(255)",
        "date_of_audit_decision": "DATE",
        "date_of_next_audit": "DATE",
        "has_conflict_of_interest": "BIT",
        "document_id": "VARCHAR(100)",
        "FOREIGN KEY": "(document_id) REFERENCES documents(document_id)"
        })
  
    odbc.create_table("fwfp",
        {"fwfp_id": "VARCHAR(100)",
        "PRIMARY KEY": "(fwfp_id)",
        "created_at": "VARCHAR(25)",
        "certification_id": "VARCHAR(100)",
        "audit_id": "VARCHAR(100)",
        "FOREIGN KEY (audit_id)": "REFERENCES audits(audit_id)",
        "FOREIGN KEY (certification_id)": "REFERENCES certifications(certification_id)"
        })
  
    odbc.create_table("land_uses",
        {"category": "VARCHAR(300)",
        "land_use_code": "VARCHAR(300)",
        "land_use": "VARCHAR(300)"
        })
  
    odbc.create_table("users",
        {"user_id": "VARCHAR(100)",
        "first_name": "VARCHAR(300)",
        "last_name": "VARCHAR(300)",
        "email": "VARCHAR(300)"
        })
    
    odbc.create_table("farm",
        {"name": "VARCHAR(300)",
        "total_area_ha": "VARCHAR(300)",
        "leased_licensed_area_ha": "VARCHAR(300)",
        "current_resource_consents": "VARCHAR(300)",
        "legal_land_titles_and_parcels": "VARCHAR(300)",
        "operator_id": "VARCHAR(100)",
        "other_contacts_id": "VARCHAR(100)",
        "fwfp_developer_id": "VARCHAR(100)",
        "address_id": "VARCHAR(100)",
        #"regional_councils": "VARCHAR(50)",
        #"land_uses": "VARCHAR(50)",
        #"boundaries": "VARCHAR(50)",
        })

    odbc.create_table("address",
        {"street_address": "VARCHAR(300)",
         "suburb": "VARCHAR(300)",
         "city": "VARCHAR(300)",
         "postcode": "VARCHAR(300)",
         "country": "VARCHAR(300)"
        })

    odbc.create_table("operator",
        {"first_name": "VARCHAR(300)",
        "last_name": "VARCHAR(300)",
        "nzbn": "VARCHAR(300)",
        "primary_phone": "VARCHAR(300)",
        "other_phone": "VARCHAR(300)",
        "email": "VARCHAR(255)"
        #"address_id": something
        })

    odbc.create_table("fwfp_developer",
        {"first_name": "VARCHAR(300)",
        "last_name": "VARCHAR(300)",
        "business_name": "VARCHAR(300)"
        })

    odbc.create_table("boundaries",
        {"additionalProp1": "VARCHAR(255)",
        "additionalProp2": "VARCHAR(255)",
        "additionalProp3": "VARCHAR(255)"
        })
    
    #odbc.create_table("regional_councils",)