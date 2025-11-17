def startTop():
	x = get_pos_x()
	y = get_pos_y() 
	worldSize = get_world_size() - 1
	
	while x != 0:
		move(West)
		x = get_pos_x()
		
	while y != worldSize:
		move(North)
		y = get_pos_y()

def startBottom():
	x = get_pos_x()
	y = get_pos_y() 
	
	while x != 0:
		move(West)
		x = get_pos_x()
		
	while y != 0:
		move(South)
		y = get_pos_y()		
		

def endTop():
	x = get_pos_x()
	y = get_pos_y() 
	worldSize = get_world_size() - 1
	
	while x != worldSize:
		move(East)
		x = get_pos_x()
		
	while y != worldSize:
		move(North)
		y = get_pos_y()
		
def endBottom():
	x = get_pos_x()
	y = get_pos_y() 
	worldSize = get_world_size() - 1
	
	while x != worldSize:
		move(East)
		x = get_pos_x()
		
	while y != 0:
		move(South)
		y = get_pos_y()
