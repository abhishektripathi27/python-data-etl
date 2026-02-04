def transform_data(rows):
    return [
        row for row in rows
        if all(row.values())
    ]
