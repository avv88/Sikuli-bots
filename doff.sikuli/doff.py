#interface scale = 1; doff window width = min; 1080p res; notifications - hidden in bottom right corner
#items:
#Shield Battery (Research Ant-Psionic Shields)
#Antigens, Medical supplies (a lot), and other goods
#Science and medical - a lot of small tasks, good for botting. 
#Military, Development - mostly medium and long times
#Colony/Development - ? (mostly okay), colonists farm
kerrat = False
Settings.MinSimilarity=0.85
import gc
import time
from datetime import datetime
from random import randrange
Debug.on(3)
Debug.setLogFile("C://Sikuli_Log.txt")
#PARAMETERS
cycles = 0
USE_LOGOFF = True
ADM_RUN_CONSTANTLY = True
WHICH_ADM = 1
COARSE_DOFF = True
LAB_PROJECT_SCHOOL_ID = 5
ADM_MINIMUM_TIER = 3
###################
tier_maintenance = 0
if ADM_MINIMUM_TIER == 2:
    tier_maintenance = 2
if ADM_MINIMUM_TIER == 3:
    tier_maintenance = 4
if ADM_MINIMUM_TIER == 4:
    tier_maintenance = 8
if ADM_MINIMUM_TIER == 5:
    tier_maintenance = 12
if ADM_MINIMUM_TIER == 6:
    tier_maintenance = 18
ADM_MINIMUM_TIER = tier_maintenance
last_ship_scan = time.time() - 50000
ship_ids = []
dailies = []
dailies_old = []
dailies.append("1603594716403.png")
dailies_old.append("1602472331885.png")
dailies_old.append("1602547268406.png")
accept_button = "accept_button.png"
exit_button = "exit_button.png"
vintrax = "vritrax.png"
adm_button = Pattern("adm_button.png").similar(0.90).targetOffset(270,-1)
adm_clicker = Pattern("adm_clicker.png").similar(0.91)
adm_fed = Pattern("adm_faction.png").similar(0.87)
adm_kdf = Pattern("adm_kdf.png").similar(0.90)
adm_rom = Pattern("adm_rom.png").similar(0.91)
adm_fer = Pattern("adm_fer.png").similar(0.91)
adm_plan = Pattern("adm_plan.png").similar(0.85)
adm_close_ships = Pattern("adm_close_ships.png").targetOffset(56,-8)
adm_select1 = Pattern("adm_select1.png").similar(0.85).targetOffset(25,-88)
adm_select2 = Pattern("adm_select2.png").similar(0.85).targetOffset(30,-24)
adm_select3 = Pattern("adm_select3.png").targetOffset(37,40)
imgTaskbar = Pattern("imgTaskbar.png").similar(0.85)
adm_assign = "adm_assign.png"
adm_good_chance = Pattern("adm_good_chance.png").similar(0.90)
adm_okay_chance = Pattern("adm_okay_chance.png").similar(0.90)
adm_begin = Pattern("adm_begin.png").similar(0.90)
adm_complete1 = Pattern("adm_complete1.png").similar(0.90)
adm_complete2 = Pattern("adm_complete2.png").similar(0.85)
admiralties = []
adm = []
TOD = Pattern("TOD.png").similar(0.85).targetOffset(0,37)
TOD_fed = "TOD_fed.png"
TOD_kdf = "TOD_kdf.png"
TOD_rom = "TOD_rom.png"
TOD_fer = "TOD_fer.png"
TOD_tier = []
TOD_tier.append("1591711035319.png")
TOD_tier.append("1591711056491.png")
TOD_tier.append("1591711073448.png")
TOD_tier.append("1591711087010.png")
TOD_tier.append("1591711108604.png")
TOD_tier.append("1591711122869.png")
TOD_tier.append("1591711147852.png")
TOD_tier.append("1591720279207.png")
TOD_tier.append("1591713351030.png")
adm_coarse = []
adm_coarse.append(Pattern("1591710038841.png").targetOffset(-40,28))
adm_coarse.append(Pattern("1591703702565.png").targetOffset(-38,28))
adm_coarse.append(Pattern("1591703840694.png").targetOffset(-43,27))
adm_coarse.append(Pattern("1591703969702.png").targetOffset(-51,28))
adm_coarse.append(Pattern("1591703804973.png").targetOffset(-29,29))
adm_coarse.append(Pattern("1591703866205.png").targetOffset(-48,30))
adm_coarse.append(Pattern("1591710085801.png").targetOffset(-26,28))
adm_coarse.append(Pattern("1591703739085.png").targetOffset(-48,26))
adm_coarse.append(Pattern("1591703756862.png").targetOffset(-25,30))
adm_coarse.append(Pattern("1591703778988.png").targetOffset(-50,27))
#Adm touple: image, duration, eng, tac, sci, reward, faction
#FED
adm.append((Pattern("1591628153301.png").targetOffset(325,52),3,45,45,105,"mat"))
adm.append((Pattern("1591628261642.png").targetOffset(295,50),3,70,70,125,"mat"))
adm.append((Pattern("1591628336712.png").targetOffset(391,54),1,20,45,20,"cred"))
adm.append((Pattern("1591628437916.png").targetOffset(373,50),0,15,25,15,"exp"))
adm.append((Pattern("1591628492671.png").targetOffset(370,53),0,60,30,30,"mat"))
adm.append((Pattern("1591628559508.png").targetOffset(310,49),0,30,30,80,"cred"))
adm.append((Pattern("1591628603876.png").targetOffset(338,49),2,55,20,20,"exp"))
adm.append((Pattern("1591628649377.png").targetOffset(309,51),4,175,90,90,"exp"))
adm.append((Pattern("1591628700261.png").targetOffset(375,52),4,190,95,95,"cred"))
adm.append((Pattern("1591628743904.png").targetOffset(322,55),2,70,110,70,"?"))
adm.append((Pattern("1591628810122.png").targetOffset(325,50),4,70,70,70,"cred"))
adm.append((Pattern("1591700827764.png").targetOffset(317,51),1,25,25,25,"exp"))
adm.append((Pattern("1591628868301.png").targetOffset(276,50),2,40,40,95,"?"))
adm.append((Pattern("1591628906453.png").targetOffset(304,55),1,20,20,45,"?"))
adm.append((Pattern("1591628944791.png").targetOffset(296,53),1,20,20,55,"mat"))
adm.append((Pattern("1591628982441.png").targetOffset(325,52),0,10,10,20,"exp"))
adm.append((Pattern("1591629016958.png").targetOffset(352,51),0,25,25,70,"mat"))
adm.append((Pattern("1591703281029.png").targetOffset(343,50),1,50,50,110,"mat"))
adm.append((Pattern("1591703341477.png").targetOffset(352,52),130,80,80,"mat"))
adm.append((Pattern("1591629053616.png").targetOffset(328,51),0,10,20,10,"exp"))
adm.append((Pattern("1591629086422.png").targetOffset(399,55),0,10,10,10,"exp"))
adm.append((Pattern("1591629128893.png").targetOffset(379,51),0,50,50,50,"exp"))
adm.append((Pattern("1591629163194.png").targetOffset(305,53),0,95,65,65,"exp"))
adm.append((Pattern("1591680806806.png").targetOffset(348,54),0,80,130,80,"exp"))
adm.append((Pattern("1591629208170.png").targetOffset(314,48),0,60,85,60,"exp"))
adm.append((Pattern("1591629333198.png").targetOffset(313,53),2,45,85,45,"?"))
adm.append((Pattern("1591630774358.png").targetOffset(291,50),3,65,25,25,"cred"))
adm.append((Pattern("1591630811629.png").targetOffset(351,51),0,45,15,15,"exp"))
adm.append((Pattern("1591630861757.png").targetOffset(309,52),0,15,15,35,"cred"))
adm.append((Pattern("1591630896775.png").targetOffset(320,50),1,55,55,55,"cred"))
adm.append((Pattern("1591630932685.png").targetOffset(327,51),1,100,100,100,"cred"))
adm.append((Pattern("1591631009758.png").targetOffset(318,50),1,35,35,90,"exp"))
adm.append((Pattern("1591631077070.png").targetOffset(329,53),0,35,70,35,"exp"))
adm.append((Pattern("1591631153453.png").targetOffset(307,51),0,20,10,10,"exp"))
#KDF
adm.append((Pattern("1591631243070.png").targetOffset(329,54),3,45,45,105,"mat"))
adm.append((Pattern("1591631289165.png").targetOffset(335,50),3,90,90,160,"dil"))
adm.append((Pattern("1591631322218.png").targetOffset(347,52),3,95,160,95,"?"))
adm.append((Pattern("1591631358286.png").targetOffset(359,48),0,15,15,15,"dil"))
adm.append((Pattern("1591631414954.png").targetOffset(317,51),0,15,25,15,"dil"))
adm.append((Pattern("1591631458049.png").targetOffset(424,54),0,75,75,75,"dil"))
adm.append((Pattern("1591631529608.png").targetOffset(305,54),0,15,15,35,"cred"))
adm.append((Pattern("1591631560744.png").targetOffset(380,52),1,20,45,20,"cred"))
adm.append((Pattern("1591631595229.png").targetOffset(333,53),0,95,65,65,"dil"))
adm.append((Pattern("1591631635903.png").targetOffset(342,50),4,125,80,80,"cred"))
adm.append((Pattern("1591631665591.png").targetOffset(313,52),2,55,20,20,"dil"))
adm.append((Pattern("1591691236447.png").targetOffset(327,52),2,85,85,150,"dil"))
adm.append((Pattern("1591631718703.png").targetOffset(293,51),4,45,45,45,"?"))
adm.append((Pattern("1591631761831.png").targetOffset(323,53),4,70,70,70,"cred"))
adm.append((Pattern("1591631901903.png").targetOffset(315,55),1,50,50,110,"mat"))
adm.append((Pattern("1591631964078.png").targetOffset(318,50),1,20,20,45,"?"))
adm.append((Pattern("1591631999528.png").targetOffset(342,50),2,35,35,35,"dil"))
adm.append((Pattern("1591632028968.png").targetOffset(335,52),3,85,85,85,"dil"))
adm.append((Pattern("1591632063206.png").targetOffset(298,55),1,20,20,55,"mat"))
adm.append((Pattern("1591632099214.png").targetOffset(307,56),0,10,10,20,"mat"))
adm.append((Pattern("1591632127758.png").targetOffset(311,47),0,30,30,80,"cred"))
adm.append((Pattern("1591632200158.png").targetOffset(351,49),0,60,30,30,"mat"))
adm.append((Pattern("1591632243788.png").targetOffset(361,55),1,75,75,75,"dil"))
adm.append((Pattern("1591632346038.png").targetOffset(397,55),0,10,10,10,"dil"))
adm.append((Pattern("1591632374356.png").targetOffset(305,49),1,25,25,25,"dil"))
adm.append((Pattern("1591632399045.png").targetOffset(319,49),2,145,85,85,"dil"))
adm.append((Pattern("1591632431292.png").targetOffset(289,54),0,60,85,60,"dil"))
adm.append((Pattern("1591632461623.png").targetOffset(315,51),0,30,60,30,"dil"))
adm.append((Pattern("1591632488398.png").targetOffset(316,52),2,145,85,85,"dil"))
adm.append((Pattern("1591632517696.png").targetOffset(315,55),2,45,85,45,"?"))
adm.append((Pattern("1591632546739.png").targetOffset(316,50),3,60,60,60,"?"))
adm.append((Pattern("1591673185943.png").targetOffset(327,56),0,45,15,15,"dil"))
adm.append((Pattern("1591632578387.png").targetOffset(319,49),1,55,55,55,"cred"))
adm.append((Pattern("1591632614496.png").targetOffset(335,48),0,35,70,35,"dil"))
adm.append((Pattern("1591691184616.png").targetOffset(319,53),0,20,10,10,"dil"))
adm.append((Pattern("1591632644462.png").targetOffset(295,53),1,40,80,40,"?"))
adm.append((Pattern("1591632671685.png").targetOffset(342,53),3,25,25,60,"dil"))
#ROM
adm.append((Pattern("1591632703599.png").targetOffset(342,53),0,95,65,65,"mat"))
adm.append((Pattern("1591632741775.png").targetOffset(301,53),3,70,70,125,"dil"))
adm.append((Pattern("1591632794158.png").targetOffset(321,53),0,15,25,15,"mat"))
adm.append((Pattern("1591632873519.png").targetOffset(352,51),0,15,15,15,"mat"))
adm.append((Pattern("1591632909878.png").targetOffset(297,51),2,80,80,80,"mat"))
adm.append((Pattern("1591632935927.png").targetOffset(299,52),10,10,20,"dil"))
adm.append((Pattern("1591632961159.png").targetOffset(317,51),0,15,15,35,"cred"))
adm.append((Pattern("1591632985393.png").targetOffset(338,48),2,55,20,20,"mat"))
adm.append((Pattern("1591633021462.png").targetOffset(296,50),4,45,45,45,"?"))
adm.append((Pattern("1591633056471.png").targetOffset(293,52),3,65,25,25,"cred"))
adm.append((Pattern("1591633091271.png").targetOffset(329,49),1,90,40,40,"cred"))
adm.append((Pattern("1591633131324.png").targetOffset(352,52),0,80,80,130,"mat"))
adm.append((Pattern("1591633167641.png").targetOffset(283,53),1,50,50,110,"dil"))
adm.append((Pattern("1591633203554.png").targetOffset(329,51),0,25,25,70,"dil"))
adm.append((Pattern("1591633236960.png").targetOffset(289,55),2,40,40,95,"?"))
adm.append((Pattern("1591633265293.png").targetOffset(301,52),1,20,20,55,"dil"))
adm.append((Pattern("1591633299894.png").targetOffset(369,48),0,10,10,10,"mat"))
adm.append((Pattern("1591633335767.png").targetOffset(337,53),1,20,45,20,"cred"))
adm.append((Pattern("1591633367630.png").targetOffset(392,50),1,75,75,75,"mat"))
adm.append((Pattern("1591633401499.png").targetOffset(318,53),0,30,60,30,"mat"))
adm.append((Pattern("1591633436378.png").targetOffset(292,47),1,65,100,65,"mat"))
adm.append((Pattern("1591633469887.png").targetOffset(331,49),0,30,30,80,"cred"))
adm.append((Pattern("1591633500124.png").targetOffset(302,47),3,60,60,60,"?"))
adm.append((Pattern("1591633529569.png").targetOffset(348,52),2,45,85,45,"?"))
adm.append((Pattern("1591633569497.png").targetOffset(334,51),1,25,25,25,"mat"))
adm.append((Pattern("1591633603465.png").targetOffset(313,49),0,35,70,35,"mat"))
adm.append((Pattern("1591633639531.png").targetOffset(315,51),1,35,35,90,"mat"))
adm.append((Pattern("1591633682177.png").targetOffset(332,51),0,45,15,15,"mat"))
adm.append((Pattern("1591633723713.png").targetOffset(363,51),1,55,55,55,"cred"))
adm.append((Pattern("1591633755718.png").targetOffset(334,53),0,80,130,80,"mat"))
adm.append((Pattern("1591633798712.png").targetOffset(312,52),0,20,10,10,"mat"))
adm.append((Pattern("1591672176418.png").targetOffset(331,50),3,25,25,60,"mat"))
adm.append((Pattern("1591672213225.png").targetOffset(368,52),3,90,90,160,"mat"))
adm.append((Pattern("1591672240161.png").targetOffset(291,50),0,80,35,35,"mat"))
#FER
adm.append((Pattern("1591672277815.png").targetOffset(301,55),3,70,70,125,"mat"))
adm.append((Pattern("1591672310831.png").targetOffset(315,51),0,15,25,15,"dil"))
adm.append((Pattern("1591678368852.png").targetOffset(293,50),0,75,75,75,"dil"))
adm.append(("1591672337848.png",0,15,15,35,"cred"))
adm.append((Pattern("1591678332907.png").targetOffset(382,50),1,20,45,20,"lat"))
adm.append((Pattern("1591682372227.png").targetOffset(299,50),0,80,130,80,"dil"))
adm.append((Pattern("1591672361529.png").targetOffset(302,52),1,85,145,85,"lat"))
adm.append((Pattern("1591672389464.png").targetOffset(312,50),2,55,20,20,"dil"))
adm.append((Pattern("1591672421594.png").targetOffset(303,56),4,45,45,45,"?"))
adm.append((Pattern("1591672448273.png").targetOffset(283,52),3,85,85,85,"?"))
adm.append((Pattern("1591672475025.png").targetOffset(330,48),0,20,10,10,"dil"))
adm.append((Pattern("1591672501499.png").targetOffset(295,51),3,65,25,25,"lat"))
adm.append((Pattern("1591672533287.png").targetOffset(284,49),2,120,70,70,"dil"))
adm.append((Pattern("1591672565162.png").targetOffset(306,53),3,110,110,110,"lat"))
adm.append((Pattern("1591672592798.png").targetOffset(338,53),0,45,15,15,"dil"))
adm.append((Pattern("1591672621392.png").targetOffset(340,50),2,35,35,35,"dil"))
adm.append((Pattern("1591672659651.png").targetOffset(314,50),2,40,40,95,"?"))
adm.append((Pattern("1591672683329.png").targetOffset(304,53),1,20,20,55,"mat"))
adm.append((Pattern("1591679602689.png").targetOffset(293,52),0,30,30,80,"lat"))
adm.append((Pattern("1591672721824.png").targetOffset(336,51),0,10,10,20,"mat"))
adm.append((Pattern("1591672748824.png").targetOffset(349,49),0,60,30,30,"mat"))
adm.append((Pattern("1591672772851.png").targetOffset(393,52),0,50,50,50,"dil"))
adm.append((Pattern("1591672797754.png").targetOffset(397,52),0,10,10,10,"dil"))
adm.append((Pattern("1591672821544.png").targetOffset(326,53),1,25,25,25,"dil"))
adm.append((Pattern("1591672848671.png").targetOffset(311,49),2,45,85,45,"?"))
adm.append((Pattern("1591672876520.png").targetOffset(304,52),1,20,20,55,"mat"))
adm.append((Pattern("1591672901504.png").targetOffset(395,53),0,15,15,15,"dil"))
adm.append((Pattern("1591672929680.png").targetOffset(368,53),2,80,80,80,"dil"))
adm.append((Pattern("1591672951648.png").targetOffset(325,47),1,55,55,55,"lat"))
adm.append((Pattern("1591672979256.png").targetOffset(363,54),1,100,100,100,"lat"))
adm.append((Pattern("1591673006264.png").targetOffset(288,49),0,80,35,35,"dil"))
adm.append((Pattern("1591673040161.png").targetOffset(283,49),4,70,70,70,"lat"))
adm.append((Pattern("1591673063904.png").targetOffset(336,53),3,25,25,6,"dil"))
adm.append((Pattern("1591673091136.png").targetOffset(288,50),0,25,25,70,"mat"))
#name(img), eng, tac, sci, maintenance
adm_ships = []
adm_ships.append(("1592656480482.png",32,52,14,12))
adm_ships.append(("1612023941425.png",37,62,18,18))
adm_ships.append(("1612023518997.png",20,48,30,12))
adm_ships.append(("1612023745291.png",25,57,35,18))
adm_ships.append(("1612023847940.png",24,40,62,18))
adm_ships.append(("1592656765856.png",35,51,19,12))
adm_ships.append(("1598142135699.png",31,30,67,18))
adm_ships.append(("1592656602976.png",25,52,28,12))
adm_ships.append(("1592657504236.png",51,31,23,12))
adm_ships.append(("1592657549966.png",20,56,29,12))
adm_ships.append(("1592656638815.png",33,51,21,12))
adm_ships.append(("1592656671570.png",18,63,24,12))
adm_ships.append(("1595999114408.png",53,39,43,18))
adm_ships.append(("1595999147464.png",66,49,20,18))
adm_ships.append(("1595999173003.png",70,35,30,18))
adm_ships.append(("1592656692744.png",66,29,40,18))
adm_ships.append(("1592656702968.png",43,29,72,18))
adm_ships.append(("1592656715592.png",31,31,73,18))
adm_ships.append(("1592656728076.png",28,28,79,18))
adm_ships.append(("1592708700210.png",30,27,78,18))
adm_ships.append(("1592658006063.png",43,17,30,8))
adm_ships.append(("1593358111261.png",49,45,41,18))
adm_ships.append(("1593358150519.png",62,42,31,18))
adm_ships.append(("1593358169695.png",23,61,51,18))
adm_fleet = []
adm_fleet.append(("1592656378162.png",3,2,1,0))
adm_fleet.append(("1612022732700.png",2,2,2,0))
adm_fleet.append(("1612022756836.png",2,3,1,0))
adm_fleet.append(("1612022783228.png",4,1,1,0))
adm_fleet.append(("1612022800019.png",4,1,1,0))
adm_fleet.append(("1612022817954.png",2,2,2,0))
adm_fleet.append(("1592656389530.png",5,3,2,0))
adm_fleet.append(("1592656415551.png",4,1,1,0))
adm_fleet.append(("1592656432386.png",6,4,4,0))
adm_fleet.append(("1592656441777.png",2,2,2,0))
adm_fleet.append(("1592656453619.png",4,3,3,0))
adm_fleet.append(("1612022845948.png",4,3,3,0))
adm_fleet.append(("1612022862172.png",4,3,3,0))
adm_fleet.append(("1612022883848.png",3,1,6,0))
adm_fleet.append(("1612022912682.png",3,4,3,0))
adm_fleet.append(("1600503727159.png",3,4,3,0))
adm_fleet.append(("1595999055652.png",7,5,4,5))
adm_fleet.append(("1592656528048.png",12,36,12,8))
adm_fleet.append(("1592656553388.png",17,47,11,12))
adm_fleet.append(("1592656681149.png",37,15,23,12))
adm_fleet.append(("1592708808226.png",47,21,15,12))
adm_fleet.append(("1592709488730.png",14,50,19,12))
adm_fleet.append(("1592746404180.png",50,12,21,12))
adm_fleet.append(("1592709426594.png",50,21,12,12))
adm_fleet.append(("1592656578473.png",16,31,36,12))
adm_fleet.append(("1592656749736.png",21,12,50,12))
adm_fleet.append(("1592656876864.png",44,17,22,12))
adm_fleet.append(("1592656931239.png",45,18,20,12))
adm_fleet.append(("1592656975480.png",50,19,14,12))
adm_fleet.append(("1592657014584.png",13,42,28,12))
adm_fleet.append(("1592657062134.png",21,47,15,12))
adm_fleet.append(("1592657090973.png",14,47,22,12))
adm_fleet.append(("1592657114934.png",15,47,21,12))
adm_fleet.append(("1592657158238.png",14,49,20,12))
adm_fleet.append(("1592657194991.png",21,50,12,12))
adm_fleet.append(("1592657234886.png",12,50,21,12))
adm_fleet.append(("1592657274790.png",17,52,14,12))
adm_fleet.append(("1592657301751.png",22,17,44,12))
adm_fleet.append(("1592657328520.png",21,12,50,12))
adm_fleet.append(("1592657348614.png",12,21,50,12))
adm_fleet.append(("1592657383744.png",15,18,50,12))
adm_fleet.append(("1613804339136.png",16,42,25,12))
adm_fleet.append(("1613803166529.png",47,21,15,12))
adm_fleet.append(("1613804305736.png",40,28,40,18))
adm_fleet.append(("1612022969674.png",28,13,13,4))
adm_fleet.append(("1592656467719.png",30,48,12,12))
adm_fleet.append(("1592656566232.png",20,55,15,12))
adm_fleet.append(("1596861610720.png",15,42,15,8))
adm_fleet.append(("1612024013426.png",35,57,16,18))
adm_fleet.append(("1612024029650.png",35,57,16,18))
adm_fleet.append(("1593147711207.png",20,15,55,12))
adm_fleet.append(("1592656591209.png",52,17,21,12))
adm_fleet.append(("1612023309298.png",55,15,20,12))
adm_fleet.append(("1612023357218.png",26,44,20,12))
adm_fleet.append(("1612023590211.png",31,52,25,18))
adm_fleet.append(("1612023639739.png",23,52,33,18))
adm_fleet.append(("1612023382755.png",26,44,20,12))
adm_fleet.append(("1612023407971.png",23,16,51,12))
adm_fleet.append(("1648238368984.png",52,20,18,12))
adm_fleet.append(("1648238402176.png",34,29,45,18))
adm_fleet.append(("1612023703339.png",60,34,23,18))
adm_fleet.append(("1612023797273.png",24,65,37,18))
adm_fleet.append(("1634929697268.png",26,49,51,18))
adm_fleet.append(("1600591751923.png",64,25,16,12))
adm_fleet.append(("1592656611353.png",20,54,24,12))
adm_fleet.append(("1592656621674.png",24,54,20,12))
adm_fleet.append(("1592656629705.png",20,50,20,12))
adm_fleet.append(("1613375408342.png",39,67,20,18))
adm_fleet.append(("1612023986132.png",37,62,18,18))
adm_fleet.append(("1648237791936.png",30,47,40,18))
adm_fleet.append(("1648237856629.png",38,61,18,18))
adm_fleet.append(("1648237940466.png",20,34,63,18))
adm_fleet.append(("1648237994492.png",44,45,16,12))
adm_fleet.append(("1648238031256.png",38,51,16,12))
adm_fleet.append(("1648238102227.png",59,28,18,12))
adm_fleet.append(("1648238171627.png",66,29,22,18))
adm_fleet.append(("1648238214507.png",23,34,60,18))
adm_fleet.append(("1648238296650.png",16,56,45,18))
adm_fleet.append(("1612023098717.png",43,17,30,8))
adm_fleet.append(("1634929793956.png",69,40,26,18))
adm_fleet.append(("1612023139122.png",36,24,15,12))
adm_fleet.append(("1612023161251.png",40,20,15,12))
adm_fleet.append(("1612023181894.png",25,25,25,12))
adm_fleet.append(("1612023197804.png",22,38,15,12))
adm_fleet.append(("1612023222602.png",23,42,10,12))
adm_fleet.append(("1612023243363.png",15,12,48,12))
adm_fleet.append(("1593417123065.png",29,16,15,8))
adm_fleet.append(("1593417815429.png",36,12,12,8))
adm_fleet.append(("1593417145923.png",14,32,14,8))
adm_fleet.append((Pattern("1593417234890.png").similar(0.90),12,12,36,8))
adm_fleet.append((Pattern("1593417274065.png").similar(0.90),40,20,15,12))
adm_fleet.append((Pattern("1593417340330.png").similar(0.90),47,11,17,12))
adm_fleet.append((Pattern("1593417367915.png").similar(0.90),47,17,11,12))
adm_fleet.append((Pattern("1593417399827.png").similar(0.90),18,44,13,12))
adm_fleet.append((Pattern("1593417545842.png").similar(0.90),11,47,17,12))
adm_fleet.append((Pattern("1593417637508.png").similar(0.90),15,20,40,12))
adm_fleet.append((Pattern("1593417679701.png").similar(0.90),17,11,47,12))
adm_fleet.append(("1593417892000.png",11,17,47,12))
adm_fleet.append(("1612061450151.png",33,54,21,18))
adm_fleet.append(("1609246190024.png",24,40,62,18))
adm_fleet.append(("1594227984596.png",60,22,26,100))
adm_fleet.append(("1594228028795.png",21,21,66,100))
adm_fleet.append(("1596439162353.png",41,50,17,100))
adm_fleet.append(("1596439183072.png",25,65,18,100))
adm_fleet.append(("1594472157545.png",70,19,19,100))
adm_fleet.append(("1594472185347.png",26,60,22,100))
adm_fleet.append(("1594472210031.png",16,68,24,100))
adm_fleet.append(("1595507702855.png",66,21,21,100))
adm_fleet.append(("1595920192412.png",26,22,60,100))
adm_fleet.append(("1648237669367.png",35,57,16,100))
adm_fleet.append(("1594472243567.png",63,40,23,100))
adm_fleet.append(("1595311081721.png",60,37,29,100))
adm_fleet.append(("1594228063164.png",73,24,20,100))
adm_fleet.append(("1594228085881.png",73,20,24,100))
adm_fleet.append(("1594228106039.png",77,20,20,100))
adm_fleet.append(("1594228139052.png",22,66,29,100))
adm_fleet.append(("1596439206417.png",64,29,33,100))
adm_fleet.append(("1613803116649.png",26,68,32,100))
adm_fleet.append(("1594277694659.png",26,66,25,100))
adm_fleet.append(("1613100034429.png",30,66,30,100))
adm_fleet.append(("1595507667524.png",34,32,60,100))
adm_fleet.append(("1595920142914.png",22,70,25,100))
adm_fleet.append(("1594646478789.png",22,60,44,100))
adm_fleet.append(("1595920229939.png",35,75,16,100))
adm_fleet.append(("1594277756925.png",31,62,33,100))
adm_fleet.append(("1594532797752.png",70,36,20,100))
adm_fleet.append(("1595999429483.png",74,24,28,100))
adm_fleet.append(("1613803024019.png",67,41,18,100))
rnd_completeImg = Pattern("rnd_completeImg.png").similar(0.91)
rnd_noslot = Pattern("rnd_noslots.png").similar(0.98)
rnd_startTask = Pattern("rnd_startTask.png").similar(0.90)
rnd_button = Pattern("rnd_button.png").similar(0.90).targetOffset(351,-1)
rnd_canIcon = Pattern("rnd_canIcon.png").similar(0.95)
rnd_beaIcon = Pattern("rnd_beaIcon.png").similar(0.90)
rnd_groIcon = Pattern("rnd_groIcon.png").similar(0.90)
rnd_kitIcon = Pattern("rnd_kitIcon.png").similar(0.90)
rnd_engIcon = Pattern("rnd_engIcon.png").similar(0.90)
rnd_proIcon = Pattern("rnd_proIcon.png").similar(0.95)
rnd_sciIcon = Pattern("rnd_sciIcon.png").similar(0.90)
rnd_shiIcon = Pattern("rnd_shiIcon.png").similar(0.90)
rnd_canStartImg = Pattern("rnd_canStartImg.png").targetOffset(399,64)
rnd_engStartImg = Pattern("rnd_engStartImg.png").targetOffset(385,76)
rnd_groStartImg = Pattern("rnd_groStartImg.png").targetOffset(364,77)
rnd_kitStartImg = Pattern("rnd_kitStartImg.png").targetOffset(353,76)
rnd_proStartImg = Pattern("rnd_proStartImg.png").targetOffset(385,69)
rnd_sciStartImg = Pattern("rnd_sciStartImg.png").targetOffset(402,66)
rnd_shiStartImg = Pattern("rnd_shiStartImg.png").targetOffset(395,69)
rnd_beaStartImg = Pattern("rnd_beaStartImg.png").targetOffset(399,67)
rnds = []
rnds.append((rnd_beaIcon, rnd_beaStartImg))
rnds.append((rnd_canIcon, rnd_canStartImg))
rnds.append((rnd_engIcon, rnd_engStartImg))
rnds.append((rnd_groIcon, rnd_groStartImg))
rnds.append((rnd_kitIcon, rnd_kitStartImg))
rnds.append((rnd_proIcon, rnd_proStartImg))
rnds.append((rnd_sciIcon, rnd_sciStartImg))
rnds.append((rnd_shiIcon, rnd_shiStartImg))
rnd_frl = Pattern("rnd_frl.png").targetOffset(483,68)
rep_click_btn = Pattern("rep_click_btn.png").similar(0.85).targetOffset(314,-1)
rep_first_rep = Pattern("rep_first_rep.png").similar(0.89)
rep_disc = Pattern("rep_disc.png").similar(0.90)
rep_omega = Pattern("rep_omega.png").similar(0.90)
rep_nukara = Pattern("rep_nukara.png").similar(0.90)
rep_romulus = Pattern("rep_romulus.png").similar(0.90)
rep_dyson = Pattern("rep_dyson.png").similar(0.90)
rep_8472 = Pattern("rep_8472.png").similar(0.90)
rep_delta = Pattern("rep_delta.png").similar(0.91)
rep_iconian = Pattern("rep_iconian.png").similar(0.90)
rep_terran = Pattern("rep_terran.png").similar(0.90)
rep_temporal = Pattern("rep_temporal.png").similar(0.90)
rep_lukari = Pattern("rep_lukari.png").similar(0.90)
rep_comp = Pattern("rep_comp.png").similar(0.90)
rep_gamma = Pattern("rep_gamma.png").similar(0.91)
rep_collectImg = Pattern("rep_collectImg.png").similar(0.90)
rep_selectImg = Pattern("rep_selectImg.png").similar(0.90)
rep_upgrade = Pattern("rep_upgrade.png").similar(0.88)
rep_fill_all = Pattern("rep_fill_all.png").similar(0.90)
rep_fill_yes = Pattern("rep_fill_yes.png").similar(0.90).targetOffset(-3,80)
rep_disc_daily = Pattern("rep_disc_daily.png").targetOffset(295,283)
rep_omega_daily = Pattern("rep_omega_daily.png").targetOffset(224,306)
rep_nukara_daily = Pattern("rep_nukara_daily.png").targetOffset(202,272)
rep_romulus_daily = Pattern("rep_romulus_daily.png").targetOffset(223,273)
rep_dyson_daily = Pattern("rep_dyson_daily.png").targetOffset(318,265)
rep_8472_daily = Pattern("rep_8472_daily.png").targetOffset(289,270)
rep_delta_daily = Pattern("rep_delta_daily.png").targetOffset(302,261)
rep_iconian_daily = Pattern("rep_iconian_daily.png").targetOffset(283,280)
rep_terran_daily = Pattern("rep_terran_daily.png").targetOffset(293,279)
rep_temporal_daily = Pattern("rep_temporal_daily.png").targetOffset(257,279)
rep_lukari_daily = Pattern("rep_lukari_daily.png").targetOffset(247,279)
rep_comp_daily = Pattern("rep_comp_daily.png").targetOffset(271,277)
rep_comp_convert = Pattern("rep_comp_convert.png").targetOffset(261,213)
rep_gamma_daily = Pattern("rep_gamma_daily.png").targetOffset(280,275)
reps = []
reps.append((rep_first_rep, rep_disc_daily))
reps.append((rep_omega, rep_omega_daily))
reps.append((rep_nukara, rep_nukara_daily))
reps.append((rep_romulus, rep_romulus_daily))
reps.append((rep_dyson, rep_dyson_daily))
reps.append((rep_8472, rep_8472_daily))
reps.append((rep_delta, rep_delta_daily))
reps.append((rep_iconian, rep_iconian_daily))
reps.append((rep_terran, rep_terran_daily))
reps.append((rep_temporal, rep_temporal_daily))
reps.append((rep_lukari, rep_lukari_daily))
reps.append((rep_comp, rep_comp_daily))
reps.append((rep_gamma, rep_gamma_daily))
disconnectImg = Pattern("disconnectImg.png").similar(0.95).targetOffset(106,-5)
passwordImg = Pattern("passwordImg.png").similar(0.90).targetOffset(218,26)
loginImg = Pattern("loginImg.png").similar(0.72).targetOffset(223,26)
loginBtn = "loginBtn.png"
playImg = "playImg.png"
noSlotsImg = Pattern("noSlotsImg.png").similar(0.96)
scrollImg = Pattern("scrollImg.png").similar(0.93).targetOffset(0,-5)

scrollUpImg = Pattern("scrollUpImg.png").similar(0.92).targetOffset(1,-12)
doffBtn = Pattern("doffBtn.png").similar(0.90).targetOffset(171,1)
departmentImg = Pattern("departmentImg.png").similar(0.90)
completedImg = Pattern("completedImg.png").similar(0.90)
collectImg = Pattern("collectImg.png").similar(0.86)
ScienceImg = Pattern("ScienceImg.png").similar(0.90).targetOffset(134,2)
TacticalImg = Pattern("TacticalImg.png").similar(0.90).targetOffset(140,-1)
MedicalImg = Pattern("MedicalImg.png").similar(0.90).targetOffset(139,1)
EngineeringImg = Pattern("EngineeringImg.png").similar(0.90).targetOffset(124,0)
OperationsImg = Pattern("OperationsImg.png").similar(0.91).targetOffset(127,2)
SecurityImg = Pattern("SecurityImg.png").similar(0.90).targetOffset(134,1)
FirstOffImg = Pattern("FirstOffImg.png").similar(0.90).targetOffset(220,-2)
PersonalImg = Pattern("PersonalImg.png").similar(0.90)
FiltersImg = Pattern("FiltersImg.png").similar(0.89)
FiltersListImg = Pattern("FiltersListImg.png").similar(0.88).targetOffset(-97,10)
HoverOn = "HoverOn.png"
pressImg = Pattern("pressImg.png").similar(0.90)
beginImg = Pattern("beginImg.png").similar(0.90)
completedPageImg = "completedPageImg.png"
unavailableImg = []
unavailableImg.append(Pattern("1591176370603.png").similar(0.93))
unavailableImg.append(Pattern("1591176419179.png").similar(0.94))
unavailableImg.append(Pattern("1591183849017.png").similar(0.85))
logoutImg = Pattern("logoutImg.png").similar(0.91)
logout2Img = Pattern("logout2Img.png").similar(0.90).targetOffset(-34,20)

whitelist = []
ERROR = []
#Science
whitelist.append((Pattern("1591290657013.png").targetOffset(331,31),1,"science"))
whitelist.append((Pattern("1591457990795.png").targetOffset(222,33),20,"science"))
whitelist.append((Pattern("1591290680873.png").targetOffset(239,35),20,"science"))
whitelist.append((Pattern("1591290778988.png").targetOffset(274,28),8,"science"))
whitelist.append((Pattern("1591290793278.png").targetOffset(257,30),4,"science"))
whitelist.append((Pattern("1591324622339.png").targetOffset(346,28),4,"science"))
#whitelist.append((Pattern("1591290809143.png").targetOffset(298,28),20,"science")) #-MAT
whitelist.append((Pattern("1591324666165.png").targetOffset(297,29),4,"science"))
whitelist.append((Pattern("1591458023331.png").targetOffset(207,28),4,"science"))
whitelist.append((Pattern("1591290823297.png").targetOffset(345,33),6,"science"))
whitelist.append((Pattern("1591290841609.png").targetOffset(288,28),2,"science"))
whitelist.append((Pattern("1591290853884.png").targetOffset(359,30),6,"science"))
whitelist.append((Pattern("1591458104564.png").targetOffset(327,29),72,"science"))
whitelist.append((Pattern("1591290867026.png").targetOffset(311,33),2,"science"))
whitelist.append((Pattern("1591290880165.png").targetOffset(255,27),4,"science"))
whitelist.append((Pattern("1591290892645.png").targetOffset(304,31),1,"science"))
#whitelist.append((Pattern("1591290912874.png").targetOffset(315,30),8,"science"))
whitelist.append((Pattern("1591324712122.png").targetOffset(374,35),8,"science"))
whitelist.append((Pattern("1591290935753.png").targetOffset(379,30),1,"science"))
whitelist.append((Pattern("1591290946196.png").targetOffset(283,30),8,"science"))
whitelist.append((Pattern("1591290964417.png").targetOffset(332,31),4,"science"))
whitelist.append((Pattern("1591290973548.png").targetOffset(299,29),2,"science"))
whitelist.append((Pattern("1591290983409.png").targetOffset(293,26),8,"science"))
whitelist.append((Pattern("1591547363786.png").targetOffset(254,33),6,"science"))
#Exploration
whitelist.append((Pattern("1591290998355.png").targetOffset(240,31),6,"science"))
whitelist.append((Pattern("1591291012065.png").targetOffset(283,26),20,"science"))
whitelist.append((Pattern("1591458311306.png").targetOffset(263,26),6,"science"))
whitelist.append((Pattern("1591353313543.png").targetOffset(319,30),4,"science"))
whitelist.append((Pattern("1591291023361.png").targetOffset(383,27),4,"science"))
whitelist.append((Pattern("1591458361826.png").targetOffset(259,30),6,"science"))
whitelist.append((Pattern("1591291034757.png").targetOffset(371,33),1,"science"))
whitelist.append((Pattern("1591291044033.png").targetOffset(385,34),3,"science"))
whitelist.append((Pattern("1591458394988.png").targetOffset(230,27),6,"science"))
whitelist.append((Pattern("1591458436636.png").targetOffset(225,33),6,"science"))
whitelist.append((Pattern("1591324747163.png").targetOffset(262,33),6,"science"))
whitelist.append((Pattern("1591458467513.png").targetOffset(252,31),6,"science"))
whitelist.append((Pattern("1591458503793.png").targetOffset(222,27),6,"science"))
whitelist.append((Pattern("1591547439181.png").targetOffset(215,29),6,"science"))
whitelist.append((Pattern("1591291061865.png").targetOffset(252,30),4,"science"))
whitelist.append((Pattern("1591891763168.png").targetOffset(365,29),3,"science"))
whitelist.append((Pattern("1591547485731.png").targetOffset(354,31),8,"science"))
whitelist.append((Pattern("1591291104481.png").targetOffset(272,27),2,"science"))
whitelist.append((Pattern("1591458573573.png").targetOffset(231,33),20,"science"))
whitelist.append((Pattern("1591547538405.png").targetOffset(304,31),8,"science"))
whitelist.append((Pattern("1591291119885.png").targetOffset(279,29),4,"science"))
whitelist.append((Pattern("1591324787827.png").targetOffset(285,29),4,"science"))
whitelist.append((Pattern("1591291145545.png").targetOffset(343,34),8,"science"))
whitelist.append((Pattern("1591291157609.png").targetOffset(300,32),8,"science"))
whitelist.append((Pattern("1591291168085.png").targetOffset(222,32),6,"science"))
whitelist.append((Pattern("1591291180418.png").targetOffset(262,26),4,"science"))
whitelist.append((Pattern("1591291193176.png").targetOffset(286,30),3,"science"))
whitelist.append((Pattern("1591291205826.png").targetOffset(240,30),6,"science"))
whitelist.append((Pattern("1591291217340.png").targetOffset(221,27),6,"science"))
#Medical
whitelist.append((Pattern("1591291238327.png").targetOffset(326,31),0,"medical"))
whitelist.append((Pattern("1591324567162.png").targetOffset(320,32),1,"medical"))
whitelist.append((Pattern("1591291249850.png").targetOffset(303,26),2,"medical"))
whitelist.append((Pattern("1591291260827.png").targetOffset(237,31),4,"medical"))
whitelist.append((Pattern("1591291271177.png").targetOffset(275,29),3,"medical"))
whitelist.append((Pattern("1591291281154.png").targetOffset(286,29),3,"medical"))
whitelist.append((Pattern("1591291290425.png").targetOffset(263,30),3,"medical"))
whitelist.append((Pattern("1591291302190.png").targetOffset(293,34),3,"medical"))
whitelist.append((Pattern("1591291311861.png").targetOffset(274,33),3,"medical"))
whitelist.append((Pattern("1591291332899.png").targetOffset(350,30),0,"medical"))
whitelist.append((Pattern("1591291344345.png").targetOffset(368,30),1,"medical"))
whitelist.append((Pattern("1591291358697.png").targetOffset(336,33),0,"medical"))
whitelist.append((Pattern("1591458626739.png").targetOffset(316,32),2,"medical"))
whitelist.append((Pattern("1591291371097.png").targetOffset(301,33),20,"medical"))
whitelist.append((Pattern("1591291383869.png").targetOffset(329,28),20, "medical"))
whitelist.append((Pattern("1591291393277.png").targetOffset(347,29),20,"medical"))
whitelist.append((Pattern("1591458664154.png").targetOffset(308,36),6,"medical"))
whitelist.append((Pattern("1591291403366.png").targetOffset(291,32),20, "medical"))
whitelist.append((Pattern("1591291412696.png").targetOffset(290,24),20, "medical"))
whitelist.append((Pattern("1591324521605.png").targetOffset(283,31),20,"medical"))
whitelist.append((Pattern("1591291422102.png").targetOffset(306,25),20, "medical"))
whitelist.append((Pattern("1591291432494.png").targetOffset(285,28),20, "medical"))
whitelist.append((Pattern("1592061079513.png").targetOffset(378,31),4,"medical"))
whitelist.append((Pattern("1591324469922.png").targetOffset(355,30),20,"medical"))
whitelist.append((Pattern("1591458722475.png").targetOffset(418,35),4,"medical"))
whitelist.append((Pattern("1591883826892.png").targetOffset(317,31),6,"medical"))
whitelist.append((Pattern("1591673567282.png").targetOffset(363,34),2,"medical"))
whitelist.append((Pattern("1591458750995.png").targetOffset(407,34),1,"medical"))
whitelist.append((Pattern("1591291443645.png").targetOffset(375,31),0,"medical"))
whitelist.append((Pattern("1591291456825.png").targetOffset(393,32),1,"medical"))
whitelist.append((Pattern("1591291470748.png").targetOffset(379,29),1,"medical"))
whitelist.append((Pattern("1591324412658.png").targetOffset(398,29),1,"medical"))
whitelist.append((Pattern("1591291480499.png").targetOffset(391,29),0,"medical"))
whitelist.append((Pattern("1591291491578.png").targetOffset(414,30),0,"medical"))
whitelist.append((Pattern("1591291504842.png").targetOffset(379,30),0,"medical"))
#Military
whitelist.append((Pattern("1591291531571.png").targetOffset(278,31),20, "tactical"))
whitelist.append((Pattern("1591291542626.png").targetOffset(341,29),4, "tactical"))
whitelist.append((Pattern("1591291555198.png").targetOffset(372,28),4, "tactical"))
whitelist.append((Pattern("1591291566968.png").targetOffset(293,32),6, "tactical"))
whitelist.append((Pattern("1591458825506.png").targetOffset(262,28),6,"tactical"))
whitelist.append((Pattern("1591458851850.png").targetOffset(269,31),6,"tactical"))
whitelist.append((Pattern("1591458881250.png").targetOffset(325,33),20,"tactical"))
whitelist.append((Pattern("1591458910635.png").targetOffset(336,26),6,"tactical"))
whitelist.append((Pattern("1591291596496.png").targetOffset(375,30),4, "tactical"))
#Espionage
whitelist.append((Pattern("1591291607465.png").targetOffset(429,31),20, "tactical"))
whitelist.append((Pattern("1591291623873.png").targetOffset(370,31),8, "tactical"))
whitelist.append((Pattern("1591324833530.png").targetOffset(388,25),20,"tactical"))
whitelist.append((Pattern("1591291639409.png").targetOffset(434,34),1, "tactical")) #48 hours, but gives doffs
whitelist.append((Pattern("1591458962986.png").targetOffset(407,30),20,"tactical"))
whitelist.append((Pattern("1591291653073.png").targetOffset(315,34),8, "tactical"))
whitelist.append((Pattern("1591459012837.png").targetOffset(366,33),1,"tactical"))
whitelist.append((Pattern("1591459055961.png").targetOffset(380,28),20,"tactical"))
whitelist.append((Pattern("1591324870666.png").targetOffset(395,34),20,"tactical"))

#Engineering
whitelist.append((Pattern("1591291666811.png").targetOffset(307,25),6, "engineering"))
whitelist.append((Pattern("1591291678313.png").targetOffset(304,28),8, "engineering"))
whitelist.append((Pattern("1591459757525.png").targetOffset(390,29),2,"engineering"))
whitelist.append((Pattern("1591291688106.png").targetOffset(339,28),6, "engineering"))
whitelist.append((Pattern("1591369326170.png").targetOffset(286,31),1,"engineering"))
whitelist.append((Pattern("1591291699393.png").targetOffset(417,28),4, "engineering"))
whitelist.append((Pattern("1591514859193.png").targetOffset(333,29),1,"engineering")) #8 hours
whitelist.append((Pattern("1591678146412.png").targetOffset(362,26),1,"engineering"))
whitelist.append((Pattern("1591971465687.png").targetOffset(384,29),1,"engineering"))
whitelist.append((Pattern("1591291710128.png").targetOffset(348,29),1, "engineering"))
whitelist.append((Pattern("1591291722054.png").targetOffset(371,29),1, "engineering"))
whitelist.append((Pattern("1591514907063.png").targetOffset(351,29),1,"engineering"))
whitelist.append((Pattern("1591291741043.png").targetOffset(343,32),1, "engineering"))
whitelist.append((Pattern("1592129921844.png").similar(0.78).targetOffset(345,40),1,"engineering"))
whitelist.append((Pattern("1591514952297.png").targetOffset(344,34),1,"engineering"))
whitelist.append((Pattern("1591609931924.png").targetOffset(385,35),1,"engineering"))
whitelist.append((Pattern("1591291751258.png").targetOffset(345,28),1, "engineering"))
whitelist.append((Pattern("1591291761412.png").targetOffset(357,32),1, "engineering"))
whitelist.append((Pattern("1591291782442.png").targetOffset(367,29),1, "engineering"))
whitelist.append((Pattern("1591291795865.png").targetOffset(363,28),1, "engineering"))
whitelist.append((Pattern("1591459797193.png").targetOffset(341,33),1,"engineering"))
whitelist.append((Pattern("1591325023323.png").targetOffset(305,29),1,"engineering"))
whitelist.append((Pattern("1591459853610.png").targetOffset(313,31),1,"engineering"))
ERROR.append(("1591459829210.png",6,"engineering"))
whitelist.append((Pattern("1591547791890.png").targetOffset(315,26),0,"engineering"))
ERROR.append(("1591459883490.png",20,"engineering"))
whitelist.append((Pattern("1591459920571.png").targetOffset(313,31),20,"engineering"))
#Colonial
whitelist.append((Pattern("1591459098393.png").targetOffset(207,32),20,"operations"))
whitelist.append((Pattern("1595920409662.png").targetOffset(342,32),3,"operations"))
whitelist.append((Pattern("1591459168241.png").targetOffset(433,32),4,"operations"))
whitelist.append((Pattern("1591324923234.png").targetOffset(292,29),0,"operations"))
whitelist.append((Pattern("1591324963213.png").targetOffset(297,31),0,"operations"))
whitelist.append((Pattern("1591891921330.png").targetOffset(275,32),0,"operations"))
whitelist.append((Pattern("1591291808492.png").targetOffset(287,30),0, "operations"))
whitelist.append((Pattern("1591459206041.png").targetOffset(256,27),0,"operations"))
whitelist.append((Pattern("1591610092009.png").targetOffset(279,32),0,"operations"))
whitelist.append((Pattern("1591459234292.png").targetOffset(284,30),0,"operations"))
whitelist.append((Pattern("1591459269410.png").targetOffset(273,26),0,"operations"))
whitelist.append((Pattern("1591883911646.png").targetOffset(285,28),0,"operations"))
whitelist.append((Pattern("1591522583365.png").targetOffset(301,28),0,"operations"))
whitelist.append((Pattern("1591464761838.png").targetOffset(295,29),0,"operations"))

#Development
whitelist.append((Pattern("1591547632899.png").targetOffset(255,31),72,"engineering"))
whitelist.append((Pattern("1591464796409.png").targetOffset(320,30),4,"operations"))
whitelist.append((Pattern("1591522634827.png").targetOffset(364,28),8,"operations"))
whitelist.append((Pattern("1591498703651.png").targetOffset(485,34),4,"operations"))
whitelist.append((Pattern("1591498749352.png").targetOffset(432,31),4,"operations"))
whitelist.append((Pattern("1591514806151.png").targetOffset(335,31),8,"operations"))
whitelist.append((Pattern("1591522672052.png").targetOffset(319,33),8,"operations"))
whitelist.append((Pattern("1591610152596.png").targetOffset(359,26),8,"operations"))
whitelist.append((Pattern("1591464847658.png").targetOffset(401,29),6,"operations"))
whitelist.append((Pattern("1591464879583.png").targetOffset(358,33),20,"operations"))

#Diplomacy
whitelist.append((Pattern("1591622572609.png").targetOffset(394,32),6,"first"))
#Personal
whitelist.append((Pattern("1591522714051.png").targetOffset(309,27),6,"personal"))
whitelist.append((Pattern("1591498810252.png").targetOffset(351,34),4,"personal"))
whitelist.append((Pattern("1592016448953.png").targetOffset(370,31),6,"personal"))
whitelist.append((Pattern("1591883696836.png").targetOffset(273,29),6,"personal"))
whitelist.append((Pattern("1591498919703.png").targetOffset(373,31),4,"personal"))
whitelist.append((Pattern("1593157337888.png").targetOffset(378,27),6,"personal")) 
whitelist.append((Pattern("1592451509898.png").targetOffset(310,32),4,"personal"))
whitelist.append((Pattern("1591503016077.png").targetOffset(285,36),2,"personal"))
whitelist.append((Pattern("1592144017339.png").targetOffset(337,31),2,"personal"))
whitelist.append((Pattern("1591691823258.png").targetOffset(363,30),2,"personal"))
whitelist.append((Pattern("1591503361290.png").targetOffset(385,31),2,"personal"))
whitelist.append((Pattern("1591503278420.png").targetOffset(367,31),2,"personal"))
whitelist.append((Pattern("1591515088350.png").targetOffset(366,34),2,"personal"))
whitelist.append((Pattern("1591626691078.png").targetOffset(381,31),4,"personal"))
whitelist.append((Pattern("1591547115580.png").targetOffset(355,30),8,"personal"))
whitelist.append((Pattern("1592488850517.png").targetOffset(285,32),4,"personal"))
whitelist.append((Pattern("1591464984903.png").targetOffset(364,30),0,"personal"))
whitelist.append((Pattern("1591610026549.png").targetOffset(273,31),0,"personal"))
whitelist.append((Pattern("1591890157895.png").targetOffset(441,28),8,"personal"))
whitelist.append((Pattern("1591678034119.png").targetOffset(429,32),4,"personal"))
whitelist.append((Pattern("1591515120886.png").targetOffset(398,32),6,"personal"))
whitelist.append((Pattern("1591691915077.png").targetOffset(369,28),4,"personal"))
whitelist.append((Pattern("1591503138356.png").targetOffset(329,30),2,"personal"))
whitelist.append((Pattern("1592016547855.png").targetOffset(329,31),2,"personal"))
whitelist.append((Pattern("1591522756091.png").targetOffset(338,30),2,"personal"))
whitelist.append((Pattern("1591890118926.png").targetOffset(394,34),2,"personal"))
whitelist.append((Pattern("1591522844277.png").targetOffset(357,32),6,"personal"))
whitelist.append((Pattern("1591622752665.png").targetOffset(362,30),4,"personal"))
whitelist.append((Pattern("1591522783789.png").targetOffset(330,25),4,"personal")) 
whitelist.append((Pattern("1591626647541.png").targetOffset(344,32),2,"personal"))
whitelist.append((Pattern("1591547162947.png").targetOffset(363,33),4,"personal"))
whitelist.append((Pattern("1591890079750.png").targetOffset(361,33),4,"personal"))
whitelist.append((Pattern("1592451462643.png").targetOffset(371,31),4,"personal"))
whitelist.append((Pattern("1592061161977.png").targetOffset(333,26),4,"personal"))
whitelist.append((Pattern("1591514993015.png").targetOffset(387,33),4,"personal"))
whitelist.append((Pattern("1591696101174.png").targetOffset(383,32),2,"personal"))
whitelist.append((Pattern("1591503314483.png").targetOffset(297,25),6,"personal"))
whitelist.append((Pattern("1591883581963.png").targetOffset(334,26),4,"personal"))
whitelist.append((Pattern("1591547026410.png").targetOffset(288,27),1,"personal"))
whitelist.append((Pattern("1591626730947.png").targetOffset(360,28),6,"personal"))
whitelist.append((Pattern("1591678073099.png").targetOffset(372,30),4,"personal"))
whitelist.append((Pattern("1591696149141.png").targetOffset(299,29),4,"personal"))
whitelist.append((Pattern("1591547266307.png").targetOffset(287,32),4,"personal"))
whitelist.append((Pattern("1593153010425.png").targetOffset(377,33),6,"personal"))
whitelist.append((Pattern("1591691867106.png").targetOffset(366,31),8,"personal"))
whitelist.append((Pattern("1591609977805.png").targetOffset(329,31),2,"personal"))
whitelist.append((Pattern("1591515046895.png").targetOffset(362,31),4,"personal"))
whitelist.append((Pattern("1591503182650.png").targetOffset(421,37),4,"personal"))
whitelist.append((Pattern("1591464919801.png").targetOffset(311,26),4,"personal"))
whitelist.append((Pattern("1591498885739.png").targetOffset(424,32),0,"personal"))
whitelist.append((Pattern("1591883746820.png").targetOffset(390,28),0,"personal"))
whitelist.append((Pattern("1591547073675.png").targetOffset(383,29),0,"personal"))
whitelist.append((Pattern("1592016488599.png").targetOffset(285,31),6,"personal"))
whitelist.append((Pattern("1591503241722.png").targetOffset(384,31),8,"personal"))
whitelist.append((Pattern("1592896149799.png").targetOffset(361,29),6,"personal"))
whitelist.append((Pattern("1591971380279.png").targetOffset(296,28),6,"science"))
whitelist.append((Pattern("1591522816927.png").targetOffset(377,29),8,"personal"))
whitelist.append((Pattern("1595137576406.png").targetOffset(419,31),48,"personal"))

tod_running = [[False,adm_fed,0], [False,adm_kdf,1], [False,adm_rom,2], [False,adm_fer,3]]
adm_slot = False
adm_started = 1
adm_slot_img = "adm_slot_img.png"
exitImg = "exitImg.png"
exitOk = Pattern("exitOk.png").targetOffset(-42,12)
playImgArc = "playImgArc.png"
engageImg = "engageImg.png"
maintenance = "maintenance.png"
closeSto = Pattern("closeSto.png").targetOffset(715,-2)
moreImg = Pattern("moreImg.png").similar(0.85).targetOffset(15,1)
moreList = Pattern("moreList.png").similar(0.85).targetOffset(-34,9)
bridgeImg = Pattern("bridgeImg.png").targetOffset(0,16)
welcomeImg = Pattern("welcomeImg.png").targetOffset(640,-2)
def ToBridge():
    if exists(moreImg):
        click(moreImg)
        wait(2)
    if exists(moreList):
        click(moreList)
        wait(5)
    if exists(bridgeImg):
        click(bridgeImg)
        wait(5)
        for i in range(5):
            if exists(HoverOn):
                break
            else:
                wait(10)
imgRoster = "imgRoster.png"
def Unstuck():
    if not exists(imgRoster):
        if not exists(adm_button):
            type("P")
        else:
            click(adm_button)
def PatchGame():
    global adm_filters_set
    adm_filters_set = False
    SafeClick(exitImg)
    wait(10)
    SafeClick(exitOk)
    wait(50)
    App.open("C:\\Program Files (x86)\\Star Trek Online_en\\Star Trek Online.exe")
    wait(120)
    if exists(maintenance):
        SafeClick(closeSto)
        wait(60*30)
        PatchGame()
    if not exists(engageImg):
        wait(60*15)
    SafeClick(engageImg)
    wait(60*5)
def CheckTOD():
    Unstuck()
    if exists(TOD_fed):
        tod_running[0][0] = True
    if exists(TOD_kdf):
        tod_running[1][0] = True
    if exists(TOD_rom):
        tod_running[2][0] = True
    if exists(TOD_fer):
        tod_running[3][0] = True
def CheckCompletedAdm(recursion = False):
    global adm_slot
    global tod_running
    if not recursion:
        adm_slot = False
        tod_running[0][0] = False
        tod_running[1][0] = False
        tod_running[2][0] = False
        tod_running[3][0] = False
    SafeClick(adm_button)
    while exists(adm_complete1):
        if exists(adm_complete1):
            click(adm_complete1)
            adm_slot = True
            wait(7)
    while exists(adm_complete2):
        if exists(adm_complete2):
            click(adm_complete2)
            adm_slot = True
            wait(7)
    if exists(adm_slot_img):
        adm_slot = True
    CheckTOD()
    if exists(scrollImg):
        MouseHold(scrollImg)
        CheckCompletedAdm(True)
    else:
        if exists(scrollUpImg):
            MouseHold(scrollUpImg)
tierFilterImg = "tierFilterImg.png"
tierFilterImg2 = "tierFilterImg2.png"
tier0Img = Pattern("tiers0Img.png").targetOffset(-50,-1)
tier1Img = Pattern("tier1Img.png").targetOffset(-31,1)
tier2Img = Pattern("tier2Img.png").targetOffset(-28,0)
tier3Img = Pattern("tier3Img.png").targetOffset(-30,3)
tier4Img = Pattern("tier4Img.png").targetOffset(-29,2)
tier5Img = Pattern("tier5Img.png").targetOffset(-29,0)
tier6Img = Pattern("tier6Img.png").targetOffset(-30,1)
tierEmpty = "tierEmpty.png"
tiersResettedImg = Pattern("tiersResettedImg.png").similar(0.90)
adm_filters_set = False
def AdmSetFilter():
    global adm_filters_set
    if adm_filters_set:
        return
    SafeClick(tierFilterImg)
    while exists(tierEmpty):
        MouseHold(tierEmpty)
    if not exists(tiersResettedImg):
        SafeClick(tierFilterImg2)
        adm_filters_set = True
        return
    if ADM_MINIMUM_TIER >= 2:
        MouseHold(tier0Img)
        MouseHold(tier1Img)
    if ADM_MINIMUM_TIER >= 4:
        MouseHold(tier2Img)
    if ADM_MINIMUM_TIER >= 8:
        MouseHold(tier3Img)
    if ADM_MINIMUM_TIER >=12:
        MouseHold(tier4Img)
    if ADM_MINIMUM_TIER >= 18:
        MouseHold(tier5Img)
    wait(1)
    SafeClick(tierFilterImg2)
    adm_filters_set = True
    ScrollUp()
def AdmGetAvailableShips(tod = False):
    global adm_started
    ids = []
    SafeClick(adm_select1)
    AdmSetFilter()
    if tod:
        ships = adm_ships
    else:
        ships = adm_fleet
    done = False
    scroll_count = 0
    ScrollUp()
    while exists(scrollImg) or not done:
        for i in range(len(ships)):
            if i in ids:
                continue
            if ships[i][4] < ADM_MINIMUM_TIER:
                continue
            if exists(ships[i][0]):
                ids.append(i)
        if exists(scrollImg) and scroll_count < 30:
            MouseHold(scrollImg)
        else:
            done = True
    SafeClick(adm_close_ships)
    if CheckConnection() == 0:
                return
    return ids
def AdmGetBestThree(tod = False):
    global ship_ids
    global last_ship_scan
    if (not tod) and (time.time() - last_ship_scan > 10800):
        ship_ids = AdmGetAvailableShips(tod)
        last_ship_scan = time.time()
    ids = ship_ids
    if tod:
        ids = AdmGetAvailableShips(tod)
    max_ids = [-1,-1,-1]
    if ids is None:
        return max_ids
    if tod:
        ships = adm_ships
    else:
        ships = adm_fleet
    for div in [1,2,3]:
        max = 0
        for id in ids:
            if ships[id][div] > max:
                max = ships[id][div]
                max_ids[div-1] = id
        if max_ids[div-1] in ids:
            ids.remove(max_ids[div-1])
    return max_ids
def ScrollUp():
    while True:
        if exists(scrollUpImg):
            MouseHold(scrollUpImg)
        else:
            break
def CoarseAdm(faction):
    global adm_slot
    global adm_started
    global ship_ids
    allTOD = tod_running[0][0] and tod_running[1][0] and tod_running[2][0] and tod_running[3][0]
    counter = 0
    for item in adm_coarse:
        counter += 1
        if counter == 4:
            if CheckConnection() == 0:
                return
        Unstuck()
        if exists(TOD):
            return
        if exists(item):
            click(item)
            wait(2)
            if not exists(adm_select1):
                adm_slot = False
                CheckCompletedAdm()
                if adm_slot:
                    SafeClick(faction)
                    Unstuck()
                    if exists(TOD):
                        return
                    wait(2)
                    SafeClick(item)
                else:
                    return 0
            if exists(scrollUpImg):
                MouseHold(scrollUpImg,5)
            if CheckConnection() == 0:
                return
            bestShips = AdmGetBestThree(False)
            has_shuttle = False
            for sel in [adm_select1, adm_select2, adm_select3]:
                if bestShips[0] == bestShips[1] == bestShips[2] == -1:
                    break
                if exists(sel):
                    click(sel)
                    wait(2)
                    ScrollUp()
                    done = False
                    while exists(scrollImg) or not done:
                        for ind, id in enumerate(bestShips):
                            if id == -1:
                                continue
                            if exists(adm_fleet[id][0]):
                                doubleClick(adm_fleet[id][0])
                                wait(1)
                                bestShips[ind] = -1
                                has_shuttle = True
                                wait(5)
                                if adm_fleet[id][4] == 0 and allTOD:
                                    return 0
                                if exists(adm_okay_chance) or (adm_fleet[id][4] == 0):
                                    SafeClick(adm_begin)
                                    adm_started += 1
                                    for ind, id in enumerate(bestShips):
                                        if id == -1:
                                            continue
                                        ship_ids.append(id)
                                    return
                                break
                        if exists(scrollImg):
                            MouseHold(scrollImg)
                        else:
                            done = True
            wait(3)
            if not has_shuttle:
                return 0
def RunTOD(faction_index):
    global adm_slot
    Unstuck()
    SafeClick(TOD)
    if not exists(adm_select1):
        adm_slot = False
        CheckCompletedAdm()
        if adm_slot:
            SafeClick(faction_index[1])
            Unstuck()
            SafeClick(TOD)
        else:
            return 0
    best_ids = AdmGetBestThree(True)
    if best_ids[0] == best_ids[1] == best_ids[2] == -1:
        return 0
    SafeClick(adm_select1)
    wait(3)
    ScrollUp()
    if best_ids[0] != -1:
        done = False
        scroll_count = 0
        while exists(scrollImg) or not done:
            if scroll_count > 30:
                ScrollUp()
            if exists(adm_ships[best_ids[0]][0]):
                doubleClick(adm_ships[best_ids[0]][0])
                break
            else:
                if exists(scrollImg):
                    MouseHold(scrollImg)
                    scroll_count += 1
                else:
                    done = True
    else:
        found = False
        done = False
        scroll_count = 0
        while exists(scrollImg) and not found or not done:
            if scroll_count > 30:
                ScrollUp()
            for ship1 in adm_ships:
                if ship1[4] > 0 and exists(ship1[0]):
                    doubleClick(ship1[0])
                    found = True
                    break
            if exists(scrollImg):
                click(scrollImg)
                scroll_count =+ 1
            else:
                done = True
        if not found:
            return 0
    wait(5)
    if exists(adm_good_chance):
        SafeClick(adm_begin)
        tod_running[faction_index[2]][0] = True
        return
    SafeClick(adm_select2)
    wait(1)
    ScrollUp()
    if best_ids[1] != -1:
        done = False
        scroll_count = 0
        while exists(scrollImg) or not done:
            if scroll_count > 30:
                ScrollUp()
            if exists(adm_ships[best_ids[1]][0]):
                doubleClick(adm_ships[best_ids[1]][0])
                break
            else:
                if exists(scrollImg):
                    MouseHold(scrollImg)
                    scroll_count =+ 1
                else:
                    done = True
    wait(5)
    if exists(adm_good_chance):
        SafeClick(adm_begin)
        tod_running[faction_index[2]][0] = True
        return
    SafeClick(adm_select3)
    wait(1)
    ScrollUp()
    if best_ids[2] != -1:
        done = False
        scroll_count = 0
        while exists(scrollImg) or not done:
            if scroll_count > 30:
                ScrollUp()
            if exists(adm_ships[best_ids[2]][0]):
                doubleClick(adm_ships[best_ids[2]][0])
                break
            else:
                if exists(scrollImg):
                    MouseHold(scrollImg)
                    scroll_count =+ 1
                else:
                    done = True
    wait(5)
    if not exists(adm_good_chance):
        return 0
    else:
        SafeClick(adm_begin)
        tod_running[faction_index[2]][0] = True
def CheckAdm():
    global adm_slot
    global tod_running
    if exists(adm_button):
        click(adm_button)
    else:
        if not exists (passwordImg):
            type('P')
            SafeClick(adm_button)
    hover(HoverOn)
    for i in range(0,3):
        tod_running[i][0] = False
    adm_slot = False
    CheckCompletedAdm()
    if not adm_slot:
        return
    for faction_index in [3,1,0,2]:
        if tod_running[faction_index][0]:
            continue
        SafeClick(tod_running[faction_index][1])
        Unstuck()
        if exists(TOD):
            res = RunTOD(tod_running[faction_index])
            if res == 0:
                return
            if adm_slot:
                CheckAdm()
            else:
                return
        else:
            while True:
                SafeClick(tod_running[faction_index][1])
                res = CoarseAdm(tod_running[faction_index][1])
                SafeClick(tod_running[faction_index][1])
                if res == 0:
                    return   
                wait(3)
                Unstuck()
                if exists(TOD):
                    res2 = RunTOD(tod_running[faction_index])
                    if res2 == 0:
                        return
                    if adm_slot:
                        CheckAdm()
                    else:
                        CheckCompletedAdm()
                        if not adm_slot:
                            return
                if res == 0:
                    break
    allTOD = tod_running[0][0] and tod_running[1][0] and tod_running[2][0] and tod_running[3][0]
    if ADM_RUN_CONSTANTLY and allTOD:
            while True:
                SafeClick(tod_running[WHICH_ADM][1])
                res = CoarseAdm(tod_running[WHICH_ADM][1])
                SafeClick(tod_running[WHICH_ADM][1])
                if res == 0:
                    if adm_slot:
                        return
                    CheckCompletedAdm()
                if not adm_slot:
                    return
                SafeClick(tod_running[WHICH_ADM][1])
                wait(3)
def CheckRep():
    if exists(rep_click_btn):
        click(rep_click_btn)
    else:
        if CheckConnection() == 0:
                return
        type('U')
        wait(1)
        if not exists(rep_click_btn):
            type('U')
            wait(1)
        if not exists(rep_click_btn):
            return 0
        else:
            SafeClick(rep_click_btn)
    if exists(rep_first_rep):
        click(rep_first_rep)
    for rep in reps:
        if exists(rep[0]):
            click(rep[0])
            wait(3)
        if exists(rep_collectImg):
            click(rep_collectImg)
            hover(HoverOn)
            wait(3)
        if exists(rep_selectImg):
            click(rep_selectImg)
            wait(3)
        if exists(rep[1]):
            click(rep[1])
            wait(3)
            if exists(rep_fill_all):
                click(rep_fill_all)
                wait(3)
                if exists(rep_fill_yes):
                    click(rep_fill_yes)
                    wait(7)
        if False: #exists(rep_upgrade):
            click(rep_upgrade)
            wait(2)
            if exists(rep_comp_convert):
                click(rep_comp_convert)
                wait(1)
                if exists(rep_fill_all):
                    click(rep_fill_all)
                    wait(3)
                    if exists(rep_fill_yes):
                        click(rep_fill_yes)
                        wait(10)
                        SafeClick(rep_collectImg)
        if CheckConnection() == 0:
                return
    if exists(rep_click_btn):
            type('U')
def AddRndTask(icon, task):
    if exists(icon):
            click(icon)
    while exists(scrollImg):
        if exists(scrollImg):
            MouseHold(scrollImg, 5)
    if exists(task):
        click(task)
        if exists(rnd_startTask):
            click(rnd_startTask)
            wait(2)
def RndProject(schoolIcon):
    if exists(rnd_noslot):
        return 0
    if exists(schoolIcon):
        click(schoolIcon)
    else:
        return 0
    while exists(scrollImg):
        if exists(rnd_frl):
            click(rnd_frl)
            wait(2)
            if exists(rnd_startTask):
                click(rnd_startTask)
                wait(25)
                return
        if exists(scrollImg):
            MouseHold(scrollImg)
def CheckCompletedRnd():
    if exists(rnd_button):
        click(rnd_button)
    while exists(rnd_completeImg):
        if exists(rnd_completeImg):
            click(rnd_completeImg)
            wait(3)
def CheckRnd():
    CheckCompletedRnd()
    RndProject(rnds[LAB_PROJECT_SCHOOL_ID][0])
    CheckCompletedRnd()
    rnd_ids = [0,0,0,5,5,5]
    while not exists(rnd_noslot):
        if not exists(rnd_noslot):
            if len(rnd_ids) != 0:
                ind = rnd_ids.pop()
            else:
                ind = randrange(8)
            AddRndTask(rnds[ind][0], rnds[ind][1])
    
def CheckRndBeforeSlot():
    if exists(rnd_button):
        click(rnd_button)
    while exists(rnd_completeImg):
        if exists(rnd_completeImg):
            click(rnd_completeImg)
    if not exists(rnd_noslot):
        for i in range(0,3):
            AddRndTask(rnd_canIcon, rnd_canStartImg)
        for j in range(0,2):
            AddRndTask(rnd_beaIcon, rnd_beaStartImg)
        
departments = "science", "medical", "tactical", "operations", "first", "personal", "engineering", "security"
def SafeClick(img):
    if exists(img):
        click(img)
def CheckConnection():
    if exists(welcomeImg):
        type(Key.ESC)
    if exists(imgTaskbar):
        click(imgTaskbar)
        wait(5)
    if exists(disconnectImg) or exists(passwordImg):
        Login()
        return 0
def Logoff():
    type(Key.ESC)
    wait(2)
    if not exists(logoutImg):
        type(Key.ESC)
        wait(2)
    if not exists(logoutImg):
        type(Key.ESC)
        wait(2)
    if not exists(logoutImg):
        type(Key.ESC)
        wait(2)
    if exists(logoutImg):
        click(logoutImg)
        wait(2)
        if exists(logout2Img):
            click(logout2Img)
            wait(10)
chars = []
chars.append(("1613542689746.png","1613542718994.png"))
chars.append(("1613542777794.png","1613542790970.png"))
hover_choose = "hover_choose.png"
login_tries = 0
def Login(char = 0):
    global login_tries
    global adm_filters_set
    adm_filters_set = False
    if login_tries > 3:
        PatchGame()
    if exists(disconnectImg):
        click(disconnectImg)
    if exists(loginImg):
        click(loginImg)
        for i in range(10):
            type(Key.BACKSPACE)
            wait(1)
        paste(loginImg, "!!!")
    if exists(passwordImg):
        #click(passwordImg)
        #wait(5)
        #type("!!!")
        click(passwordImg)
        for i in range(10):
            type(Key.BACKSPACE)
        paste(passwordImg,"!!!")
        wait(1)
        click(loginBtn)
        wait(60)
    if exists(hover_choose):
        hover(hover_choose)
        wait(3)
    if exists(chars[char][0]):
        click(chars[char][0])
        wait(15)
    if exists(playImg):    
        click(playImg)
        login_tries = 0
        wait(60)
    else:
        wait(60*30)
        if not exists(playImg):
            login_tries += 1
            Login()
        else:
            click(playImg)
            wait(60)
    if exists(welcomeImg):
        type(Key.ESC)
    while not exists(pressImg) and exists(HoverOn):
        if not kerrat:
            ToBridge()
        if not exists(pressImg):
            type('P')
            wait(5)
        if exists(doffBtn):
            click(doffBtn)
    if CheckConnection() == 0:
        return
    SafeClick(PersonalImg)
    wait(1)
    SafeClick(FiltersImg)
    wait(1)
    SafeClick(FiltersListImg)
def CheckCompleted(dep = "science"):
    if exists(doffBtn):
        click(doffBtn)
    if exists(pressImg):
        click(pressImg)
    if exists(HoverOn):
        hover(HoverOn)
    if exists(completedImg):
        click(completedImg)
        hover(HoverOn)
        wait(5)
        while exists(collectImg):
            if exists(collectImg):
                click(collectImg)
                hover(HoverOn)
                wait(7)
    OpenDepartment(dep)
def OpenDepartment(dep):
    if exists(pressImg):
        click(pressImg)
    if exists(HoverOn):
        hover(HoverOn)
    if exists(departmentImg):    
        click(departmentImg)
    if dep == "science" :
        SafeClick(ScienceImg)
    if dep == "medical":
        SafeClick(MedicalImg)
    if dep == "tactical":
        SafeClick(TacticalImg)
    if dep == "security":
        SafeClick(SecurityImg)
    if dep == "engineering":
        SafeClick(EngineeringImg)
    if dep == "operations":
        SafeClick(OperationsImg)
    if dep == "first":
        SafeClick(FirstOffImg)
    if dep == "personal":
        SafeClick(PersonalImg)
    wait(10)
def MouseHold(img, duration = .5):
    hover(img)
    mouseDown(Button.LEFT)
    wait(duration)
    mouseUp(Button.LEFT)
def FindJob(job):
    SafeClick(job)
    wait(3)
    SafeClick(beginImg)
    if exists(HoverOn):
        hover(HoverOn)
def StartDoff(maxLen):
    if not exists(doffBtn):
        type("P")
    if exists(doffBtn):
        click(doffBtn)
    if exists(noSlotsImg):
        hover(noSlotsImg)
        return
    if exists(pressImg):
        click(pressImg)
        if exists(HoverOn):
            hover(HoverOn)
    for dep in departments:
        if exists(completedPageImg):
            SafeClick(doffBtn)
            CheckCompleted()
            OpenDepartment(dep)
        OpenDepartment(dep)
        if exists(HoverOn):
            hover(HoverOn)
        scroll_count = 3
        while scroll_count > 0:
            found = 0
            for job in whitelist:
                if job[1] > maxLen or job[2] != dep:
                    continue
                if exists(job[0]):
                    reg = find(job[0])
                    valid = True
                    #for img in unavailableImg:
                        #if reg.exists(img):
                            #reg.highlight(10)
                            #reg.exists(img).highlight(10)
                            #valid = False
                    if valid:
                        FindJob(job[0])
                        wait(2)
                        if exists(noSlotsImg):
                            CheckCompleted(dep)
                            if exists(noSlotsImg):
                                hover(noSlotsImg)
                                return
                        found += 1
                        scroll_count = 3
            if found == 0:
                scroll_count -= 1
                if exists(scrollImg):
                    MouseHold(scrollImg)
                    wait(1)
                else:
                    scroll_count = 0
missionWnd = Pattern("missionWnd.png").targetOffset(-135,4)
def CheckDailyMission():
    if exists(vintrax):
        click(vintrax)
        wait(1)
        type(Key.UP)
        type("F")
        wait(5)
        type(Key.ESC)
        wait(1)
    if not exists(missionWnd):
        type("J")
        wait(2)
    if not exists(missionWnd):
        return
    click(missionWnd)
    wait(3)
    while exists(scrollImg):
        MouseHold(scrollImg)
        if not exists(scrollImg):
            break
    names = ['Arena', 'Kerrat', 'Capture']
    indx = -1
    for mission in dailies:
        indx =+ 1
        if exists(mission):
            doubleClick(mission)
            wait(2)
            type(Key.UP)
            wait(1)
            type("F")
            wait(5)
            type(Key.ESC)
            with open("C:\\Users\\Jet\\Desktop\\DailyLog.txt", "a") as myfile:
                myfile.write(str(datetime.now())[:-10]+" "+names[indx]+" taken.\n")
                myfile.close()
            break
    wait(2)
    if exists(missionWnd):
        type("J")
wait(5)
lastDailyCheck = time.time()

def CheckAlt():
    global adm_filters_set
    global ADM_MINIMUM_TIER
    global last_ship_scan
    last_ship_scan = time.time() - 50000
    Logoff()
    wait(15)
    Login(char=1)
    ToBridge()
    #==copy-paste code
    SafeClick(doffBtn)
    for i in range(5):
        wait(2)
        if not exists(pressImg) and exists(HoverOn):
            type('P')
            wait(5)
    CheckConnection()
    #adm_filters_set = False
    #old_amt = ADM_MINIMUM_TIER
    #ADM_MINIMUM_TIER = 0
    CheckAdm()
    last_ship_scan = time.time() - 50000
    #adm_filters_set = False
    #ADM_MINIMUM_TIER = old_amt
    #switch char before logoff, at this time. later maybe it worth to rework everything to alternate all chars but faster, without doff maybe
    #==/copy-paste code (end)
while True:
    CheckConnection()
    if not kerrat:
        ToBridge()
    SafeClick(doffBtn)
    for i in range(5):
        wait(2)
        if not exists(pressImg) and exists(HoverOn):
            type('P')
            wait(5)
    runs = 0        
    while runs < 2: 
        CheckCompleted()
        CheckConnection()
        waiting = 0
        while exists(noSlotsImg) and waiting < 1:
            if exists(noSlotsImg):
                wait(10)
                waiting =+ 1
                CheckConnection()
                CheckCompleted()
        if COARSE_DOFF:
            doffLen = [100]
        else:
            doffLen = [1,4,8,100]
        for i in doffLen:
            StartDoff(i)
            CheckConnection()
            if exists(noSlotsImg):
                break
        CheckConnection()
        CheckAdm()
        CheckConnection()
        runs += 1
    #if (time.time() - lastDailyCheck) > 2400: #40*60 sec
    #CheckRnd()
    #CheckConnection()
    #CheckDailyMission()
    #CheckRep()
    #lastDailyCheck = time.time()
    #SafeClick(doffBtn)

    #CheckAdm()
    CheckAlt()
    Logoff()
    wait_time = randrange(7200,9000)
    last_ship_scan = time.time() - 50000
    #if kerrat:
    #    wait_time = wait_time // 2
    with open("C:\\Users\\Jet\\Desktop\\LoginLog.txt", "a") as myfile:
        myfile.write(str(datetime.now())[:-10]+" out.\n")
        myfile.close()    
    wait(wait_time)
    Login()
    with open("C:\\Users\\Jet\\Desktop\\LoginLog.txt", "a") as myfile:
        myfile.write(str(datetime.now())[:-10]+" in.\n")
        myfile.close() 

    gc.collect()