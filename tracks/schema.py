from ninja import Schema
from datetime import datetime

class TrackSchema(Schema):
  title: str
  artist: str
  duration : float
  last_play: datetime 
  
class NotFoundSchema(Schema):
  message: str