import isEven
import setPos

setPos.startBottom()
def treeFarm(i1 = Entities.Carrot):
	
	x = get_pos_x()
	y = get_pos_y()
	worldSize = get_world_size() - 1
	groundType = get_ground_type()
	
	if can_harvest():
		harvest()
	if (isEven.x(x) and isEven.x(y)) or (not isEven.x(x) and not isEven.x(y)):
		plant(Entities.Tree)
	else:
		if (i1 == Entities.Carrot or i1 == Entities.Pumpkin) and groundType != Grounds.Soil:
			till()
			plant(i1)
		else:
			plant(i1)

	if(y < worldSize):
		move(North)
	else:
		move(North)
		move(East)
clear()
while True:
	treeFarm(Entities.Carrot)
