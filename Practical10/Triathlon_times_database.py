class Triathlon(object):
	def __init__(self,first_name,last_name,location,swim,cycle,run):
		self.first_name=first_name
		self.last_name=last_name
		self.location=location
		self.swim=float(swim)
		self.cycle=float(cycle)
		self.run=float(run)
		self.total=self.swim+self.cycle+self.run
	def print(self):
		print(f"firstname={self.first_name},lastname={self.last_name},location={self.location},swim={self.swim},cycle={self.cycle},run={self.run},total={self.total}")

#example	
a=Triathlon("Adam","Li","Texas","1.3","1.4","1.5")
a.print()	