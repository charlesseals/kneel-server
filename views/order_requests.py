CUSTOM_ORDERS = [
    {

    }
]

def get_all_custom_orders():
    return CUSTOM_ORDERS

def get_single_custom_order(id):
    requested_custom_order = None
    for custom_order in CUSTOM_ORDERS:
        if custom_order["id"] == id:
            requested_custom_order = custom_order
    return requested_custom_order

def create_custom_order(custom_order):
    max_id = CUSTOM_ORDERS[-1]["id"]
    new_id = max_id + 1
    custom_order["id"] = new_id
    CUSTOM_ORDERS.append(custom_order)
    return custom_order

def delete_custom_order(id):
    custom_order_index = -1
    for index, custom_order in enumerate(CUSTOM_ORDERS):
        if custom_order["id"] == id:
            custom_order_index = index
    if custom_order_index >= 0:
        CUSTOM_ORDERS.pop(custom_order_index)

def update_custom_order(id, new_custom_order):
    for index, custom_order in enumerate(CUSTOM_ORDERS):
        if custom_order["id"] == id:
            CUSTOM_ORDERS[index] = new_custom_order
            break