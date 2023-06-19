def to_json(obj):
    item = obj.__dict__
    if "_sa_instance_state" in item:
        del item["_sa_instance_state"]
    return item
