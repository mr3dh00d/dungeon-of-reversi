def CollisionBlock(position, points):
    center_lateral = (points[0][0]-40, points[1][0]+40)
    center_vertical = (points[0][1], points[1][1]+40)
    if(position[0] <= center_lateral[0]+10):
        if(position[0] >= center_lateral[0] and center_vertical[1] > position[1] > center_vertical[0]):
            position = (center_lateral[0], position[1])
    if(position[0] >= center_lateral[1]-10):
        if(position[0] <= center_lateral[1] and center_vertical[1] > position[1] > center_vertical[0]):
            position = (center_lateral[1], position[1])
    if(position[1] <= center_vertical[0]+10):
        if(position[1] >= center_vertical[0] and center_lateral[1] > position[0] > center_lateral[0]):
            position = (position[0], center_vertical[0])
    if(position[1] >= center_vertical[1]-10):
        if(position[1] <= center_vertical[1] and center_lateral[1] > position[0] > center_lateral[0]):
            position = (position[0], center_vertical[1])
    return position