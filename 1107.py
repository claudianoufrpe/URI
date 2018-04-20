# @author Matheus Alves dos Santos
# TITLE: Escultura a Laser
# ID: 1107

while True:
    height, width = map(int, raw_input().split())
    if ((height == 0) and (width == 0)):
        break
        
    sculpture = map(int, raw_input().split())
    laser_on = height - sculpture[0]
    
    for i in range(1, len(sculpture)):
        if (sculpture[i] < sculpture[i - 1]):
            laser_on += (sculpture[i - 1] - sculpture[i])
    
    print laser_on
