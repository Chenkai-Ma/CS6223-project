import statistics

def buggy_1(data):
    return str(statistics.mean(data))


def buggy_2(data):
    return [statistics.mean(data)]


def buggy_3(data):
    return {'mean': statistics.mean(data)}


def buggy_4(data):
    return None


def buggy_5(data):
    calendar_list = ["January", "February", "March", "April", 
                     "May", "June", "July", "August", 
                     "September", "October", "November", "December"]
    
    # calculating the index position for mean value
    index = int(statistics.mean(data))
    
    # return some random output that is not numeric i.e calendar month's name
    return calendar_list[index % 12]