
from guardrails import (
    input_guardrail,
    escalation_check,
    empty_query_check,
    sql_injection_check
)

from memory import (
    save_memory,
    get_memory,
    is_session_expired,
    clear_session
)

from tools import (
    order_query_tool,
    answer_tool
)


# Main chatbot function
def chatagent(user_id, user_query):

    # Empty query check
    if not empty_query_check(user_query):
        return "Please enter a valid query."

    # Session timeout check
    if is_session_expired(user_id):

        clear_session(user_id)

        return (
            "Your session expired due to inactivity. "
            "Please start a new conversation."
        )

    # Input guardrail check
    if not input_guardrail(user_query):

        return (
            "Your request violates FoodHub security policies "
            "and cannot be processed."
        )

    # SQL injection check
    if not sql_injection_check(user_query):

        return (
            "Potential malicious query detected. "
            "Request blocked for security reasons."
        )

    # Escalation handling
    if escalation_check(user_query):

        response = (
            "Your issue has been escalated to a human "
            "support agent for immediate assistance."
        )

        save_memory(user_id, user_query, response)

        return response

    # Retrieve order information
    order_id, raw_data = order_query_tool(user_query)

    # Handle missing order ID
    if order_id is None:

        save_memory(user_id, user_query, raw_data)

        return raw_data

    # Generate final answer
    final_response = answer_tool(user_query, raw_data)

    # Save memory
    save_memory(user_id, user_query, final_response)

    return final_response
