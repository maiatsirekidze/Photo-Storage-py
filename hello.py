
import math
def number_of_photos(photo_size_mb, drive_size_gb):
    mb = drive_size_gb * 1000
    return math.floor(mb/photo_size_mb)
print(number_of_photos(1,1))