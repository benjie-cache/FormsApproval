from django.db import models
from accounts.models import User
# Create your models here.
CONSERVATION_AREAS = (('MOUNTAIN CONSERVATION AREA', 'MOUNTAIN CONSERVATION AREA'), 
('SOUTHERN CONSERVATION AREA', 'SOUTHERN CONSERVATION AREA'), 
('CENTRAL-RIFT CONSERVATION AREA', 'CENTRAL-RIFT CONSERVATION AREA'),
('TSAVOS(TSAVO CONSERVATION AREA)','TSAVOS(TSAVO CONSERVATION AREA)'),
('COAST CONSERVATION AREA','COAST CONSERVATION AREA'),
('EASTERN CONSERVATION AREA','EASTERN CONSERVATION AREA'),
('WESTERN CONSERVATION AREA','WESTERN CONSERVATION AREA'),
)
STATIONS=(('ABERDARES', 'ABERDARES'), 
('MT KENYA', 'MT KENYA'), 
('MWEA NATIONAL RESERVE', 'MWEA NATIONAL RESERVE'),
('AMBOSELI','AMBOSELI'),
('NAIROBI','NAIROBI'),
('OL DONYO SABUK','OL DONYO SABUK'),
('SAFARI WALK','SAFARI WALK'),
('ORPHANAGE','ORPHANAGE'),
#central rift 
('LAKE NAKURU','LAKE NAKURU'),

('HELLS GATE/LONGONOT','HELLS GATE/LONGONOT'),
#TSAVOS
('TSAVO EAST','TSAVO EAST'),
('TSAVO WEST','TSAVO WEST'),
('CHYULU HILLS','CHYULU HILLS'),
#COASTAL CONSERVATION
('MOMBASA','MOMBASA'),
('MALINDI','MALINDI'),
('DIANI','DIANI'),
('KISITE MPUNGUTI N. PARK','KISITE MPUNGUTI N. PARK'),
('SHIMBA HILLS NATIONAL PARK','SHIMBA HILLS NATIONAL PARK'),
('MOMBASA MARINE PARK','MOMBASA MARINE PARK'),
('ARABUKO SOKOKE NATIONAL  PARK','ARABUKO SOKOKE NATIONAL  PARK'),
('WATAMU MARINE N. RESERVE','WATAMU MARINE N. RESERVE'),
('KIUNGA MARINR NATIONAL PARK','KIUNGA MARINR NATIONAL PARK'),
('TANA RIVER PRIMATE N. RESERVE','TANA RIVER PRIMATE N. RESERVE'),
('MERU NATIONAL PARK','MERU NATIONAL PARK'),
('SIBILOI NATIONAL PARK','SIBILOI NATIONAL PARK'),
('MARSABIT NATIONAL PARK','MARSABIT NATIONAL PARK'),
('SOUTHERN ISLANDS NATIONAL PARK','SOUTHERN ISLANDS NATIONAL PARK'),
('MT. ELGON N.P','MT. ELGON N.P'),
('SAIWA SWAMP N. P.','SAIWA SWAMP N. P.'),
('KAKAMEGA FOREST N RESERVE','KAKAMEGA FOREST N RESERVE'),
('NASOLOT N RESERVE','NASOLOT N RESERVE'),
('CENTRAL ISLAND NATIONAL PARK','CENTRAL ISLAND NATIONAL PARK'),
('RUMA N. P','RUMA N. P'),
('KISUMU IMPAL','KISUMU IMPALA'),
('NDERE ISLANDS NATIONAL PARK','NDERE ISLANDS NATIONAL PARK'),
('S.TURKANA','S.TURKANA'),
('LAKE ELEMENTEITA','LAKE ELEMENTEITA')



)
class UserNotifications(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_id}"
    
    class Meta:
        verbose_name = "Notifications"
        verbose_name_plural = verbose_name