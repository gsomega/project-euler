#PE_228
#The math:
#Normals to the edges (sides) are preserved through addition
# S3 + S4 = 6 edges because there is a duplicate normal edge (RHS)
# Because these are regular polygons in a particular config,
# we can represent the normal direction as an angle about the center
# ex: S3 = [0, 120, 240]
# ex: S4 = [0, 90, 180, 270]
# S3+S4 = S3 U S4 = [0, 90, 120, 180, 240, 270] (6 sided)
# (this doesn't need to use 360 degrees, but will for readability)

angle_list=[]
new_angle=0

for shape_size in range(1864, 1910):
    for i in range(0,shape_size):
        new_angle= (360*i)/shape_size
        if new_angle not in angle_list:
            angle_list.append(new_angle)
            #print(new_angle)
    print(len(angle_list))