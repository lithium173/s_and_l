class Player:
	def __init__(self):
		pass
	def move(self):
		pass
class Table:
	def __init__(self):
		pass
	def show(self):
		pass
class Bit:
	def __init__(self):
		pass
class Dice:
	def __init__(self,screen,players):
		self.screen=screen
		self.p=playars
		self.turn=0
		self.ran=random.randint(1,6)
		self.r1=pygame.image.load('red0.png')
		self.r2=pygame.image.load('red1.png')
		self.r3=pygame.image.load('red2.png')
		self.r4=pygame.image.load('red3.png')
		self.r5=pygame.image.load('red4.png')
		self.r6=pygame.image.load('red5.png')
		self.r7=pygame.image.load('red6.png')
		self.r8=pygame.image.load('red7.png')
		self.d1=pygame.image.load('1.png')
		seld.d2=pygame.image.load('2.png')
		self.d3=pygame.image.load('3.png')
		self.d4=pygame.image.load('4.png')
		self.d5=pygame.image.load('5.png')
		self.d6=pygame.image.load('6.png')
		self.sound=pygame.mixer.music.load('dice_s.wav')
	def randDice(self):
		pass

