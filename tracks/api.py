from ninja import NinjaAPI,UploadedFile, File
from .models import Track
from .schema import TrackSchema, NotFoundSchema
from typing import List,Optional

api = NinjaAPI(
    title="Api teste",
    version= "1.0.0",
)

@api.get("/tracks", response=List[TrackSchema])
def tracks(request, title: Optional[str]=None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()

@api.get("/tracks/{id}", response={200:TrackSchema, 403:NotFoundSchema})
def track(request, id:int):
    try:
        track = Track.objects.get(pk=id)
        return 200, track
    except Track.DoesNotExist as e:
        return 403,{"message":f"{e}"}
            
@api.post("/tracks",response={201:TrackSchema})
def create_track(request, track : TrackSchema):
    track=  Track.objects.create(**track.dict())
    return track

@api.delete("/tracks/{id}", response={200:None, 403:NotFoundSchema})
def delete_track(request, id:int, data:TrackSchema):
    try:
        track = Track.objects.get(pk=id)
        track.delete()
        return 200
    except Track.DoesNotExist as e:
        return 403,{"message":f"{e}"}
    
    
@api.post("/upload", url_name="upload")
def upload(request,file:UploadedFile = File(...)):
    data = file.read().decode()
    return {
        "Name":file.name,
        "data":data
        
    }
     
            