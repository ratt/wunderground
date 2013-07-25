''' Weather Underground Defined settings '''

''' 
Set th default country to pre select
NOTE: This is the Wunderground code NOT the real ISO code
TODO: Change this to jmbo preferences
'''    
WUNDERGROUND_DEFAULT_COUNTRY   = 'ZA'
'''
Weather Underground uses different country codes than standard ISO.
@link http://www.wunderground.com/weather/api/d/docs?d=resources/country-to-iso-matching&MR=1
Format: Wunderground Code,ISO Code
'''
WUNDERGROUND_ISO_CHOICES = (
    ('AD','AD'),
    ('ER','AE'),
    ('AH','AF'),
    ('AT','AG'),
    ('A1','AI'),
    ('AB','AL'),
    ('AM','AM'),
    ('AN','AN'),
    ('AN','AO'),
    ('AA','AQ'),
    ('AG','AR'),
    ('AS','AS'),
    ('OS','AT'),
    ('AU','AU'),
    ('AW','AW'),
    ('A2','AZ'),
    ('BA','BA'),
    ('BR','BB'),
    ('BW','BD'),
    ('BX','BE'),
    ('HV','BF'),
    ('BU','BG'),
    ('BN','BH'),
    ('BI','BI'),
    ('BJ','BJ'),
    ('BE','BM'),
    ('BF','BN'),
    ('BO','BO'),
    ('BZ','BR'),
    ('BS','BS'),
    ('B2','BT'),
    ('BV','BV'),
    ('BC','BW'),
    ('BY','BY'),
    ('BH','BZ'),
    ('CA','CA'),
    ('CC','CC'),
    ('CD','CD'),
    ('CE','CF'),
    ('CG','CG'),
    ('SW','CH'),
    ('IV','CI'),
    ('KU','CK'),
    ('CH','CL'),
    ('CM','CM'),
    ('CI','CN'),
    ('CO','CO'),
    ('CS','CR'),
    ('CU','CU'),
    ('CV','CV'),
    ('CX','CX'),
    ('CY','CY'),
    ('CZ','CZ'),
    ('DL','DE'),
    ('DJ','DJ'),
    ('DN','DK'),
    ('DO','DM'),
    ('DR','DO'),
    ('AL','DZ'),
    ('EQ','EC'),
    ('EE','EE'),
    ('EG','EG'),
    ('EH','EH'),
    ('E1','ER'),
    ('SP','ES'),
    ('ET','ET'),
    ('FI','FI'),
    ('FJ','FJ'),
    ('FK','FK'),
    ('US_FM','FM'),
    ('FA','FO'),
    ('FR','FR'),
    ('GO','GA'),
    ('UK','GB'),
    ('GD','GD'),
    ('GE','GE'),
    ('FG','GF'),
    ('GH','GH'),
    ('GI','GI'),
    ('GL','GL'),
    ('GB','GM'),
    ('GN','GN'),
    ('GP','GP'),
    ('GQ','GQ'),
    ('GR','GR'),
    ('GS','GS'),
    ('GU','GT'),
    ('GU','GU'),
    ('GW','GW'),
    ('GY','GY'),
    ('HK','HK'),
    ('HM','HM'),
    ('HO','HN'),
    ('RH','HR'),
    ('HA','HT'),
    ('HU','HU'),
    ('ID','ID'),
    ('IE','IE'),
    ('IS','IL'),
    ('IN','IN'),
    ('BT','IO'),
    ('IQ','IQ'),
    ('IR','IR'),
    ('IL','IS'),
    ('IY','IT'),
    ('JM','JM'),
    ('JD','JO'),
    ('JP','JP'),
    ('KN','KE'),
    ('KG','KG'),
    ('KH','KH'),
    ('KB','KI'),
    ('IC','KM'),
    ('K1','KN'),
    ('KR','KP'),
    ('KO','KR'),
    ('KV','KV'),
    ('KW','KW'),
    ('GC','KY'),
    ('KZ','KZ'),
    ('LA','LA'),
    ('LB','LB'),
    ('LC','LC'),
    ('LT','LI'),
    ('SB','LK'),
    ('LI','LR'),
    ('LS','LS'),
    ('L1','LT'),
    ('LU','LU'),
    ('LV','LV'),
    ('LY','LY'),
    ('MC','MA'),
    ('M3','MC'),
    ('M1','MD'),
    ('M4','ME'),
    ('MG','MG'),
    ('MH','MH'),
    ('MK','MK'),
    ('MI','ML'),
    ('BM','MM'),
    ('MO','MN'),
    ('MU','MO'),
    ('MP','MP'),
    ('US_MP','MP'),
    ('MR','MQ'),
    ('MT','MR'),
    ('M2','MS'),
    ('ML','MT'),
    ('MA','MU'),
    ('MV','MV'),
    ('MW','MW'),
    ('MX','MX'),
    ('MS','MY'),
    ('MZ','MZ'),
    ('NM','NA'),
    ('NC','NC'),
    ('NR','NE'),
    ('XX_NF','NF'),
    ('NI','NG'),
    ('NK','NI'),
    ('NL','NL'),
    ('NO','NO'),
    ('NP','NP'),
    ('NW','NR'),
    ('N1','NU'),
    ('NZ','NZ'),
    ('OM','OM'),
    ('PM','PA'),
    ('PR','PE'),
    ('PF','PF'),
    ('NG','PG'),
    ('PH','PH'),
    ('PK','PK'),
    ('PL','PL'),
    ('P1','PM'),
    ('P2','PN'),
    ('PR','PR'),
    ('PS','PS'),
    ('PO','PT'),
    ('PW','PW'),
    ('PY','PY'),
    ('QT','QA'),
    ('RE','RE'),
    ('RO','RO'),
    ('RB','RS'),
    ('RS','RU'),
    ('RW','RW'),
    ('SD','SA'),
    ('SO','SB'),
    ('SC','SC'),
    ('SU','SD'),
    ('SN','SE'),
    ('SR','SG'),
    ('HE','SH'),
    ('LJ','SI'),
    ('SJ','SJ'),
    ('S1','SK'),
    ('SL','SL'),
    ('SM','SM'),
    ('SG','SN'),
    ('SI','SO'),
    ('SM','SR'),
    ('TP','ST'),
    ('ES','SV'),
    ('SY','SY'),
    ('SV','SZ'),
    ('TB','TB'),
    ('TI','TC'),
    ('CD','TD'),
    ('TF','TF'),
    ('TG','TG'),
    ('TH','TH'),
    ('TJ','TJ'),
    ('TK','TK'),
    ('EA','TL'),
    ('TM','TM'),
    ('TS','TN'),
    ('TO','TO'),
    ('TU','TR'),
    ('TD','TT'),
    ('TV','TV'),
    ('TW','TW'),
    ('TN','TZ'),
    ('UR','UA'),
    ('UG','UG'),
    ('US_UM','UM'),
    ('US','US'),
    ('UY','UY'),
    ('UZ','UZ'),
    ('VA','VA'),
    ('VC','VC'),
    ('VN','VE'),
    ('VG','VG'),
    ('VI','VI'),
    ('VS','VN'),
    ('NH','VU'),
    ('FW','WF'),
    ('ZM','WS'),
    ('YE','YE'),
    ('YT','YT'),
    ('ZA','ZA'),
    ('ZB','ZM'),
    ('ZW','ZW'),
)