class Bucket:
	def __init__(self, name, current_volume, max_volume):
		self.name = name
		self.max = max_volume
		self.current = current_volume

	def getName(self):
		return self.name

	def getMax(self):
		return self.max

	def getCurrent(self):
		return self.current

	def setCurrent(self, new_current_volume):
		self.current = new_current_volume


	def fillBucket(self, source_bucket):
		space_left = self.max - self.current

		if source_bucket.getCurrent() <= space_left:
			self.current = self.current + source_bucket.getCurrent()
			source_bucket.setCurrent(0)

		else:
			self.current = self.current + space_left
			source_bucket.setCurrent( source_bucket.getCurrent() - space_left )
