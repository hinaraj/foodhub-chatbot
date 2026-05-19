
import re
from database import get_database

db = get_database()


# Validate SQL query
def validate_sql_query(sql_query):

    forbidden_keywords = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    sql_upper = sql_query.upper()

    for keyword in forbidden_keywords:
        if keyword in sql_upper:
            return False

    return True


# Rule-based SQL Agent
def sql_agent_from_query(user_query):

    # Extract Order ID
    match = re.search(r'O\d+', user_query)

    if not match:
        return None, "Please provide a valid order ID (e.g., O12486)."

    order_id = match.group()

    query = f'''
    SELECT *
    FROM orders
    WHERE order_id = "{order_id}"
    '''

    if not validate_sql_query(query):
        return None, "Unsafe SQL query detected."

    result = db.run(query)

    if result.strip() == "":
        return order_id, "Order not found."

    return order_id, result
