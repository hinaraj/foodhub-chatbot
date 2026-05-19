
import re

# Block malicious queries
def input_guardrail(user_query):

    blocked_terms = [
        "hack",
        "drop table",
        "delete database",
        "sql injection",
        "steal",
        "bypass",
        "all orders",
        "admin access",
        "password"
    ]

    query_lower = user_query.lower()

    for term in blocked_terms:
        if term in query_lower:
            return False

    return True


# Detect escalation situations
def escalation_check(user_query):

    escalation_keywords = [
        "angry",
        "complaint",
        "refund",
        "not resolved",
        "immediate response",
        "human agent",
        "frustrated",
        "worst service"
    ]

    query_lower = user_query.lower()

    for word in escalation_keywords:
        if word in query_lower:
            return True

    return False


# Empty input validation
def empty_query_check(user_query):

    if not user_query.strip():
        return False

    return True


# SQL injection protection
def sql_injection_check(user_query):

    dangerous_patterns = [
        ";",
        "--",
        "DROP",
        "DELETE",
        "INSERT",
        "UPDATE",
        "ALTER"
    ]

    for pattern in dangerous_patterns:
        if pattern.lower() in user_query.lower():
            return False

    return True
