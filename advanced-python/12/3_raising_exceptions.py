def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is no good - Harry")

a = increment('e34')
print(a)
