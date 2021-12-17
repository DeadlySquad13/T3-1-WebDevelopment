def field(items, *selected_fields):
    num_of_selected_fields = len(selected_fields)
    assert num_of_selected_fields > 0, 'No fields for selection! Please pass at least one!'
    if (num_of_selected_fields == 1):
        return (item.get(selected_fields[0]) for item in items
                if item.get(selected_fields[0]) != None)
            
    return (
        {sf:item.get(sf) for sf in selected_fields
            if item.get(sf) != None}
        for item in items
    )
