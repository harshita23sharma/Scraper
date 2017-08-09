from sqlalchemy import Column, String, Integer, DateTime, MetaData,Table
from connection import Base,engine
class DBMS():

	def __init__(self,platform=None,tbname=None,title=None,review=None,rating=None,upvotes=None):
		self.platform = platform
		self.tbname = tbname
		self.title = title
		self.review = review

	def __check_create_table__(self):
		if not engine.dialect.has_table(engine,self.tbname):
			metadata = MetaData(engine)
			if self.platform == 'thebetterindia':
				Table(self.tbname, metadata,Column('title', String(1000)),Column('review', String(100000)))
				metadata.create_all()
			return True
		else:
			return False

	# def __repr__(self):
	# 	if self.platform == 'amazon':
	# 		return "<AllData: title='%s', rating='%d', upvotes='%d', review='%s'>" % (self.title, self.rating, self.upvotes, self.review)
	# 	elif self.platform == 'snapdeal':
	# 		return "<AllData: title='%s', rating='%d', review='%s'>" % (self.title, self.rating, self.review)

