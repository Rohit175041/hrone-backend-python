from bson import ObjectId

def is_valid_objectid(id_str: str) -> bool:
    try:
        ObjectId(id_str)
        return True
    except Exception:
        return False
