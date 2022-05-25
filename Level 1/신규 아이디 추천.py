import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^0-9a-zA-Z\-\._]", "", new_id)
    new_id = re.sub(r"\.\.+", ".", new_id)
    new_id = re.sub(r"\.$|^\.", "", new_id)
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 15:
        new_id = new_id[:15]
    new_id = re.sub(r"\.$", "", new_id)
    if len(new_id) < 3:
        new_id += new_id[-1]*(3-len(new_id))
    return new_id

# URL : https://programmers.co.kr/learn/courses/30/lessons/72410