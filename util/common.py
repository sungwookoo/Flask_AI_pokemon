# ObjectId 타입의 ['_id']를 string 타입으로 변환
# ex) users = objectIdToString(users)
def object_id_to_string(find_list):
    results = []
    for i in find_list:
        i['_id'] = str(i['_id'])
        results.append(i)
    return results
