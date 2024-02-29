def normalize_cert(data) -> dict:
    data["document_id"] = data["documents"][0]["document_id"]
    return data

def normalize_audit(data) -> dict:
    data["document_id"] = data["documents"][0]["document_id"]
    return data

def normalize_farm(data) -> dict:
    data["farm"]["regional_councils"] = data["farm"]["regional_councils"][0]
    return data["farm"]

def normalize_address(data) -> dict:
    return data["farm"]["address"]

def normalize_operator(data) -> dict:
    return data["farm"]["operator"]

def normalize_fwfp_dev(data) -> dict:
    return data["farm"]["fwfp_developer"]

def normalize_boundaries(data) -> dict:
    return data["farm"]["boundaries"]

def normalize_fwfp(data) -> dict:
    data["certification_id"] = data["certifications"][0]["certification_id"]
    data["audit_id"] = data["audits"][0]["audit_id"]
    return data