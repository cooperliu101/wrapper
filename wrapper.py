keys=['a','b','c','d']

def wrapper(input_keys, input_values, params):
    input=dict(zip(input_keys,input_values))
    params.update(input)
    params_keys=set(params.keys())
    default_keys=set(keys)
    if params_keys != default_keys:
        raise Exception("wrong keys match! %s != %s"%(params_keys, default_keys))
    #print params
    values=map(lambda key:params[key], keys)
    #print values
    return values

if __name__ == '__main__':
    params={'a':10,
            'c':20}
    input_values=[3,4]
    input_keys=['b','d']

    values=wrapper(input_keys, input_values, params)
    print(values)