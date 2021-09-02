def Portal(portal, positon):
    if(portal[0][0] <= positon[0] <= portal[1][0]):
        if(portal[0][1] <= positon[1] <= portal[1][1]):
            return True
    return False