from sqlalchemy import Column, String, Integer, DateTime
from connection import Base,engine
import re
#import define_variable 
class PutTodB(Base):
    #platform = define_variable.platform_name
    #product = define_variable.table_name
    platform = 'thebetterindia'
    __tablename__ = "thebetterindia"
    urls = Column(String(1000))
    blog = Column(String(1000000))
    Id = Column(Integer, primary_key=True)

    def __init__(self, Id = None,urls=None,blog = None):
        # self.platform= platform
        self.Id = Id,
        self.urls = urls,
        self.blog = blog
       
    def __repr__(self):
        if platform == 'thebetterindia':
            return "<AllData: Id='%s' , urls='%s' , blog='%s'>" % (self.Id,self.urls,self.blog)
        elif platform == 'snapdeal':
            return "<AllData: title='%s', rating='%d', review='%s'>" % (self.title, self.rating, self.review)
# import pymongo

# from scrapy.exceptions import DropItem
# from scrapy import log

# settings = {'MONGODB_SERVER':"localhost","MONGODB_PORT":27017,"MONGODB_DB":"amazon","MONGODB_COLLECTION":"reviews"}

# class MongoDBPipeline(object):

#     def __init__(self):
#         connection = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]

#     def process_item(self, item, spider):
#         valid = True
#         for data in item:
#             if not data:
#                 valid = False
#                 raise DropItem("Missing {0}!".format(data))
#         if valid:
#             self.collection.insert(dict(item))
#             log.msg("Review added to db",
#                     level=log.DEBUG, spider=spider)
#         return item