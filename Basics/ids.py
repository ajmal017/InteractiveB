import os
import json

file_name = "Last_reqId.json"


def read_req_id():
    """
    :return: json file with reqId
    """
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        _id = file.read()
        _id = json.loads(_id)
        file.close()
    else:
        _id = {"reqId": 0}
    return _id


def write_req_id():
    _id = read_req_id()
    i = _id['reqId']
    i += 1
    with open(file_name,"w") as file:
        _id = {"reqId": i}
        data = json.dumps(_id)
        file.write(data)
        file.close()
    return _id


next_reqId = write_req_id()['reqId']
