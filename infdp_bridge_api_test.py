import json
import logging

# Everything here only returns the example. Used for testing while the actual API isn't there.

def get_fwfps() -> dict:
	logging.warn("'get_fwfps' is using example data.")
	return json.loads("""{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
	{
	  "fwfp_id": "string",
	  "updated_at": "2024-02-19T01:58:36.244Z"
	}
  ]
}""")

def get_fwfps_by_id(id) -> dict:
	logging.warn("'get_fwfps_by_id' is using example data.")
	return json.loads("""{
  "fwfp_id": "string",
  "created_at": "2024-02-19T01:59:23.127Z",
  "updated_at": "2024-02-19T01:59:23.127Z",
  "certifications": [
	{
	  "certification_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
	  "date_of_engagement": "2024-02-19",
	  "status": "ASSIGNED",
	  "updated_at": "2024-02-19T01:59:23.127Z"
	}
  ],
  "audits": [
	{
	  "audit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
	  "date_of_engagement": "2024-02-19",
	  "status": "IN_PROGRESS",
	  "updated_at": "2024-02-19T01:59:23.127Z"
	}
  ]
}""")

def get_certification(id) -> dict:
	logging.warn("'get_certification' is using example data.")
	return json.loads("""{
  "fwfp_id": "string",
  "certification_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "date_of_engagement": "2024-02-19",
  "status": "ASSIGNED",
  "certifier_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "certification_requirements_met": true,
  "certification_type": "FULL",
  "date_of_certification_decision": "2024-02-19",
  "has_conflict_of_interest": true,
  "is_second_certifier": true,
  "part_certification_description": "string",
  "documents": [
	{
	  "document_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
	  "document_type": "FWFP"
	}
  ],
  "other_regulatory_requirements_included": true,
  "other_regulatory_requirements_statement": "string",
  "next_certification_due_date": "2024-02-19",
  "farm": {
	"name": "string",
	"total_area_ha": "154448",
	"leased_licensed_area_ha": "-3530201176.8",
	"current_resource_consents": "string",
	"legal_land_titles_and_parcels": "string",
	"operator": {
	  "first_name": "string",
	  "last_name": "string",
	  "nzbn": "string",
	  "primary_phone": "string",
	  "other_phone": "string",
	  "email": "user@example.com",
	  "address": {
		"street_address": "string",
		"suburb": "string",
		"city": "string",
		"postcode": "string",
		"country": "string"
	  }
	},
	"other_contacts": [
	  {
		"first_name": "string",
		"last_name": "string",
		"primary_phone": "string",
		"other_phone": "string",
		"email": "user@example.com",
		"address": {
		  "street_address": "string",
		  "suburb": "string",
		  "city": "string",
		  "postcode": "string",
		  "country": "string"
		}
	  }
	],
	"fwfp_developer": {
	  "first_name": "string",
	  "last_name": "string",
	  "business_name": "string"
	},
	"address": {
	  "street_address": "string",
	  "suburb": "string",
	  "city": "string",
	  "postcode": "string",
	  "country": "string"
	},
	"regional_councils": [
	  "AKL_UC"
	],
	"land_uses": [
	  "string"
	],
	"boundaries": {
	  "additionalProp1": "string",
	  "additionalProp2": "string",
	  "additionalProp3": "string"
	}
  },
  "reassignment_reason": "REASSIGN_UNFORESEEN",
  "recertification_reason": "RECERT_REG_27",
  "created_at": "2024-02-19T02:00:13.788Z",
  "updated_at": "2024-02-19T02:00:13.788Z",
  "completed_at": "2024-02-19T02:00:13.788Z"
}""")

def get_audit(id) -> dict:
	logging.warn("'get_audit' is using example data.")
	return json.loads("""{
  "fwfp_id": "string",
  "audit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "date_of_engagement": "2024-02-19",
  "status": "IN_PROGRESS",
  "auditor_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "audit_grade": "A",
  "audit_grade_summary": "string",
  "date_of_audit_decision": "2024-02-19",
  "date_of_next_audit": "2024-02-19",
  "has_conflict_of_interest": true,
  "documents": [
	{
	  "document_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
	  "document_type": "FWFP"
	}
  ],
  "farm": {
	"name": "string",
	"total_area_ha": "-",
	"leased_licensed_area_ha": "-558363129",
	"current_resource_consents": "string",
	"legal_land_titles_and_parcels": "string",
	"operator": {
	  "first_name": "string",
	  "last_name": "string",
	  "nzbn": "string",
	  "primary_phone": "string",
	  "other_phone": "string",
	  "email": "user@example.com",
	  "address": {
		"street_address": "string",
		"suburb": "string",
		"city": "string",
		"postcode": "string",
		"country": "string"
	  }
	},
	"other_contacts": [
	  {
		"first_name": "string",
		"last_name": "string",
		"primary_phone": "string",
		"other_phone": "string",
		"email": "user@example.com",
		"address": {
		  "street_address": "string",
		  "suburb": "string",
		  "city": "string",
		  "postcode": "string",
		  "country": "string"
		}
	  }
	],
	"fwfp_developer": {
	  "first_name": "string",
	  "last_name": "string",
	  "business_name": "string"
	},
	"address": {
	  "street_address": "string",
	  "suburb": "string",
	  "city": "string",
	  "postcode": "string",
	  "country": "string"
	},
	"regional_councils": [
	  "AKL_UC"
	],
	"land_uses": [
	  "string"
	]
  },
  "reassignment_reason": "REASSIGN_UNFORESEEN",
  "created_at": "2024-02-19T02:01:57.375Z",
  "updated_at": "2024-02-19T02:01:57.375Z",
  "completed_at": "2024-02-19T02:01:57.375Z"
}""")

def get_document(id) -> dict:
	logging.warn("'get_document' is using example data.")
	return json.loads("""{
  "document_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "document_type": "FWFP"
}""")

def get_land_uses() -> list:
	logging.warn("'get_land_uses' is using example data.")
	return json.loads("""[
  {
	"category": "string",
	"land_use_code": "string",
	"land_use": "string"
  }
]""")

def get_users() -> dict:
	logging.warn("'get_users' is using example data.")
	return json.loads("""{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
	{
	  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
	  "first_name": "string",
	  "last_name": "string",
	  "email": "user@example.com",
	  "regional_roles": [
		{
		  "role": "AUDITOR",
		  "regional_council": "string"
		}
	  ]
	}
  ]
}""")

def get_user(id) -> dict:
	logging.warn("'get_user' is using example data.")
	return json.loads("""{
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "first_name": "string",
  "last_name": "string",
  "email": "user@example.com",
  "regional_roles": [
	{
	  "role": "AUDITOR",
	  "regional_council": "string"
	}
  ]
}""")