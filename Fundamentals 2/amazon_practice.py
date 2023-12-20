

resp = []


def check_dict_values(logs_dict, num):
    if num not in logs_dict:
        logs_dict[num] = 1
    else:
        value = logs_dict.get(num) + 1
        logs_dict.update({num: value})


def processLogs(logs, threshold):
    # Write your code here
    logs_dict = {}
    num = ''

    for elem in logs:
        if num != '':
            check_dict_values(logs_dict, num)
            num = ''
        for id in elem:
            if id != ' ':
                num = num + str(id)
            else:
                check_dict_values(logs_dict, num)
                num = ''

    check_dict_values(logs_dict, num)

    for k, v in logs_dict.items():
        if v >= threshold:
            resp.append(k)

    return resp.sort()


processLogs(["1 7 70", "1 3 20", "2 2 17"], 2)
print(resp)
