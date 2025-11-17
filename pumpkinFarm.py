def pumpkin(pumpkinTileCount):
	for j in range(get_world_size()):
		for i in range(get_world_size()):
			if(get_ground_type() == Grounds.Grassland):
				till()
			if(can_harvest()):
				pumpkinTileCount += 1
			else:
				if(get_water() < 0.2):
					use_item(Items.Water)

			plant(Entities.Pumpkin)
			move(North)
		move(East)

	realWorldSize = get_world_size() * get_world_size()
	if (pumpkinTileCount == realWorldSize):
		harvest()

	return pumpkinTileCount

clear()	
while True:
	pumpkinTileCount = 0
	pumpkinTileCount = pumpkin(pumpkinTileCount)
	