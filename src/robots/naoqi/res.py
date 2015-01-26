from robots.resources import Resource, CompoundResource

# hardware resource that need to be shared
LEYE = Resource("left eye")
REYE = Resource("right eye")
EYES = CompoundResource(LEYE, REYE, name = "eyes")
AUDIO = Resource("audio")


