import uuid # id

requests = {}

def create_request(user_id, arrival, duration):
    request_id = str(uuid.uuid4())

    requests[request_id] = {
        'user_id': user_id,
        'arrival': arrival,
        'duration': duration,
        'status': 'pending'
    }

    return request_id


def get_request(request_id):
    return requests.get(request_id)

def get_requests():
    return requests

def set_request_status(request_id, status):
    if request_id in requests:
        requests[request_id]['status'] = status