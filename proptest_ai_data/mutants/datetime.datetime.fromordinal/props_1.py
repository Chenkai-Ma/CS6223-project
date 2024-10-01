import datetime

def buggy_1(ordinal): 
    result = datetime.datetime.fromordinal(ordinal) 
    # modifies output to integer
    return int(result.timestamp())

def buggy_2(ordinal): 
    result = datetime.datetime.fromordinal(ordinal)
    # modifies output to string
    return result.strftime("%Y-%m-%d %H:%M:%S")

def buggy_3(ordinal): 
    result = datetime.datetime.fromordinal(ordinal)
    # modifies output to a tuple of the datetime attributes
    return (result.year, result.month, result.day)

def buggy_4(ordinal): 
    result = datetime.datetime.fromordinal(ordinal)
    # modifies to only date part
    return result.date()

def buggy_5(ordinal): 
    result = datetime.datetime.fromordinal(ordinal)
    # modifies to only time part
    return result.time()