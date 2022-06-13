def addressEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "city": item["city"],
        "state": item["state"],
        "zip": item["zip"],
        "lat": item["lat"],
        "lng": item["lng"],
    }


def addressEntityList(entity) -> list:
    return [addressEntity(item) for item in entity]