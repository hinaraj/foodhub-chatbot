
import time

# Store conversation memory
conversation_memory = {}

# Store last activity time
last_activity = {}

# Timeout duration (60 seconds)
TIMEOUT = 60


def save_memory(user_id, query, response):

    if user_id not in conversation_memory:
        conversation_memory[user_id] = []

    conversation_memory[user_id].append({
        "query": query,
        "response": response
    })

    last_activity[user_id] = time.time()


def get_memory(user_id):

    return conversation_memory.get(user_id, [])


def is_session_expired(user_id):

    if user_id not in last_activity:
        return False

    current_time = time.time()

    if current_time - last_activity[user_id] > TIMEOUT:
        return True

    return False


def clear_session(user_id):

    if user_id in conversation_memory:
        del conversation_memory[user_id]

    if user_id in last_activity:
        del last_activity[user_id]
