import prettytable

import six


def print_dict(d, property="Property"):
    pt = prettytable.PrettyTable([property, 'Value'], caching=False)
    pt.aligns = ['l', 'l']
    [pt.add_row(list(r)) for r in six.iteritems(d)]
    print(pt.get_string(sortby=property))


def kv_string_to_dict(kv_string):
    new_dict = {}
    items = kv_string.split(',')
    for item in items:
        kvs = item.split('=')
        new_dict[kvs[0]] = kvs[1]

def print_result(objs, depth=None, fields=None, json=False):
    # If a depth is provided, we print it as a tree:
    if depth is not None:
        print_result_as_tree(objs, depth)
        return

    # If json is true, we print it as json:
    if json == True:
        print_result_as_json(objs)

    # If fields are provided, we print it as a table
    if fields is not None:
        print_result(objs)

def print_result_as_json(objs):
    print(json.dumps(json.loads(jsonpickle.encode(ListAccountsResult)),indent=4))

def get_result_as_tree(objs, depth=1, currentDepth=0, lastKey = ""):
    stringToReturn = ""
    if(currentDepth > depth):
        return "<to see more details, increase depth>\n"
    if(type(objs) is str or type(objs) is bool or type(objs) is int):
        return str(objs) + "\n"
    if(type(objs) is list):
        stringToReturn += "\n"
        for i in range(len(objs)):
            obj = objs[i]
            stringToReturn += currentDepth*"    "+get_result_as_tree(obj, depth, currentDepth+1, lastKey)
        return stringToReturn
    if(type(objs) is dict):
        stringToReturn += "\n"
        for key in objs:
            stringToReturn += currentDepth*"    "+key+":   "+get_result_as_tree(objs[key], depth, currentDepth+1, key)
        return stringToReturn
    if(objs is None):
        return stringToReturn
    mydict = objs.__dict__
    stringToReturn += "\n"
    for key in mydict:
        stringToReturn += currentDepth*"    "
        stringToReturn += key+":   "+get_result_as_tree(mydict[key], depth, currentDepth+1, key)
    return stringToReturn

# Keypaths is arranged as follows:
# it is a nested dict with the order of the keys.
def filter_objects(objs, keyPaths):
    # Otherwise, we keep recursing deeper.
    # Because there are deeper keys, we know that we can go deeper.
    # This means we are dealing with either an array or a dict.
    # If keyPaths looks like this:
    # {"username": True, "volumes": {"Id": True}}
    # The keys in this sequence will be username and volumes.
    # When we recurse into volumes, the keys will be Id.
    finalFilteredObjects = dict()
    if keyPaths == True and type(objs) is not list:
        return objs
    for key in keyPaths:
        print(key)
        # This is our terminating condition. If it is a dict, we need to
        # go ahead and pull out the details of the object.
        if keyPaths[key] == True and (type(objs) is bool or type(objs) is str or type(objs) is int):
            finalFilteredObjects[key] = objs
            continue

        # If we've found a list, we recurse deeper to pull out the objs.
        # We do not advance our keyPath recursion because this is just a list.
        if type(objs) is list:
            # If we have a list of objects, we will need to assemble and return a list of stuff.
            filteredObjsDict = [None]*len(objs)
            for i in range(len(objs)):
                # Each element could be a string, dict, or list.
                print(type(objs[i]))
                filteredObjsDict[i] = filter_objects(objs[i], keyPaths)
            finalFilteredObjects[key] = filteredObjsDict
            continue

        # If we've found a dict, we recurse deeper to pull out the objs.
        # Because this is a dict, we must advance our keyPaths recursion.
        # Consider the following example:
        dictionaryOfInterest = None
        if type(objs) is dict:
            dictionaryOfInterest = objs
        else:
            dictionaryOfInterest = objs.__dict__
        print(dictionaryOfInterest[key])
        print(keyPaths[key])
        finalFilteredObjects[key] = filter_objects(dictionaryOfInterest[key], keyPaths[key])
    return finalFilteredObjects

def print_result_as_table(objs, keyPaths):
    filteredDictionary = filter_objects(objs, keyPaths)


def print_result_as_tree(objs, depth=1):
    print(get_result_as_tree(objs, depth))

def print_list(objs, fields, formatters={}, order_by=None):
    pt = prettytable.PrettyTable([f for f in fields], caching=False)
    pt.aligns = ['l' for f in fields]
    pt.max_width = 80
    if not objs:
        objs = []

    for o in objs:
        row = []
        for field in fields:
            if field == 'qos':
                # The QoS attribute is ridiculously long with the curve
                # data, which frankly isn't that useful for an end user, so
                # let's pop it off of the object here for display
                o['qos'].pop('curve', None)
            if field in formatters:
                row.append(formatters[field](o))
            else:
                field_name = field.replace(' ', '_')
                if type(o) == dict and field in o:
                    data = o[field]
                else:
                    data = getattr(o, field_name, '')
                row.append(data)
        pt.add_row(row)

    print(pt)
