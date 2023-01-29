

import re
class KeyDict(dict):

    def __missing__(self, key):
        return -1

    def __add__(self, other_dict):
        other_keys = other_dict.keys()
        for i in other_keys:
            self[i] = other_dict[i]

        return self

a_space = re.compile("^ㄚˉ")
a_3 = re.compile("^ㄚˇ")
a_4 = re.compile("^ㄚˋ")
a_6 = re.compile("^ㄚˊ")
a_7 = re.compile("^ㄚ˙")

ai_space = re.compile("^ㄞˉ")
ai_3 = re.compile("^ㄞˇ")
ai_4 = re.compile("^ㄞˋ")
ai_6 = re.compile("^ㄞˊ")
ai_7 = re.compile("^ㄞ˙")

an_space = re.compile("^ㄢˉ")
an_3 = re.compile("^ㄢˇ")
an_4 = re.compile("^ㄢˋ")
an_6 = re.compile("^ㄢˊ")
an_7 = re.compile("^ㄢ˙")

ang_space = re.compile("^ㄤˉ")
ang_3 = re.compile("^ㄤˇ")
ang_4 = re.compile("^ㄤˋ")
ang_6 = re.compile("^ㄤˊ")
ang_7 = re.compile("^ㄤ˙")

ao_space = re.compile("^ㄠˉ")
ao_3 = re.compile("^ㄠˇ")
ao_4 = re.compile("^ㄠˋ")
ao_6 = re.compile("^ㄠˊ")
ao_7 = re.compile("^ㄠ˙")


ba_space = re.compile("ㄅㄚˉ")
ba_3 = re.compile("ㄅㄚˇ")
ba_4 = re.compile("ㄅㄚˋ")
ba_6 = re.compile("ㄅㄚˊ")
ba_7 = re.compile("ㄅㄚ˙")


bai_space = re.compile("ㄅㄞˉ")
bai_3 = re.compile("ㄅㄞˇ")
bai_4 = re.compile("ㄅㄞˋ")
bai_6 = re.compile("ㄅㄞˊ")
bai_7 = re.compile("ㄅㄞ˙")

ban_space = re.compile("ㄅㄢˉ")
ban_3 = re.compile("ㄅㄢˇ")
ban_4 = re.compile("ㄅㄢˋ")
ban_6 = re.compile("ㄅㄢˊ")
ban_7 = re.compile("ㄅㄢ˙")

bang_space = re.compile("ㄅㄤˉ")
bang_3 = re.compile("ㄅㄤˇ")
bang_4 = re.compile("ㄅㄤˋ")
bang_6 = re.compile("ㄅㄤˊ")
bang_7 = re.compile("ㄅㄤ˙")

bao_space = re.compile("ㄅㄠˉ")
bao_3 = re.compile("ㄅㄠˇ")
bao_4 = re.compile("ㄅㄠˋ")
bao_6 = re.compile("ㄅㄠˊ")
bao_7 = re.compile("ㄅㄠ˙")



bei_space = re.compile("ㄅㄟˉ")
bei_3 = re.compile("ㄅㄟˇ")
bei_4 = re.compile("ㄅㄟˋ")
bei_6 = re.compile("ㄅㄟˊ")
bei_7 = re.compile("ㄅㄟ˙")

ben_space = re.compile("ㄅㄣˉ")
ben_3 = re.compile("ㄅㄣˇ")
ben_4 = re.compile("ㄅㄣˋ")
ben_6 = re.compile("ㄅㄣˊ")
ben_7 = re.compile("ㄅㄣ˙")

beng_space = re.compile("ㄅㄥˉ")
beng_3 = re.compile("ㄅㄥˇ")
beng_4 = re.compile("ㄅㄥˋ")
beng_6 = re.compile("ㄅㄥˊ")
beng_7 = re.compile("ㄅㄥ˙")


bi_space = re.compile("ㄅㄧˉ")
bi_3 = re.compile("ㄅㄧˇ")
bi_4 = re.compile("ㄅㄧˋ")
bi_6 = re.compile("ㄅㄧˊ")
bi_7 = re.compile("ㄅㄧ˙")

bian_space = re.compile("ㄅㄧㄢˉ")
bian_3 = re.compile("ㄅㄧㄢˇ")
bian_4 = re.compile("ㄅㄧㄢˋ")
bian_6 = re.compile("ㄅㄧㄢˊ")
bian_7 = re.compile("ㄅㄧㄢ˙")

biao_space = re.compile("ㄅㄧㄠˉ")
biao_3 = re.compile("ㄅㄧㄠˇ")
biao_4 = re.compile("ㄅㄧㄠˋ")
biao_6 = re.compile("ㄅㄧㄠˊ")
biao_7 = re.compile("ㄅㄧㄠ˙")

bie_space = re.compile("ㄅㄧㄝˉ")
bie_3 = re.compile("ㄅㄧㄝˇ")
bie_4 = re.compile("ㄅㄧㄝˋ")
bie_6 = re.compile("ㄅㄧㄝˊ")
bie_7 = re.compile("ㄅㄧㄝ˙")

bin_space = re.compile("ㄅㄧㄣˉ")
bin_3 = re.compile("ㄅㄧㄣˇ")
bin_4 = re.compile("ㄅㄧㄣˋ")
bin_6 = re.compile("ㄅㄧㄣˊ")
bin_7 = re.compile("ㄅㄧㄣ˙")

bing_space = re.compile("ㄅㄧㄥˉ")
bing_3 = re.compile("ㄅㄧㄥˇ")
bing_4 = re.compile("ㄅㄧㄥˋ")
bing_6 = re.compile("ㄅㄧㄥˊ")
bing_7 = re.compile("ㄅㄧㄥ˙")


bo_space = re.compile("ㄅㄛˉ")
bo_3 = re.compile("ㄅㄛˇ")
bo_4 = re.compile("ㄅㄛˋ")
bo_6 = re.compile("ㄅㄛˊ")
bo_7 = re.compile("ㄅㄛ˙")

bu_space = re.compile("ㄅㄨˉ")
bu_3 = re.compile("ㄅㄨˇ")
bu_4 = re.compile("ㄅㄨˋ")
bu_6 = re.compile("ㄅㄨˊ")
bu_7 = re.compile("ㄅㄨ˙")

ca_space = re.compile("ㄘㄚˉ")
ca_3 = re.compile("ㄘㄚˇ")
ca_4 = re.compile("ㄘㄚˋ")
ca_6 = re.compile("ㄘㄚˊ")
ca_7 = re.compile("ㄘㄚ˙")

cai_space = re.compile("ㄘㄞˉ")
cai_3 = re.compile("ㄘㄞˇ")
cai_4 = re.compile("ㄘㄞˋ")
cai_6 = re.compile("ㄘㄞˊ")
cai_7 = re.compile("ㄘㄞ˙")

can_space = re.compile("ㄘㄢˉ")
can_3= re.compile("ㄘㄢˇ")
can_4= re.compile("ㄘㄢˋ")
can_6= re.compile("ㄘㄢˊ")
can_7= re.compile("ㄘㄢ˙")

cang_space = re.compile("ㄘㄤˉ")
cang_3 = re.compile("ㄘㄤˇ")
cang_4 = re.compile("ㄘㄤˋ")
cang_6 = re.compile("ㄘㄤˊ")
cang_7 = re.compile("ㄘㄤ˙")

cao_space = re.compile("ㄘㄠˉ")
cao_3 = re.compile("ㄘㄠˇ")
cao_4 = re.compile("ㄘㄠˋ")
cao_6 = re.compile("ㄘㄠˊ")
cao_7 = re.compile("ㄘㄠ˙")

ce_space = re.compile("ㄘㄜˉ")
ce_3 = re.compile("ㄘㄜˇ")
ce_4 = re.compile("ㄘㄜˋ")
ce_6 = re.compile("ㄘㄜˊ")
ce_7 = re.compile("ㄘㄜ˙")

cen_space = re.compile("ㄘㄣˉ")
cen_3 = re.compile("ㄘㄣˇ")
cen_4 = re.compile("ㄘㄣˋ")
cen_6= re.compile("ㄘㄣˊ")
cen_7= re.compile("ㄘㄣ˙")

ceng_space = re.compile("ㄘㄥˉ")
ceng_3= re.compile("ㄘㄥˇ")
ceng_4= re.compile("ㄘㄥˋ")
ceng_6= re.compile("ㄘㄥˊ")
ceng_7= re.compile("ㄘㄥ˙")


cha_space= re.compile("ㄔㄚˉ")
cha_3= re.compile("ㄔㄚˇ")
cha_4= re.compile("ㄔㄚˋ")
cha_6= re.compile("ㄔㄚˊ")
cha_7= re.compile("ㄔㄚ˙")


chai_space= re.compile("ㄔㄞˉ")
chai_3= re.compile("ㄔㄞˇ")
chai_4= re.compile("ㄔㄞˋ")
chai_6= re.compile("ㄔㄞˊ")
chai_7= re.compile("ㄔㄞ˙")

         
chan_space= re.compile("ㄔㄢˉ")
chan_3= re.compile("ㄔㄢˇ")
chan_4= re.compile("ㄔㄢˋ")
chan_6= re.compile("ㄔㄢˊ")
chan_7= re.compile("ㄔㄢ˙")


chang_space= re.compile("ㄔㄤˉ")
chang_3= re.compile("ㄔㄤˇ")
chang_4= re.compile("ㄔㄤˋ")
chang_6= re.compile("ㄔㄤˊ")
chang_7= re.compile("ㄔㄤ˙")


chao_space= re.compile("ㄔㄠˉ")
chao_3= re.compile("ㄔㄠˇ")
chao_4= re.compile("ㄔㄠˋ")
chao_6= re.compile("ㄔㄠˊ")
chao_7= re.compile("ㄔㄠ˙")

che_space= re.compile("ㄔㄜˉ")
che_3= re.compile("ㄔㄜˇ")
che_4= re.compile("ㄔㄜˋ")
che_6= re.compile("ㄔㄜˊ")
che_7= re.compile("ㄔㄜ˙")

chen_space= re.compile("ㄔㄣˉ")
chen_3= re.compile("ㄔㄣˇ")
chen_4= re.compile("ㄔㄣˋ")
chen_6= re.compile("ㄔㄣˊ")
chen_7= re.compile("ㄔㄣ˙")
            

cheng_space= re.compile("ㄔㄥˉ")
cheng_3= re.compile("ㄔㄥˇ")
cheng_4= re.compile("ㄔㄥˋ")
cheng_6= re.compile("ㄔㄥˊ")
cheng_7= re.compile("ㄔㄥ˙")

chi_space= re.compile("ㄔˉ")
chi_3= re.compile("ㄔˇ")
chi_4= re.compile("ㄔˋ")
chi_6= re.compile("ㄔˊ")
chi_7= re.compile("ㄔ˙")
          

chong_space= re.compile("ㄔㄨㄥˉ")
chong_3= re.compile("ㄔㄨㄥˇ")
chong_4= re.compile("ㄔㄨㄥˋ")
chong_6= re.compile("ㄔㄨㄥˊ")
chong_7= re.compile("ㄔㄨㄥ˙")


chou_space= re.compile("ㄔㄡˉ")
chou_3= re.compile("ㄔㄡˇ")
chou_4= re.compile("ㄔㄡˋ")
chou_6= re.compile("ㄔㄡˊ")
chou_7= re.compile("ㄔㄡ˙")
            
chu_space= re.compile("ㄔㄨˉ")
chu_3= re.compile("ㄔㄨˇ")
chu_4= re.compile("ㄔㄨˋ")
chu_6= re.compile("ㄔㄨˊ")
chu_7= re.compile("ㄔㄨ˙")

chuai_space= re.compile("ㄔㄨㄞ ˉ")
chuai_3= re.compile("ㄔㄨㄞ ˇ")
chuai_4= re.compile("ㄔㄨㄞ ˋ")
chuai_6= re.compile("ㄔㄨㄞ ˊ")
chuai_7= re.compile("ㄔㄨㄞ ˙")



chuai_space= re.compile("ㄔㄨㄞˉ")
chuai_3= re.compile("ㄔㄨㄞˇ")
chuai_4= re.compile("ㄔㄨㄞˋ")
chuai_6= re.compile("ㄔㄨㄞˊ")
chuai_7= re.compile("ㄔㄨㄞ˙")

chuan_space= re.compile("ㄔㄨㄢˉ")
chuan_3= re.compile("ㄔㄨㄢˇ")
chuan_4= re.compile("ㄔㄨㄢˋ")
chuan_6= re.compile("ㄔㄨㄢˊ")
chuan_7= re.compile("ㄔㄨㄢ˙")
               
chuang_space= re.compile("ㄔㄨㄤˉ")
chuang_3= re.compile("ㄔㄨㄤˇ")
chuang_4= re.compile("ㄔㄨㄤˋ")
chuang_6= re.compile("ㄔㄨㄤˊ")
chuang_7= re.compile("ㄔㄨㄤ˙")
                      
chui_space= re.compile("ㄔㄨㄟˉ")
chui_3= re.compile("ㄔㄨㄟˇ")
chui_4= re.compile("ㄔㄨㄟˋ")
chui_6= re.compile("ㄔㄨㄟˊ")
chui_7= re.compile("ㄔㄨㄟ˙")         
            
chun_space= re.compile("ㄔㄨㄣˉ")
chun_3= re.compile("ㄔㄨㄣˇ")
chun_4= re.compile("ㄔㄨㄣˋ")
chun_6= re.compile("ㄔㄨㄣˊ")
chun_7= re.compile("ㄔㄨㄣ˙")         
            
chuo_space= re.compile("ㄔㄨㄛˉ")
chuo_3= re.compile("ㄔㄨㄛˇ")
chuo_4= re.compile("ㄔㄨㄛˋ")
chuo_6= re.compile("ㄔㄨㄛˊ")
chuo_7= re.compile("ㄔㄨㄛ˙")                   
         
            
ci_space= re.compile("ㄘˉ")
ci_3= re.compile("ㄘˇ")
ci_4= re.compile("ㄘˋ")
ci_6= re.compile("ㄘˊ")
ci_7= re.compile("ㄘ˙") 
           
cong_space= re.compile("ㄘㄨㄥˉ")
cong_3= re.compile("ㄘㄨㄥˇ")
cong_4= re.compile("ㄘㄨㄥˋ")
cong_6= re.compile("ㄘㄨㄥˊ")
cong_7= re.compile("ㄘㄨㄥ˙") 
                       
cou_space= re.compile("ㄘㄡˉ")
cou_3= re.compile("ㄘㄡˇ")
cou_4= re.compile("ㄘㄡˋ")
cou_6 = re.compile("ㄘㄡˊ")
cou_7= re.compile("ㄘㄡ˙")            

   
cu_space= re.compile("ㄘㄨˉ")
cu_3= re.compile("ㄘㄨˇ")
cu_4 = re.compile("ㄘㄨˋ")
cu_6 = re.compile("ㄘㄨˊ")
cu_7= re.compile("ㄘㄨ˙")

cuan_space= re.compile("ㄘㄨㄢˉ")
cuan_3 = re.compile("ㄘㄨㄢˇ")
cuan_4  = re.compile("ㄘㄨㄢˋ")
cuan_6  = re.compile("ㄘㄨㄢˊ")
cuan_7 = re.compile("ㄘㄨㄢ˙")


cui_space= re.compile("ㄘㄨㄟˉ")
cui_3 = re.compile("ㄘㄨㄟˇ")
cui_4  = re.compile("ㄘㄨㄟˋ")
cui_6  = re.compile("ㄘㄨㄟˊ")
cui_7 = re.compile("ㄘㄨㄟ˙")  
         
      
cun_space= re.compile("ㄘㄨㄣˉ")
cun_3 = re.compile("ㄘㄨㄣˇ")
cun_4  = re.compile("ㄘㄨㄣˋ")
cun_6  = re.compile("ㄘㄨㄣˊ")
cun_7 = re.compile("ㄘㄨㄣ˙")

cuo_space= re.compile("ㄘㄨㄛˉ")
cuo_3 = re.compile("ㄘㄨㄛˇ")
cuo_4  = re.compile("ㄘㄨㄛˋ")
cuo_6  = re.compile("ㄘㄨㄛˊ")
cuo_7 = re.compile("ㄘㄨㄛ˙")    

da_space= re.compile("ㄉㄚˉ")
da_3 = re.compile("ㄉㄚˇ")
da_4  = re.compile("ㄉㄚˋ")
da_6  = re.compile("ㄉㄚˊ")
da_7 = re.compile("ㄉㄚ˙")       

dai_space= re.compile("ㄉㄞˉ")
dai_3 = re.compile("ㄉㄞˇ")
dai_4  = re.compile("ㄉㄞˋ")
dai_6  = re.compile("ㄉㄞˊ")
dai_7 = re.compile("ㄉㄞ˙")                

dan_space= re.compile("ㄉㄢˉ")
dan_3 = re.compile("ㄉㄢˇ")
dan_4  = re.compile("ㄉㄢˋ")
dan_6  = re.compile("ㄉㄢˊ")
dan_7 = re.compile("ㄉㄢ˙")         

dang_space= re.compile("ㄉㄤˉ")
dang_3 = re.compile("ㄉㄤˇ")
dang_4  = re.compile("ㄉㄤˋ")
dang_6  = re.compile("ㄉㄤˊ")
dang_7 = re.compile("ㄉㄤ˙")                  
           
          

dun_space =re.compile("ㄉㄨㄣˉ")
dun_3 =re.compile("ㄉㄨㄣˇ")
dun_4 =re.compile("ㄉㄨㄣˋ")
dun_6 =re.compile("ㄉㄨㄣˊ")
dun_7 =re.compile("ㄉㄨㄣ˙")

duo_space =re.compile("ㄉㄨㄛˉ")
duo_3 =re.compile("ㄉㄨㄛˇ")
duo_4 =re.compile("ㄉㄨㄛˋ")
duo_6 =re.compile("ㄉㄨㄛˊ")
duo_7 =re.compile("ㄉㄨㄛ˙")

dao_space  = re.compile("ㄉㄠˉ")
dao_3 =re.compile("ㄉㄠˇ")
dao_4 =re.compile("ㄉㄠˋ")
dao_6 =re.compile("ㄉㄠˊ")
dao_7 =re.compile("ㄉㄠ˙")


de_space  = re.compile("ㄉㄜˉ")
de_3 =re.compile("ㄉㄜˇ")
de_4 =re.compile("ㄉㄜˋ")
de_6 =re.compile("ㄉㄜˊ")
de_7 =re.compile("ㄉㄜ˙")

dei_space  = re.compile("ㄉㄟˉ")
dei_3 =re.compile("ㄉㄟˇ")
dei_4 =re.compile("ㄉㄟˋ")
dei_6 =re.compile("ㄉㄟˊ")
dei_7 =re.compile("ㄉㄟ˙")

   
deng_space  = re.compile("ㄉㄥˉ")
deng_3 =re.compile("ㄉㄥˇ")
deng_4 =re.compile("ㄉㄥˋ")
deng_6 =re.compile("ㄉㄥˊ")
deng_7 =re.compile("ㄉㄥ˙")

di_space  = re.compile("ㄉㄧˉ")
di_3 =re.compile("ㄉㄧˇ")
di_4 =re.compile("ㄉㄧˋ")
di_6 =re.compile("ㄉㄧˊ")
di_7 =re.compile("ㄉㄧ˙")   
       
dian_space  = re.compile("ㄉㄧㄢˉ")
dian_3 =re.compile("ㄉㄧㄢˇ")
dian_4 =re.compile("ㄉㄧㄢˋ")
dian_6 =re.compile("ㄉㄧㄢˊ")
dian_7 =re.compile("ㄉㄧㄢ˙")
    
       

diao_space  = re.compile("ㄊㄧㄠˉ")
diao_3  =re.compile("ㄊㄧㄠˇ")
diao_4 =re.compile("ㄊㄧㄠˋ")
diao_6 =re.compile("ㄊㄧㄠˊ")
diao_7 =re.compile("ㄊㄧㄠ˙")

die_space  = re.compile("ㄉㄧㄝˉ")
die_3  =re.compile("ㄉㄧㄝˇ")
die_4 =re.compile("ㄉㄧㄝˋ")
die_6 =re.compile("ㄉㄧㄝˊ")
die_7 =re.compile("ㄉㄧㄝ˙")   

ding_space  = re.compile("ㄉㄧㄥˉ")
ding_3   =re.compile("ㄉㄧㄥˇ")
ding_4 =re.compile("ㄉㄧㄥˋ")
ding_6 =re.compile("ㄉㄧㄥˊ")
ding_7 =re.compile("ㄉㄧㄥ˙")             

diu_space  = re.compile("ㄉㄧㄡˉ")
diu_3   =re.compile("ㄉㄧㄡˇ")
diu_4  =re.compile("ㄉㄧㄡˋ")
diu_6 =re.compile("ㄉㄧㄡˊ")
diu_7 =re.compile("ㄉㄧㄡ˙")             
          

dong_space  = re.compile("ㄉㄨㄥˉ")
dong_3   =re.compile("ㄉㄨㄥˇ")
dong_4  =re.compile("ㄉㄨㄥˋ")
dong_6 =re.compile("ㄉㄨㄥˊ")
dong_7 =re.compile("ㄉㄨㄥ˙")             
                      
dou_space  = re.compile("ㄉㄡˉ")
dou_3   =re.compile("ㄉㄡˇ")
dou_4  =re.compile("ㄉㄡˋ")
dou_6 =re.compile("ㄉㄡˊ")
dou_7 =re.compile("ㄉㄡ˙")

du_space  = re.compile("ㄉㄨˉ")
du_3   =re.compile("ㄉㄨˇ")
du_4  =re.compile("ㄉㄨˋ")
du_6 =re.compile("ㄉㄨˊ")
du_7 =re.compile("ㄉㄨ˙")   
                           
duan_space  = re.compile("ㄉㄨㄢˉ")
duan_3   =re.compile("ㄉㄨㄢˇ")
duan_4  =re.compile("ㄉㄨㄢˋ")
duan_6 =re.compile("ㄉㄨㄢˊ")
duan_7 =re.compile("ㄉㄨㄢ˙")       
       
dui_space  = re.compile("ㄉㄨㄟˉ")
dui_3   =re.compile("ㄉㄨㄟˇ")
dui_4  =re.compile("ㄉㄨㄟˋ")
dui_6 =re.compile("ㄉㄨㄟˊ")
dui_7 =re.compile("ㄉㄨㄟ˙")                 
            
dun_space  = re.compile("ㄉㄨㄣˉ")
dun_3    =re.compile("ㄉㄨㄣˇ")
dun_4  =re.compile("ㄉㄨㄣˋ")
dun_6 =re.compile("ㄉㄨㄣˊ")
dun_7 =re.compile("ㄉㄨㄣ˙")               
           
duo_space  = re.compile("ㄉㄨㄛˉ")
duo_3    =re.compile("ㄉㄨㄛˇ")
duo_4  =re.compile("ㄉㄨㄛˋ")
duo_6 =re.compile("ㄉㄨㄛˊ")
duo_7 =re.compile("ㄉㄨㄛ˙")      
         
e_space = re.compile("ㄜˉ")
e_3 = re.compile("ㄜˇ")
e_4 = re.compile("ㄜˋ")
e_6 = re.compile("ㄜˊ")
e_7 = re.compile("ㄜ˙")

ei_space = re.compile("ㄞˉ")
ei_3 = re.compile("ㄞˇ")
ei_4 = re.compile("ㄞˋ")
ei_6 = re.compile("ㄞˊ")
ei_7 = re.compile("ㄞ˙")

en_space = re.compile("ㄣˉ")
en_3 = re.compile("ㄣˇ")
en_4 = re.compile("ㄣˋ")
en_6 = re.compile("ㄣˊ")
en_7 = re.compile("ㄣ˙")

er_space = re.compile("ㄦˉ")
er_3 = re.compile("ㄦˇ")
er_4 = re.compile("ㄦˋ")
er_6 = re.compile("ㄦˊ")
er_7 = re.compile("ㄦ˙")


fa_space = re.compile("ㄈㄚˉ")
fa_3 = re.compile("ㄈㄚˇ")
fa_4 = re.compile("ㄈㄚˋ")
fa_6 = re.compile("ㄈㄚˊ")
fa_7 = re.compile("ㄈㄚ˙")


fan_space= re.compile("ㄈㄢˉ")
fan_3= re.compile("ㄈㄢˇ")
fan_4= re.compile("ㄈㄢˋ")
fan_6= re.compile("ㄈㄢˊ")
fan_7= re.compile("ㄈㄢ˙")

fang_space=re.compile("ㄈㄤˉ")
fang_3=re.compile("ㄈㄤˇ")
fang_4=re.compile("ㄈㄤˋ")
fang_6=re.compile("ㄈㄤˊ")
fang_7=re.compile("ㄈㄤ˙")

fei_space=re.compile("ㄈㄟˉ")
fei_3=re.compile("ㄈㄟˇ")
fei_4=re.compile("ㄈㄟˋ")
fei_6=re.compile("ㄈㄟˊ")
fei_7=re.compile("ㄈㄟ˙")

fen_space=re.compile("ㄈㄣˉ")
fen_3=re.compile("ㄈㄣˇ")
fen_4=re.compile("ㄈㄣˋ")
fen_6=re.compile("ㄈㄣˊ")
fen_7=re.compile("ㄈㄣ˙")

feng_space=re.compile("ㄈㄥˉ")
feng_3=re.compile("ㄈㄥˇ")
feng_4=re.compile("ㄈㄥˋ")
feng_6=re.compile("ㄈㄥˊ")
feng_7=re.compile("ㄈㄥ˙")

fo_space=re.compile("ㄈㄛˉ")
fo_3=re.compile("ㄈㄛˇ")
fo_4=re.compile("ㄈㄛˋ")
fo_6=re.compile("ㄈㄛˊ")
fo_7=re.compile("ㄈㄛ˙")

fou_space=re.compile("ㄈㄡˉ")
fou_3=re.compile("ㄈㄡˇ")
fou_4=re.compile("ㄈㄡˋ")
fou_6=re.compile("ㄈㄡˊ")
fou_7=re.compile("ㄈㄡ˙")


fu_space =re.compile("ㄈㄨˉ")
fu_3 =re.compile("ㄈㄨˇ")
fu_4 =re.compile("ㄈㄨˋ")
fu_6 =re.compile("ㄈㄨˊ")
fu_7 =re.compile("ㄈㄨ˙")

ga_space =re.compile("ㄍˉ")
ga_3 =re.compile("ㄍˇ")
ga_4 =re.compile("ㄍˋ")
ga_6 =re.compile("ㄍˊ")
ga_7 =re.compile("ㄍ˙")

gai_space =re.compile("ㄍㄞˉ")
gai_3 =re.compile("ㄍㄞˇ")
gai_4 =re.compile("ㄍㄞˋ")
gai_6 =re.compile("ㄍㄞˊ")
gai_7 =re.compile("ㄍㄞ˙")

gan_space =re.compile("ㄍㄢˉ")
gan_3 =re.compile("ㄍㄢˇ")
gan_4 =re.compile("ㄍㄢˋ")
gan_6 =re.compile("ㄍㄢˊ")
gan_7 =re.compile("ㄍㄢ˙")

gang_space =re.compile("ㄍㄤˉ")
gang_3 =re.compile("ㄍㄤˇ")
gang_4 =re.compile("ㄍㄤˋ")
gang_6 =re.compile("ㄍㄤˊ")
gang_7 =re.compile("ㄍㄤ˙")

gao_space=re.compile("ㄍㄠˉ")
gao_3=re.compile("ㄍㄠˇ")
gao_4=re.compile("ㄍㄠˋ")
gao_6=re.compile("ㄍㄠˊ")
gao_7=re.compile("ㄍㄠ˙")

ge_space=re.compile("ㄍㄜˉ")
ge_3=re.compile("ㄍㄜˇ")
ge_4=re.compile("ㄍㄜˋ")
ge_6=re.compile("ㄍㄜˊ")
ge_7=re.compile("ㄍㄜ˙")

gei_space=re.compile("ㄍㄟˉ")
gei_3=re.compile("ㄍㄟˇ")
gei_4=re.compile("ㄍㄟˋ")
gei_6=re.compile("ㄍㄟˊ")
gei_7=re.compile("ㄍㄟ˙")

gen_space=re.compile("ㄍㄣˉ")
gen_3=re.compile("ㄍㄣˇ")
gen_4=re.compile("ㄍㄣˋ")
gen_6=re.compile("ㄍㄣˊ")
gen_7=re.compile("ㄍㄣ˙")

geng_space=re.compile("ㄍㄥˉ")
geng_3=re.compile("ㄍㄥˇ")
geng_4=re.compile("ㄍㄥˋ")
geng_6=re.compile("ㄍㄥˊ")
geng_7=re.compile("ㄍㄥ˙")

gong_space=re.compile("ㄍㄨㄥˉ")
gong_3=re.compile("ㄍㄥˇ")
gong_4=re.compile("ㄍㄥˋ")
gong_6=re.compile("ㄍㄥˊ")
gong_7=re.compile("ㄍㄥ˙")

gou_space=re.compile("ㄍㄨㄥˉ")
gou_3=re.compile("ㄍㄨㄥˇ")
gou_4=re.compile("ㄍㄨㄥˋ")
gou_6=re.compile("ㄍㄨㄥˊ")
gou_7=re.compile("ㄍㄨㄥ˙")

gu_space=re.compile("ㄍㄨˉ")
gu_3=re.compile("ㄍㄨˇ")
gu_4=re.compile("ㄍㄨˋ")
gu_6=re.compile("ㄍㄨˊ")
gu_7=re.compile("ㄍㄨ˙")

gua_space=re.compile("ㄍㄨㄚˉ")
gua_3=re.compile("ㄍㄨㄚˇ")
gua_4=re.compile("ㄍㄨㄚˋ")
gua_6=re.compile("ㄍㄨㄚˊ")
gua_7=re.compile("ㄍㄨㄚ˙")


guai_space=re.compile("ㄍㄨㄞˉ")
guai_3=re.compile("ㄍㄨㄞˇ")
guai_4=re.compile("ㄍㄨㄞˋ")
guai_6=re.compile("ㄍㄨㄞˊ")
guai_7=re.compile("ㄍㄨㄞ˙")

guan_space=re.compile("ㄍㄨㄢˉ")
guan_3=re.compile("ㄍㄨㄢˇ")
guan_4=re.compile("ㄍㄨㄢˊ")
guan_6=re.compile("ㄍㄨㄢˋ")
guan_7=re.compile("ㄍㄨㄢ˙")

guang_space=re.compile("ㄍㄨㄤˉ")
guang_3=re.compile("ㄍㄨㄤˇ")
guang_4=re.compile("ㄍㄨㄤˊ")
guang_6=re.compile("ㄍㄨㄤˋ")
guang_7=re.compile("ㄍㄨㄤ˙")

gui_space=re.compile("ㄍㄨㄟˉ")
gui_3=re.compile("ㄍㄨㄟˇ")
gui_4=re.compile("ㄍㄨㄟˊ")
gui_6=re.compile("ㄍㄨㄟˋ")
gui_7=re.compile("ㄍㄨㄟ˙")

gun_space=re.compile("ㄍㄨㄣˉ")
gun_3=re.compile("ㄍㄨㄣˇ")
gun_4=re.compile("ㄍㄨㄣˊ")
gun_6=re.compile("ㄍㄨㄣˋ")
gun_7=re.compile("ㄍㄨㄣ˙")

guo_space=re.compile("ㄍㄨㄛˉ")
guo_3=re.compile("ㄍㄨㄛˇ")
guo_4=re.compile("ㄍㄨㄛˊ")
guo_6=re.compile("ㄍㄨㄛˋ")
guo_7=re.compile("ㄍㄨㄛ˙")

ha_space =re.compile("ㄏㄚˉ")
ha_3 =re.compile("ㄏㄚˇ")
ha_4 =re.compile("ㄏㄚˊ")
ha_6 =re.compile("ㄏㄚˋ")
ha_7 =re.compile("ㄏㄚ˙")

hai_space =re.compile("ㄏㄞˉ")
hai_3 =re.compile("ㄏㄞˇ")
hai_4 =re.compile("ㄏㄞˊ")
hai_6 =re.compile("ㄏㄞˋ")
hai_7 =re.compile("ㄏㄞ˙")

han_space =re.compile("ㄏㄢˉ")
han_3 =re.compile("ㄏㄢˇ")
han_4 =re.compile("ㄏㄢˊ")
han_6 =re.compile("ㄏㄢˋ")
han_7 =re.compile("ㄏㄢ˙")

hang_space =re.compile("ㄏㄤˉ")
hang_3 =re.compile("ㄏㄤˇ")
hang_4 =re.compile("ㄏㄤˊ")
hang_6 =re.compile("ㄏㄤˋ")
hang_7 =re.compile("ㄏㄤ˙")

hao_space =re.compile("ㄏㄠˉ")
hao_3 =re.compile("ㄏㄠˇ")
hao_4 =re.compile("ㄏㄠˊ")
hao_6 =re.compile("ㄏㄠˋ")
hao_7 =re.compile("ㄏㄠ˙")

he_space =re.compile("ㄏㄜˉ")
he_3 =re.compile("ㄏㄜˇ")
he_4 =re.compile("ㄏㄜˊ")
he_6 =re.compile("ㄏㄜˋ")
he_7 =re.compile("ㄏㄜ˙")

hei_space =re.compile("ㄏㄟˉ")
hei_3 =re.compile("ㄏㄟˇ")
hei_4 =re.compile("ㄏㄟˊ")
hei_6 =re.compile("ㄏㄟˋ")
hei_7 =re.compile("ㄏㄟ˙")

hen_space =re.compile("ㄏㄣˉ")
hen_3 =re.compile("ㄏㄣˇ")
hen_4 =re.compile("ㄏㄣˊ")
hen_6 =re.compile("ㄏㄣˋ")
hen_7 =re.compile("ㄏㄣ˙")

heng_space =re.compile("ㄏㄥˉ")
heng_3 =re.compile("ㄏㄥˇ")
heng_4 =re.compile("ㄏㄥˊ")
heng_6 =re.compile("ㄏㄥˋ")
heng_7 =re.compile("ㄏㄥ˙")        

hong_space =re.compile("ㄏㄨㄥˉ")
hong_3 =re.compile("ㄏㄨㄥˇ")
hong_4 =re.compile("ㄏㄨㄥˊ")
hong_6 =re.compile("ㄏㄨㄥˋ")            
hong_7 =re.compile("ㄏㄨㄥ˙")

hou_space =re.compile("ㄏㄡˉ")
hou_3 =re.compile("ㄏㄡˇ")
hou_4 =re.compile("ㄏㄡˊ")
hou_6 =re.compile("ㄏㄡˋ")
hou_7 =re.compile("ㄏㄡ˙")

hu_space =re.compile("ㄏㄨˉ")
hu_3 =re.compile("ㄏㄨˇ")
hu_4 =re.compile("ㄏㄨˊ")
hu_6 =re.compile("ㄏㄨˋ")
hu_7 =re.compile("ㄏㄨ˙")

hua_space =re.compile("ㄏㄨㄚˉ")
hua_3 =re.compile("ㄏㄨㄚˇ")
hua_4 =re.compile("ㄏㄨㄚˊ")
hua_6 =re.compile("ㄏㄨㄚˋ")
hua_7 =re.compile("ㄏㄨㄚ˙")

huai_space =re.compile("ㄏㄨㄞˉ")
huai_3 =re.compile("ㄏㄨㄞˇ")
huai_4 =re.compile("ㄏㄨㄞˊ")
huai_6 =re.compile("ㄏㄨㄞˋ")
huai_7 =re.compile("ㄏㄨㄞ˙")

huan_space =re.compile("ㄏㄨㄢˉ")
huan_3 =re.compile("ㄏㄨㄢˇ")
huan_4 =re.compile("ㄏㄨㄢˊ")
huan_6 =re.compile("ㄏㄨㄢˋ")
huan_7 =re.compile("ㄏㄨㄢ˙")

huang_space =re.compile("ㄏㄨㄤˉ")
huang_3 =re.compile("ㄏㄨㄤˇ")
huang_4 =re.compile("ㄏㄨㄤˊ")
huang_6 =re.compile("ㄏㄨㄤˋ")
huang_7 =re.compile("ㄏㄨㄤ˙")


hui_space =re.compile("ㄏㄨㄟˉ")
hui_3 =re.compile("ㄏㄨㄟˇ")
hui_4 =re.compile("ㄏㄨㄟˊ")
hui_6 =re.compile("ㄏㄨㄟˋ")
hui_7 =re.compile("ㄏㄨㄟ˙")

hun_space =re.compile("ㄏㄨㄣˉ")
hun_3 =re.compile("ㄏㄨㄣˇ")
hun_4 =re.compile("ㄏㄨㄣˊ")
hun_6 =re.compile("ㄏㄨㄣˋ")
hun_7 =re.compile("ㄏㄨㄣ˙")

huo_space =re.compile("ㄏㄨㄛˉ")
huo_3 =re.compile("ㄏㄨㄛˇ")
huo_4 =re.compile("ㄏㄨㄛˊ")
huo_6 =re.compile("ㄏㄨㄛˋ")
huo_7 =re.compile("ㄏㄨㄛ˙")

ji_space = re.compile("ㄐㄧˉ")
ji_3 = re.compile("ㄐㄧˇ")
ji_4 = re.compile("ㄐㄧˊ")
ji_6 = re.compile("ㄐㄧˋ")
ji_7 = re.compile("ㄐㄧ˙")


jia_space = re.compile("ㄐㄧㄚˉ")
jia_3 = re.compile("ㄐㄧㄚˇ")
jia_4 = re.compile("ㄐㄧㄚˊ")
jia_6 = re.compile("ㄐㄧㄚˋ")
jia_7 = re.compile("ㄐㄧㄚ˙")

jian_space = re.compile("ㄐㄧㄢˉ")
jian_3 = re.compile("ㄐㄧㄢˇ")
jian_4 = re.compile("ㄐㄧㄢˊ")
jian_6 = re.compile("ㄐㄧㄢˋ")
jian_7 = re.compile("ㄐㄧㄢ˙")

jiang_space = re.compile("ㄐㄧㄤˉ")
jiang_3 = re.compile("ㄐㄧㄤˇ")
jiang_4 = re.compile("ㄐㄧㄤˊ")
jiang_6 = re.compile("ㄐㄧㄤˋ")
jiang_7 = re.compile("ㄐㄧㄤ˙")


jiao_space = re.compile("ㄐㄧㄠˉ")
jiao_3 = re.compile("ㄐㄧㄠˇ")
jiao_4 = re.compile("ㄐㄧㄠˊ")
jiao_6 = re.compile("ㄐㄧㄠˋ")
jiao_7 = re.compile("ㄐㄧㄠ˙")

jie_space = re.compile("ㄐㄧㄝˉ")
jie_3 = re.compile("ㄐㄧㄝˇ")
jie_4 = re.compile("ㄐㄧㄝˊ")
jie_6 = re.compile("ㄐㄧㄝˋ")
jie_7 = re.compile("ㄐㄧㄝ˙")

jin_space = re.compile("ㄐㄧㄣˉ")
jin_3 = re.compile("ㄐㄧㄣˇ")
jin_4 = re.compile("ㄐㄧㄣˊ")
jin_6 = re.compile("ㄐㄧㄣˋ")
jin_7 = re.compile("ㄐㄧㄣ˙")

jing_space = re.compile("ㄐㄧㄥˉ")
jing_3 = re.compile("ㄐㄧㄥˇ")
jing_4 = re.compile("ㄐㄧㄥˊ")
jing_6 = re.compile("ㄐㄧㄥˋ")
jing_7 = re.compile("ㄐㄧㄥ˙")

jiong_space = re.compile("ㄐㄩㄥˉ")
jiong_3 = re.compile("ㄐㄩㄥˇ")
jiong_4 = re.compile("ㄐㄩㄥˊ")
jiong_6 = re.compile("ㄐㄩㄥˋ")
jiong_7 = re.compile("ㄐㄩㄥ˙")

jiu_space = re.compile("ㄐㄧㄡˉ")
jiu_3 = re.compile("ㄐㄧㄡˇ")
jiu_4 = re.compile("ㄐㄧㄡˊ")
jiu_6 = re.compile("ㄐㄧㄡˋ")
jiu_7 = re.compile("ㄐㄧㄡ˙")

ju_space = re.compile("ㄐㄩˉ")
ju_3 = re.compile("ㄐㄩˇ")
ju_4 = re.compile("ㄐㄩˊ")
ju_6 = re.compile("ㄐㄩˋ")
ju_7 = re.compile("ㄐㄩ˙")

juan_space = re.compile("ㄐㄩㄢˉ")
juan_3 = re.compile("ㄐㄩㄢˇ")
juan_4 = re.compile("ㄐㄩㄢˊ")
juan_6 = re.compile("ㄐㄩㄢˋ")
juan_7 = re.compile("ㄐㄩㄢ˙")

jue_space = re.compile("ㄐㄩㄝˉ")
jue_3 = re.compile("ㄐㄩㄝˇ")
jue_4 = re.compile("ㄐㄩㄝˊ")
jue_6 = re.compile("ㄐㄩㄝˋ")
jue_7 = re.compile("ㄐㄩㄝ˙")


jun_space = re.compile("ㄐㄩㄣˉ")
jun_3 = re.compile("ㄐㄩㄣˇ")
jun_4 = re.compile("ㄐㄩㄣˊ")
jun_6 = re.compile("ㄐㄩㄣˋ")
jun_7 = re.compile("ㄐㄩㄣ˙")

ka_space = re.compile("ㄎㄚˉ")
ka_3 = re.compile("ㄎㄚˇ")
ka_4 = re.compile("ㄎㄚˊ")
ka_6 = re.compile("ㄎㄚˋ")
ka_7 = re.compile("ㄎㄚ˙")



kai_space = re.compile("ㄎㄞˉ")
kai_3 = re.compile("ㄎㄞˇ")
kai_4 = re.compile("ㄎㄞˊ")
kai_6 = re.compile("ㄎㄞˋ")
kai_7 = re.compile("ㄎㄞ˙")

kan_space = re.compile("ㄎㄢˉ")
kan_3 = re.compile("ㄎㄢˇ")
kan_4 = re.compile("ㄎㄢˊ")
kan_6 = re.compile("ㄎㄢˋ")
kan_7 = re.compile("ㄎㄢ˙")

kang_space = re.compile("ㄎㄤˉ")
kang_3 = re.compile("ㄎㄤˇ")
kang_4 = re.compile("ㄎㄤˊ")
kang_6 = re.compile("ㄎㄤˋ")
kang_7 = re.compile("ㄎㄤ˙")


kao_space = re.compile("ㄎㄠˉ")
kao_3 = re.compile("ㄎㄠˇ")
kao_4 = re.compile("ㄎㄠˊ")
kao_6 = re.compile("ㄎㄠˋ")
kao_7 = re.compile("ㄎㄠ˙")

ke_space = re.compile("ㄎㄜˉ")
ke_3 = re.compile("ㄎㄜˇ")
ke_4 = re.compile("ㄎㄜˊ")
ke_6 = re.compile("ㄎㄜˋ")
ke_7 = re.compile("ㄎㄜ˙")

ken_space = re.compile("ㄎㄣˉ")
ken_3 = re.compile("ㄎㄣˇ")
ken_4 = re.compile("ㄎㄣˊ")
ken_6 = re.compile("ㄎㄣˋ")
ken_7 = re.compile("ㄎㄣ˙")

keng_space = re.compile("ㄎㄥˉ")
keng_3 = re.compile("ㄎㄥˇ")
keng_4 = re.compile("ㄎㄥˊ")
keng_6 = re.compile("ㄎㄥˋ")
keng_7 = re.compile("ㄎㄥ˙")

kong_space = re.compile("ㄎㄨㄥˉ")
kong_3 = re.compile("ㄎㄨㄥˇ")
kong_4 = re.compile("ㄎㄨㄥˊ")
kong_6 = re.compile("ㄎㄨㄥˋ")
kong_7 = re.compile("ㄎㄨㄥ˙")

kou_space = re.compile("ㄎㄡˉ")
kou_3 = re.compile("ㄎㄡˇ")
kou_4 = re.compile("ㄎㄡˊ")
kou_6 = re.compile("ㄎㄡˋ")
kou_7 = re.compile("ㄎㄡ˙")

ku_space = re.compile("ㄎㄨˉ")
ku_3 = re.compile("ㄎㄨˇ")
ku_4 = re.compile("ㄎㄨˊ")
ku_6 = re.compile("ㄎㄨˋ")
ku_7 = re.compile("ㄎㄨ˙")

kua_space = re.compile("ㄎㄨㄚˉ")
kua_3 = re.compile("ㄎㄨㄚˇ")
kua_4 = re.compile("ㄎㄨㄚˊ")
kua_6 = re.compile("ㄎㄨㄚˋ")
kua_7 = re.compile("ㄎㄨㄚ˙")

kuai_space = re.compile("ㄎㄨㄞˉ")
kuai_3 = re.compile("ㄎㄨㄞˇ")
kuai_4 = re.compile("ㄎㄨㄞˊ")
kuai_6 = re.compile("ㄎㄨㄞˋ")
kuai_7 = re.compile("ㄎㄨㄞ˙")

kuan_space = re.compile("ㄎㄨㄢˉ")
kuan_3 = re.compile("ㄎㄨㄢˇ")
kuan_4 = re.compile("ㄎㄨㄢˊ")
kuan_6 = re.compile("ㄎㄨㄢˋ")
kuan_7 = re.compile("ㄎㄨㄢ˙")

kuang_space = re.compile("ㄎㄨㄤˉ")
kuang_3 = re.compile("ㄎㄨㄤˇ")
kuang_4 = re.compile("ㄎㄨㄤˊ")
kuang_6 = re.compile("ㄎㄨㄤˋ")
kuang_7 = re.compile("ㄎㄨㄤ˙")

kui_space =  re.compile("ㄎㄨㄟˉ")
kui_3 =  re.compile("ㄎㄨㄟˇ")
kui_4 =  re.compile("ㄎㄨㄟˊ")
kui_6 =  re.compile("ㄎㄨㄟˋ")
kui_7 =  re.compile("ㄎㄨㄟ˙")


kun_space =  re.compile("ㄎㄨㄣˉ")
kun_3 =  re.compile("ㄎㄨㄣˇ")
kun_4 =  re.compile("ㄎㄨㄣˊ")
kun_6 =  re.compile("ㄎㄨㄣˋ")
kun_7 =  re.compile("ㄎㄨㄣ˙")

kuo_space =  re.compile("ㄎㄨㄛˉ")
kuo_3 =  re.compile("ㄎㄨㄛˇ")
kuo_4 =  re.compile("ㄎㄨㄛˊ")
kuo_6 =  re.compile("ㄎㄨㄛˋ")
kuo_7 =  re.compile("ㄎㄨㄛ˙")

la_space = re.compile("ㄌㄚˉ")
la_3 = re.compile("ㄌㄚˇ")
la_4 = re.compile("ㄌㄚˊ")
la_6 = re.compile("ㄌㄚˋ")
la_7 = re.compile("ㄌㄚ˙")                    

lai_space = re.compile("ㄌㄞˉ")
lai_3 = re.compile("ㄌㄞˇ")
lai_4 = re.compile("ㄌㄞˊ")
lai_6 = re.compile("ㄌㄞˋ")
lai_7 = re.compile("ㄌㄞ˙")  


lan_space = re.compile("ㄌㄢˉ")
lan_3 = re.compile("ㄌㄢˇ")
lan_4 = re.compile("ㄌㄢˊ")
lan_6 = re.compile("ㄌㄢˋ")
lan_7 = re.compile("ㄌㄢ˙")

lang_space = re.compile("ㄌㄤˉ")
lang_3 = re.compile("ㄌㄤˇ")
lang_4 = re.compile("ㄌㄤˊ")
lang_6 = re.compile("ㄌㄤˋ")
lang_7 = re.compile("ㄌㄤ˙")


lao_space = re.compile("ㄌㄠˉ")
lao_3 = re.compile("ㄌㄠˇ")
lao_4 = re.compile("ㄌㄠˊ")
lao_6 = re.compile("ㄌㄠˋ")
lao_7 = re.compile("ㄌㄠ˙")

le_space = re.compile("ㄌㄜˉ")
le_3 = re.compile("ㄌㄜˇ")
le_4 = re.compile("ㄌㄜˊ")
le_6 = re.compile("ㄌㄜˋ")
le_7 = re.compile("ㄌㄜ˙")

lei_space = re.compile("ㄌㄟˉ")
lei_3 = re.compile("ㄌㄟˇ")
lei_4 = re.compile("ㄌㄟˊ")
lei_6 = re.compile("ㄌㄟˋ")
lei_7 = re.compile("ㄌㄟ˙")

leng_space = re.compile("ㄌㄥˉ")
leng_3 = re.compile("ㄌㄥˇ")
leng_4 = re.compile("ㄌㄥˊ")
leng_6 = re.compile("ㄌㄥˋ")
leng_7 = re.compile("ㄌㄥ˙")



li_space = re.compile("ㄌㄧˉ")
li_3 = re.compile("ㄌㄧˇ")
li_4 = re.compile("ㄌㄧˊ")
li_6 = re.compile("ㄌㄧˋ")
li_7 = re.compile("ㄌㄧ˙")


lia_space = re.compile("ㄌㄧㄚˉ")
lia_3 = re.compile("ㄌㄧㄚˇ")
lia_4 = re.compile("ㄌㄧㄚˊ")
lia_6 = re.compile("ㄌㄧㄚˋ")
lia_7 = re.compile("ㄌㄧㄚ˙")


lian_space	= re.compile("ㄌㄧㄢˉ")
lian_3 = re.compile("ㄌㄧㄢˇ")
lian_4 = re.compile("ㄌㄧㄢˊ")
lian_6 = re.compile("ㄌㄧㄢˋ")
lian_7 = re.compile("ㄌㄧㄢ˙")

liang_space	= re.compile("ㄌㄧㄤˉ")
liang_3 = re.compile("ㄌㄧㄤˇ")
liang_4 = re.compile("ㄌㄧㄤˊ")
liang_6 = re.compile("ㄌㄧㄤˋ")
liang_7 = re.compile("ㄌㄧㄤ˙")

liao_space	= re.compile("ㄌㄧㄠˉ")
liao_3 = re.compile("ㄌㄧㄠˇ")
liao_4 = re.compile("ㄌㄧㄠˊ")
liao_6 = re.compile("ㄌㄧㄠˋ")
liao_7 = re.compile("ㄌㄧㄠ˙")

	

lie_space   = re.compile("ㄌㄧㄝˉ")
lie_3 = re.compile("ㄌㄧㄝˇ")
lie_4 = re.compile("ㄌㄧㄝˊ")
lie_6 = re.compile("ㄌㄧㄝˋ")
lie_7 = re.compile("ㄌㄧㄝ˙")

lin_space = re.compile("ㄌㄧㄣˉ")
lin_3 = re.compile("ㄌㄧㄣˇ")
lin_4 = re.compile("ㄌㄧㄣˊ")
lin_6 = re.compile("ㄌㄧㄣˋ")
lin_7 = re.compile("ㄌㄧㄣ˙")

ling_space      = re.compile("ㄌㄧㄥˉ")
ling_3 = re.compile("ㄌㄧㄥˇ")
ling_4 = re.compile("ㄌㄧㄥˊ")
ling_6 = re.compile("ㄌㄧㄥˋ")
ling_7 = re.compile("ㄌㄧㄥ˙")

liu_space = re.compile("ㄌㄧㄡˉ")
liu_3     = re.compile("ㄌㄧㄡˇ")
liu_4     = re.compile("ㄌㄧㄡˊ")
liu_6     = re.compile("ㄌㄧㄡˋ")
liu_7     = re.compile("ㄌㄧㄡ˙")

long_space = re.compile("ㄌㄨㄥˉ")
long_3     = re.compile("ㄌㄨㄥˇ")
long_4     = re.compile("ㄌㄨㄥˊ")
long_6     = re.compile("ㄌㄨㄥˋ")
long_7     = re.compile("ㄌㄨㄥ˙")


lou_space = re.compile("ㄌㄡˉ")
lou_3     = re.compile("ㄌㄡˇ")
lou_4     = re.compile("ㄌㄡˊ")
lou_6     = re.compile("ㄌㄡˋ")
lou_7     = re.compile("ㄌㄡ˙")

lu_space = re.compile("ㄌㄨˉ")
lu_3     = re.compile("ㄌㄨˇ")
lu_4     = re.compile("ㄌㄨˊ")
lu_6     = re.compile("ㄌㄨˋ")
lu_7     = re.compile("ㄌㄨ˙")

lyu_space = re.compile("ㄌㄩˉ")
lyu_3     = re.compile("ㄌㄩˇ")
lyu_4     = re.compile("ㄌㄩˊ")
lyu_6     = re.compile("ㄌㄩˋ")
lyu_7     = re.compile("ㄌㄩ˙")
#ㄌㄩㄝ
lyue_space = re.compile("ㄌㄩㄝˉ")
lyue_3 = re.compile("ㄌㄩㄝˇ")
lyue_4 = re.compile("ㄌㄩㄝˊ")             
lyue_6 = re.compile("ㄌㄩㄝˋ")
lyue_7 = re.compile("ㄌㄩㄝ˙")
#ㄌㄨㄢ
luan_space = re.compile("ㄌㄨㄢˉ")
luan_3 = re.compile("ㄌㄨㄢˇ")
luan_4 = re.compile("ㄌㄨㄢˊ")             
luan_6 = re.compile("ㄌㄨㄢˋ")
luan_7 = re.compile("ㄌㄨㄢ˙")
#ㄌㄨㄣ
lun_space = re.compile("ㄌㄨㄣˉ")
lun_3 = re.compile("ㄌㄨㄣˇ")
lun_4 = re.compile("ㄌㄨㄣˊ")             
lun_6 = re.compile("ㄌㄨㄣˋ")
lun_7 = re.compile("ㄌㄨㄣ˙")
#ㄌㄠ
luo_space	= re.compile("ㄌㄠˉ")
luo_3	= re.compile("ㄌㄠˇ")
luo_4	= re.compile("ㄌㄠˊ")
luo_6	= re.compile("ㄌㄠˋ")
luo_7	= re.compile("ㄌㄠ˙")
#ㄇㄚ
ma_space	= re.compile("ㄇㄚˉ")
ma_3	= re.compile("ㄇㄚˇ")
ma_4	= re.compile("ㄇㄚˊ")
ma_6	= re.compile("ㄇㄚˋ")
ma_7	= re.compile("ㄇㄚ˙")

#ㄇㄞ

mai_space	= re.compile("ㄇㄞˉ")
mai_3	= re.compile("ㄇㄞˇ")
mai_4	= re.compile("ㄇㄞˊ")
mai_6	= re.compile("ㄇㄞˋ")
mai_7	= re.compile("ㄇㄞ˙")

#ㄇㄢ
man_space= re.compile("ㄇㄢˉ")
man_3	= re.compile("ㄇㄢˇ")
man_4	= re.compile("ㄇㄢˊ")
man_6	= re.compile("ㄇㄢˋ")
man_7	= re.compile("ㄇㄢ˙")

#ㄇㄤ
mang_space= re.compile("ㄇㄤˉ")
mang_3	= re.compile("ㄇㄤˇ")
mang_4	= re.compile("ㄇㄤˊ")
mang_6	= re.compile("ㄇㄤˋ")
mang_7	= re.compile("ㄇㄤ˙")

#ㄇㄠ

mao_space= re.compile("ㄇㄠˉ")
mao_3	= re.compile("ㄇㄠˇ")
mao_4	= re.compile("ㄇㄠˊ")
mao_6	= re.compile("ㄇㄠˋ")
mao_7	= re.compile("ㄇㄠ˙")
#ㄇㄜ

me_space= re.compile("ㄇㄜˉ")
me_3	= re.compile("ㄇㄜˇ")
me_4	= re.compile("ㄇㄜˊ")
me_6	= re.compile("ㄇㄜˋ")
me_7	= re.compile("ㄇㄜ˙")

#ㄇㄟ
mei_space= re.compile("ㄇㄟˉ")
mei_3	= re.compile("ㄇㄟˇ")
mei_4	= re.compile("ㄇㄟˊ")
mei_6	= re.compile("ㄇㄟˋ")
mei_7	= re.compile("ㄇㄟ˙")

#ㄇㄣ
men_space= re.compile("ㄇㄣˉ")
men_3	= re.compile("ㄇㄣˇ")
men_4	= re.compile("ㄇㄣˊ")
men_6	= re.compile("ㄇㄣˋ")
men_7	= re.compile("ㄇㄣ˙")

#ㄇㄥ
meng_space= re.compile("ㄇㄥˉ")
meng_3	= re.compile("ㄇㄥˇ")
meng_4	= re.compile("ㄇㄥˊ")
meng_6	= re.compile("ㄇㄥˋ")
meng_7	= re.compile("ㄇㄥ˙")

#ㄇㄧ
mi_space= re.compile("ㄇㄧˉ")
mi_3	= re.compile("ㄇㄧˇ")
mi_4	= re.compile("ㄇㄧˊ")
mi_6	= re.compile("ㄇㄧˋ")
mi_7	= re.compile("ㄇㄧ˙")

#ㄇㄧㄢ
mian_space= re.compile("ㄇㄧㄢˉ")
mian_3	= re.compile("ㄇㄧㄢˇ")
mian_4	= re.compile("ㄇㄧㄢˊ")
mian_6	= re.compile("ㄇㄧㄢˋ")
mian_7	= re.compile("ㄇㄧㄢ˙")

#ㄇㄧㄠ
miao_space= re.compile("ㄇㄧㄠˉ")
miao_3	= re.compile("ㄇㄧㄠˇ")
miao_4	= re.compile("ㄇㄧㄠˊ")
miao_6	= re.compile("ㄇㄧㄠˋ")
miao_7	= re.compile("ㄇㄧㄠ˙")

#ㄇㄧㄝ
mie_space= re.compile("ㄇㄧㄝˉ")
mie_3	= re.compile("ㄇㄧㄝˇ")
mie_4	= re.compile("ㄇㄧㄝˊ")
mie_6	= re.compile("ㄇㄧㄝˋ")
mie_7	= re.compile("ㄇㄧㄝ˙")

#ㄇㄧㄣ
min_space= re.compile("ㄇㄧㄣˉ")
min_3	= re.compile("ㄇㄧㄣˇ")
min_4	= re.compile("ㄇㄧㄣˊ")
min_6	= re.compile("ㄇㄧㄣˋ")
min_7	= re.compile("ㄇㄧㄣ˙")

#ㄇㄧㄥ
ming_space= re.compile("ㄇㄧㄥˉ")
ming_3	= re.compile("ㄇㄧㄥˇ")
ming_4	= re.compile("ㄇㄧㄥˊ")
ming_6	= re.compile("ㄇㄧㄥˋ")
ming_7	= re.compile("ㄇㄧㄥ˙")

#ㄇㄧㄡ
miu_space= re.compile("ㄇㄧㄡˉ")
miu_3	= re.compile("ㄇㄧㄡˇ")
miu_4	= re.compile("ㄇㄧㄡˊ")
miu_6	= re.compile("ㄇㄧㄡˋ")
miu_7	= re.compile("ㄇㄧㄡ˙")

#ㄇㄛ
mo_space= re.compile("ㄇㄛˉ")
mo_3	= re.compile("ㄇㄛˇ")
mo_4	= re.compile("ㄇㄛˊ")
mo_6	= re.compile("ㄇㄛˋ")
mo_7	= re.compile("ㄇㄛ˙")

#ㄇㄡ
mou_space= re.compile("ㄇㄡˉ")
mou_3	= re.compile("ㄇㄡˇ")
mou_4	= re.compile("ㄇㄡˊ")
mou_6	= re.compile("ㄇㄡˋ")
mou_7	= re.compile("ㄇㄡ˙")

#ㄇㄨ
mu_space= re.compile("ㄇㄨˉ")
mu_3	= re.compile("ㄇㄨˇ")
mu_4	= re.compile("ㄇㄨˊ")
mu_6	= re.compile("ㄇㄨˋ")
mu_7	= re.compile("ㄇㄨ˙")

#ㄋㄚ

na_space= re.compile("ㄋㄚˉ")
na_3	= re.compile("ㄋㄚˇ")
na_4	= re.compile("ㄋㄚˊ")
na_6	= re.compile("ㄋㄚˋ")
na_7	= re.compile("ㄋㄚ˙")
#ㄋㄞ
nai_space= re.compile("ㄋㄞˉ")
nai_3	= re.compile("ㄋㄞˇ")
nai_4	= re.compile("ㄋㄞˊ")
nai_6	= re.compile("ㄋㄞˋ")
nai_7	= re.compile("ㄋㄞ˙")

#ㄋㄞ
nan_space= re.compile("ㄋㄢˉ")
nan_3	= re.compile("ㄋㄢˇ")
nan_4	= re.compile("ㄋㄢˊ")
nan_6	= re.compile("ㄋㄢˋ")
nan_7	= re.compile("ㄋㄢ˙")

#ㄋㄤ
nang_space= re.compile("ㄋㄤˉ")
nang_3	= re.compile("ㄋㄤˇ")
nang_4	= re.compile("ㄋㄤˊ")
nang_6	= re.compile("ㄋㄤˋ")
nang_7	= re.compile("ㄋㄤ˙")


#ㄋㄠ
nao_space= re.compile("ㄋㄠˉ")
nao_3	= re.compile("ㄋㄠˇ")
nao_4	= re.compile("ㄋㄠˊ")
nao_6	= re.compile("ㄋㄠˋ")
nao_7	= re.compile("ㄋㄠ˙")

#ㄋㄜ
ne_space= re.compile("ㄋㄜˉ")
ne_3	= re.compile("ㄋㄜˇ")
ne_4	= re.compile("ㄋㄜˊ")
ne_6	= re.compile("ㄋㄜˋ")
ne_7	= re.compile("ㄋㄜ˙")





#ㄋㄟ
nei_space= re.compile("ㄋㄟˉ")
nei_3	= re.compile("ㄋㄟˇ")
nei_4	= re.compile("ㄋㄟˊ")
nei_6	= re.compile("ㄋㄟˋ")
nei_7	= re.compile("ㄋㄟ˙")

#ㄋㄣ
nen_space= re.compile("ㄋㄣˉ")
nen_3	= re.compile("ㄋㄣˇ")
nen_4	= re.compile("ㄋㄣˊ")
nen_6	= re.compile("ㄋㄣˋ")
nen_7	= re.compile("ㄋㄣ˙")

#ㄋㄥ
neng_space= re.compile("ㄋㄥˉ")
neng_3	= re.compile("ㄋㄥˇ")
neng_4	= re.compile("ㄋㄥˊ")
neng_6	= re.compile("ㄋㄥˋ")
neng_7	= re.compile("ㄋㄥ˙")

#ㄋㄧ
ni_space= re.compile("ㄋㄧˉ")
ni_3	= re.compile("ㄋㄧˇ")
ni_4	= re.compile("ㄋㄧˊ")
ni_6	= re.compile("ㄋㄧˋ")
ni_7	= re.compile("ㄋㄧ˙")


#ㄋㄧㄢ
nian_space= re.compile("ㄋㄧㄢˉ")
nian_3	= re.compile("ㄋㄧㄢˇ")
nian_4	= re.compile("ㄋㄧㄢˊ")
nian_6	= re.compile("ㄋㄧㄢˋ")
nian_7	= re.compile("ㄋㄧㄢ˙")

#ㄋㄧㄤ
niang_space= re.compile("ㄋㄧㄤˉ")
niang_3	= re.compile("ㄋㄧㄤˇ")
niang_4	= re.compile("ㄋㄧㄤˊ")
niang_6	= re.compile("ㄋㄧㄤˋ")
niang_7	= re.compile("ㄋㄧㄤ˙")

#ㄋㄧㄠ
niao_space= re.compile("ㄋㄧㄠˉ")
niao_3	= re.compile("ㄋㄧㄠˇ")
niao_4	= re.compile("ㄋㄧㄠˊ")
niao_6	= re.compile("ㄋㄧㄠˋ")
niao_7	= re.compile("ㄋㄧㄠ˙")

#ㄋㄧㄝ
nie_space= re.compile("ㄋㄧㄝˉ")
nie_3	= re.compile("ㄋㄧㄝˇ")
nie_4	= re.compile("ㄋㄧㄝˊ")
nie_6	= re.compile("ㄋㄧㄝˋ")
nie_7	= re.compile("ㄋㄧㄝ˙")

#ㄋㄧㄣ
nin_space= re.compile("ㄋㄧㄣˉ")
nin_3	= re.compile("ㄋㄧㄣˇ")
nin_4	= re.compile("ㄋㄧㄣˊ")
nin_6	= re.compile("ㄋㄧㄣˋ")
nin_7	= re.compile("ㄋㄧㄣ˙")

#ㄋㄧㄣ
ning_space= re.compile("ㄋㄧㄥˉ")
ning_3	= re.compile("ㄋㄧㄥˇ")
ning_4	= re.compile("ㄋㄧㄥˊ")
ning_6	= re.compile("ㄋㄧㄥˋ")
ning_7	= re.compile("ㄋㄧㄥ˙")


#ㄋㄧㄥ
niu_space= re.compile("ㄋㄧㄡˉ")
niu_3	= re.compile("ㄋㄧㄡˇ")
niu_4	= re.compile("ㄋㄧㄡˊ")
niu_6	= re.compile("ㄋㄧㄡˋ")
niu_7	= re.compile("ㄋㄧㄡ˙")


#ㄋㄨㄥ
nong_space= re.compile("ㄋㄨㄥˉ")
nong_3	= re.compile("ㄋㄨㄥˇ")
nong_4	= re.compile("ㄋㄨㄥˊ")
nong_6	= re.compile("ㄋㄨㄥˋ")
nong_7	= re.compile("ㄋㄨㄥ˙")

#ㄋㄡ
nou_space= re.compile("ㄋㄡˉ")
nou_3	= re.compile("ㄋㄡˇ")
nou_4	= re.compile("ㄋㄡˊ")
nou_6	= re.compile("ㄋㄡˋ")
nou_7	= re.compile("ㄋㄡ˙")


#ㄋㄨ
nu_space= re.compile("ㄋㄨˉ")
nu_3	= re.compile("ㄋㄨˇ")
nu_4	= re.compile("ㄋㄨˊ")
nu_6	= re.compile("ㄋㄨˋ")
nu_7	= re.compile("ㄋㄨ˙")

#ㄋㄩ
nyu_space= re.compile("ㄋㄩˉ")
nyu_3	= re.compile("ㄋㄩˇ")
nyu_4	= re.compile("ㄋㄩˊ")
nyu_6	= re.compile("ㄋㄩˋ")
nyu_7	= re.compile("ㄋㄩ˙")

#ㄋㄨㄢ
nuan_space= re.compile("ㄋㄨㄢˉ")
nuan_3	= re.compile("ㄋㄨㄢˇ")
nuan_4	= re.compile("ㄋㄨㄢˊ")
nuan_6	= re.compile("ㄋㄨㄢˋ")
nuan_7	= re.compile("ㄋㄨㄢ˙")

#ㄋㄨㄛ
nuo_space= re.compile("ㄋㄨㄛˉ")
nuo_3	= re.compile("ㄋㄨㄛˇ")
nuo_4	= re.compile("ㄋㄨㄛˊ")
nuo_6	= re.compile("ㄋㄨㄛˋ")
nuo_7	= re.compile("ㄋㄨㄛ˙")	 	 

#ㄛ
o_space= re.compile("ㄛˉ")
o_3	= re.compile("ㄛˇ")
o_4	= re.compile("ㄛˊ")
o_6	= re.compile("ㄛˋ")
o_7	= re.compile("ㄛ˙")

#ㄡ
ou_space= re.compile("ㄡˉ")
ou_3	= re.compile("ㄡˇ")
ou_4	= re.compile("ㄡˊ")
ou_6	= re.compile("ㄡˋ")
ou_7	= re.compile("ㄡ˙")

#ㄆㄚ
pa_space= re.compile("ㄆㄚˉ")
pa_3	= re.compile("ㄆㄚˇ")
pa_4	= re.compile("ㄆㄚˊ")
pa_6	= re.compile("ㄆㄚˋ")
pa_7	= re.compile("ㄆㄚ˙")	

#ㄆㄞ
pai_space= re.compile("ㄆㄞˉ")
pai_3	= re.compile("ㄆㄞˇ")
pai_4	= re.compile("ㄆㄞˊ")
pai_6	= re.compile("ㄆㄞˋ")
pai_7	= re.compile("ㄆㄞ˙")

#ㄆㄢ
pan_space= re.compile("ㄆㄢˉ")
pan_3	= re.compile("ㄆㄢˇ")
pan_4	= re.compile("ㄆㄢˊ")
pan_6	= re.compile("ㄆㄢˋ")
pan_7	= re.compile("ㄆㄢ˙")	

#ㄆㄤ
pang_space= re.compile("ㄆㄤˉ")
pang_3	= re.compile("ㄆㄤˇ")
pang_4	= re.compile("ㄆㄤˊ")
pang_6	= re.compile("ㄆㄤˋ")
pang_7	= re.compile("ㄆㄤ˙")

#ㄆㄠ
pao_space= re.compile("ㄆㄠˉ")
pao_3	= re.compile("ㄆㄠˇ")
pao_4	= re.compile("ㄆㄠˊ")
pao_6	= re.compile("ㄆㄠˋ")
pao_7	= re.compile("ㄆㄠ˙")

#ㄆㄟ
pei_space= re.compile("ㄆㄟˉ")
pei_3	= re.compile("ㄆㄟˇ")
pei_4	= re.compile("ㄆㄟˊ")
pei_6	= re.compile("ㄆㄟˋ")
pei_7	= re.compile("ㄆㄟ˙")

#ㄆㄣ
pen_space= re.compile("ㄆㄣˉ")
pen_3	= re.compile("ㄆㄣˇ")
pen_4	= re.compile("ㄆㄣˊ")
pen_6	= re.compile("ㄆㄣˋ")
pen_7	= re.compile("ㄆㄣ˙")	

#ㄆㄥ
peng_space= re.compile("ㄆㄥˉ")
peng_3	= re.compile("ㄆㄥˇ")
peng_4	= re.compile("ㄆㄥˊ")
peng_6	= re.compile("ㄆㄥˋ")
peng_7	= re.compile("ㄆㄥ˙")

#ㄆㄧ
pi_space= re.compile("ㄆㄧˉ")
pi_3	= re.compile("ㄆㄧˇ")
pi_4	= re.compile("ㄆㄧˊ")
pi_6	= re.compile("ㄆㄧˋ")
pi_7	= re.compile("ㄆㄧ˙")

#ㄆㄧㄢ
pian_space= re.compile("ㄆㄧㄢˉ")
pian_3	= re.compile("ㄆㄧㄢˇ")
pian_4	= re.compile("ㄆㄧㄢˊ")
pian_6	= re.compile("ㄆㄧㄢˋ")
pian_7	= re.compile("ㄆㄧㄢ˙")

#ㄆㄧㄠ
piao_space= re.compile("ㄆㄧㄠˉ")
piao_3	= re.compile("ㄆㄧㄠˇ")
piao_4	= re.compile("ㄆㄧㄠˊ")
piao_6	= re.compile("ㄆㄧㄠˋ")
piao_7	= re.compile("ㄆㄧㄠ˙")

#ㄆㄧㄝ
pie_space= re.compile("ㄆㄧㄝˉ")
pie_3	= re.compile("ㄆㄧㄝˇ")
pie_4	= re.compile("ㄆㄧㄝˊ")
pie_6	= re.compile("ㄆㄧㄝˋ")
pie_7	= re.compile("ㄆㄧㄝ˙")	

#ㄆㄧㄣ
pin_space= re.compile("ㄆㄧㄣˉ")
pin_3	= re.compile("ㄆㄧㄣˇ")
pin_4	= re.compile("ㄆㄧㄣˊ")
pin_6	= re.compile("ㄆㄧㄣˋ")
pin_7	= re.compile("ㄆㄧㄣ˙")

#ㄆㄧㄥ
ping_space= re.compile("ㄆㄧㄥˉ")
ping_3	= re.compile("ㄆㄧㄥˇ")
ping_4	= re.compile("ㄆㄧㄥˊ")
ping_6	= re.compile("ㄆㄧㄥˋ")
ping_7	= re.compile("ㄆㄧㄥ˙")

#ㄆㄧㄥ
po_space= re.compile("ㄆㄛˉ")
po_3	= re.compile("ㄆㄛˇ")
po_4	= re.compile("ㄆㄛˊ")
po_6	= re.compile("ㄆㄛˋ")
po_7	= re.compile("ㄆㄛ˙")

#ㄆㄡ
pou_space= re.compile("ㄆㄡˉ")
pou_3	= re.compile("ㄆㄡˇ")
pou_4	= re.compile("ㄆㄡˊ")
pou_6	= re.compile("ㄆㄡˋ")
pou_7	= re.compile("ㄆㄡ˙")	

#ㄆㄧㄥ
pu_space= re.compile("ㄆㄨˉ")
pu_3	= re.compile("ㄆㄨˇ")
pu_4	= re.compile("ㄆㄨˊ")
pu_6	= re.compile("ㄆㄨˋ")
pu_7	= re.compile("ㄆㄨ˙")

#ㄑㄧ
qi_space= re.compile("ㄑㄧˉ")
qi_3	= re.compile("ㄑㄧˇ")
qi_4	= re.compile("ㄑㄧˊ")
qi_6	= re.compile("ㄑㄧˋ")
qi_7	= re.compile("ㄑㄧ˙")

#ㄑㄧㄚ
qia_space= re.compile("ㄑㄧㄚˉ")
qia_3	= re.compile("ㄑㄧㄚˇ")
qia_4	= re.compile("ㄑㄧㄚˊ")
qia_6	= re.compile("ㄑㄧㄚˋ")
qia_7	= re.compile("ㄑㄧㄚ˙")

#ㄑㄧㄢ
qian_space= re.compile("ㄑㄧㄢˉ")
qian_3	= re.compile("ㄑㄧㄢˇ")
qian_4	= re.compile("ㄑㄧㄢˊ")
qian_6	= re.compile("ㄑㄧㄢˋ")
qian_7	= re.compile("ㄑㄧㄢ˙")

#ㄑㄧㄤ
qiang_space= re.compile("ㄑㄧㄤˉ")
qiang_3	= re.compile("ㄑㄧㄤˇ")
qiang_4	= re.compile("ㄑㄧㄤˊ")
qiang_6	= re.compile("ㄑㄧㄤˋ")
qiang_7	= re.compile("ㄑㄧㄤ˙")

#ㄑㄧㄠ
qiao_space= re.compile("ㄑㄧㄠˉ")
qiao_3	= re.compile("ㄑㄧㄠˇ")
qiao_4	= re.compile("ㄑㄧㄠˊ")
qiao_6	= re.compile("ㄑㄧㄠˋ")
qiao_7	= re.compile("ㄑㄧㄠ˙")


#ㄑㄧㄝ
qie_space= re.compile("ㄑㄧㄝˉ")
qie_3	= re.compile("ㄑㄧㄝˇ")
qie_4	= re.compile("ㄑㄧㄝˊ")
qie_6	= re.compile("ㄑㄧㄝˋ")
qie_7	= re.compile("ㄑㄧㄝ˙")

#ㄑㄧㄣ
qin_space= re.compile("ㄑㄧㄣˉ")
qin_3	= re.compile("ㄑㄧㄣˇ")
qin_4	= re.compile("ㄑㄧㄣˊ")
qin_6	= re.compile("ㄑㄧㄣˋ")
qin_7	= re.compile("ㄑㄧㄣ˙")

#ㄑㄧㄥ
qing_space= re.compile("ㄑㄧㄥˉ")
qing_3	= re.compile("ㄑㄧㄥˇ")
qing_4	= re.compile("ㄑㄧㄥˊ")
qing_6	= re.compile("ㄑㄧㄥˋ")
qing_7	= re.compile("ㄑㄧㄥ˙")

#ㄑㄩㄥ
qiong_space= re.compile("ㄑㄩㄥˉ")
qiong_3	= re.compile("ㄑㄩㄥˇ")
qiong_4	= re.compile("ㄑㄩㄥˊ")
qiong_6	= re.compile("ㄑㄩㄥˋ")
qiong_7	= re.compile("ㄑㄩㄥ˙")

#ㄑㄧㄡ
qiu_space= re.compile("ㄑㄧㄡˉ")
qiu_3	= re.compile("ㄑㄧㄡˇ")
qiu_4	= re.compile("ㄑㄧㄡˊ")
qiu_6	= re.compile("ㄑㄧㄡˋ")
qiu_7	= re.compile("ㄑㄧㄡ˙")

#ㄑㄩ
qu_space= re.compile("ㄑㄩˉ")
qu_3	= re.compile("ㄑㄩˇ")
qu_4	= re.compile("ㄑㄩˊ")
qu_6	= re.compile("ㄑㄩˋ")
qu_7	= re.compile("ㄑㄩ˙")

#ㄑㄩㄢ
quan_space= re.compile("ㄑㄩㄢˉ")
quan_3	= re.compile("ㄑㄩㄢˇ")
quan_4	= re.compile("ㄑㄩㄢˊ")
quan_6	= re.compile("ㄑㄩㄢˋ")
quan_7	= re.compile("ㄑㄩㄢ˙")


#ㄑㄩㄝ
que_space= re.compile("ㄑㄩㄝˉ")
que_3	= re.compile("ㄑㄩㄝˇ")
que_4	= re.compile("ㄑㄩㄝˊ")
que_6	= re.compile("ㄑㄩㄝˋ")
que_7	= re.compile("ㄑㄩㄝ˙")

#ㄑㄩㄣ
qun_space= re.compile("ㄑㄩㄣˉ")
qun_3	= re.compile("ㄑㄩㄣˇ")
qun_4	= re.compile("ㄑㄩㄣˊ")
qun_6	= re.compile("ㄑㄩㄣˋ")
qun_7	= re.compile("ㄑㄩㄣ˙")


#ㄖㄢ
ran_space= re.compile("ㄖㄢˉ")
ran_3	= re.compile("ㄖㄢˇ")
ran_4	= re.compile("ㄖㄢˊ")
ran_6	= re.compile("ㄖㄢˋ")
ran_7	= re.compile("ㄖㄢ˙")

#ㄖㄤ
rang_space= re.compile("ㄖㄤˉ")
rang_3	= re.compile("ㄖㄤˇ")
rang_4	= re.compile("ㄖㄤˊ")
rang_6	= re.compile("ㄖㄤˋ")
rang_7	= re.compile("ㄖㄤ˙")

#ㄖㄠ
rao_space= re.compile("ㄖㄜˉ")
rao_3	= re.compile("ㄖㄜˇ")
rao_4	= re.compile("ㄖㄜˊ")
rao_6	= re.compile("ㄖㄜˋ")
rao_7	= re.compile("ㄖㄜ˙")

#ㄖㄜ
re_space= re.compile("ㄖㄜˉ")
re_3	= re.compile("ㄖㄜˇ")
re_4	= re.compile("ㄖㄜˊ")
re_6	= re.compile("ㄖㄜˋ")
re_7	= re.compile("ㄖㄜ˙")

#ㄖㄣ
ren_space= re.compile("ㄖㄣˉ")
ren_3	= re.compile("ㄖㄣˇ")
ren_4	= re.compile("ㄖㄣˊ")
ren_6	= re.compile("ㄖㄣˋ")
ren_7	= re.compile("ㄖㄣ˙")

#ㄖㄥ
reng_space= re.compile("ㄖㄥˉ")
reng_3	= re.compile("ㄖㄥˇ")
reng_4	= re.compile("ㄖㄥˊ")
reng_6	= re.compile("ㄖㄥˋ")
reng_7	= re.compile("ㄖㄥ˙")

#ㄖ
ri_space= re.compile("ㄖˉ")
ri_3	= re.compile("ㄖˇ")
ri_4	= re.compile("ㄖˊ")
ri_6	= re.compile("ㄖˋ")
ri_7	= re.compile("ㄖ˙")

#ㄖㄨㄥ
rong_space= re.compile("ㄖㄨㄥˉ")
rong_3	= re.compile("ㄖㄨㄥˇ")
rong_4	= re.compile("ㄖㄨㄥˊ")
rong_6	= re.compile("ㄖㄨㄥˋ")
rong_7	= re.compile("ㄖㄨㄥ˙")

#ㄖㄡ
rou_space= re.compile("ㄖㄡˉ")
rou_3	= re.compile("ㄖㄡˇ")
rou_4	= re.compile("ㄖㄡˊ")
rou_6	= re.compile("ㄖㄡˋ")
rou_7	= re.compile("ㄖㄡ˙")

#ㄖㄨ
ru_space= re.compile("ㄖㄨˉ")
ru_3	= re.compile("ㄖㄨˇ")
ru_4	= re.compile("ㄖㄨˊ")
ru_6	= re.compile("ㄖㄨˋ")
ru_7	= re.compile("ㄖㄨ˙")


#ㄖㄨㄢ
ruan_space= re.compile("ㄖㄨㄢˉ")
ruan_3	= re.compile("ㄖㄨㄢˇ")
ruan_4	= re.compile("ㄖㄨㄢˊ")
ruan_6	= re.compile("ㄖㄨㄢˋ")
ruan_7	= re.compile("ㄖㄨㄢ˙")

#ㄖㄨㄢ
rui_space= re.compile("ㄖㄨㄟˉ")
rui_3	= re.compile("ㄖㄨㄟˇ")
rui_4	= re.compile("ㄖㄨㄟˊ")
rui_6	= re.compile("ㄖㄨㄟˋ")
rui_7	= re.compile("ㄖㄨㄟ˙")

#ㄖㄨㄣ
run_space= re.compile("ㄖㄨㄣˉ")
run_3	= re.compile("ㄖㄨㄣˇ")
run_4	= re.compile("ㄖㄨㄣˊ")
run_6	= re.compile("ㄖㄨㄣˋ")
run_7	= re.compile("ㄖㄨㄣ˙")

#ㄖㄨㄛ
ruo_space= re.compile("ㄖㄨㄛˉ")
ruo_3	= re.compile("ㄖㄨㄛˇ")
ruo_4	= re.compile("ㄖㄨㄛˊ")
ruo_6	= re.compile("ㄖㄨㄛˋ")
ruo_7	= re.compile("ㄖㄨㄛ˙")


#ㄙㄚ
sa_space= re.compile("ㄙㄚˉ")
sa_3	= re.compile("ㄙㄚˇ")
sa_4	= re.compile("ㄙㄚˊ")
sa_6	= re.compile("ㄙㄚˋ")
sa_7	= re.compile("ㄙㄚ˙")

#ㄙㄞ
sai_space= re.compile("ㄙㄞˉ")
sai_3	= re.compile("ㄙㄞˇ")
sai_4	= re.compile("ㄙㄞˊ")
sai_6	= re.compile("ㄙㄞˋ")
sai_7	= re.compile("ㄙㄞ˙")

#ㄙㄢ
san_space= re.compile("ㄙㄢˉ")
san_3	= re.compile("ㄙㄢˇ")
san_4	= re.compile("ㄙㄢˊ")
san_6	= re.compile("ㄙㄢˋ")
san_7	= re.compile("ㄙㄢ˙")

#ㄙㄤ
sang_space= re.compile("ㄙㄤˉ")
sang_3	= re.compile("ㄙㄤˇ")
sang_4	= re.compile("ㄙㄤˊ")
sang_6	= re.compile("ㄙㄤˋ")
sang_7	= re.compile("ㄙㄤ˙")

#ㄙㄠ
sao_space= re.compile("ㄙㄠˉ")
sao_3	= re.compile("ㄙㄠˇ")
sao_4	= re.compile("ㄙㄠˊ")
sao_6	= re.compile("ㄙㄠˋ")
sao_7	= re.compile("ㄙㄠ˙")

#ㄙㄜ
se_space= re.compile("ㄙㄜˉ")
se_3	= re.compile("ㄙㄜˇ")
se_4	= re.compile("ㄙㄜˊ")
se_6	= re.compile("ㄙㄜˋ")
se_7	= re.compile("ㄙㄜ˙")

#ㄙㄣ
sen_space= re.compile("ㄙㄣˉ")
sen_3	= re.compile("ㄙㄣˇ")
sen_4	= re.compile("ㄙㄣˊ")
sen_6	= re.compile("ㄙㄣˋ")
sen_7	= re.compile("ㄙㄣ˙")

#ㄙㄣ
seng_space= re.compile("ㄙㄥˉ")
seng_3	= re.compile("ㄙㄥˇ")
seng_4	= re.compile("ㄙㄥˊ")
seng_6	= re.compile("ㄙㄥˋ")
seng_7	= re.compile("ㄙㄥ˙")

#ㄙㄣ
sha_space= re.compile("ㄕㄚˉ")
sha_3	= re.compile("ㄕㄚˇ")
sha_4	= re.compile("ㄕㄚˊ")
sha_6	= re.compile("ㄕㄚˋ")
sha_7	= re.compile("ㄕㄚ˙")

#ㄕㄞ
shai_space= re.compile("ㄕㄞˉ")
shai_3	= re.compile("ㄕㄞˇ")
shai_4	= re.compile("ㄕㄞˊ")
shai_6	= re.compile("ㄕㄞˋ")
shai_7	= re.compile("ㄕㄞ˙")

#ㄕㄢ
shan_space= re.compile("ㄕㄢˉ")
shan_3	= re.compile("ㄕㄢˇ")
shan_4	= re.compile("ㄕㄢˊ")
shan_6	= re.compile("ㄕㄢˋ")
shan_7	= re.compile("ㄕㄢ˙")

#ㄕㄤ
shang_space= re.compile("ㄕㄤˉ")
shang_3	= re.compile("ㄕㄤˇ")
shang_4	= re.compile("ㄕㄤˊ")
shang_6	= re.compile("ㄕㄤˋ")
shang_7	= re.compile("ㄕㄤ˙")

#ㄕㄠ
shao_space= re.compile("ㄕㄠˉ")
shao_3	= re.compile("ㄕㄠˇ")
shao_4	= re.compile("ㄕㄠˊ")
shao_6	= re.compile("ㄕㄠˋ")
shao_7	= re.compile("ㄕㄠ˙")

#ㄕㄜ
she_space= re.compile("ㄕㄜˉ")
she_3	= re.compile("ㄕㄜˇ")
she_4	= re.compile("ㄕㄜˊ")
she_6	= re.compile("ㄕㄜˋ")
she_7	= re.compile("ㄕㄜ˙")

#ㄕㄨㄟ
shei_space= re.compile("ㄕㄨㄟˉ")
shei_3	= re.compile("ㄕㄨㄟˇ")
shei_4	= re.compile("ㄕㄨㄟˊ")
shei_6	= re.compile("ㄕㄨㄟˋ")
shei_7	= re.compile("ㄕㄨㄟ˙")

#ㄕㄣ
shen_space= re.compile("ㄕㄣˉ")
shen_3	= re.compile("ㄕㄣˇ")
shen_4	= re.compile("ㄕㄣˊ")
shen_6	= re.compile("ㄕㄣˋ")
shen_7	= re.compile("ㄕㄣ˙")

#ㄕㄥ
sheng_space= re.compile("ㄕㄥˉ")
sheng_3	= re.compile("ㄕㄥˇ")
sheng_4	= re.compile("ㄕㄥˊ")
sheng_6	= re.compile("ㄕㄥˋ")
sheng_7	= re.compile("ㄕㄥ˙")

#ㄕ
shi_space= re.compile("ㄕˉ")
shi_3	= re.compile("ㄕˇ")
shi_4	= re.compile("ㄕˊ")
shi_6	= re.compile("ㄕˋ")
shi_7	= re.compile("ㄕ˙")

#ㄕㄡ
shou_space= re.compile("ㄕㄡˉ")
shou_3	= re.compile("ㄕㄡˇ")
shou_4	= re.compile("ㄕㄡˊ")
shou_6	= re.compile("ㄕㄡˋ")
shou_7	= re.compile("ㄕㄡ˙")

#ㄕㄨ
shu_space= re.compile("ㄕㄨˉ")
shu_3	= re.compile("ㄕㄨˇ")
shu_4	= re.compile("ㄕㄨˊ")
shu_6	= re.compile("ㄕㄨˋ")
shu_7	= re.compile("ㄕㄨ˙")

#ㄕㄨㄚ
shua_space= re.compile("ㄕㄨㄚˉ")
shua_3	= re.compile("ㄕㄨㄚˇ")
shua_4	= re.compile("ㄕㄨㄚˊ")
shua_6	= re.compile("ㄕㄨㄚˋ")
shua_7	= re.compile("ㄕㄨㄚ˙")


#ㄕㄨㄞ
shuai_space= re.compile("ㄕㄨㄞˉ")
shuai_3	= re.compile("ㄕㄨㄞˇ")
shuai_4	= re.compile("ㄕㄨㄞˊ")
shuai_6	= re.compile("ㄕㄨㄞˋ")
shuai_7	= re.compile("ㄕㄨㄞ˙")

#ㄕㄨㄢ
shuan_space= re.compile("ㄕㄨㄢˉ")
shuan_3	= re.compile("ㄕㄨㄢˇ")
shuan_4	= re.compile("ㄕㄨㄢˊ")
shuan_6	= re.compile("ㄕㄨㄢˋ")
shuan_7	= re.compile("ㄕㄨㄢ˙")

#ㄕㄨㄤ
shuang_space= re.compile("ㄕㄨㄤˉ")
shuang_3	= re.compile("ㄕㄨㄤˇ")
shuang_4	= re.compile("ㄕㄨㄤˊ")
shuang_6	= re.compile("ㄕㄨㄤˋ")
shuang_7	= re.compile("ㄕㄨㄤ˙")

#ㄕㄨㄟ
shui_space= re.compile("ㄕㄨㄟˉ")
shui_3	= re.compile("ㄕㄨㄟˇ")
shui_4	= re.compile("ㄕㄨㄟˊ")
shui_6	= re.compile("ㄕㄨㄟˋ")
shui_7	= re.compile("ㄕㄨㄟ˙")

#ㄕㄨㄣ
shun_space= re.compile("ㄕㄨㄣˉ")
shun_3	= re.compile("ㄕㄨㄣˇ")
shun_4	= re.compile("ㄕㄨㄣˊ")
shun_6	= re.compile("ㄕㄨㄣˋ")
shun_7	= re.compile("ㄕㄨㄣ˙")

#ㄕㄨㄛ
shuo_space= re.compile("ㄕㄨㄛˉ")
shuo_3	= re.compile("ㄕㄨㄛˇ")
shuo_4	= re.compile("ㄕㄨㄛˊ")
shuo_6	= re.compile("ㄕㄨㄛˋ")
shuo_7	= re.compile("ㄕㄨㄛ˙")

#ㄙ
si_space= re.compile("ㄙˉ")
si_3	= re.compile("ㄙˇ")
si_4	= re.compile("ㄙˊ")
si_6	= re.compile("ㄙˋ")
si_7	= re.compile("ㄙ˙")

#ㄙㄨㄥ
song_space= re.compile("ㄙㄨㄥˉ")
song_3	= re.compile("ㄙㄨㄥˇ")
song_4	= re.compile("ㄙㄨㄥˊ")
song_6	= re.compile("ㄙㄨㄥˋ")
song_7	= re.compile("ㄙㄨㄥ˙")

#ㄙㄡ
sou_space= re.compile("ㄙㄡˉ")
sou_3	= re.compile("ㄙㄡˇ")
sou_4	= re.compile("ㄙㄡˊ")
sou_6	= re.compile("ㄙㄡˋ")
sou_7	= re.compile("ㄙㄡ˙")

#ㄙㄨ
su_space= re.compile("ㄙㄨˉ")
su_3	= re.compile("ㄙㄨˇ")
su_4	= re.compile("ㄙㄨˊ")
su_6	= re.compile("ㄙㄨˋ")
su_7	= re.compile("ㄙㄨ˙")

#ㄙㄨㄢ
suan_space= re.compile("ㄙㄨㄢˉ")
suan_3	= re.compile("ㄙㄨㄢˇ")
suan_4	= re.compile("ㄙㄨㄢˊ")
suan_6	= re.compile("ㄙㄨㄢˋ")
suan_7	= re.compile("ㄙㄨㄢ˙")

#ㄙㄨㄢ
sui_space= re.compile("ㄙㄨㄟˉ")
sui_3	= re.compile("ㄙㄨㄟˇ")
sui_4	= re.compile("ㄙㄨㄟˊ")
sui_6	= re.compile("ㄙㄨㄟˋ")
sui_7	= re.compile("ㄙㄨㄟ˙")

#ㄙㄨㄣ
sun_space= re.compile("ㄙㄨㄣˉ")
sun_3	= re.compile("ㄙㄨㄣˇ")
sun_4	= re.compile("ㄙㄨㄣˊ")
sun_6	= re.compile("ㄙㄨㄣˋ")
sun_7	= re.compile("ㄙㄨㄣ˙")

#ㄙㄨㄣ
suo_space= re.compile("ㄙㄨㄛˉ")
suo_3	= re.compile("ㄙㄨㄛˇ")
suo_4	= re.compile("ㄙㄨㄛˊ")
suo_6	= re.compile("ㄙㄨㄛˋ")
suo_7	= re.compile("ㄙㄨㄛ˙")

#ㄊㄚ
ta_space= re.compile("ㄊㄚˉ")
ta_3	= re.compile("ㄊㄚˇ")
ta_4	= re.compile("ㄊㄚˊ")
ta_6	= re.compile("ㄊㄚˋ")
ta_7	= re.compile("ㄊㄚ˙")

#ㄊㄞ
tai_space= re.compile("ㄊㄞˉ")
tai_3	= re.compile("ㄊㄞˇ")
tai_4	= re.compile("ㄊㄞˊ")
tai_6	= re.compile("ㄊㄞˋ")
tai_7	= re.compile("ㄊㄞ˙")

#ㄊㄢ
tan_space= re.compile("ㄊㄢˉ")
tan_3	= re.compile("ㄊㄢˇ")
tan_4	= re.compile("ㄊㄢˊ")
tan_6	= re.compile("ㄊㄢˋ")
tan_7	= re.compile("ㄊㄢ˙")

#ㄊㄤ
tang_space= re.compile("ㄊㄤˉ")
tang_3	= re.compile("ㄊㄤˇ")
tang_4	= re.compile("ㄊㄤˊ")
tang_6	= re.compile("ㄊㄤˋ")
tang_7	= re.compile("ㄊㄤ˙")

#ㄊㄠ
tao_space= re.compile("ㄊㄠˉ")
tao_3	= re.compile("ㄊㄠˇ")
tao_4	= re.compile("ㄊㄠˊ")
tao_6	= re.compile("ㄊㄠˋ")
tao_7	= re.compile("ㄊㄠ˙")


#ㄊㄜ
te_space= re.compile("ㄊㄜˉ")
te_3	= re.compile("ㄊㄜˇ")
te_4	= re.compile("ㄊㄜˊ")
te_6	= re.compile("ㄊㄜˋ")
te_7	= re.compile("ㄊㄜ˙")

#ㄊㄥ
teng_space= re.compile("ㄊㄥˉ")
teng_3	= re.compile("ㄊㄥˇ")
teng_4	= re.compile("ㄊㄥˊ")
teng_6	= re.compile("ㄊㄥˋ")
teng_7	= re.compile("ㄊㄥ˙")

#ㄊㄥ
ti_space= re.compile("ㄊㄧˉ")
ti_3	= re.compile("ㄊㄧˇ")
ti_4	= re.compile("ㄊㄧˊ")
ti_6	= re.compile("ㄊㄧˋ")
ti_7	= re.compile("ㄊㄧ˙")

#ㄊㄥ
tian_space= re.compile("ㄊㄧㄢˉ")
tian_3	= re.compile("ㄊㄧㄢˇ")
tian_4	= re.compile("ㄊㄧㄢˊ")
tian_6	= re.compile("ㄊㄧㄢˋ")
tian_7	= re.compile("ㄊㄧㄢ˙")

#ㄊㄧㄠ
tiao_space= re.compile("ㄊㄧㄠˉ")
tiao_3	= re.compile("ㄊㄧㄠˇ")
tiao_4	= re.compile("ㄊㄧㄠˊ")
tiao_6	= re.compile("ㄊㄧㄠˋ")
tiao_7	= re.compile("ㄊㄧㄠ˙")

#ㄊㄧㄝ
tie_space= re.compile("ㄊㄧㄝˉ")
tie_3	= re.compile("ㄊㄧㄝˇ")
tie_4	= re.compile("ㄊㄧㄝˊ")
tie_6	= re.compile("ㄊㄧㄝˋ")
tie_7	= re.compile("ㄊㄧㄝ˙")

#ㄊㄧㄥ
ting_space= re.compile("ㄊㄧㄥˉ")
ting_3	= re.compile("ㄊㄧㄥˇ")
ting_4	= re.compile("ㄊㄧㄥˊ")
ting_6	= re.compile("ㄊㄧㄥˋ")
ting_7	= re.compile("ㄊㄧㄥ˙")

#ㄊㄨㄥ
tong_space= re.compile("ㄊㄨㄥˉ")
tong_3	= re.compile("ㄊㄨㄥˇ")
tong_4	= re.compile("ㄊㄨㄥˊ")
tong_6	= re.compile("ㄊㄨㄥˋ")
tong_7	= re.compile("ㄊㄨㄥ˙")

#ㄊㄡ
tou_space= re.compile("ㄊㄡˉ")
tou_3	= re.compile("ㄊㄡˇ")
tou_4	= re.compile("ㄊㄡˊ")
tou_6	= re.compile("ㄊㄡˋ")
tou_7	= re.compile("ㄊㄡ˙")

#ㄊㄨ
tu_space= re.compile("ㄊㄨˉ")
tu_3	= re.compile("ㄊㄨˇ")
tu_4	= re.compile("ㄊㄨˊ")
tu_6	= re.compile("ㄊㄨˋ")
tu_7	= re.compile("ㄊㄨ˙")

#ㄊㄨㄢ
tuan_space= re.compile("ㄊㄨㄢˉ")
tuan_3	= re.compile("ㄊㄨㄢˇ")
tuan_4	= re.compile("ㄊㄨㄢˊ")
tuan_6	= re.compile("ㄊㄨㄢˋ")
tuan_7	= re.compile("ㄊㄨㄢ˙")

#ㄊㄨㄟ
tui_space= re.compile("ㄊㄨㄟˉ")
tui_3	= re.compile("ㄊㄨㄟˇ")
tui_4	= re.compile("ㄊㄨㄟˊ")
tui_6	= re.compile("ㄊㄨㄟˋ")
tui_7	= re.compile("ㄊㄨㄟ˙")

#ㄊㄨㄣ
tun_space= re.compile("ㄊㄨㄣˉ")
tun_3	= re.compile("ㄊㄨㄣˇ")
tun_4	= re.compile("ㄊㄨㄣˊ")
tun_6	= re.compile("ㄊㄨㄣˋ")
tun_7	= re.compile("ㄊㄨㄣ˙")

#ㄊㄨㄛ
tuo_space= re.compile("ㄊㄨㄣˉ")
tuo_3	= re.compile("ㄊㄨㄣˇ")
tuo_4	= re.compile("ㄊㄨㄣˊ")
tuo_6	= re.compile("ㄊㄨㄣˋ")
tuo_7	= re.compile("ㄊㄨㄣ˙")

#ㄨㄚ
wa_space= re.compile("ㄨㄚˉ")
wa_3	= re.compile("ㄨㄚˇ")
wa_4	= re.compile("ㄨㄚˊ")
wa_6	= re.compile("ㄨㄚˋ")
wa_7	= re.compile("ㄨㄚ˙")

#ㄨㄞ
wai_space= re.compile("ㄨㄞˉ")
wai_3	= re.compile("ㄨㄞˇ")
wai_4	= re.compile("ㄨㄞˊ")
wai_6	= re.compile("ㄨㄞˋ")
wai_7	= re.compile("ㄨㄞ˙")

#ㄨㄢ
wan_space= re.compile("ㄨㄢˉ")
wan_3	= re.compile("ㄨㄢˇ")
wan_4	= re.compile("ㄨㄢˊ")
wan_6	= re.compile("ㄨㄢˋ")
wan_7	= re.compile("ㄨㄢ˙")

#ㄨㄤ
wang_space= re.compile("ㄨㄤˉ")
wang_3	= re.compile("ㄨㄤˇ")
wang_4	= re.compile("ㄨㄤˊ")
wang_6	= re.compile("ㄨㄤˋ")
wang_7	= re.compile("ㄨㄤ˙")

#ㄨㄟ
wei_space= re.compile("ㄨㄟˉ")
wei_3	= re.compile("ㄨㄟˇ")
wei_4	= re.compile("ㄨㄟˊ")
wei_6	= re.compile("ㄨㄟˋ")
wei_7	= re.compile("ㄨㄟ˙")

#ㄨㄟ
wen_space= re.compile("ㄨㄣˉ")
wen_3	= re.compile("ㄨㄣˇ")
wen_4	= re.compile("ㄨㄣˊ")
wen_6	= re.compile("ㄨㄣˋ")
wen_7	= re.compile("ㄨㄣ˙")

#ㄨㄥ
weng_space= re.compile("ㄨㄥˉ")
weng_3	= re.compile("ㄨㄥˇ")
weng_4	= re.compile("ㄨㄥˊ")
weng_6	= re.compile("ㄨㄥˋ")
weng_7	= re.compile("ㄨㄥ˙")

#ㄨㄥ
wo_space= re.compile("ㄨㄛˉ")
wo_3	= re.compile("ㄨㄛˇ")
wo_4	= re.compile("ㄨㄛˊ")
wo_6	= re.compile("ㄨㄛˋ")
wo_7	= re.compile("ㄨㄛ˙")

#ㄨ
wu_space= re.compile("ㄨˉ")
wu_3	= re.compile("ㄨˇ")
wu_4	= re.compile("ㄨˊ")
wu_6	= re.compile("ㄨˋ")
wu_7	= re.compile("ㄨ˙")

#ㄒㄧ
xi_space= re.compile("ㄒㄧˉ")
xi_3	= re.compile("ㄒㄧˇ")
xi_4	= re.compile("ㄒㄧˊ")
xi_6	= re.compile("ㄒㄧˋ")
xi_7	= re.compile("ㄒㄧ˙")

#ㄒㄧㄚ
xia_space= re.compile("ㄒㄧㄚˉ")
xia_3	= re.compile("ㄒㄧㄚˇ")
xia_4	= re.compile("ㄒㄧㄚˊ")
xia_6	= re.compile("ㄒㄧㄚˋ")
xia_7	= re.compile("ㄒㄧㄚ˙")
	
#ㄒㄧㄢ
xian_space= re.compile("ㄒㄧㄢˉ")
xian_3	= re.compile("ㄒㄧㄢˇ")
xian_4	= re.compile("ㄒㄧㄢˊ")
xian_6	= re.compile("ㄒㄧㄢˋ")
xian_7	= re.compile("ㄒㄧㄢ˙")



#ㄒㄧㄤ
xiang_space= re.compile("ㄒㄧㄤˉ")
xiang_3	= re.compile("ㄒㄧㄤˇ")
xiang_4	= re.compile("ㄒㄧㄤˊ")
xiang_6	= re.compile("ㄒㄧㄤˋ")
xiang_7	= re.compile("ㄒㄧㄤ˙")

#ㄒㄧㄠ
xiao_space= re.compile("ㄒㄧㄠˉ")
xiao_3	= re.compile("ㄒㄧㄠˇ")
xiao_4	= re.compile("ㄒㄧㄠˊ")
xiao_6	= re.compile("ㄒㄧㄠˋ")
xiao_7	= re.compile("ㄒㄧㄠ˙")

#ㄒㄧㄝ
xie_space= re.compile("ㄒㄧㄝˉ")
xie_3	= re.compile("ㄒㄧㄝˇ")
xie_4	= re.compile("ㄒㄧㄝˊ")
xie_6	= re.compile("ㄒㄧㄝˋ")
xie_7	= re.compile("ㄒㄧㄝ˙")

#ㄒㄧㄣ
xin_space= re.compile("ㄒㄧㄣˉ")
xin_3	= re.compile("ㄒㄧㄣˇ")
xin_4	= re.compile("ㄒㄧㄣˊ")
xin_6	= re.compile("ㄒㄧㄣˋ")
xin_7	= re.compile("ㄒㄧㄣ˙")

#ㄒㄧㄥ
xing_space= re.compile("ㄒㄧㄥˉ")
xing_3	= re.compile("ㄒㄧㄥˇ")
xing_4	= re.compile("ㄒㄧㄥˊ")
xing_6	= re.compile("ㄒㄧㄥˋ")
xing_7	= re.compile("ㄒㄧㄥ˙")

#ㄒㄩㄥ
xiong_space= re.compile("ㄒㄩㄥˉ")
xiong_3	= re.compile("ㄒㄩㄥˇ")
xiong_4	= re.compile("ㄒㄩㄥˊ")
xiong_6	= re.compile("ㄒㄩㄥˋ")
xiong_7	= re.compile("ㄒㄩㄥ˙")

#ㄒㄧㄡ
xiu_space= re.compile("ㄒㄧㄡˉ")
xiu_3	= re.compile("ㄒㄧㄡˇ")
xiu_4	= re.compile("ㄒㄧㄡˊ")
xiu_6	= re.compile("ㄒㄧㄡˋ")
xiu_7	= re.compile("ㄒㄧㄡ˙")

#ㄒㄩ
xu_space= re.compile("ㄒㄩˉ")
xu_3	= re.compile("ㄒㄩˇ")
xu_4	= re.compile("ㄒㄩˊ")
xu_6	= re.compile("ㄒㄩˋ")
xu_7	= re.compile("ㄒㄩ˙")

#ㄒㄩㄢ
xuan_space= re.compile("ㄒㄩㄢˉ")
xuan_3	= re.compile("ㄒㄩㄢˇ")
xuan_4	= re.compile("ㄒㄩㄢˊ")
xuan_6	= re.compile("ㄒㄩㄢˋ")
xuan_7	= re.compile("ㄒㄩㄢ˙")

#ㄒㄩㄝ
xue_space= re.compile("ㄒㄩㄝˉ")
xue_3	= re.compile("ㄒㄩㄝˇ")
xue_4	= re.compile("ㄒㄩㄝˊ")
xue_6	= re.compile("ㄒㄩㄝˋ")
xue_7	= re.compile("ㄒㄩㄝ˙")

#ㄒㄩㄣ
xun_space= re.compile("ㄒㄩㄣˉ")
xun_3	= re.compile("ㄒㄩㄣˇ")
xun_4	= re.compile("ㄒㄩㄣˊ")
xun_6	= re.compile("ㄒㄩㄣˋ")
xun_7	= re.compile("ㄒㄩㄣ˙")

#ㄧㄚ
ya_space= re.compile("ㄧㄚˉ")
ya_3	= re.compile("ㄧㄚˇ")
ya_4	= re.compile("ㄧㄚˊ")
ya_6	= re.compile("ㄧㄚˋ")
ya_7	= re.compile("ㄧㄚ˙")

#ㄧㄢ
yan_space= re.compile("ㄧㄢˉ")
yan_3	= re.compile("ㄧㄢˇ")
yan_4	= re.compile("ㄧㄢˊ")
yan_6	= re.compile("ㄧㄢˋ")
yan_7	= re.compile("ㄧㄢ˙")

#ㄧㄤ
yang_space= re.compile("ㄧㄤˉ")
yang_3	= re.compile("ㄧㄤˇ")
yang_4	= re.compile("ㄧㄤˊ")
yang_6	= re.compile("ㄧㄤˋ")
yang_7	= re.compile("ㄧㄤ˙")

#ㄧㄠ
yao_space= re.compile("ㄧㄠˉ")
yao_3	= re.compile("ㄧㄠˇ")
yao_4	= re.compile("ㄧㄠˊ")
yao_6	= re.compile("ㄧㄠˋ")
yao_7	= re.compile("ㄧㄠ˙")

#ㄧㄝ
ye_space= re.compile("ㄧㄝˉ")
ye_3	= re.compile("ㄧㄝˇ")
ye_4	= re.compile("ㄧㄝˊ")
ye_6	= re.compile("ㄧㄝˋ")
ye_7	= re.compile("ㄧㄝ˙")

#ㄧㄝ
yi_space= re.compile("ㄧˉ")
yi_3	= re.compile("ㄧˇ")
yi_4	= re.compile("ㄧˊ")
yi_6	= re.compile("ㄧˋ")
yi_7	= re.compile("ㄧ˙")

#ㄧㄣ
yin_space= re.compile("ㄧㄣˉ")
yin_3	= re.compile("ㄧㄣˇ")
yin_4	= re.compile("ㄧㄣˊ")
yin_6	= re.compile("ㄧㄣˋ")
yin_7	= re.compile("ㄧㄣ˙")

#ㄧㄥ
ying_space= re.compile("ㄧㄥˉ")
ying_3	= re.compile("ㄧㄥˇ")
ying_4	= re.compile("ㄧㄥˊ")
ying_6	= re.compile("ㄧㄥˋ")
ying_7	= re.compile("ㄧㄥ˙")

#ㄧㄛ
yo_space= re.compile("ㄧㄛˉ")
yo_3	= re.compile("ㄧㄛˇ")
yo_4	= re.compile("ㄧㄛˊ")
yo_6	= re.compile("ㄧㄛˋ")
yo_7	= re.compile("ㄧㄛ˙")

#ㄧㄛ
yong_space= re.compile("ㄩㄥˉ")
yong_3	= re.compile("ㄩㄥˇ")
yong_4	= re.compile("ㄩㄥˊ")
yong_6	= re.compile("ㄩㄥˋ")
yong_7	= re.compile("ㄩㄥ˙")

#ㄧㄛ
you_space= re.compile("ㄧㄡˉ")
you_3	= re.compile("ㄧㄡˇ")
you_4	= re.compile("ㄧㄡˊ")
you_6	= re.compile("ㄧㄡˋ")
you_7	= re.compile("ㄧㄡ˙")

#ㄩ
yu_space= re.compile("ㄩˉ")
yu_3	= re.compile("ㄩˇ")
yu_4	= re.compile("ㄩˊ")
yu_6	= re.compile("ㄩˋ")
yu_7	= re.compile("ㄩ˙")

#ㄩㄢ
yuan_space= re.compile("ㄩㄢˉ")
yuan_3	= re.compile("ㄩㄢˇ")
yuan_4	= re.compile("ㄩㄢˊ")
yuan_6	= re.compile("ㄩㄢˋ")
yuan_7	= re.compile("ㄩㄢ˙")

#ㄩㄝ
yue_space= re.compile("ㄩㄝˉ")
yue_3	= re.compile("ㄩㄝˇ")
yue_4	= re.compile("ㄩㄝˊ")
yue_6	= re.compile("ㄩㄝˋ")
yue_7	= re.compile("ㄩㄝ˙")

#ㄩㄣ
yun_space= re.compile("ㄩㄣˉ")
yun_3	= re.compile("ㄩㄣˇ")
yun_4	= re.compile("ㄩㄣˊ")
yun_6	= re.compile("ㄩㄣˋ")
yun_7	= re.compile("ㄩㄣ˙")

#ㄗㄚ
za_space= re.compile("ㄗㄚˉ")
za_3	= re.compile("ㄗㄚˇ")
za_4	= re.compile("ㄗㄚˊ")
za_6	= re.compile("ㄗㄚˋ")
za_7	= re.compile("ㄗㄚ˙")

#ㄗㄚ
zai_space= re.compile("ㄗㄞˉ")
zai_3	= re.compile("ㄗㄞˇ")
zai_4	= re.compile("ㄗㄞˊ")
zai_6	= re.compile("ㄗㄞˋ")
zai_7	= re.compile("ㄗㄞ˙")

#ㄗㄢ
zan_space= re.compile("ㄗㄢˉ")
zan_3	= re.compile("ㄗㄢˇ")
zan_4	= re.compile("ㄗㄢˊ")
zan_6	= re.compile("ㄗㄢˋ")
zan_7	= re.compile("ㄗㄢ˙")

#ㄗㄤ
zang_space= re.compile("ㄗㄤˉ")
zang_3	= re.compile("ㄗㄤˇ")
zang_4	= re.compile("ㄗㄤˊ")
zang_6	= re.compile("ㄗㄤˋ")
zang_7	= re.compile("ㄗㄤ˙")

#ㄗㄠ
zao_space= re.compile("ㄗㄠˉ")
zao_3	= re.compile("ㄗㄠˇ")
zao_4	= re.compile("ㄗㄠˊ")
zao_6	= re.compile("ㄗㄠˋ")
zao_7	= re.compile("ㄗㄠ˙")

#ㄗㄜ
ze_space= re.compile("ㄗㄜˉ")
ze_3	= re.compile("ㄗㄜˇ")
ze_4	= re.compile("ㄗㄜˊ")
ze_6	= re.compile("ㄗㄜˋ")
ze_7	= re.compile("ㄗㄜ˙")

#ㄗㄟ
zei_space= re.compile("ㄗㄟˉ")
zei_3	= re.compile("ㄗㄟˇ")
zei_4	= re.compile("ㄗㄟˊ")
zei_6	= re.compile("ㄗㄟˋ")
zei_7	= re.compile("ㄗㄟ˙")

#ㄗㄣ
zen_space= re.compile("ㄗㄣˉ")
zen_3	= re.compile("ㄗㄣˇ")
zen_4	= re.compile("ㄗㄣˊ")
zen_6	= re.compile("ㄗㄣˋ")
zen_7	= re.compile("ㄗㄣ˙")

#ㄗㄥ
zeng_space= re.compile("ㄗㄥˉ")
zeng_3	= re.compile("ㄗㄥˇ")
zeng_4	= re.compile("ㄗㄥˊ")
zeng_6	= re.compile("ㄗㄥˋ")
zeng_7	= re.compile("ㄗㄥ˙")

#ㄗㄥ
zeng_space= re.compile("ㄗㄥˉ")
zeng_3	= re.compile("ㄗㄥˇ")
zeng_4	= re.compile("ㄗㄥˊ")
zeng_6	= re.compile("ㄗㄥˋ")
zeng_7	= re.compile("ㄗㄥ˙")

#ㄓㄚ
zha_space= re.compile("ㄓㄚˉ")
zha_3	= re.compile("ㄓㄚˇ")
zha_4	= re.compile("ㄓㄚˊ")
zha_6	= re.compile("ㄓㄚˋ")
zha_7	= re.compile("ㄓㄚ˙")

#ㄓㄚ
zhai_space= re.compile("ㄓㄞˉ")
zhai_3	= re.compile("ㄓㄞˇ")
zhai_4	= re.compile("ㄓㄞˊ")
zhai_6	= re.compile("ㄓㄞˋ")
zhai_7	= re.compile("ㄓㄞ˙")

#ㄓㄢ
zhan_space= re.compile("ㄓㄢˉ")
zhan_3	= re.compile("ㄓㄢˇ")
zhan_4	= re.compile("ㄓㄢˊ")
zhan_6	= re.compile("ㄓㄢˋ")
zhan_7	= re.compile("ㄓㄢ˙")

#ㄓㄤ
zhang_space= re.compile("ㄓㄤˉ")
zhang_3	= re.compile("ㄓㄤˇ")
zhang_4	= re.compile("ㄓㄤˊ")
zhang_6	= re.compile("ㄓㄤˋ")
zhang_7	= re.compile("ㄓㄤ˙")

#ㄓㄠ
zhao_space= re.compile("ㄓㄠˉ")
zhao_3	= re.compile("ㄓㄠˇ")
zhao_4	= re.compile("ㄓㄠˊ")
zhao_6	= re.compile("ㄓㄠˋ")
zhao_7	= re.compile("ㄓㄠ˙")

#ㄓㄜ
zhe_space= re.compile("ㄓㄜˉ")
zhe_3	= re.compile("ㄓㄜˇ")
zhe_4	= re.compile("ㄓㄜˊ")
zhe_6	= re.compile("ㄓㄜˋ")
zhe_7	= re.compile("ㄓㄜ˙")

#ㄓㄣ
zhen_space= re.compile("ㄓㄣˉ")
zhen_3	= re.compile("ㄓㄣˇ")
zhen_4	= re.compile("ㄓㄣˊ")
zhen_6	= re.compile("ㄓㄣˋ")
zhen_7	= re.compile("ㄓㄣ˙")

#ㄓㄥ
zheng_space= re.compile("ㄓㄥˉ")
zheng_3	= re.compile("ㄓㄥˇ")
zheng_4	= re.compile("ㄓㄥˊ")
zheng_6	= re.compile("ㄓㄥˋ")
zheng_7	= re.compile("ㄓㄥ˙")
	 	 
#ㄓ
zhi_space= re.compile("ㄓˉ")
zhi_3	= re.compile("ㄓˇ")
zhi_4	= re.compile("ㄓˊ")
zhi_6	= re.compile("ㄓˋ")
zhi_7	= re.compile("ㄓ˙")

#ㄓㄨㄥ
zhong_space= re.compile("ㄓㄨㄥˉ")
zhong_3	= re.compile("ㄓㄨㄥˇ")
zhong_4	= re.compile("ㄓㄨㄥˊ")
zhong_6	= re.compile("ㄓㄨㄥˋ")
zhong_7	= re.compile("ㄓㄨㄥ˙")

#ㄓㄡ
zhou_space= re.compile("ㄓㄡˉ")
zhou_3	= re.compile("ㄓㄡˇ")
zhou_4	= re.compile("ㄓㄡˊ")
zhou_6	= re.compile("ㄓㄡˋ")
zhou_7	= re.compile("ㄓㄡ˙")

#ㄓㄨ
zhu_space= re.compile("ㄓㄨˉ")
zhu_3	= re.compile("ㄓㄨˇ")
zhu_4	= re.compile("ㄓㄨˊ")
zhu_6	= re.compile("ㄓㄨˋ")
zhu_7	= re.compile("ㄓㄨ˙")

#ㄓㄨㄚ
zhua_space= re.compile("ㄓㄨㄚˉ")
zhua_3	= re.compile("ㄓㄨㄚˇ")
zhua_4	= re.compile("ㄓㄨㄚˊ")
zhua_6	= re.compile("ㄓㄨㄚˋ")
zhua_7	= re.compile("ㄓㄨㄚ˙")

#ㄓㄨㄚ
zhuai_space= re.compile("ㄓㄨㄞˉ")
zhuai_3	= re.compile("ㄓㄨㄞˇ")
zhuai_4	= re.compile("ㄓㄨㄞˊ")
zhuai_6	= re.compile("ㄓㄨㄞˋ")
zhuai_7	= re.compile("ㄓㄨㄞ˙")

#ㄓㄨㄢ
zhuan_space= re.compile("ㄓㄨㄢˉ")
zhuan_3	= re.compile("ㄓㄨㄢˇ")
zhuan_4	= re.compile("ㄓㄨㄢˊ")
zhuan_6	= re.compile("ㄓㄨㄢˋ")
zhuan_7	= re.compile("ㄓㄨㄢ˙")

#ㄓㄨㄤ
zhuang_space= re.compile("ㄓㄨㄤˉ")
zhuang_3	= re.compile("ㄓㄨㄤˇ")
zhuang_4	= re.compile("ㄓㄨㄤˊ")
zhuang_6	= re.compile("ㄓㄨㄤˋ")
zhuang_7	= re.compile("ㄓㄨㄤ˙")

#ㄓㄨㄣ
zhui_space= re.compile("ㄓㄨㄣˉ")
zhui_3	= re.compile("ㄓㄨㄣˇ")
zhui_4	= re.compile("ㄓㄨㄣˊ")
zhui_6	= re.compile("ㄓㄨㄣˋ")
zhui_7	= re.compile("ㄓㄨㄣ˙")

#ㄓㄨㄣ
zhun_space= re.compile("ㄓㄨㄣˉ")
zhun_3	= re.compile("ㄓㄨㄣˇ")
zhun_4	= re.compile("ㄓㄨㄣˊ")
zhun_6	= re.compile("ㄓㄨㄣˋ")
zhun_7	= re.compile("ㄓㄨㄣ˙")

#ㄓㄨㄛ
zhuo_space= re.compile("ㄓㄨㄛˉ")
zhuo_3	= re.compile("ㄓㄨㄛˇ")
zhuo_4	= re.compile("ㄓㄨㄛˊ")
zhuo_6	= re.compile("ㄓㄨㄛˋ")
zhuo_7	= re.compile("ㄓㄨㄛ˙")

#ㄓㄨㄛ
zi_space= re.compile("ㄗˉ")
zi_3	= re.compile("ㄗˇ")
zi_4	= re.compile("ㄗˊ")
zi_6	= re.compile("ㄗˋ")
zi_7	= re.compile("ㄗ˙")

#ㄗㄨㄥ
zong_space= re.compile("ㄗㄨㄥˉ")
zong_3	= re.compile("ㄗㄨㄥˇ")
zong_4	= re.compile("ㄗㄨㄥˊ")
zong_6	= re.compile("ㄗㄨㄥˋ")
zong_7	= re.compile("ㄗㄨㄥ˙")

#ㄗㄨㄥ
zou_space= re.compile("ㄗㄡˉ")
zou_3	= re.compile("ㄗㄡˇ")
zou_4	= re.compile("ㄗㄡˊ")
zou_6	= re.compile("ㄗㄡˋ")
zou_7	= re.compile("ㄗㄡ˙")

#ㄗㄨ
zu_space= re.compile("ㄗㄨˉ")
zu_3	= re.compile("ㄗㄨˇ")
zu_4	= re.compile("ㄗㄨˊ")
zu_6	= re.compile("ㄗㄨˋ")
zu_7	= re.compile("ㄗㄨ˙")

#ㄗㄨ
zuan_space= re.compile("ㄗㄨㄢˉ")
zuan_3	= re.compile("ㄗㄨㄢˇ")
zuan_4	= re.compile("ㄗㄨㄢˊ")
zuan_6	= re.compile("ㄗㄨㄢˋ")
zuan_7	= re.compile("ㄗㄨㄢ˙")

#ㄗㄨ
zui_space= re.compile("ㄗㄨㄟˉ")
zui_3	= re.compile("ㄗㄨㄟˇ")
zui_4	= re.compile("ㄗㄨㄟˊ")
zui_6	= re.compile("ㄗㄨㄟˋ")
zui_7	= re.compile("ㄗㄨㄟ˙")

#ㄗㄨㄣ
zun_space= re.compile("ㄗㄨㄣˉ")
zun_3	= re.compile("ㄗㄨㄣˇ")
zun_4	= re.compile("ㄗㄨㄣˊ")
zun_6	= re.compile("ㄗㄨㄣˋ")
zun_7	= re.compile("ㄗㄨㄣ˙")

#ㄗㄨㄛ
zuo_space= re.compile("ㄗㄨㄛˉ")
zuo_3	= re.compile("ㄗㄨㄛˇ")
zuo_4	= re.compile("ㄗㄨㄛˊ")
zuo_6	= re.compile("ㄗㄨㄛˋ")
zuo_7	= re.compile("ㄗㄨㄛ˙")



bopomofoDict = KeyDict({a_space : ["阿", "啊", "錒", "锕"],
               a_3     : [],
               a_4     : ["阿","啊","錒"],
               a_6     : ["嗄"],
               a_7     : ["啊"],
               
               ai_space: ["哀", "埃", "挨", "唉", "哎", "誒", "锿"],
               ai_3    : ["矮", "藹", "靄", "毐", "譪", "佁", "嗳", "敱", "昹", "欸", "絠", "蔼", "躷", "霭", "馤"],
               ai_4    : ["愛","艾","礙","璦","隘","曖","嬡","曖","靉","乂","譺","薆","伌","僾","嗳","堨","嫒","懝","暧","濭","爱","瑷","皧","瞹","砹",
                         "硋","碍","誒","譪","賹","鑀","镴","阸","餲","鴱"],
               ai_6    : ["癌","捱","皚","呆","嘊","嵦","敳","皑","騃"],
               ai_7    : ["唉"],
               
               an_space: ["安","鞍","諳","胺","庵","氨","銨","垵","ㄢ","鵪","菴","厂","侒","厈","媕","峖","痷","盦","盫","腤","萻","葊","蓭","誝","谙","闇",
                          "阥","鞌","韽","鶕","鹌"],
               an_3    : ["俺","唵","匼","堷","晻","罯","铵"],
               an_4    : ["案","按","岸","暗","黯","闇","桉","儑","匎","匼","咹","婩","揞","洝","犴","荌","菴","葊","豻","貋","錌","鮟"],
               an_6    : ["啽","玵","雸"],
               an_7    : [],

               ang_space:["ㄤ","骯","腌"],
               ang_3    :["軮"],
               ang_4    :["盎","醠","駚"],
               ang_6    :["昂","卬","岇","峁","昻","枊"],
               ang_7    :[],

               ao_space :["凹","ㄠ","坳","柪","坳"],
               ao_3     :["襖","媼","抝","拗","狕","芺","袄","镺"],
               ao_4     :["奧","澳","拗","傲","拗","奡","擙","噢","圫","垇","墺","奥","嫯","岙","嶴","慠","扷","詏","謸","軪","鐡","驁","骜","鱩"],
               ao_6     :["敖","熬","鰲","翱","螯","遨","獒","鼇","嗷","驁","璈","鏖","聱","鏊","厫","嗸","嚣","嶅","廒","摮","滶","爊","獓","磝",
                          "簢","翺","蔜","謷","隞","鳌","鷔"],
               ao_7     :["噢"],
                
               ba_space :["八","巴","吧","峇","芭","疤","扒","叭","笆","粑","鈀","捌","仈","哵","朳","県","羓","蚆","豝","釟"],
               ba_3     :["把","靶","鈀","钯"],
               ba_4     :["爸","霸","壩","罷","灞","吧","伯","坝","埧","弝","把","欛","猈","皅","矲","罢","皅","耙","覇","靶","鲅"],
               ba_6     :["拔","鈸","跋","魃","菝","叐","坺","妭","抜","犮","癹","秡","胈","茇","軷","詙","颰","鮁","鼥"],
               ba_7     :["吧","爸","巴","杷","琶","罷"],

               bai_space:["掰"],
               bai_3    :["百","擺","佰","襬","捭","粨","摆","矲","絔"],
               bai_4    :["拜","敗","稗","呗","唄","庍","拝","絆","眬","矲","粺","贁","败"],
               bai_6    :["白"],
               bai_7    :[""],

               ban_space:["班","般","搬","斑","頒","扳","瘢","攽","斒","朌","癍","虨","螌","褩","辬","颁","鳻"],
               ban_3    :["版","板","坂","阪","粄","闆","鈑","舨","昄","岅","瓪","蝂","軅","钣","飖"],
               ban_4    :["半","辦","伴","扮","拌","瓣","絆","爿","办","姅","怑","湴","秚","绊","鉡","靽"],
               ban_6    :[""],
               ban_7    :[""],

               bang_space:["幫","邦","傍","梆","浜","垹","峀","帮","幇","幚","縍","邫","鞤"],
               bang_3   : ["綁","榜","膀","蚌","氆","绑","騯"],
               bang_4   : ["蚌","棒","傍","磅","謗","棓","鎊","蒡","塝","挷","旁","玤","甏","稖","膀","艕","蜯","谤","镑"],
               bang_6   : [],
               bang_7   : [],

               bao_space: ["包","胞","褒","苞","煲","孢","枹","炮","礟","笣","蕔","裦","襃","闁","煲","龅"],
               bao_3    : ["保","寶","堡","飽","葆","媬","褓","鴇","駂","堢","宝","宲","寚","寳","怉","珤","緥","賲","饱","鳵","鸨"],
               bao_4    : ["報","抱","爆","暴","鮑","豹","刨","鉋","趵","儤","勽","嚗","忁","报","曓","鮑","瀑","煲","煿","犦","菢","虣","袌","鑤","骲","鲍"],
               bao_6    : ["薄","雹","瓝","窇"],
               bao_7    : ["寶"],

               bei_space :["杯","盃","背","碑","卑","揹","悲","鵯","庳","埤","伓","俾","偝","唄","桮","椑","痺","箄","綼","萆","藣","裨","軣","錃","鞞","鹎"],
               bei_3:["北"],
               bei_4:["被","倍","備","貝","背","輩","蓓","悖","焙","琲","鋇","憊","狽","臂","碚","珼","褙","梖","俻","偝","偹","僃","哱","唄","垻","备","奰","孛","怫","惫","愂","昁","牬","犕","狈","瞆","糒","紴","茇","蛽","誖","贝","軰","辈","邶","郥","鄁","钡","鞴","鱫"],
               bei_6:[],
               bei_7:["唄","呗"],

               ben_space:["奔","犇","渀","賁","錛","倴","泍","贲","锛"],
               ben_3    :["本","苯","畚","夲","奋","奙","撪","楍"],
               ben_4    :["笨","坌","体","倴","捹","桳","獖","籡","躵","輽","逩"],
               ben_6    :[],
               ben_7    :[],

               beng_space:["崩","繃","祊","塴","伻","傰","嘣","奟","嵭","弸","瞓","絣","綳","绷","閍"],
               
               beng_3:["埲","玤","琫","绷","菶","誁","鞛"],
               beng_4:["蹦","迸","泵","洴","搒","榜","绷","蜯","跰","逬"],
               beng_6:["甭"],
               beng_7:[],
               
               
               bi_space:["逼","屄","偪","咇","幅","悂","稫","螕","豍"],
               bi_3  :  ["比","筆","彼","鄙","匕","秕","妣","柀","佊","夶","屄","朼","毴","沘","滗","潷","疕","笔","粃","蚍","貏","饤","魮"],
               bi_4  :  ["蹕","必","避","壁","畢","幣","臂","跛","弊","閉","俾","斃","祕","璧","蔽","庇","痹","痺","弼","嗶","疪","敝","辟",
                         "毖","篳","蹕","裨","皕","比","篦","蓽","埤","婢","躄","愎","畀","襞","贔","鉍","楅","苾","薜","菎","陛","髀","嬖",
                         "睥","胇","蓖","鄙","閟","佖","佛","吡","哔","坒","堛","夶","妼","嫳","庳","廦","弻","彃","怭","愊","揊","朇","枇",
                         "柫","柲","梐","毕","毙","泌","湢","滭","煏","熚","狴","獘","獙","珌","畁","睤","秘","稗","稫","笓","筚","箄","箅",
                         "箆","粊","綼","縪","繴","罼","聛","肶","腷","芘","荜","萆","蘗","虑","蜌","袐","襒","襣","觱","詖","貱","賁","贲",
                         "跸","軣","輌","邲","鄨","鄪","鎞","鏎","鐴","鐾","铋","閇","闭","鞸","韠","飶","饆","馝","駜","驆","骳","髲","魓",
                         "鮅","鰏","鵖","鷝","鷩","鼊"],
               bi_6  :  ["鼻","荸"],
               bi_7  :  [],
               
            bian_space:["邊","編","鞭","鯿","蝙","煸","砭","籩","猵","匥","柉","楄","甂","稨","笾","箯","糄","编","边","邉","鍽","飚","鯾","鳊","鳠"],
            bian_3    :["扁","貶","匾","窆","惼","褊","蝙","碥","萹","藊","藊","豍","贬"],
            bian_4    :["變","便","遍","辯","辨","汴","卞","辮","釆","弁","閞","变","平","変",
                        "徧","忭","抃","拤","揙","昪","汳","牑","玣","緶","矈","蹕","缏","艑",
                        "芐","覍","苄","辡","辧","辩","辧","鴘"],
            bian_6    :[],
            bian_7    :[],

            biao_space:["標","飆","鏢","贆","彪","杓","鑣","膘","嘌","驫","颮","摽","熛","滮","麃","儦","墂","幖","徱","标","瀌",
                        "爂","猋","瘭","矋","磦","穮","羆","脿","臕","蔈","藨","謤","镖","镳","閊","颩","颷","飇","飈","飊","飍",
                        "飑","飙","骠","髟","麅"],
            biao_3:["表","錶","裱","俵","婊","褾","檦","諘"],
            biao_4:["鰾","摽","鳔"],
            biao_6:[],
            biao_7:[],

            bie_space:["鱉","憋","鼈","瘪","虌","鳖","龞"],
            bie_3:["癟","瘪","蛂"],
            bie_4:["彆","縪"],
            bie_6:["別","蹩","别","咇","徶","蛂","莂","蟞","襒"],
            bie_7:[],


            bin_space:["濱","斌","賓","彬","檳","瀕","殯","繽",
                       "鑌","儐","璸","霦","玢","邠","豳","驞",
                       "傧","攽","梹","椕","槟","汃","浜","滨",
                       "濒","濵","矉","砏","穦","缤","蠙","豩",
                       "賔","镔","顮","馪"],
               
          
            bin_3:[],
            bin_4:["殯","鬢","髕","臏","擯","儐","摈","殡","膑",
                   "髌","髩","鬂","鬓","鶣"],            
            bin_6:[],
            bin_7:[],

            bing_space:["冰","兵","并","栟","仌","掤","槟","氷"],
            bing_3:["炳","餅","丙","秉","柄","稟","邴","苪","陃",
                    "屏","昺","偋","帲","幈","庰","怲","抦","怲",
                    "棅","眪","窉","蛃","鈵","鉼","鞞","餠","饼"],
               
            bing_4:["並","病","併","摒","倂","偋","傡","寎","并",
                    "幷","庰","开","柄","栤","竝","靐","鮩","鵧"],
            
            bing_6:[],
            bing_7:[],
    
     
            bo_space:["波","撥","剝","播","玻","缽","菠","啵","磻","砵","剥","嚗","岥","嶓","拨"
                      "柭","癶","盋","碆","般","袚","襏","蹳","鉢","钵","餑","饽","驋","鮁","鱍"],            
            bo_3:["跛","簸","蚾"],
            bo_4:["播","擘","亳","蘗","薄","挀","丠","奙","孹","檗","檘","簸","繴","蔢","薜","蘖","譒"],
            bo_6:["博","伯","柏","泊","薄","搏","駁","勃","帛","栢","箔","鉑","渤","舶","脖","孛","膊"
                  "蔔","白","礡","礴","踣","桲","荸","踄","檗","駮","侼","僰","侼","剝","墢","彴","愂",
                  "愽","懪","挬","敀","欂","浡","牔","犮","猼","瓝","百","簙","糪","胉","艊","苩","葧"
                  "嶓","襮","謈","郣","鈸","鋍","鎛","鏄","鑮","钹","铂","餑","餺","馛","馞","驳","髆",
                  "鮊","鰙","鵓","钹","鸔","鹁"],
                  
            bo_7:["蔔","伯"],

            bu_space:["餔","晡","逋","峬","庯","钸","鵏"],
            bu_3:["補","捕","卜","哺","埔","獛","补","鳪"],
            bu_4:["不","部","布","步","佈","簿","鈽","埠",
                  "怖","咘","悑","抪","捗","柨","歨","歩",
                  "歨","沠","篰","荹","蔀","钚","飏","餢",
                  "鵏"],
            bu_6:["不","轐","醭","鯱"],
            bu_7:[],

            ca_space:["擦","嚓","搽","硳"],
            ca_3:["礤"],
            ca_4:["囃"],
            ca_6:[],
            ca_7:[],

            cai_space:["猜"],
            cai_3:["採","彩","踩","采","綵","睬","婇","棌","倸","寀","跴"],
            cai_4:["蔡","菜","埰","砿","硁","縩","婇","采"],
            cai_6:["才","財","材","裁","纔","财"], 
            cai_7:[],

            can_space:["餐","參","驂","傪","叁","参","叄","叅","湌","謲","飡","骖"],
            can_3:["慘","噆","惨","憯","朁","黪","黲"],
            can_4:["蔡","菜","埰","砿","硁","縩","婇","采"],
            can_6:["殘","蠶","慚","嬠","惭","慙","残","蚕","蝅","蠺"], 
            can_7:[],

            cang_space:["倉","艙","滄","蒼","傖","嵢","仓","仺","伧","凔","沧","篬","舱","苍","鶬"],
            cang_3:[],
            cang_4:[],
            cang_6:["藏","匨","蔵","鑶"],
            cang_7:[],
            #ㄘㄠ
            cao_space:["操","糙","喿","幧","撡","鄵"],
            cao_3:["草","艸","愺","慅","懆","艹","騲"],
            cao_4:["襙","操","肏","襙","鄵"],
            cao_6:["曹","槽","嘈","漕","嶆","硙","硚","艚","蓸","螬","褿","鏪"],  
            cao_7:[],
            #ㄘㄜ
            ce_space:[],
            ce_3:[],
            ce_4:["測","側","策","冊","廁","惻","侧","册","厕","厠","嫧","恻","嫧",
                  "憡","拺","敇","测","畟","矠","硛","笧","筴","箣","簎","粣","茦",
                  "萗","蓛","銏"],
            ce_6:[],  
            ce_7:[],
            #ㄘㄣ
            cen_space:["參","嵾","梫","篸"],
            cen_3:[],
            cen_4:[],
            cen_6:["岑","涔","埁","梣","橬","汵","笒"],  
            cen_7:[],
            #ㄘㄥ
            ceng_space:["噌"],
            ceng_4:["蹭"],
            ceng_6:["曾","層","嶒","层","碀","竲","鄫","驓"],
            ceng_7:[],
            #ㄔㄚ
            cha_space:["差","插","叉","杈","偛","喳","嗏","嚓",
                        "扠","挿","揷","疀","肞","臿","艖","芆",
                        "銟","鎈","锸","餷","馇"],
            cha_4:["岔","剎","衩","汊","詫","奼","仛","侘","刹","姹","差","杈","硲","紁","蜡","訍","诧"],
            
            cha_6:["查","茶","察","搽","碴","叉","垞","査","槎","檫","猹","秅","臿","褨","詧"],
            cha_7:[],
            #ㄔㄞ
            chai_space:["拆","釵","差","偨","嫅","硳","钗","靫"],
            chai_3    :["笧"],
            chai_4    :["袃","蠆","囆","瘥","虿","骉"],
            chai_6    :["柴","儕","豺","祡","侪","喍","犲","硴","硵","贠"],
            chai_7    :[],

            #ㄔㄢ
            chan_space:["摻","攙","嬓","幨","惉","掺","搀","梴","脠","袩","裧","襜","觇","辿","鋓"],
            chan_3    :["產","鏟","剷","闡","諂","丳","产","冁","剗","嘽","囅","嘽","嵼","囅","幝",
                        "摌","旵","滻","灛","燀","産","簅","繟","蒇","譂","讇","谄","醦","鐦","铲",
                        "閳","阐","驏","骣"],
            chan_4    :["羼","懺","儳","嚵","幨","韂","顫","颤"],
          
            chan_6    :["禪","纏","蟬","嬋","蟾","饞","潺","讒","廛","孱","澶","躔","僝","儳",
                        "劖","单","単","厘","單","嚵","婵","巉","棎","毚","湹","潹","瀍","瀺",
                        "煘","獑","磛","禅","緾","繵","纒","缠","艬","蝉","誗","谗","鄽","酁","鋋","鏰",
                        "鑱","镡","馋","鯅"],
            chan_7    :[],

            chang_space:["昌","娼","錩","菖","鯧","猖","淐","琩","倀","閶","伥","倡","晿","裮","阊","鱂","鲯","鲳","鼚"],
            chang_3    :["場","廠","昶","敞","僘","厰","场","惝","氅","鋹"],
            chang_4    :["唱","暢","倡","悵","怅","瑒","畅","畼","誯","韔","鬯"],
            chang_6    :["長","常","嘗","腸","償","嚐","嫦","場","徜","萇",
                         "仧","偿","兏","麃","塲","场","尝","瑺","瓺","甞","粻",
                         "肠","膓","苌","裳","鋿","鏛","镸","长","鱨"],
            chang_7    :[],
            #ㄔㄠ 
            chao_space:["超","鈔","抄","剿","勦","弨","怊","绰","罺","訬","钞"],
            chao_3    :["炒","吵","巐","煼","眧","麨"],
            chao_4    :["耖","觘"],
            chao_6    :["朝","潮","巢","晁","嘲","樔","巣","漅","謿","轈","鄛","鼂"],
            chao_7    :[],
            
            #ㄔㄜ 
            che_space:["車","车","硨","俥","唓","砗","莗","蛼"],
            che_3    :["扯","偖","哆","奲","尺","撦"],
            che_4    :["撤","徹","澈","轍","掣","坼","勶","呫","屮","彻","烲","爡","瞮","硩","碵","碶","聅","詀","迠","頙"],
            che_6    :[],
            che_7    :[],
               
            #ㄔㄣ 
            chen_space:["琛","嗔","瞋","謓","棽","堔","捵","搷","諃","賝","郴","镃"],
            chen_3    :["磣","墋","捵","裖","贂","趻","踸","醦","鍖"],
            chen_4    :["趁","襯","稱","讖","櫬","儭","嚫","夦","榇","澵","疢","称","穪","藽","衬","谶","趂","齓","齔","龀"],
            chen_6    :["陳","晨","辰","沉","臣","塵","宸","忱","諶","茞","沈","伔","娠","尘","愖","敐","敶","曟","梣","樄",
                        "湛","煁","莀","莐","蔯","薼","螴","谌","軙","迧","鈂","陈","陙","霃","鷐","麎"],
            chen_7    :["伧"],
            #ㄔㄥ
            cheng_space:["稱","撐","檉","瞠","蟶","橕","牚","偁","埥","崝","庱","憆","摚","撑","柽","棦","槍","泟","浾","爯",
                         "琤","盯","称","竀","緽","赬","娍","鎗","鏿"",鐺","铛","阷","頳","饓"],
               
            cheng_3:["逞","騁","塣","庱","徎","悜","睈","磗","骋"],            
            cheng_4:["秤","稱","乘","偁","爯","牚","靗"],
            cheng_6:["成","城","峸","程","誠","盛","承","呈","乘","澄","埕","丞","橙","晟","懲","澂","裎","呈","鋮","掁","珵","荿","宬",
                     "棖","乗","堘","塍","塖","娍","峥","峸","惩","挰","揨","撜","晠","枨","椉","娍","湞","瀓","珹","畻","筬","脀","脭",
                     "诚","郕","酲","铖","騬"],
            cheng_7:[],
            #ㄔ
            chi_space:["吃","癡","痴","嗤","喫","笞","ㄔ","鴟","摛","蚩","哧","魑","媸","卨","呞","噄","妛","岻","彲","欫","瓻","眵","瞝",
                       "离","粚","絺","胵","脪","螭","訵","誺","貾","郗","鸱","麶","黐","齝","齹"],
               
            chi_3:["呎","欼","齒","恥","侈","豉","褫","勅","禠","鶒","伬","傂","垑","姼","恀","拸","搋","撴","欼","耻","歯","蚇","袳","誃","鉹","齿"],           
            chi_4:["赤","斥","翅","熾","叱","飭","敕","啻","彳","乿","侙","傺","勅","勑","卙","哧","恜","慗","慸","憏","懘","戠","烾",
                   "抶","痓","湁","痸","瘛","眙","摰","糦","淔","旘","杘","翄","腟","翤","趩","跇","跮","踅","遫","鉓","饎","饬","鶒","鷘"],
               
            chi_6:["持","池","遲","馳","匙","墀","篪","弛","茬","徥","踟","俿","坻","徲","忯","栘","歭","汦","治","泜","痄","竾","筂","箈",
                   "箎","耛","茌","荎","蚔","蚳","蝭","裭","謘","貾","赿","趍","遅","遟","邌","驰"],
            chi_7:[],
            #ㄔㄨㄥ
            chong_space:["衝","沖","充","冲","舂","忡","憧","嘃","徸","憃","摏","浺","珫","祌","茺","蚛","蹖"],
            chong_3    :["寵","埫","宠"],
            chong_4    :["銃","揰","衝","蹱","铳"],
            chong_6    :["重","崇","蟲","崈","漴","烛","爞","痋","种","翀","茧","虫","蛊","蝩","隀"],
            chong_7    :[],
            #ㄔㄡ
            chou_space:["抽","紬","婤","搊","犨","犫","瘳","篘"],
            chou_3    :["醜","丑","瞅","丒","侴","偢","吜","杻","杽","矁","莥"],
            chou_4    :["臭","憱","殠","溴","簉","臰","遚"],
            chou_6    :["籌","仇","愁","酬","稠","綢","疇","儔","讎","躊","惆","俦","圳","嬦",
                         "幬","怞","懤","栦","椆","燽","畴","皗","磵","筹","紬","絒",
                         "绸","菗","薵","裯","詶","讐","赟","踌","酧","醻","雔","雠","魗","鯈"],
               
            chou_7    :[],
            #ㄔㄨ
            chu_space :["出","初","齣","岀","礃","貙"],
            chu_3 :["處","楚","礎","褚","杵","楮",
                        "濋","储","儲","处","憷","柠",
                        "椘","檚","础","礖","禇","齭","齼"],            
            chu_4     :["處","楚","礎","褚","杵","楮",
                        "濋","储","儲","处","憷","柠",
                        "椘","檚","础","礖","禇","齭","齼"
                        ],
            chu_6     :["鋤","除","儲","鋤","雛","櫥","芻","躇","鶵",
                        "滁","蜍","躕","刍","厨","幮","橱","犓","篨",
                        "耝","耡","蒢","蕏","蒭","藸","貙","跦","蹰",
                        "鉏","锄","雏"
                       ],
            chu_7     :[],
               
            #ㄔㄨㄞ   
            chuai_space :["搋"],
            chuai_3     :["揣"],
            chuai_4     :["踹","嘬","酛"],
            chuai_6     :["膗"],
            chuai_7     :[],

            #ㄔㄨㄢ
            chuan_space :["穿","川","氚","剶","巛","瑏","釧","鐉"],
            chuan_3     :["喘","舛","歂","荈"],
            chuan_4     :["串","釧","玔","汌","夼","腨","賗","钏","鶨"],
            chuan_6     :["船","傳","椽","諯","传","暷","歂","猭","篅","舩","輲","遄"],  
            chuan_7     :[],
            #ㄔㄨㄤ 
            chuang_space:["窗","瘡","創","窓","刅","创","刽","囪","憃","戧","摐","牎",
                          "牕","疮","窻"],
            chuang_3    :["闖","搶","摤","漺","闯"],
            chuang_4    :["創","愴","创","刱","刽","剏","剙","怆","獊","闖"],
            chuang_6    :["床","幢","牀","噇","撞","橦","疒"],
            chuang_7    :[],

            #ㄔㄨㄟ
            chui_space:["吹","炊","龡"],
            chui_3    :[],
            chui_4    :["吹","炊","諈"],
            chui_6    :["垂","槌","捶","錘","搥","鎚","陲","棰","倕",
                        "厜","圌","埀","娷","桘","椎","湷","甀","磓",
                        "箠","綞","腄","菙","锤","顀"],
            chui_7    :[],
            #ㄔㄨㄣ 
            chun_space:["春","椿","鰆","暙","焞","媋","旾","杶","橁",
                        "櫄","瑃","萅","輴","鶞"],
               
            chun_3    :["蠢","萶","偆","僢","堾","惷","睶","箺","蝽","踳"],
            chun_4    :[],
            chun_6    :["純","唇","淳","醇","脣","錞","鶉","屯","憌","浱",
                        "湻","滣","漘","焞","纯","莼","蒓","蓴","醕","鯙",
                        "鹑"],
            chun_7    :[],
            #ㄔㄨㄛ
            chuo_space:["戳","礳"],
            chuo_3    :[],
            chuo_4    :["輟","啜","綽","齪","叕","吷","嚽","娖","婥","婼",
                        "惙","擉","歠","涰","珿","畷","磭","繛","绰","腏",
                        "諁","趠","辍","辵","辶","逴","遬","酛","醊","鋜",
                        "鑡","龊"],
            chuo_6    :[],
            chuo_7    :[],

            #ㄘ
            ci_space  :["雌","疵","差","庛","偨","趀","骴"],
            ci_3      :["此","玼","佌","泚","皉","跐"],
            ci_4      :["次","刺","莿","賜","伺","朿","佽","庛","廁",
                        "栨","絘","蚝","蛓","螆","赐","赼","趦"],
            ci_6      :["慈","詞","辭","祠","磁","瓷","茨","鶿","雌","兹","呲",
                        "垐","嬨","柌","濨","珁","甆","疵","礠","祃","粢","糍",
                        "茊","茲","薋","词","辝","辞","辤","飺","餈","鴜","鷀",
                        "鹚"],
            ci_7      :[],
            
            #ㄘㄨㄥ
            cong_space:["聰","蔥","璁","匆","囪","驄","從","蓯","葱",
                        "瑽","蟌","鏦","囱","忩","怱","悤","暰","枞",
                        "棇","樅","楤","漗","樬","焧","熜","燪","瞛",
                        "祎","篵","総","繱","聡","聦","聪","苁","鍐",
                        "鍯","鏓","騘","骢"],
            
            cong_3    :["幒"],
            cong_4    :["欉","藂","謥"],
            cong_6    :["從","叢","琮","欉","淙","孮","悰","漎","丛",
                        "从","婃","従","徖","慒","樷","潀","潨","灇",
                        "爜","碂","苁","藂","誴","賨","賩","錝","锜",
                        "锳"],
            cong_7    :[],

            #ㄘㄡ
            cou_space :[],
            cou_3     :[],
            cou_4     :["湊","腠","輳","凑","楱","辏","鞆"],
            cou_6     :[],
            cou_7     :[],

            #ㄘㄨ
            cu_space  :["粗","觕","麁","麄","麤"],
            cu_3      :[],
            cu_4      :["促","醋","猝","槭","簇","蹴","蹙","卒","窣",
                        "卆","噈","憱","數","梀","殧","瘯","縬","蔟",                        
                        "蜶","趗","趣","趨","踧","蹵","酢","鉃","錯",
                        "鏃","顣","鼀"],
            cu_6      :["徂","殂","豠","鼀"],
            
            #ㄘㄨㄢ
            cuan_space  :["汆","躥","攛","撺","蹿","鋑","鑹","镩"],
            
            cuan_3      :[],
            cuan_4      :["竄","篡","爨","熶","窜","篹","簒","韨"],
            
            cuan_6      :["劗","巑","攒","攢","欑"],
            cuan_7      :[],

            #ㄘㄨㄟ
            cui_space   :["催","崔","摧","嗺","墔","榱","槯","磪","縗","衰","鏙"],
            cui_3       :["璀","洒","漼","皠","趡"],
            cui_4       :["翠","脆","粹","萃","淬","焠","瘁","綷","悴","伜","倅",
                          "啐","啛","忰","橇","毳","濢","琗","酂","竁","紣","翆","粋",
                          "脃","脺","膬","膵","臎","酂","韢"],
            cui_6       :["凗","慛"],
            cui_7       :[],

            #ㄘㄨㄣ
            cun_space   :["村","皴","竴","踆"],
            cun_3       :["忖","刌"],
            cun_4       :["吋","寸","籿"],
            cun_6       :["存","墫","拵","穣","袸"],
            cun_7       :[],
            
            #ㄘㄨㄛ   
            cuo_space   :["搓","磋","蹉","瑳","差","撮","蒫","遳","髊"],
            cuo_3       :["瑳","硰","縒","脞"],
            cuo_4       :["錯","厝","挫","措","撮","剉","銼","侳","剒",
                          "夎","棤","縒","莝","莡","蓌","襊","逪","锉",
                          "错","齚","齰"],
            cuo_6       :["矬","嵯","痤","嵖","嵳","瘥","睉","蒫","蔖",
                          "虘","醝","鹺","鹾"],
            cuo_7       :[],

            #ㄉㄚ
            da_space    :["搭","撘","答","褡","瘩","耷","咑","哒"],
            da_3        :["打"],
            da_4        :["大","亣","詚"],
            da_6        :["達","答","妲","噠","韃","瘩","怛","鎝",
                          "鐽","剳","匒","呾","榙","溚","炟","畣",
                          "笪","繨","羍","荅","薘","褟","靼","鞑"],
            da_7        :["瘩"],

            #ㄉㄞ
            dai_space    :["待","呆","獃","帒","懛"],
            dai_3        :["逮","歹","傣","歺"],
            dai_4        :["帶","代","戴","待","袋","貸","黛","岱",
                          "怠","殆","玳","大","紿","迨","逮","貸",
                          "靆","埭","甙","軩","亣","侢","带","帯",
                          "廗","忕","忲","摕","曃","柋","毒","汏",
                          "瀻","瑇","簤","緿","绐","艜","蝳","襶",
                          "詒","贷","跢","蹛","軑","軚","酨","隶",
                          "霴","駘","骀","黱"],
            
            dai_6        :[],
            dai_7        :[],

            #ㄉㄢ
            dan_space    :["單","丹","酖","擔","耽","襌","眈","躭",
                           "殫","担","簞","鄲","儋","勯","匰","单",
                           "単","噡","嚪","妉","媅","殚","甔","瘅",
                           "癉","砃","箪","耼","聃","聸","郸","駲"],
               
            dan_3        :["膽","丼","衴","撢","撣","疸","亶","刐",
                           "掸","澸","燀","玬","瓭","瘅","紞","胆",
                           "赕","餤","駲","黕","黵"],
               
            dan_4        :["但","蛋","淡","狚","旦","擔","啖","氮","彈",
                           "誕","憚","澹","鉭","蜑","殫","泹","僤","幨",
                           "儋","啗","啿","嘾","噉","嚪","帎","潬","沊",
                           "弹","弾","惮","摕","暺","柦","檐","餤","灗",
                           "擔","僤","灗","瘅","酨","隶","霴","駘","霮",
                           "癚","石","繵","腅","臽","舕","萏","觛","诞",
                           "醈","霮","餤","饏","駲","駳","髧","鴠","餤",
                           "駲","饏","駳","髧","鴠"],
            dan_6        :["馾"],
            dan_7        :[],
            
            #ㄉㄤ
            dang_space   :["當","噹","鐺","襠","璫","蟷","澢","儅","嵣",
                           "嵣","簹","艡","裆","铛"],
            dang_3       :["黨","檔","擋","党","讜","挡","攩","欓","灙",
                           "譡","谠"],
            
            dang_4       :["盪","當","蕩","宕","礑","踼","璗","逿","碭",
                           "凼","圵","婸","嵣","当","愓","擋","档","潒",
                           "瓽","瞊","砀","簜","荡","菪","蘯","趤","闣",
                           "雼"],
            dang_6       :[],
            dang_7       :[],

            #ㄉㄠ
            dao_space   :["刀","叨","氘","刂","幍","忉","朷","舠","裯","釖","魛"],

            dao_3       :["島","導","倒","搗","禱","擣","嶋","壔","导","岛","嶌",
                          "捣","捯","祷","禂","隝","隯"],
            dao_4       :["到","道","倒","盜","稻","蹈","悼","纛","檤","噵","導",
                          "帱","幬","焘","瓙","盗","稲","翢","翿","菿","衜","衟",
                          "軇"],
            dao_6       :["捯"],
            dao_7       :[],

            #ㄉㄜ
            de_space    :[],
            de_3        :[],
            de_4        :[],
            de_6        :["德","咳","欷","壳","殻","颏"],
            de_7        :["的","地","得"],

            #ㄉㄟ
            dei_space    :[],
            dei_3        :["得"],
            dei_4        :[],
            dei_6        :[],
            dei_7        :[],

            #ㄉㄥ
            deng_space  :["燈","登","豋","灯","噔","嬁","璒","竳","簦","鐙"],
            deng_3      :["等","戥"],
            deng_4      :["鄧","瞪","蹬","凳","嶝","鐙","磴","僜","墱","憕",
                          "櫈","澄","覴","邆","镫","隥","霯"],
            deng_6      :[],
            deng_7      :[],

            #ㄉㄧㄢ
            dian_space  :["顛","滇","巔","癲","掂","槙","傎","厧","嵮","巅","巓","敁","槇","瘨","癫","蹎","顚","颠","齻"],
            dian_3      :["點","典","碘","錪","奌","婰","敟","点","琠","痶","秴","窡","蒧","蕇","鰘"],
            dian_4      :["店","電","墊","殿","甸","澱","奠","佃","鈿","惦","踮","靛","淀","玷","壂",
                          "癜","坫","婝","扂","橂","琔","田","电","痁","磹","秾","簟","蜔","軈","钿",
                          "阽","頕","驔"],
            dian_6      :[],
            dian_7      :[],

            #ㄉㄧ
            di_space    :["低","滴","氐","熵","袛","仾","墑","奃","彽","提","磾","羝","菂","鍉","镝","隄","鞮"],
            di_3        :["底","抵","邸","柢","砥","牴","詆","呧","骶","坘","坻","弤","扺","拞","掋","氐","詆","菧","觝","诋","趆","軧","閪","阺"],
            di_4        :["第","地","弟","蒂","帝","遞","棣","締","的","諦","娣","墬","旳","玓","杕","睇","馰","偙",
                          "僀","啇","坔","埊","墆","奃","媂","嵽","嶳","怟","梊","楴","樀","渧","焍","珶","甋","碲",
                          "嶳","禘","绨","缔","肑","蔕","虳","螮","谛","踶","軑","递","逓","遰","釱","鍗"],
            di_6        :["迪","笛","狄","敵","的","滌","荻","苖","嫡","嘀","糴","鏑","抵","藋","唙","嚁",
                          "廸","梑","浟","涤","潪","鏑","甋","篴","籴","翟","芽","蔋","蔐","藡","覿","觌",
                          "豴","踧","蹢","適","镝","靮","頔","魡","鸐"],
            di_7        :["弟"],
            #ㄊㄧㄠ
            diao_space  :["挑","祧","佻","庣","恌","旫","聎","莜","蓨","鮡"],
            diao_3      :["挑","窕","嬥","宨","晀","窱","誂"],
            diao_4      :["跳","眺","糶","朓","嬥","窱","粜","絩","脁","覜","鑃","頫"],
            diao_6      :["條","調","迢","苕","髫","佻","鰷","岧","岹","条","樤","祒",
                          "笤","芀","萔","蜩","调","趒","銚","鋚","鎥","鞗","鲌","鲦",
                          "齠","龆"],
            diao_7      :[],
            
            #ㄉㄧㄝ
            die_space   :["爹","嗲","鰘"],
            die_3       :[],
            die_4       :["耊"],
            die_6       :["跌","蝶","疊","碟","迭","諜","牒","耋","鰈","喋","垤","堞","瓞","蹀","叠","呋","咥","墆",
                          "峌","嵽","嶀","惵","戜","挕","昳","曡","柣","楪","涉","渫","疉","眣","眰","絰","聑","胅",
                          "臷","艓","苵","蜨","褋","褶","褺","詄","谍","趃","跕","镻","鲽","鳉"],
            die_7       :["爹"],

            #ㄉㄧㄥ
            ding_space  :["丁","盯","叮","汀","町","釘","疔","玎","仃","奵","帄","稤","虰","酊","钉","靪"],
            ding_3      :["頂","鼎","酊","耵","嵿","檙","濎","薡","顶","鼑"],
            ding_4      :["定","訂","釘","碇","錠","萣","啶","椗","娗","忊",
                          "掟","矴","碠","磸","腚","订","鋌","钉","铤","锭",
                          "顁","飣"],
            ding_6      :[],
            ding_7      :[],

            #ㄉㄧㄡ
            diu_space   :["丟","銩","丢","乣","厾","铥"],
            diu_3       :[],
            diu_4       :[],
            diu_6       :[],
            diu_7       :[],

            
            #ㄉㄨㄥ
            dong_space  :["東","冬","苳","咚","崠","鶇",
                          "涷","氡","鼕","东","倲","埬",
                          "娻","岽","崬","昸","氭","炵",
                          "笗","菄","蝀","釼","鯟","鸫"],
            
            dong_3      :["董","懂","墥","嬞","箽","蕫","諌"],
            dong_4      :["動","棟","洞","凍","恫","侗","胴","迵","働",
                          "冻","峒","峝","戙","挏","栋","湩","胨","詷",
                          "霘","駧"],
            
            dong_6      :[],
            dong_7      :[],
            
            #ㄉㄡ  
            dou_space   :["都","兜","兠","吺","唗","篼","蔸","郖","魸"],
            dou_3       :["斗","陡","抖","枓","蚪","唗","敨","阧"],
            dou_4       :["豆","逗","鬥","痘","竇","荳","鬪","餖","斣",
                          "梪","毭","浢","瀆","穃","窦","脰","讀","读",
                          "郖","鋀","雬","鬦","鬬"],
            dou_6       :[],
            dou_7       :[],

            #ㄉㄨ
            du_space    :["督","都","嘟","闍","醏"],
            du_3        :["賭","堵","篤","睹","肚","帾","匵","嬻","暏","琽","穒","笃","裻","覩","簬","簵","鬶"],
            du_4        :["簵","度","肚","渡","鍍","妒","蠹","喥","妬","斁","歝","殬","秺","穒","簬","簵","荰","螙","蠧","镀","靯"],
            du_6        :["讀","獨","毒","瀆","犢","牘","黷","髑","櫝","儥","殰","椟","渎","牍","犊","独","瓄","皾","碡","纛","蝳",
                          "襡","讟","读","豄","贕","鑟","韇","韣","韥","頓","顿","騳","黩"],
               
            du_7        :[],

            #ㄉㄨㄢ
            duan_space  :["端","耑","偳","剬","媏","褍","鍴"],
            duan_3      :["短"],
            duan_4      :["段","斷","緞","鍛","椴","籪","断","毈","煅","瑖","碫","簖","缎","腶","葮","躖","锻"],
            duan_6      :[],
            duan_7      :[],

            
            #ㄉㄨㄟ
            dui_space   :["堆","垖","塠","嵟","痽","碓","穝","追","陮","頧"],

            dui_3       :[],
            dui_4       :["對","隊","兌","碓","懟","兊","兑","对","対","怼",
                          "憝","敦","濧","濻","瀢","瀩","祋","穞","綐","薱",
                          "譈","譵","轛","錞","镦","队"],
            dui_6       :[],
            dui_7       :[],
            #ㄉㄨㄣ
            dun_space   :["敦","蹲","墩","惇","礅","墪","弴","撉","燉","犜","穣","蜳","鐓","鐜","镦","驐"],
            dun_3       :["躉","盹","趸"],
            dun_4       :["頓","噸","燉","盾","鈍","遁","沌","遯","炖","飩",
                          "伅","囤","坉","崸","庉","憞","扽","潡","盹","腞",
                          "踲","腞","钝","頬","顿","鶨"],
            dun_6       :[],
            dun_7       :[],

            #ㄉㄨㄛ
            duo_space   :["多","哆","夛","崜","柁","茤"],
            duo_3       :["朵","躲","垛","綞","埵","嚲","憜","挅","挆",
                          "朶","痑","缍","袳","趓","躱","軃","鬌"],
            duo_4       :["剁","舵","墮","踱","惰","跺","馱","咄",
                          "度","刴","垛","垜","堕","墯","嶞","挆",
                          "杝","柂","柮","沱","炧","炨","笜","袉",
                          "貀","跢","陊","陏","飿","驮","鵽"],
            duo_6      :["奪","鐸","掇","襗","凙","剟","剫","喥",
                      "多","夛","夺","敓","敚","敠","敪","椯","毲",
                      "痥","腏","莌","裰","铎","鮵"],
            duo_7      :["朵"],

            #ㄜ
            e_space     :["痾","阿","婀","屙","哦","妸","娿","峉","峩","錒"],
            e_3         :["噁","婐","恶","頋"],
            e_4         :["惡","餓","俄","厄","顎","鱷","鄂","鶚","扼",
                          "遏","萼","諤","噩","愕","呃","軛","堊","鍔",
                          "阨","姶","偔","僫","卾","呝","咢","唖","啞",
                          "囐","圔","堨","堮","屵","岋","崿","颚","嶭",
                          "悪","硆","戹","搹","枙","櫮","湂","琧","砐",
                          "砨","硆","窎","胺","腭","苊","蕚","蘁","蚅",
                          "蝁","覨","詻","讍","谔","豟","貖","軶","轭",
                          "遌","鑩","锷","閼","阏","阸","頞","颚","頞",
                          "饿","魥","鰐","鳄","鳑","鹗","齶"],
            e_6          :["額","鵝","娥","俄","峨","蛾","訛","莪","吪",
                           "哦","囮","涐","珴","皒","睋","硪","磀","蚵",
                           "誐","譌","讹","迗","鈋","鋨","锇","頟","额",
                           "騀","魤","鰪","鵞","鹅"],
            e_7         :["呃","哦"],
            #ㄞ
            ei_space    :["哀","埃","挨","唉","ㄞ","哎","誒","锿"],
            ei_3        :["矮","藹","靄","毐","譪","佁","敱","昹",
                          "欸","絠","蔼","絠","躷","霭","馤"],
            ei_4        :["愛","艾","礙","隘","璦","曖","嬡","噯","靉",
                          "乂","譺","薆","伌","僾","嗳","堨","嫒","懝",
                          "暧","濭","爱","瑷","皧","瞹","砹","硋","碍",
                          "誒","譪","賹","鑀","镴","阸","餲","嬡","鴱"],
            ei_6        :["癌","捱","皚","呆","嘊","嵦","敳","皑","騃"],
            
            ei_7        :["唉"],
            
            
            en_space    :["恩","嗯","ㄣ","煾","蒽"], 
            en_3        :[],
            en_4        :["摁"],
            en_6        :[""],
            en_7        :[""],

            er_space    :["兒","ㄦ"],
            er_3        :["爾","耳","餌","洱","珥","邇","薾","鉺","儞","尒","尔","栮","峏","迩","铒","饵","駬"],
            er_4        :["二","貳","佴","刵","咡","弍","樲","毦","眲","聏","衈","誀","貮","贰","ㄦˋ"],
            er_6        :["而","兒","鴯","唲","鮞","侕","児","栭","檽","洏","耏","聏","胹","荋","袻","輀","轜","陑","隭","髵","鲕","鸸"],
            er_7        :[],

            fa_space    :["嗎","媽","嬤","嘛","妈","嬷","臜","蚂"],
            fa_3        :["馬","瑪","碼","嘜","螞","嗎","溤","鎷","吗","犸","玛","码","蚂","马","鰢","鷌"],
            fa_4        :["罵","傌","禡","嘜","杩","榪","獁","睰","蚂","螞","閁","駡","骂"],
            fa_6        :["麻","嘛","痲","蔴","蟆","吗","尛","犘","麼","麽"],
            fa_7        :["嗎","嘛","媽","蟆","吗","嬤","蟇"],
               
            fan_space   :["屘","颟"],
            fan_3       :["滿","屘","悗","満","满","矕","螨","鏋"],
            fan_4       :["慢","曼","漫","蔓","嫚","幔","縵","謾","僈","鏝","墁","摱","澫","澷","熳","獌","缦","蔄","谩","鄤","镘"],
            fan_6       :["蠻","鰻","瞞","饅","蹣","璊","顢","埋","姏","悗","慲","槾","樠","漫","瞒","脵","脷","蔓","蛮","謾","谩","鞔","馒","鬗","鬘","鳗"],
            fan_7       :[],

            fang_space  :[],
            fang_3      :["蟒","莽","壾","庬","汒","漭","硥","茻","莾","蠎"],
            fang_4      :["吂"],
            fang_6      :["忙","盲","茫","氓","邙","厖","吂","哤","奀",
                          "娏","尨","庬","恾","杗","汒","浝","牻","狵","痝",
                          "盳","硭","笀","蘉","蛖","釯","鋩","駹","鼆"],
            #ㄈㄟ
            fei_space   :["啡","非","菲","飛","妃","啡","緋","霏","蜚","扉",
                          "馡","婔","渄","妃","緋","霏","蜚","扉","飞","餥",
                          "騑","騛","鯡","鲪","鲱"],
            fei_3       :["斐","匪","翡","誹","榧","奜","悱","菲","蜚",
                          "棐","朏","篚","蕜","诽","阇","餥"],
            fei_4       :["費","廢","肺","沸","吠","芾","癈","狒","痱"
                          "俷","剕","厞","屝","废","廃","怫","怫","曊",
                          "櫠","濷","疿","砩","胇","蕟","蟦","费","鐨",
                          "蝞","陫","靅","鼣"],
            fei_6       :["肥","腓","淝","萉","蜰","蟦"],
            fei_7       :[],

            fen_space   :["分","芬","紛","氛","奮","忿","雰","吩","昐","棻",
                          "岎","帉","梤","玢","砏","纷","酚","吩","訜","翂",
                          "鈖","餴","饙","鳻"],
                          
            fen_3       :["粉","黺"],
            fen_4       :["忿","分","憤","糞","奮","忿","僨","坋","偾","愤",
                          "朆","愤","橨","瀵","獖","秎","粪","羵","膹","魵",
                          "鱝","鳈"],
            fen_6       :["焚","墳","汾","豶","棼","枌","坟","枌","妢","帉",
                          "幩","弅","橨","濆","炃","燌","燓","羒","羵","肦",
                          "蕡","蒶","蚠","蚡","轒","鐼","隫","馚","馩","黂",
                          "鼖","鼢"],
            fen_7       :["們","們","捫","亹","扪","樠","璊","穈","菛","虋",
                          "鍆","钔","閅"],
            feng_space  :["風","豐","封","峰","鋒","楓","蜂","瘋","烽",
                          "丰","峯","灃","酆","妦","捀","蘴","桻","仹",
                          "偑","僼","凨","凬","凮","堼","寷","崶","枫",
                          "檒","犎","猦","疯","盽","砜","笂","篈","肨",
                          "莑","葑","蠭","諷","鄷","鏠","锋","靊","飌",
                          "风","麷"],
            feng_3      :["唪","覂","讽"],
            feng_4      :["鳳","奉","縫","俸","諷","凤","凮","湗","焨",
                          "煈","甮","綘","缝","賵","風","鳯","鴌"],
            feng_6      :["逢","馮","縫","夆","冯","堸","摓","渢","漨",
                          "笇","綘","缝","艂","逄"],
            
            feng_7      :[],
            
            fo_space    :[],
            fo_3        :[],
            fo_4        :[],
            fo_6        :["佛","仏","坲"],
            fo_7        :[],

            #ㄈㄡ
            fou_space   :[],
            fou_3       :["否","不","殕","缶","缹","缻","鴀"],
            fou_4       :[],
            fou_6       :["剻","哹","紑","罘","艀","芣","錇"],
            fou_7       :[],

            
            #ㄈㄨ
            fu_space   :["夫","膚","敷","伕","孵","麩","趺","衭","尃",
                         "柎","鈇","傅","妋","姇","怤","懯","旉","枹",
                         "泭","溥","玞","璷","砆","稃","筟","箙","粰",
                         "糐","紨","綒","罦","肤","荴","跗","邞","鄜",
                         "饾","鳺","麬","麱","麸"],
               
            fu_3       :["府","甫","輔","腐","撫","釜","嘸","斧","俯",
                         "腑","滏","拊","黼","暊","俌","俛","冹","弣",
                         "抚","捬","旊","柎","焤","父","盙","秿","簠",
                         "胕","脯","莆","蚥","蜅","軵","辅","郙","頫",
                         "鯆"],
            fu_4       :["副","富","赴","復","付","附","傅","婦","負",
                         "父","複","覆","腹","賦","馥","阜","訃","褔",
                         "咐","駙","蝮","仅","偩","冨","圑","坿","复",
                         "妇","姇","婏","媍","嬔","峊","椱","榑","疈",
                         "癁","祔","稪","竎","筜","緮","缚","胕","萯",
                         "蕧","蚹","蛗","蝜","袝","詂","讣","賻","负",
                         "赋","蕧","蛗","赙","鍑","驸","鮒","鰒","鲋",
                         "鳆","鳚",],
            fu_6       :["福","服","幅","浮","扶","畐","符","伏","芙",
                         "巿","弗","孚","拂","氟","蝠","彿","縛","垺",
                         "芙","俘","涪","袱","匐","祓","鳧","蜉","黻",
                         "榑","茀","鵩","桴","紱","茯","苻","乀","佛",
                         "偪","凫","枎","刜","垘","夫","宓","岪","帗",
                         "怫","澓","昲","枹","柫","栿","棴","沷","泭",
                         "帗","畗","笰","箙","紼","絥","綍","绂","绋",
                         "罘","罦","翇","胕","艀","艴","綍","咈","洑",
                         "虙","蚨","袚","諨","踾","辐","郛","绂","鉘",
                         "鉜","韍","韛","颫","颰","饾","骕","髴","鮄",
                         "鳬","鮄","鴔","鶝"],              
            fu_7       :[],
            ga_space   :[],
            ga_3       :[],
            ga_4       :[],
            ga_6       :[],
            ga_7       :[],

            gai_space  :["該","垓","祴","賅","侅","姟","峐","晐","畡",
                         "絯","胲","荄","该","豥","賌","赅","郂","陔",
                         "隑"],
            gai_3      :["改","忋"],
            gai_4      :["蓋","概","鈣","溉","丐","乢","匃","匄","戤",
                         "摡","槩","槪","漑","瓂","盖","葢","鑉","钙"],
               
               
            gai_6      :[],
            gai_7      :[],

            gan_space  :["乾","桿","肝","甘","柑","干","竿","杆","尷"
                         "咁","矸","酐","坩","疳","泔","苷","乹","亁",
                         "凲","尴","嵅","忓","攼","氹","玕","筸","鳱",
                         "筺","筼","筽","粓","芉","虷","蜬","迀","飦"],
            gan_3      :["感","趕","敢","桿","稈","擀","橄","撖","仠",
                         "澉","皯","盰","秆","筿","簳","芉","衦","赶",
                         "鱤"],
            gan_4      :["幹","淦","贛","紺","榦","倝","嵅","旰","檊",
                         "涻","灨","簳","绀","詌","贑","赣","骭"],
            gan_6      :[],
            gan_7      :[],
            gang_space :["剛","鋼","岡","扛","綱","崗","缸","肛","罡",
                         "堽","杠","釭","亢","刚","堈","掆","棡","牨",
                         "犅","疘","碙","笐","纲","罁","舡","鎠","钢"],
            gang_3     :["港","崗"],
            gang_4     :["槓","戇","戆","焵","鋼","钢"],
            gang_6     :[],
            gang_7     :[],

            
            gao_space  :["高","糕","膏","篙","皋","睪","羔","睾","咎",
                         "槔","槹","橰","櫜","滜","皐","睪","臯","韟",
                         "羙","餻","鷎","鷱","鼛"],
            gao_3      :["搞","稿","槁","杲","縞","睪","筶","撹","攪","暠","槀","檺","稁","稾","箚","缟","菒","藁"
                         ,"藳","鎬","镐"],
            gao_4      :["告","誥","鋯","郜","叝","吿","煰","祰","禞","诰","锆"],
            gao_6      :[],
            gao_7      :[],
            
            
            ge_space   :["歌","哥","鴿","割","戈","擱","胳","菏","疙",
                         "咯","仡","妿","戓","戨","搁","渮","滒","牁",
                         "牫","牱","纥","肐","謌","鎶","鴚","鸽","麧"],
            ge_3       :["葛","舸","哿","個","各","合","擖","砈","笴",
                         "蓋","騔","魺"],
            ge_4       :["各","各","鉻","箇","个","硌","虼","铬","骎"],
            ge_6       :["格","隔","閣","革","噶","蛤","鎘","閤","膈",
                         "葛","骼","嗝","頜","佮","挌","翮","茖","轕",
                         "假","匌","呄","咯","塥","愅","搁","搹","搿",
                         "擖","敆","敋","槅","滆","獦","臈","臵","蛒",
                         "裓","觡","諽","輵","郃","醗","镉","阁","鞐",
                         "鞷","韐","韚","鬲","鮯","鰪","鵅","齃"],
            ge_7       :["個","哥"],

            gei_space  :[],
            gei_3      :["給","给"],
            gei_4      :[],
            gei_6      :[],
            gei_7      :[],
            
            geng_space :["更","耕","庚","岡","綱","崗","缸","肛","揯",
                         "浭","畊","秔","緪","羮","菮","赓","鶊"],
            geng_3     :["耿","梗","哽","鯁","埂","骾","挭","炛","綆",
                         "绠","莄","郠","頸","颈","鲀","鲠"],
            geng_4     :["更","亙","堩","揯","絚"],
            geng_6     :[],
            geng_7     :[],

            gong_space :["公","工","更","供","宮","功","攻","龔","恭","弓",
                         "躬","肱","蚣","觥","紅","侊","共","匑","厷",
                         "咣","塨","宫","幊","杛","愩","玜","疘","碽",
                         "篏","篒","篢","糼","糿","红","觵","躳","釭",
                         "靏","髸","龏","龚"],
            gong_3     :["梗","鲠","耿","哽","鯁","埂","骾","挭","炛","綆",
                         "绠","莄","郠","頸","颈","鲀","鲠",],
             
            gong_4     :["亙","更","堩","揯","絚"],
            gong_6     :[],
            gong_7     :[],
            
            gou_space  :["工","公","供","宮","功","攻","龔","恭","弓","躬",
                         "肱","蚣","觥","紅","侊","共","匑","厷","咣","塨",
                         "宫","幊","愩","杛","玜","疘","碽","篏","篒","篢",
                         "糼","糿","红","觵","躳","釭","靏","髸","龏","龚"],
            gou_3     :["穬","拱","汞","栱","共","奣","孒","巩","廾","拲",
                        "珙","礦","穬","蛬","輁","銾"],
            gou_4     :["共","貢","供","摃","羾","贡"],
            gou_6     :[],
            gou_7     :[],

            guai_space:["乖","掴"],
            guai_3    :["拐","柺","枴","箉"],
            guai_4    :["怪","夬","叏","廥","旝","癐"],
            guai_6    :[],
            guai_7    :[],

            guan_space:["關","官","觀","棺","倌","冠","鰥","綸","毌","瘝",
                        "癏","矜","窤","簓","簔","簗","纶","莞","蒄","覌",
                        "観","观","輨","関","闗","鱞","鳏"],
            guan_3    :["館","管","莞","琯","舘","悹","痯","筦","脘","輨","錧","馆"],
            guan_4    :["冠","灌","罐","慣","貫","摜","鸛","瓘","盥",
                        "觀","丱","卝","悹","悺","惯","掼","樌","毌",
                        "泴","涫","潅","爟","矔","祼","簗","观","贯",
                        "遦","鏆","鑵","雚","鱹","鹳"],
               
            guan_6    :[],
            guan_7    :[],

            gu_space  :["辜","估","菇","孤","姑","咕","箍","沽","轂","鈷","呱","菰",
                        "鮕","鴣","蛄","觚","哌","夃","嫴","家","柧","橭","毂","泒",
                        "痼","笟","箛","罛","苽","軱","轱","酤","鈲","骨","鸪"],

            gu_3      :["股","古","鼓","谷","骨","穀","榖","罟","盬","牯","蠱","汩",
                        "詁","滑","瞽","嘏","臌","薣","賈","凸","唂","唃","啒","尳",
                        "愲","扢","抇","杚","榾","毂","沽","淈","濲","瀔","焸","狜",
                        "瑴","皷","糓","縎","羖","蓇","蛊","蛌","诂","贾","轂","鈷",
                        "钴","餶","鵠","鶻","鹄","鹘","鼔"],
            gu_4      :["故","顧","固","雇","僱","錮","鯝","崮","痼","凅","堌","梏",
                        "估","告","崓","棝","榾","牿","祮","祻","稒","锢","顾","鲴",
                        "鲹","鶮"],
            gu_6      :["骨","鶻"],
            gu_7      :["姑"],
            
               
            guan_3    :["館","管","莞","琯","舘","悹","痯","筦","脘","輨","錧","馆"],
            guan_4    :["冠","灌","罐","慣","貫","摜","鸛","瓘","盥",
                        "觀","丱","卝","悹","悺","惯","掼","樌","毌",
                        "泴","涫","潅","爟","矔","祼","簗","观","贯",
                        "遦","鏆","鑵","雚","鱹","鹳"],
               
            guan_6    :[],
            guan_7    :[],

            
            gui_space :["規","歸","龜","鮭","圭","瑰","珪","閨","皈","硅","媯","槻",
                        "亀","傀","妫","嫢","帰","廆","归","摫","槼","洼","溈","瞡",
                        "窐","罓","茥","袿","规","邽","郌","銈","闺","雟","騩","鬹",
                        "鲑","龟"],
            gui_3      :["軌","鬼","癸","詭","匭","氿","晷","宄","簋","佹","匦","厬",
                         "垝","姽","孂","庪","恑","攱","湀","祪","蛫","蟡","觤","诡",
                         "轨","陒"],
            gui_4      :["貴","櫃","桂","跪","瞶","撌","柜","溎","鱖","乔","刿","劌","匱",
                         "嬀","嶡","撌","攰","昋","暩","桧","炔","璝","瓌","禬","筀","簱",
                         "蓕","襘","贵","鞼","鱥","鳜"],

            gui_6      :[],
            gui_7      :[],

            
            guang_space:["光","洸","胱","桄","銧","珖","僙","垙","姯","灮","炗","炚","炛","烡","硄","茪","輄","黆"],
            guang_3    :["廣","獷","広","犷","臩","黋"],
            guang_4    :["逛","矌","撗","桄","臦","臩"],
            guang_6    :[],
            guang_7    :[],
               
            guo_space   :["郭","鍋","嘓","蟈","埻","墎","堝","冎","叧","呙",
                          "埚","崞","櫎","涡","渦","濄","瘑","緺","蝈","過",
                          "鈛","锅"],
            guo_3       :["果","粿","裹","菓","槨","惈","椁","淉","猓","綶",
                          "蜾","輠","錁","鐹","猓"],
            guo_4       :["過","过"],
            guo_6       :[],
            guo_7       :[],

            ha_space    :["哈","鉿","铪"],
            ha_3        :["哈"],
            ha_4        :[],
            ha_6        :["蝦","蛤"],
            ha_7        :[],

            hai_space   :["嗨","咍","咳"],
            hai_3       :["海","烸","酼","醢","靱"],
            hai_4       :["害","駭","亥","氦","嗐","嗨","絯","餀","饚","駴",
                          "骇"],
            hai_6       :["還","孩","骸","頦","豥"],
            hai_7       :[],

            han_space   :["酣","憨","蚶","鼾","頇","唅","嫨","炶","甝","谽","顸","馠","魽"],
            han_3       :["喊","罕","厂","厈","嚂","浫","蔊","豃","阚","鬫"],
            han_4       :["和","漢","翰","汗","瀚","旱","焊","憾","悍","撼",
                          "頷","捍","銲","菡","扞","駻","熯","傼","咊","哻",
                          "垾","娨","屽","惒","攌","攼","旰","晘","晥","暵",
                          "涆","淊","犴","猂","琀","皔","睅","罕","莟","蛿",
                          "蜭","螒","譀","豻","貋","釬","鋎","閈","雗","鞎",
                          "頜","顄","颌","颔","馯","鶾"],
            han_6      :["韓","函","含","涵","寒","汗","邯","佄","凾","唅",
                         "圅","娢","崡","幹","晗","梒","榦","浛","澏","焓",
                         "琀","甝","筨","虷","蜬","邗","鋡","韩"],
            han_7      :[],

            hang_space :["夯","籡"],
            hang_3     :["奛","酐"],
            hang_4     :["行","沆"],
            hang_6     :["行","沆","航","杭","吭","妔","斻","桁","绗","肮",
                         "苀","蚢","貥","迒","雽","頏","颃","魧"],
            hang_7     :[],

            
            hao_space  :["蒿","侾","嚆","茠","薅","迲"],
            hao_3      :["好","郝","恏"],
            hao_4      :["號","浩","耗","皓","好","灝","昊","鎬","顥","皞","澔","秏","傐","号","哠","夰","悎","昦",
                         "晧","暤","暭","涸","淏","滈","瀥","灏","皜","皡","皥","箚","聕","薃","藃","鄗","镐","颢",
                         "鰝"],
            hao_6      :["豪","毫","嚎","濠","蠔","壕","號","蚝","儫","勂","嗥","嘷","噑","椃","獆","獋","獔","籇",
                         "蚵","諕","譹","貉","鶴"],
            hao_7      :[],

            he_space   :["喝","呵","訶","嗬","峆","抲","诃"],
            he_3       :["賀","赫","鶴","荷","嚇","喝","和",
                         "何","佫","俰","嗃","暍","煂","熇",
                         "爀","猲","癋","碋","粂","翯","蠚",
                         "袔","謞","贺","郝","鸖","鹤"],
            he_6       :["和","何","合","河","核","盒","荷","禾","褐",
                         "闔","龢","涸","覈","蝎","劾","閡","貉","紇",
                         "乢","咊","哬","啝","嗑","姀","廅","惒","敆",
                         "曷","柇","楁","毼","渮","渴","滆","澕","熆",
                         "狢","盇","盉","盍","盖","礉","篕","籺","纥",
                         "翮","耠","菏","萂","葢","蒚","蓋","螛","訸",
                         "詥","貈","趷","郃","釛","鉌","鉿","閤","阂",
                         "阖","鞨","颌","餲","魺","鶡","麧","齃","齕"],
            he_7       :["呵"],

            hei_space  :["黑","嘿","潶","黒"],
            hei_3      :["黑"],
            hei_4      :["嘿"],
            hei_6      :[],
            hei_7      :["嘿"],

            hen_space  :[],
            hen_3      :["很","狠"],
            hen_4      :["恨"],
            hen_6      :["痕","拫","鞎"],
            hen_7      :[],

            heng_space  :["亨","哼","脝","諻","悙"],
            heng_3      :["很","狠"],
            heng_4      :["橫","澋","哼","啈","撔","横","絎"],
            heng_6      :["恆","橫","衡","珩","恒","姮","桁",
                          "鴴","蘅","楻","佷","揘","横","胻",
                          "誙","諻","遖","鐄","鑅"],
               
            heng_7      :[],
            hong_space  :["轟","烘","魟","哄","箜","揈","吽","呍","哅","渹","焢","粏","粐","薨","谾","輷","轰","鍧","顭"],
            hong_3      :["哄","嗊","晎","粐"],
            hong_4      :["鬨","蕻","澒","戅","汞","粐","讧","鍙","閧","闀"],
            hong_6      :["洪","紅","宏","鴻","弘","虹","泓","紘","閎",
                          "浤","鋐","竑","鈜","葒","汯","黌","訌","苰",
                          "竤","翃","仜","叿","吰","妅","娂","宖","彋",
                          "彋","渱","潂","灴","玒","瓨","硡","篊","粠",
                          "紭","綋","红","翝","耾","舼","荭","葓","触",
                          "谹","谼","闂","闳","霐","霟","鞃","鸿","黉"],
            hong_7      :[],

            hou_space   :["齁"],
            hou_3       :["吼","吽","犼"],
            hou_4       :["後","厚","候","后","鱟","逅","垕","堠","洉",
                          "缿","郈","鄇","鈨","鮜","鲎"],
            hou_6       :["鯸","侯","猴","喉","餱","瘊","帿","睺","矦","篌",
                          "糇","翭","葔","鄇","銗","骺","鍭","鯸"],
            hou_7       :[],

            hu_space    :["呼","乎","忽","惚","虎","匢","匫","吰",
                          "唿","啒","嘑","垀","寣","峘","幠","恗",
                          "惖","戲","昒","曶","欻","歑","歘","泘",
                          "淲","淴","滹","烀","烼","猢","粭","膴",
                          "苸","虍","虖","謼","軤","轷","鍃","雐",
                          "雽"],
            hu_3        :["虎","唬","琥","滸","汻","浒","萀","虝",
                          "許","铚"],
            hu_4        :["戶","護","互","扈","滬","瓠","謢","笏","槴",
                          "怙","祜","冱","冴","婟","嫭","嫮","嬳","岵",
                          "帍","户","戸","戽","摢","昈","枑","楛","沍",
                          "沪","熩","玍","簄","糊","綔","臛","芐","芦",
                          "蔰","豰","鄠","釺","頀","鳸","鹱"],

            hu_6        :["胡","湖","壺","糊","弧","狐","鬍","瑚","蝴",
                          "鵠","葫","斛","箎","楜","餬","醐","槲","猢",
                          "衚","囫","和","喖","嘝","壶","壷","媩","抇",
                          "搰","瀫","焀","煳","瓳","箶","絗","縠","蔛",
                          "螜","觳","鍸","頶","駅","鰗","鶘","鶦","鶻",
                          "鹄","鹕","鹘"],
            hu_7        :["呼"],

            hua_space   :["花","嘩","華","化","哗","澅","芲","荂","蕐","錵","鷨"],
            hua_3       :[],
            hua_4       :["畫","化","話","劃","樺","華","繣","咶","婳","嫿","嬅",
                          "崋","摦","杹","桦","槬","澅","画","畵","糘","舙","蕐",
                          "蘳","觟","话"],
            hua_6       :["華","滑","划","驊","鏵","譁","猾","猾","崋","劃","哗",
                          "搳","敌","樺","磆","蕐","螖","豁","釫","铧","骅"],

            hua_7       :[],

            huai_space  :[],
            huai_3      :[],
            huai_4      :["壞","咶","坏","壊","孬","蘹","蘾","諙"],
            huai_6      :["淮","懷","踝","槐","徊","佪","怀","懐",
                          "蝴","櫰","瀤","耲","蘹","褢","褱"],
            huai_7      :[],

            huan_space  :["貛","歡","獾","嚾","巜","懽","欢","歓","犿","讙","酄","驩","鴅","鵍"],
            huan_3      :["緩","唍","嵈","晥","浣","澣","皖","睆","缓","藧","輐","鰀"],
            huan_4      :["換","患","換","幻","喚","奐","渙","瘓","宦","漶","瑍","逭",
                          "豢","唤","喚","垸","奂","嚾","愌","换","擐","梙","梡","槵",
                          "涣","痪","焕","瞣","肒","觨","躛","轘","鯇","鲖","鲩"],
               
            huan_6      :["還","韓","環","桓","鍰","圜","鐶","繯","嬛","鬟","寏","峘",
                          "懁","捖","梡","洹","澴","狟","环","瓛","糫","絙","缳","羦",
                          "肒","荁","萈","萑","豲","貆","轘","还","锾","闤","雈"],
               
            huan_7      :[],

            huang_space :["荒","慌","肓","嚝","塃","巟","朚","衁"],
            huang_3     :["粐","哄","晎","粐"],
            huang_4     :["晃","岲","愰","晄","曂","軦"],
            huang_6     :["黃","煌","皇","遑","磺","凰","璜","隍",
                          "惶","簧","潢","鍠","篁","湟","徨","堭",
                          "蝗","熿","蟥","偟","喤","鰉","墴","媓",
                          "崲","揘","撗","獚","瑝","癀","穔","糹",
                          "艎","葟","趪","鈬","韹","餭","騜","鱑",
                          "鳇","鳛","鷬","黄"],
            huang_7     :[],

            hui_space   :["輝","揮","灰","暉","徽","恢","煇","麾",
                          "褘","翬","詼","隳","鰴","咴","噅","噕",
                          "堕","墮","婎","幑","拻","挥","撝","晖",
                          "洃","瀈","灳","烣","珲","睳","禈","褌",
                          "诙","豗","辉","钘","隓","顪","骍"],
            hui_3        :["毀","悔","虫","燬","會","譭","誨","檓",
                           "毁","毇","湏","烠","虺","蛕","賄","骍"],
               
            hui_4        :["會","惠","慧","匯","繪","賄","蕙","卉",
                           "燴","彙","喙","薈","諱","穢","譿","彗",
                           "誨","晦"],
            hui_6        :["回","迴","洄","茴","囘","囬","廻","廽",
                           "恛","痐","藱","蚘","蛔","蜖","逥","鮰"],
            hui_7        :[],

            hun_space    :["婚","昏","葷","惛","敯","昬","棔","殙",
                           "涽","湣","睧","睯","荤","蔒","閽","阍"],
            hun_3        :["混","睔","鯇","鯶"],
            hun_4        :["混","諢","溷","俒","倱","圂","婫","慁","梡","渾","焝","诨","輥"],
            hun_6        :["魂","渾","琿","混","餛","堚","媈","昆","棞","楎","浑","珲","繉",
                           "轋","钘","顐","餫","馄","鼲"],
            hun_7        :[],
               
            huo_space    :["劐","豁","锪"],
            huo_3        :["火","夥","伙","灬","炛","邩","鈥","钬","飠"],
            huo_4        :["或","獲","貨","霍","禍","惑","穫","豁","壑",
                           "藿","鑊","和","剨","咟","嗀","嚄","嚛","嚿",
                           "奯","彠","捇","掝","擭","攉","旤","曤","楇",
                           "檴","沎","湱","濩","瀖","瓁","癨","眓","矆",
                           "矐","矱","砉","硅","礊","祸","紦","耯","臒",
                           "臛","艧","蒦","蠖","謋","货","镬","閄","雘",
                           "靃","韄","騞","鱯","鸌"],
            huo_6        :["活","鈥","佸","姡","秮","秳","萿"],
            huo_7        :["和"],

            ji_space     :["機","基","雞","積","肌","績","跡","激","姬",
                           "蹟","躋","稽","譏","幾","磯","畸","碁","羈",
                           "乩","飢","嘰","饑","璣","嵇","箕","几","屐",
                           "笄","畿","樍","咭","勣","机","稘","觭","禨",
                           "齏","剞","奇","迹","齎","丌","其","击","刉",
                           "卟","唧","嗘","坖","尐","朞","峜","居","敧",
                           "期","枅","槣","櫅","欚","毄","犄","癘","癪",
                           "积","竒","筓","簊","绩","羁","羇","耭","聻",
                           
                           "虀","虮","蛣","襀","覉","覊","諅","譤","讥",
                           "赍","跻","鎺","鐖","鑇","鑙","隮","鞿","躸",
                           "韲","饥","饻","鰿","鳮","鷄","鸄","鸡","麡",
                           "齍","齑"],
            ji_3         :["幾","己","擠","脊","給","麂","戟","濟","丮",
                           "几","剞","妀","嵴","庋","挤","掎","撠","泲",
                           "犱","玘","穖","纪","给","蟣","踦","撠","济",
                           "魕","魢"],
            ji_4         :["季","既","濟","計","記","紀","繼","技","暨",
                           "寄","祭","劑","際","繫","齌","忌","妓","伎",
                           "驥","冀","悸","髻","霽","薊","覬","鯽","稷",
                           "騎","鮆","薺","徛","芰","鯚","偈","兾","刉",
                           "剤","剤","哜","嚌","旣","垍","塈","墍","彐",
                           "彑","惎","懻","斊","旡","暩","曁","梞","檕",
                           "檵","櫭","洎","济","済","漈","瀱","璾","痵",
                           "瘈","皍","瞡","稩","穄","穊","穧","継","縘",
                           "纪","继","罽","臮","荠","萕","葪","蔇","蘎",
                           "蘮","蔇","蘻","裚","觊","誋","諅","计","记",
                           "跽","记","躋","际","霁","骥","覬","鬾","鯯",
                           "魝","鱀","鰶","鱭","鲗","鲚","鲫","鵋","齊",
                           "齌"],
            
             ji_6       :["及","即","級","極","籍","吉","急","集","擊",
                          "疾","輯","亟","寂","茍","棘","佶","汲","殛",
                          "楫","笈","嫉","瘠","唧","庴","戢","伋","岌",
                          "洁","姞","蒺","潗","秸","藉","脊","芨",
                          "蕺","鶺","墼","蕀","踖","吃","丮","亼","偮",
                          "卙","卽","喞","圾","堲","塉","嶯","塉","彶",
                          "忣","愱","揖","揤","撃","极","楖","槉","橶",
                          "檝","欴","毄","湒","漃","濈","焏","狤","焏",
                          "皀","皍","禝","箿","级","缉","耤","膌","艥",
                          "莋","蓻","蝍","螏","衱","襋","觙","诘","趞",
                          "蹐","躤","轚","辑","郆","鈒","銡","鍓","鏶",
                          "雦","雧","霵","鞊","鰿","鴶","鷑"],
                          
                          
            ji_7        :[],
            jia_space:["家","加","佳","嘉","珈","迦","痂","傢","枷",
                      "鎵","葭","笳","鴐","耞","泇","茄","夹","袈",
                      "夾","宊","幏","拁","毠","犌","猳","腵","豭",
                      "貑","跏","迌","迚","鉫","镓","麚"],
            jia_3   :["假","甲","賈","鉀","岬","胛","榎","徦","舺",
                      "瘕","叚","夏","夓","婽","斚","斝","椵","檟",
                      "玾","贾","钾"],
            jia_4    :["價","架","嫁","駕","假","稼","价","価","夾",
                      "幏","榢","賈","驾"],
            jia_6    :["夾","頰","莢","戛","鋏","筴","浹","唊","蛺",
                      "圿","埉","夹","恝","戞","扴","挟","挾","梜",                     
                     "浃","硈","磍","秸","舺","荚","蛱","袷","裌",
                     "跲","郏","鉿","郟","铗","藉","脊","芨","蕺",
                     "鵊"],
               
            jia_7    :[],
               
            jian_space:["間","監","兼","堅","肩","尖","煎","姦","奸",
                        "緘","艱","鰹","菅","箋","殲","戔","廌","犍",
                        "牋","蒹","湔","鰜","鶼","椷","偂","冿","凲",
                        "囏","坚","姧","尶","幵","惤","开","戋","揃",
                        "搛","椾","櫼","歼","淺","渐","溅","漸","濺",
                        "瀐","瀸","熞","櫼","猏","玪","监","睷","礛",
                        "礷","笺","籛","縑","缄","缣","艰","菺","葌",
                        "蔪","蕑","虃","譼","豜","鈃","鑯","閚","间",
                        "靬","鞬","鞯","韀","韉","韯","餰","馢","騝",
                        "鬋","魐","鲉","鲣","鳽","鵳","鹣","麉","黬"],
            jian_3   :["檢","減","簡","剪","撿","鹼","揀","儉","繭",
                        "柬","瞼","翦","蹇","碱","筧","戩","挸","俭",
                        "倹","减","囝","堿","寋","弿","拣","捡","揃",
                        "暕","枧","检","検","湕","瀽","瑐","睑","硷",
                        "笕","暕","絸","臉","简","藆","蠒","襺","謇",
                        "謭","譾","谫","趼","錢","锏","鰔","鹻"],
               
            jian_4   :[ "建","件","見","健","漸","艦","鑑","鍵","劍",
                        "箭","濺","薦","賤","腱","鑒","踐","諫","間",
                        "荐","澗","鐧","毽","餞","僭","珔","閒","楗",
                        "洊","監","鐗","侟","俴","剑","剣","劎","劒",
                        "劔","徤","揵","擶","旔","栫","梘","榗","槛",
                        "檻","涧","渐","溅","瀳","牮","监","瞯","瞷",
                        "礀","糋","糮","続","綛","繝","臶","舰","葥",
                        "蔪","螹","襉","覵","见","諓","譼","谏","贱",
                        "趝","践","踺","轞","鉴","鋻","鍳","鏩","鑬",
                        "鑳","锏","键","间","饯","鰎"],
            jian_6   :[],
            jian_7   :[],

            jiang_space:["將","江","蔣","槳","薑","奨","僵","韁","橿",
                         "殭","豇","缰","傹","壃","将","彊","摪","浆",
                         "瓨","畕","畺","疅","矼","礓","繮","翞","茳",
                         "葁","螿"],
            jiang_3   :["獎","講","蔣","槳","奖","奨","奬","桨","膙",
                        "蒋","讲","顜"],
            
               
            jiang_4   :[ "降","醬","匠","將","絳","強","匞","夅","嵹",
                         "弜","降","弶","彊","摾","洚","浆","犟","糡","糨",
                         "绛","萢","袶","謽","酱"],
            jiang_6   :[],
            jiang_7   :[],
            
            
            jiao_space:[ "交","教","膠","焦","嬌","礁","澆","蕉","郊",
                         "椒","驕","跤","蛟","鮫","茭","噍","鷦","艽",
                         "穚","僬","敎","儌","咬","嘄","姣","娇","嶕",
                         "徼","憍","憿","浇","燋","簥","膲","茮","蟂",
                         "蟂","虠","蟭","詨","鐎","骄","鱎","鲛","鵁",
                         "鷍","鸄","鹪"],
            jiao_3:    [ "繳","腳","角","絞","攪","餃","佼","筊","矯",
                         "剿","狡","皎","勦","姣","僥","撟","湫","煍",
                         "侥","儌","劋","憿","挢","捁","搅","摷","撹",
                         "敿","晈","暞","曒","漅","灚","烄","犞","璬",
                         "皦","矫","绞","缴","脚","臫","蟜","覐","詨",
                         "譑","賋","赑","踋","蹻","較","鉸","铰","饺"],
            jiao_4:    [ "較","叫","教","覺","轎","醮","嶠","窖","校",
                         "叽","呌","嘂","噍","噭","嬓","峤","徼","挍",
                         "斍","斠","滘","漖","潐","灂","獥","珓","皭",
                         "窌","覐","觉","訆","譥","趭","轿","较","釂",
                         "髉","鯲"],

            jiao_6:    [ "嚼","峤","矫"],
            jiao_7:    [ ],

            jie_space  :[ "接","街","皆","揭","階","偕","堦","結","嗟",
                          "啑","喈","啑","媘","媫","幯","掲","擑","椄",
                          "湝","煯","疖","痎","癤","稭","緔","结","脻",
                          "腉","节","菨","薢","蝔","袺","阶","鶛"],
            jie_3      :[ "解","姊","姐","檞","动","姉","媎","觧","飷"],
            jie_4      :[ "屆","界","藉","借","介","戒","芥","誡","玠",
                          "堺","疥","解","砎","丯","价","匧","吤","唶",
                          "喈","届","岕","庎","徣","忦","悈","衸","械",
                          "楐","犗","琾","畍","紒","祴","繲","蚧","褯",
                          "诫","躤","魀","魪"],
            jie_6      :["節","傑","結","杰","截","捷","潔","劫","絜",
                         "婕","竭","詰","羯","楬","訐","拮","桀","擷",
                         "頡","孑","緁","睫","偈","倢","癤","劼","櫛",
                         "碣","榤","桔","滐","偼","刦","刧","刼","卩",
                         "卪","厇","咭","啑","尐","岊","崨","嵑","嵥",
                         "巀","揤","搩","擮","擳","昅","栨","楶","瀄",
                         "犵","狤","疌","緕","緳","结","节","莭","葜",
                         "蓵","蛣","蜐","蝍","蠘","蠞","蠽","衱","袺",
                         "誱","讦","诘","趌","踕","迼","鉣","鍻","鐑",
                         "颉","騔","鮚","鲒","鵖"],

            jie_7      :["姊","姐"],

            jin_space  :["金","今","斤","禁","津","筋","巾","襟","衿",
                         "矜","觔","兓","埐","嶜","惍","浸","濅","珒",
                         "瑧","祲","紟","荕","菳","黅"],

            jin_3      :["緊","僅","緊","儘","謹","瑾","堇","槿","菫",
                         "覲","慬","墐","饉","卺","嫤","巹","廑","懄",
                         "殣","漌","瘽","紧","菦","谨","赾","辀","锦",
                         "馑"],
            jin_4      :["進","近","盡","晉","禁","浸","靳","噤","縉",
                         "妗","燼","寖","藎","贐","伒","僅","僸","儘",
                         "凚","劤","劲","勁","厪","唫","嚍","嬧","尽",
                         "廑","晋","搢","榗","歏","溍","濅","濜","烬",
                         "瑨","璡","瘽","璶","缙","肵","荩","蓳","覲",
                         "觐","賮","赆","进","鄑","齽"],
            jin_6      :[],
            jin_7      :[],

            jing_space :["經","精","晶","驚","鯨","京","菁","睛","莖",
                         "荊","兢","涇","旌","箐","鼱","腈","亰","仱",
                         "坕","婙","婛","巠","惊","旍","更","梷","泾",
                         "猄","粳","経","縅","縆","经","茎","荆","葏",
                         "鲸","鵛","鶁","鶄","鹶","麖","麠","黥"
                         ],
            jing_3     :["警","景","井","頸","璟","憬","阱","儆","暻",
                         "暻","燛","丼","刭","剄","憼","汫","汬","烴",
                         "穽","肼","蟼","靌","頚","颈"
                         ],
            jing_4     :["竟","靜","境","淨","競","勁","鏡","敬","靖",
                         "逕","徑","靚","瀞","凈","痙","脛","凊","竫",
                         "俓","倞","净","劲","妌","婧","弪","弳","径",
                         "擏","曔","桱","浄","淸","滰","濪","獍","痉",
                         "竞","竧","竸","经","胫","葝","誩","請","迳",
                         "镜","靓","静"],

            jing_6     :[],
            jing_7     :[],


            jing_space :["經","精","晶","驚","鯨","京","菁","睛","莖",
                         "荊","兢","涇","旌","箐","鼱","腈","亰","仱",
                         "坕","婙","婛","巠","惊","旍","更","梷","泾",
                         "猄","粳","経","縅","縆","经","茎","荆","葏",
                         "鲸","鵛","鶁","鶄","鹶","麖","麠","黥"
                         ],
            jing_3     :["警","景","井","頸","璟","憬","阱","儆","暻",
                         "暻","燛","丼","刭","剄","憼","汫","汬","烴",
                         "穽","肼","蟼","靌","頚","颈"
                         ],
            jing_4     :["竟","靜","境","淨","競","勁","鏡","敬","靖",
                         "逕","徑","靚","瀞","凈","痙","脛","凊","竫",
                         "俓","倞","净","劲","妌","婧","弪","弳","径",
                         "擏","曔","桱","浄","淸","滰","濪","獍","痉",
                         "竞","竧","竸","经","胫","葝","誩","請","迳",
                         "镜","靓","静"],

            jing_6     :[],
            jing_7     :[],
            #ㄐㄩㄥ
            jiong_space:["冂","冋","坰","垧","扃","煛","駉","駫"],
            jiong_3:    ["炯","窘","烱","炅","煚","迥","侰","囧",
                         "幜","檾","泂","炛","熲","皛","絅","綗",
                         "蘏","褧","逈","顈"],
            jiong_4:    ["澃"],
            jiong_6:    [],
            jiong_7:    [],
            #ㄐㄧㄡ
            jiu_space  :["糾","鳩","揪","啾","赳","鬮","轇","丩","九",
                         "勼","揂","揫","摎","朻","樛","湫","湬","牞",
                         "稵","糺","纠","芁","萛","蝤","觓","阄","鬏",
                         "鯎","鸠"],
            jiu_3      :["九","酒","久","玖","灸","韭","乆","匛","奺",
                         "糾","紤","舏","赳","韮"],
            
            jiu_4      :["就","舊","救","究","舅","臼","咎","鷲","疚",
                         "柩","廄","倃","僦","匓","匛","匶","厩","廏",
                         "廐","慦","捄","旧","柾","桕","玐","縨","鯦",
                         "鹫","麔","齨"],
            jiu_6      :[],
            jiu_7      :["舅"],
            #ㄐㄩ
            ju_space   :["居","疽","駒","拘","狙","据","琚","車","罝",
                         "裾","苴","趄","鮈","痀","雎","且","俱","倶",
                         "凥","娵","婮","岨","崌","揟","斪","椐","沮",
                         "涺","眗","砠","腒","菹","葅","蛆","蜛","跔",
                         "踙","輋","车","鋦","鋸","锔","锯","镈","驹",                         
                         "鴡","鶋"],
            ju_3       :["舉","櫸","矩","莒","咀","袓","沮","齟","蒟",
                         "踽","竘","举","弆","挙","擧","枸","柜","椇",
                         "榉","榘","筥","簱","蝺","跙","龃"],

            ju_4       :["具","據","劇","句","聚","拒","距","巨","鉅",
                         "俱","遽","鋸","懼","炬","踞","岠","苣","埧",
                         "倨","屨","詎","颶","秬","洰","佢","冣","剧",
                         "勮","埾","壉","姖","寠","屦","忂","怇","怚",
                         "惧","愳","懅","拠","据","昛","檋","歫","沮",
                         "泃","澽","焣","犋","狊","瞿","窭","窶","簴"
                         "粔","絇","耉","耟","虡","蚷","讵","豦","貗",
                         "足","躆","邭","醵","鐻","钜","飓","锯","飔",
                         "駏","鮔"],
            ju_6      :["局","菊","橘","桔","焗","掬","鞠","侷","趜",
                         "跼","鴃","匊","婅","巈","挶","梮","椈","毩",
                         "毱","淗","湨","犑","狊","箤","粷","蘜","諊",
                         "踘","蹫","躹","輂","郹","鄓","鋦","锔","陱",
                         "鞫","駶","驧","鵙","鵴","鶪","鼰","鼳"],
            ju_7      :[],
            #ㄐㄩㄢ
            juan_space  :["捐","娟","涓","鵑","鐫","圈","朘","蠲","勬",
                         "埍","姢","瓹","脧","裐","身","鎸","镌","鞙",
                         "鹃"],
            juan_3      :["捲","卷","埢","奆","臇","菤","锩"],
            juan_4      :["眷","卷","絹","雋","倦","狷","劵","絭","鄄",
                          "圈","勌","巻","帣","悁","慻","桊","淃","獧",
                          "睊","睠","繊","繋","绢","罥","羂","腃","觹",
                          "觽","錈","韏","飬","餋","鬳"],
            juan_6      :[],
            juan_7      :[],

            jue_space   :["噘","撅","刔","嗟"],
            jue_4       :["倔","鴂"],
            jue_6       :["絕","決","覺","爵","掘","蕨","訣","崛","厥",
                          "玨","攫","角","抉","孓","矍","玦","倔","蹶",
                          "譎","獗","嚼","爝","噱","堀","炔","傕","僪",
                          "决","劂","叏","孒","屩","屫","嵑","嶡","彏",
                          "憠","憰","戄","挗","捔","撧","斍","桷","橛",
                          "橜","欔","欮","殌","氒","潏","焆","焳","熦",
                          "爑","爴","玃","珏","璚","疦","瘚","矡","砄",
                          "穱","絶","绝","腳","臄","芵","蕝","蚗","蟨",
                          "蟩","蠼","覐","覚","觉","觖","觼","诀","谲",
                          "谻","貜","赽","趹","蹷","蹻","躩","逫","鈌",
                          "鐍","鐝","钁","镢","駃","鱊","鱖","鴃","鵙",
                          "鷢","龣"],
            jue_7       :[],
            #ㄐㄩㄣ
            
            jun_space   :["噘","撅","刔","嗟"],
            jun_3       :["窘","蜠"],  
            jun_4       :["俊","菌","駿","郡","峻","竣","浚","濬","畯",
                          "寯","晙","焌","儁","呁","埈","懏","捃","捘",
                          "攈","攗","攟","殾","珺","睃","箘","箟","莙",
                          "葰","蔨","蕈","蜠","殾","觽","陖","隽","雋",
                          "餕","骏","鵔","鵘"],
            jun_6       :[],
            jun_7       :[],

            #ㄎㄚ
            ka_space   :["咖","喀","鉲","哈","繧"],
            ka_3       :["卡","佧","咯","咳","胩"],  
            ka_4       :["髂","喀"],
            ka_6       :[],
            ka_7       :[],

            #ㄎㄞ

            kai_space   :["開","揩","侅","奒","痎","锎"],
            kai_3       :["凱","楷","愷","慨","鎧","鍇","剴","塏","闓",
                          "颽","豈","凯","剀","垲","恺","暟","蒈","輆",
                          "铠","锴"],  
            kai_4       :["愾","慨","勓","咳","嘅","壒","愒","欬","炌",
                          "炏","烗","礚","鎎"],
            kai_6       :[],
            kai_7       :[],
            #ㄎㄢ
            kan_space   :["勘","刊","堪","看","龕","戡","嵁","栞","龛"],
            kan_3       :["顑","砍","坎","侃","檻","凵","嵌","偘","埳",
                          "塪","惂","槛","欿","歁","歞","輡","轁","轗",
                          "阚","顑"],  
            kan_4       :["看","阚","瞰","墈","矙","磡","竷","衎","闞",
                          "阚","鬫"],
            kan_6       :[],
            kan_7       :[],
            #ㄎㄤ
            kang_space   :["康","糠","慷","鏮","嫝","嵻","槺","漮","穅",
                           "粇","躿","闶"],
            kang_3       :["忼","慷","骯"],  
            kang_4       :["抗","亢","炕","伉","匟","囥","犺","砊","邟",
                           "鈧","钪","閌","闶"],
            kang_6       :["扛"],
            kang_7       :[],

            kao_space   :["康","糠","慷","鏮","嫝","嵻","槺","漮","穅",
                           "粇","躿","闶"],
            kao_3       :["忼","慷","骯"],  
            kao_4       :["抗","亢","炕","伉","匟","囥","犺","砊","邟",
                           "鈧","钪","閌","闶"],
            kao_6       :["扛"],
            kao_7       :[],
            #ㄎㄠ
            kao_space   :["尻","嵪","髛"],
            kao_3       :["考","烤","拷","栲","丂","攷","洘","燺","薧"],
            kao_4       :["靠","銬","犒","焅","铐","鮳","鯌"],
            kao_6       :[],
            kao_7       :[],
            #ㄎㄜ
            ke_space   :["科","柯","顆","棵","蚵","苛","嵙","珂","刻",
                         "窠","軻","磕","瞌","坷","稞","頦","髁","蝌",
                         "峇","搕","樖","犐","疴","砢","窼","簻","纃",
                         "胢","萪","薖","轲","鈳","钶","颏","颕","颗",
                         "馃","馎"],
            ke_3       :["可","渴","岢","哿","坷","堁","嵑","嶱","敤",
                         "渇","炣","礍","軻","轲","釻","閜"],
            ke_4       :["克","課","客","刻","嗑","喀","剋","恪","溘",
                         "氪","可","勀","勊","厒","垎","娔","尅","愙",
                         "揢","搕","榼","碦","緙","缂","蚵","衉","课",
                         "醘","錁","锞","騍","骒","髁"],
            ke_6       :["殼","咳","欷","壳","殻","颏"],
            ke_7       :[],

            #ㄎㄣ
            ke_space   :["科","柯","顆","棵","蚵","苛","嵙","珂","刻",
                         "窠","軻","磕","瞌","坷","稞","頦","髁","蝌",
                         "峇","搕","樖","犐","疴","砢","窼","簻","纃",
                         "胢","萪","薖","轲","鈳","钶","颏","颕","颗",
                         "馃","馎"],
            ke_3       :["可","渴","岢","哿","坷","堁","嵑","嶱","敤",
                         "渇","炣","礍","軻","轲","釻","閜"],
            ke_4       :["克","課","客","刻","嗑","喀","剋","恪","溘",
                         "氪","可","勀","勊","厒","垎","娔","尅","愙",
                         "揢","搕","榼","碦","緙","缂","蚵","衉","课",
                         "醘","錁","锞","騍","骒","髁"],
            ke_6       :["殼","咳","欷","壳","殻","颏"],
            ke_7       :[],
            
            
            #ㄎㄣ
            ken_space   :[],
            ken_3       :["肯","啃","墾","懇","恳","纐","肎","豤","錹",
                         "齗","齦","龈"],
            ken_4       :["掯","硍","裉","褃","騨"],
            ken_6       :[],
            ken_7       :[],

            keng_space   :["坑","鏗","吭","羥","娙","劥","奟","挳","摼",
                         "殸","牼","硍","硜","硻","誙","踁","銵","鍞",
                         "铿","阬"],
            keng_3       :["挳"],
            keng_4       :[],
            keng_6       :[],
            keng_7       :[],

            #ㄎㄡ
            kou_space   :["摳","彄","抠","眍","眗","芤","袧","鏂"],
            kou_3       :["口","劶"],
            kou_4       :["扣","寇","蔻","叩","釦","佝","伛","冦","宼",
                          "怐","滱","瞉","窛","筘","簆","蔲","鷇"],
            kou_6       :[],
            kou_7       :[],

            #ㄎㄨ
            ku_space    :["哭","枯","窟","堀","骷","挎","刳","圐","桍",
                          "橭","纮","纴","胐","跍","骷","郀","顝","鮬",],
            ku_3       :["苦","楛","纻"],
            ku_4       :["庫","褲","酷","矻","嚳","俈","喾","库","焅",
                         "瘔","秙","絝","纼","绔","绖","绤","袴","裤",
                         "趶","鮬"],
            ku_6       :[],
            ku_7       :[],

            #ㄎㄨㄚ
            kua_space    :["誇","夸","侉","叧","姱","恗","晇","绬","荂"],
            kua_3       :["垮","侉","咵","绹","銙"],
            kua_4       :["跨","胯","骻","缊","缐","缞"],
            kua_6       :[],
            kua_7       :[],

            #ㄎㄨㄞ
            kuai_space    :["叧","咼","喎"],
            kuai_3       :["擓","蒯"],
            kuai_4       :["快","塊","筷","酷","嚳","俈","劊","澮","獪",
                           "会","侩","儈","凷","哙","噲","块","巜","廥",
                           "旝","欳","浍","狯","脍","蹾","郐","鄶","駃",
                           "鬠","鱠"],
            kuai_6       :[],
            kuai_7       :[],

            #ㄎㄨㄢ
            kuan_space    :["寬","髖","臗","宽","寛","髋"],
            kuan_3       :["款","梡","欵","歀","窽","窾"],
            kuan_4       :[],
            kuan_6       :[],
            kuan_7       :[],

            #ㄎㄨㄤ

            kuang_space    :["框","眶","匡","誆","筐","劻","匩","恇","洭",
                             "硄","诓","軖","軭","邼"],
            kuang_3       :["俇","儣","懬","懭"],
            kuang_4       :["況","礦","鄺","曠","爌","壙","仼","兤","况",
                            "圹","彉","懭","旷","框","眖","眶","矌","矿",
                            "絖","纊","纩","罉","貺","贶","軦","邝","鋛",
                            "鑛","黋"],
            kuang_6       :["狂","鵟","誑","抂","诳"],
            kuang_7       :[],
            #ㄎㄨㄟ
            kui_space    :["框","眶","匡","誆","筐","劻","匩","恇","洭",
                             "硄","诓","軖","軭","邼"],
            kui_3       :["俇","儣","懬","懭"],
            kui_4       :["況","礦","鄺","曠","爌","壙","仼","兤","况",
                            "圹","彉","懭","旷","框","眖","眶","矌","矿",
                            "絖","纊","纩","罉","貺","贶","軦","邝","鋛",
                            "鑛","黋"],
            kui_6       :["狂","鵟","誑","抂","诳"],
            kui_7       :[],
            #ㄎㄨㄣ

            kun_space    :["坤","堃","昆","崑","焜","鯤","琨","錕","崐",
                           "褌","惃","混","晜","瑻","猑","罤","菎","蜫",
                           "醌","铦","锟","騉","髠","髡","髨","鲬","鲲",
                           "鵾","鶤"],
            kun_3       :["捆","綑","壼","梱","悃","硱","祵","稇","稛",
                          "裍","閫","閸","阃","齫"
                          ],
            kun_4       :["困","睏","涃"],
            kun_6       :[],
            kun_7       :[],

            #ㄎㄨㄛ
            kuo_space    :[],
            kuo_3       :["擃"],
            kuo_4       :["擴","括","廓","闊","蛞","姡","彉","彍","扩",
                          "拡","挄","漷","濶","籗","阔","霩","鞟","鞹",
                          "韕","髺","鬠"],
            
            kuo_6       :[],
            kuo_7       :[],
            #ㄌㄚ
            la_space   :["拉","啦","菈","喇","邋","搚","柆","磖","翋",
                         "鞡"],
            la_3       :["喇","藞"],
            la_4       :["辣","蠟","臘","剌","鱲","瘌","蜡","揧","擸",
                         "楋","爉","瓎","腊","落","蝲","蝲","鑞","鬎",
                         "鯻"],
            
            la_6       :["旯","剌","揦","邋"],
            la_7       :["啦","蓝"],


            #ㄌㄞ
            la_space   :["拉","啦","菈","喇","邋","搚","柆","磖","翋",
                         "鞡"],
            la_3       :["喇","藞"],
            la_4       :["辣","蠟","臘","剌","鱲","瘌","蜡","揧","擸",
                         "楋","爉","瓎","腊","落","蝲","蝲","鑞","鬎",
                         "鯻"],
            
            la_6       :["旯","剌","揦","邋"],
            la_7       :["啦","蓝"],

            #ㄌㄞ
            lai_space   :[],
            lai_3       :[],
            lai_4       :["賴","瀨","癩","睞","籟","娕","勑","徠","攋",
                         "櫴","濑","瀬","癞","睐","籁","藾","襰","鑞",
                         "赉","赖","頼","鵣"],
            
            lai_6       :["來","萊","錸","徠"],
            lai_7       :["啦","蓝"],
            #ㄌㄢ
            lan_space   :["啉"],
            lan_3       :["覽","懶","攬","纜","攬","滥","醂","壈","嬾","孄",
                          "孏","懒","揽","擥","榄","浨","漤","灠","爦","缆",
                          "覧","览","顲"],
               
            lan_4       :["濫","爛","壏","滥","烂","燗","爁","爤","瓓",
                         "糷","纜","鑭"],
            
            lan_6       :["藍","蘭","攔","欄","籃","嵐","瀾","闌","欗",
                          "躝","婪","斕","襤","鑭","儖","兰","厱","囒",
                          "岚","惏","懢","拦","斓","栏","澜","灆","灡",
                          "燣","璼","篮","籣","糷","繿","葻","蓝","蘫",
                          "褴","襴","襽","譋","讕","谰","镧","阑","韊"],
            lan_7       :[],
            #ㄌㄤ 
            lang_space  :["啷"],
            lang_3       :["朗","塱","烺","閬","峎","悢","朖","朤","硠","誏"],
               
            lang_4       :["浪","埌","蒗","阆"],
            
            lang_6       :["郎","廊","狼","瑯","榔","琅","瀾","闌","欗",
                          "躝","婪","斕","襤","鑭","儖","兰","厱","囒",
                          "岚","惏","懢","拦","斓","栏","澜","灆","灡",
                          "燣","璼","篮","籣","糷","繿","葻","蓝","蘫",
                          "褴","襴","襽","譋","讕","谰","镧","阑","韊"],
            lang_7       :[],
            #ㄌㄠ
            lao_space    :["撈","捞"],
            lao_3        :["老","荖","佬","咾","姥","栳","銠","恅","橑",
                           "潦","狫","轑","铑"],
            lao_4        :["烙","落","澇","勞","嫪","僗","劳","労","憦",
                           "橯","涝","潦","絡","络","耢","耮","軂","酪"],
            lao_6        :["勞","牢","癆","嘮","醪","嶗","僗","劳","労",
                           "哰","崂","憥","撈","浶","澇","痨","磱","窂",
                           "簩","蟧","鐒","铹","顟","髝"],
            lao_7        :[],
            
            #ㄌㄜ
            le_space    :["嘞"],
            le_3        :[],
            le_4        :["樂","勒","垃","肋","叻","埒","捋","竻","乐",
                           "仂","协","哷","埓","忇","扐","楽","氻","泐",
                          "玏","皬","砳","簕","艻","阞","韷","頱","鰳",
                          "鳓"],
            le_6        :[],
            le_7        :["了","咯"],
            #ㄌㄟ
            lei_space    :["勒","哩"],
            lei_3        :["壘","蕾","磊","累","儡","絫","樏","誄","儽",
                           "厽","垒","櫐","櫑","洡","漯","灅","瘣","癗",
                           "磥","礌","礧","礨","纍","耒","腂","蕌","藟",
                           "蘲","蘽","虆","蠝","讄","诔","鑸","頛","鸓"],
            lei_4        :["類","累","淚","纇","傫","儽","擂","攂","泪",
                           "涙","礌","禷","类","蘱","酹","銇","錑","頪"],
            lei_6        :["雷","擂","鐳","纍","縲","羸","嫘","畾","檑",
                           "累","虆","壨","攂","櫑","欙","瓃","礧","纝",
                           "缧","罍","羪","罍","蠝","轠","錑","镭","靁",
                           "鼺"],
               
            lei_7        :["了","咯"],
            #ㄌㄥ
            leng_space    :[],
            leng_3        :["冷"],
            leng_4        :["愣","楞","倰","睖","踜"],
            leng_6        :["稜","崚","棱","蔆","薐","楞","倰","塄","掕"],
               
            leng_7        :[],

            #ㄌㄧ
            li_space      :["哩"],
            li_3          :["李","裡","里","理","禮","裏","浬","鯉","哩",
                            "豊","澧","鱧","俚","鋰","醴","邐","娌","劙",
                            "喱","峛","峲","欚","盠","礼","粴","蠡","赪",
                            "逦","锂","鯵","鲤","鳢"],
            
            li_4          :["立","利","力","例","莉","粒","麗","歷","勵",
                            "俐","栗","厲","壢","蒞","儷","曆","瀝","笠",
                            "荔","琍","隸","吏","猁","痢","礫","櫟","礪",
                            "苙","犡","犡","嚦","癘","蠣","慄","岦","戾",
                            "櫪","秝","溧","酈","瓅","唳","悧","欐","娳",
                            "靋","瑮","沴","濿","皪","糲","綟","藶","丽",
                            "俪","傈","儮","凓","励","历","厉","厤","厯",
                            "叻","呖","唎","坜","塛","婯","屴","巁","悷",
                            "搮","攊","攦","攭","斄","暦","曞","朸","枥",
                            "栎","栛","栵","棙","椞","櫔","歴","沥","沵",
                            "癧","浰","爄","爏","珕","瓑","瓥","疠","疬",
                            "沵","盭","粝","纅","翙","翚","苈","茘","莅",
                            "蒚","蚸","蛎","蛠","蜧","蝷","蠇","蠫","觻",
                            "詈","讈","赲","跞","躒","轢","轣","轹","郦",
                            "釙","鉝","銐","隷","雳","雴","鬁","鬲","鬴",
                            "鱱","鱳","鳨","鴗","鷅","鷑","麜"],
            
            li_6          :["離","梨","黎","罹","厘","釐","鱺","籬",
                            "璃","貍","狸","孋","漓","驪","藜","犛",
                            "褵","瓈","蜊","蠡","鸝","犂","鑗","黧",
                            "蘺","灕","縭","蔾","麗","离","粍","喱",
                            "攡","刕","剓","剺","劙","卨","哩","嚟",
                            "囇","嫠","孷","廲","悡","梩","梸","棃",
                            "樆","氂","漦","猍","孷","睝","穲","篱",
                            "缡","艃","荲","菞","蓠","蟍","蟸","蠫",
                            "謧","邌","酦","醨","釃","鋫","錅","鏫",
                            "蟸","謧","邌","酦","醨","釃","鋫","錅",
                            "鏫","騹","骊","鯬","鲃","鲡","鵹","鹂",
                            "麶","黐"],
               
            
            li_7          :[],

            lia_space     :[],
            lia_3         :["倆","俩"],
            lia_4         :[],
            lia_6         :[],
            lia_7         :[],

            lian_space     :[],
            lian_3         :["臉","僆","摙","敛","琏","稴","羷","脸","哩",
                            "蔹","裣","鄻","醶","铇"],
               
            lian_4         :["練","戀","鍊","鏈","煉","斂","歛","楝","殮",
                            "瀲","薟","襝","僆","堜","媡","恋","殓","湅",
                            "潋","澰","炼","瑓","稴","纞","练","萰","蘝",
                            "蘞","錬","链","陦","鰊"],
               
            lian_6         :["連","聯","蓮","廉","濂","憐","璉","簾","鰱",
                            "漣","鐮","鎌","帘","联","槤","奩","蠊","褳",
                            "嗹","奱","亷","劆","匲","匳","奁","嫾","嬚",
                            "慩","攣","櫣","涟","溓","濓","燫","磏","籢",
                            "縺","翴","聨","聫","聮","臁","莲","薕","螊",
                            "裢","覝","謰","譧","蹥","连","镰","鬑","鲄",
                            "鲢"],
            lian_7         :[],


            liang_space     :["",],
            liang_3         :["兩","倆","両","两","俩","啢","掚","緉","脼",
                            "蜽","裲","魉","魎"],
               
            liang_4         :["輛","量","亮","諒","晾","喨","踉","倞","啢",
                            "悢","涼","湸","谅","辆","靓"],
               
            liang_6         :["量","良","梁","樑","糧","涼","粱","椋","俍",
                            "凉","墚","粮","綡","莨","踉","輬","駺"],
            liang_7         :[],

            liao_space      :["撩"],
            liao_3      :["了","瞭","暸","釕","憭","爒","蓼","蟟","鄝",
                          "钌","镽"],
            liao_4      :["廖","料","撂","瞭","炓","尥","熮","燎","窲",
                          "蟉","釕","鐐","钌","镣"],
            
            liao_6      :["療","寮","聊","僚","遼","撩","燎","潦","寥",
                          "繚","鐐","嘹","獠","僚","鷚","嫽","翏","尞",
                          "屪","嵺","嶚","嶛","廫","憀","憭","摎","敹",
                          "漻","疗","窌","窷","竂","簝","缭","膋","蟟",
                          "豂","賿","蹘","辽","醸","镽","顟","飂","飉",
                          "髎","鷯","鹩"],
            liao_7      :[],
            #ㄌㄧㄝ
            lie_space      :["咧","巤"],
            lie_3      :["咧"],
            lie_4      :["列","烈","裂","獵","劣","冽","鬣","洌","捩",
                          "躐","儠","姴","挒","擸","棙","浖","烮","煭",
                         "爉","犣","睙","聗","脟","茢","蛚","蛶","趔",
                         "迾","颲","鬛","鮤","鯐","鴷"],
            
            lie_6      :[],
            lie_7      :["咧"],

            #ㄌㄧㄣ
            lin_space  :["崊"],
              lin_3      :["凜","懍","澟","廩","亃","凛","廪","懔","撛",
                           "檁","檩","癛","禀","綝","菻"],
               
            lin_4      :["吝","藺","賃","躪","恡","悋","橉","焛","甐",
                          "蔺","赁","蹸","躏","躙","轥","閵","麐"],
            
            lin_6      :["林","臨","霖","琳","麟","鄰","淋","遴","磷",
                         "鱗","璘","燐","嶙","潾","僯","綝","淋","粼",
                         "轔","鏻","痳","驎","箖","罧","厸","壣","临","惏",
                         "斴","晽","暽","杮","枾","瀶","獜","甐","疄",
                         "瞵","矝","碄","粦","繗","翷","蹸","辚","邻",
                         "隣","颪","魿","鮲","鳞"],
               
            lin_7      :[],

            ling_space :["拎"],
            ling_3  :["領","嶺","彾","领"],
            ling_4  :["另","令","炩","狑"],
            ling_6  :["齡","玲","靈","齡","鈴","凌","陵","伶","苓",
                         "菱","翎","笭","羚","聆","綾","淩","泠","姈",
                         "蛉","呤","櫺","樑","岭","柃","皊","舲","澪",
                         "鯪","瓴","駖","囹","刢","呬","坽","堎","夌",
                         "婈","孁","岺","彾","怜","掕","昤","朎","棂",
                         "欞","灵","燯","爧","狑","獜","琌","睖","砱",
                         "碐","欞","秢","竛","詅","紷","聢","蔆","蕶",
                         "蘦","衑","袊","裬","跉","軨","輘","酃","醽",
                         "酃","錂","铃","閝","阾","霊","霗","霛","霝",
                         "魿","鲙","鲮","鹷","麢","龄","龗"],
             ling_7    :[],

            liu_space  :["溜","澑","鬸"],
            liu_3      :["柳","綹","栁","桺","橮","珋","绺","罶","羀",
                         "鉚","锍","飹"],
            liu_4      :["六","溜","遛","蹓","餾","廇","坴","塯","畂",
                         "翏","镏","陆","陸","雡","霤","馏","鷚","鹨"],
            liu_6      :["劉","流","留","瘤","琉","硫","瑠","鎏","榴",
                         "瀏","鰡","騮","鎦","鶹","鏐","旒","翏","刘",
                         "嚠","媹","嬼","嵧","巰","懰","旈","橊","浏",
                         "瑬","璢","畄","畱","疁","癅","磂","綂","蒥",
                         "蓅","藰","蟉","裗","遛","疁","磂","飀","綂",
                         "駠","駵","驑","骝","鱪","鷎","麍"],
            liu_7      :[],

            lou_space  :["搂","摟","瞜"],
            lou_3      :["摟","簍","塿","嵝","嶁","搂","甊","篓"],
            lou_4      :["露","漏","陋","鏤","瘺","屚","瘘","瘻","镂"],
            lou_6      :["樓","嘍","婁","廔","僂","蔞","髏","耬","螻",
                         "偻","剅","喽","娄","慺","摟","楼","漊","熡",
                         "瞜","窶","耧","艛","蒌","蝼","謱","軁","遱",
                         "鞻","髅","鷜"],
            lou_7      :["喽"],

            #ㄌㄨ
            lu_space  :["嚕","噜","撸"],
            lu_3      :["魯","擄","滷","鹵","虜","櫓","塷","掳","擼",
                        "樐","橹","氌","瀂","磠","艣","艪","蓾","虏",
                        "鏀","鐪","镥","鲁"],
            lu_4      :["路","陸","錄","鹿","露","祿","鷺","麓","璐",
                        "轆","碌","戮","逯","菉","賂","輅","潞","蕗",
                        "稑","蓼","漉","籙","廘","鏕","淥","騄","侓",
                        "僇","六","剹","勎","勠","圥","坴","垏","塶",
                        "娽","峍","彔","录","摝","椂","樚","氯","淕",
                        "渌","熝","琭","甪","盝","睩","硉","磟","禄",
                        "膔","蔍","虂","螰","角","觮","觻","赂","趢",
                        "踛","蹗","辂","辘","醁","録","錴","鏴","陆",
                        "騼","鯥","鴼","鵦","鵱","鹭"],
            lu_6      :["盧","爐","蘆","顱","鸕","鱸","廬","臚","鑪",
                         "瀘","壚","轤","嚧","顱","垆","庐","攎","臚",
                         "櫨","泸","炉","獹","玈","瓐","皶","矑","籚",
                         "纑","瀘","胪","舻","艫","芦","蠦","轳","険",
                        "颅","髗","魲","鲈","鸬","黸"],
            lu_7      :["氇","轳","険"],
            #ㄌㄩ
            lyu_space :[],
            lyu_3 :["呂","旅","屢","鋁","履","侶","縷","梠","褸",
                    "膂","儢","婁","屡","挔","捋","捛","漊","祣",
                    "稆","穭","絽","缕","膐","褛","郘","铝","饹"],
            lyu_4 :["綠","率","律","慮","濾","氯","嵂","葎","儢",
                    "勴","卛","壘","寽","櫖","滤","爈","箻","繂",
                    "绿","膟","菉","藘","虑","鑢"],
            lyu_6 :["驢","閭","櫚","慺","曥","榈","氀","膢","藘",
                    "闾","馿","驴"],
            lyu_7 :[],
            #ㄌㄩㄝ
            lyue_space :[],
            lyue_3 :[],
            lyue_4 :["略","掠","剠","撂","擽","畧","鋝","鋢","锊"],
               
            lyue_6 :[],
            lyue_7 :[],
            #ㄌㄨㄢ
            luan_space :[],
            luan_3 :["卵"],
            luan_4 :["亂","乱","薍","覼","釠"],
               
            luan_6 :["鑾","鸞","巒","攣","欒","孿","孌","灤","臠",
                     "圝","圞","癵","娈","峦","曫","栾","孌","臠",
                     "羉","脔","脟","虊","銮","鸾"],
            luan_7 :[],
               
            lun_space:["抡","掄"],
            lun_3   :["埨","稐"],
            lun_4   :["論","溣","论"],
            lun_6   :["倫","輪","淪","崙","綸","侖","掄","錀","碖",
                      "論","圇","仑","伦","囵","婨","崘","惀","錀",
                      "棆","沦","纶","耣","腀","菕","蜦","论","踚",
                      "轮","陯","鯩"],
            lun_7   :[],


            luo_space:["抡","掄"],
            luo_3   :["埨","稐"],
            luo_4   :["論","溣","论"],
            luo_6   :["倫","輪","淪","崙","綸","侖","掄","錀","碖",
                      "論","圇","仑","伦","囵","婨","崘","惀","錀",
                      "棆","沦","纶","耣","腀","菕","蜦","论","踚",
                      "轮","陯","鯩"],
            ma_7   :[],

            ma_space:["發","伐","佱","傠","发","罰","橃","瞂"],
            ma_3   :["馬","瑪","碼","嘜","螞","溤","嗎","鎷",
                     "吗","犸","玛","码","蚂","马","鰢","鷌"],
            
            ma_4   :["罵","傌","禡","嘜","杩","榪","獁","睰","蚂",
                     "螞","閁","駡","骂"],
            ma_6   :["麻","嘛","痲","蔴","蟆","吗","尛","犘","麼",
                      "麽"],
            ma_7   :["嗎","嘛","媽","蟆","吗","嬤","蟇"],

            mai_space:[],
            mai_3   :["買","嘪","买","荬","蕒","鷶"],
            
            mai_4   :["鷶","買","买","荬","蕒","鷶"],
            mai_6   :["埋","霾","薶"],
            mai_7   :[],

            man_space :["屘","颟"],
            man_3    :["滿","屘","悗","満","满","矕","螨","鏋"],
            man_4    :["慢","曼","漫","蔓","嫚","幔","縵","謾","僈",
                       "鏝","墁","摱","澫","澷","熳","獌","缦","蔄",
                       "谩","鄤","镘"],
            man_6    :["蠻","鰻","瞞","饅","蹣","璊","顢","埋","姏",
                       "悗","慲","槾","樠","漫","瞒","脵","脷","蔓",
                       "蛮","謾","谩","鞔","馒","鬗","鬘","鳗"],
            
            man_7    :[],
               
            mang_space:[],
            mang_3    :["蟒","莽","壾","庬","汒","漭","茻","硥","莾","蠎"],
            mang_4    :["吂"],
            mang_6    :["忙","盲","芒","茫","氓","邙","厖","吂","哤",
                       "奀","娏","尨","庬","恾","杗","汒","浝","牻",
                       "狵","痝","盳","硭","笀","蘉","蛖","釯","鋩",
                       "駹","鼆"],
            
            mang_7    :[],

            mao_space:["貓","猫"],
            mao_3    :["卯","茆","昴","鉚","戼","泖","铆"],
            mao_4    :["茂","冒","帽","貿","貌","懋","袤","楙","冃",
                       "冐","媢","旄","暓","柕","毣","毷","瑁","皃",
                       "眊","瞀","瞐","耄","艒","芼","萺","蓩","贸",
                       "鄮","镋","颒"],
            mao_6    :["毛","茅","錨","矛","髦","芼","旄","鶜","堥",
                       "媌","嫹","枆","氂","渵","牦","緢","罞","腖",
                       "腗","茆","蝥","蟊","覒","軞","酕","锚","髳"],
            
            mao_7    :[],

            me_space :[],
            me_3     :[],
            me_4     :[],
            me_6     :[],
            me_7     :["麼","嚜"],

            mei_space :[],
            mei_3     :["每","美","鎂","媺","渼","媄","浼","凂","嬍",
                        "嵄","挴","毎","燘","鋂","镁","黣"],
            mei_4     :["妹","媚","昧","沬","魅","寐","袂","眛","瑁",
                        "抺","煝","痗","眫","睸","祙","脄","蝐","蝞",
                        "谜","跊","韎","鬽"],
            mei_6     :["沒","梅","枚","眉","媒","玫","煤","湄","莓",
                        "黴","楣","霉","酶","苺","脢","呅","郿","嵋",
                        "瑂","坆","堳","塺","徾","攗","某","楳","槑",
                        "没","湈","猸","珻","睂","矀","禖","腜","葿",
                        "鋂","镅","鶥","鹛"],

            mei_7     :["妹"],

            men_space :[],
           
            men_3     :["暪"],
            men_4     :["燜","悶","懣","懑","焖","闷"],
            men_6     :["們","門","捫","亹","扪","樠","璊","穈","菛",
                        "虋","鍆","钔","閅","门"],

            men_7     :["們","们"],

            meng_space :["矇"],
           
            meng_3     :["猛","錳","艋","蜢","勐","懞","懵","瓾","艨",
                        "蠓","锰","鯭","黽","鼆"],
               
            meng_4     :["夢","孟","夣","盟","梦","瞢","霥","霿","鯍"],
            meng_6     :["盟","蒙","萌","濛","檬","朦","懵","蠓","懞",
                        "曚","矇","虻","幪","甍","瞢","儚","冡","尨",
                        "懜","橗","氋","氓","溕","獴","甿","矒","礞",
                        "罞","艨","莔","蕄","蝱","鄳","鄸","雺","霿",
                        "駹","鼆"],

            meng_7     :[],

            men_7     :["們","们"],
            #ㄇㄧ
            mi_space :["咪","瞇","眯"],
           
            mi_3     :["米","靡","弭","濔","渳","侎","孊","敉","洣",
                        "灖","猕","眯","羋","脒","芈","葞","蔝","蝆",
                       "銤"],
               
            mi_4     :["密","蜜","秘","覓","宓","祕","泌","汨","謐",
                       "糸","冪","嘧","冖","塓","宻","峚","幂","幎",
                       "幦","日","髻","樒","櫁","淧","淿","滵","漞",
                       "濗","簚","羃","膤","膥","蔤","藌","蠠","覔",
                       "觅","谧","鼏"],
            mi_6     :["迷","謎","彌","瀰","糜","獼","醚","禰","靡",
                        "蘼","麋","冞","弥","戂","擟","攠","檷","爢",
                        "狝","猕","瓕","籋","縻","罙","蒾","蘪","詸",
                        "谜","醾","醿","釄","镾","鸍","麊","麛"],

            mi_7     :[],
            #ㄇㄧㄢ
            mian_space :[],
           
            mian_3     :["免","勉","緬","靦","冕","鮸","湎","娩","俛",
                        "眄","丏","偭","厸","喕","愐","鮸","汅","沔",
                         "渑","絻","缅","絻","腼","莬","鱚"],
               
            mian_4     :["面","麵","湣","勔","泯","眠","瞑","糆","汨",
                       "麪","麫"],
            mian_6     :["眠","棉","綿","緜","婂","媔","嬵","宀","檰",
                        "櫋","瞑","矊","矏","绵","臱","芇","蝒"],

            mian_7     :[],

            #ㄇㄧㄠ
            miao_space :["喵"],
           
            miao_3     :["秒","淼","渺","邈","藐","緲","杳","眇","仦",
                        "仯","劰","杪","篎","缈","膶","訬"],
               
            miao_4     :["廟","妙","玅","庙","庿","眇","繆","缪"],
            miao_6     :["苗","瞄","描","鶓","鱙","鹋"],

            miao_7     :[],

            miao_space :["咩","乜","哶","羋"],
           
            miao_3     :["吀"],
               
            miao_4     :["滅","衊","蔑","篾","幭","懱","搣","櫗","瀎",
                         "灭","烕","眜","礣","薎","蠛","覕","鑖","鱴",
                         "鴓"],
            miao_6     :[],

            miao_7     :[],
            #ㄇㄧㄣ
            min_space  :[],
            min_3  :["敏","閔","閩","抿","泯","憫","皿","愍","澠",
                     "黽","僶","冺","刡","勄","悯","惽","慜","捪",
                     "敃","敯","暋","湣","潣","笢","簢","闵","闽",
                     "鰵","鱚","鳘","黾"],
            min_4  :[],
            min_6  :["民","旻","岷","珉","旼","忞","暋","冺","姄",
                     "崏","忟","怋","玟","琘","瑉","痻","盿","砇",
                     "碈","緍","緡","缗","罠","苠","鈱","錉","鍲",
                     "閩","閺"],
            min_7  :[],
            #ㄇㄧㄥ
            ming_space  :[],
            ming_3  :["凕","姳","慏","眳","茗","酩"],
            ming_4  :["命","暝"],
            ming_6  :["名","明","銘","鳴","茗","冥","酩","暝","螟",
                     "洺","瞑","溟","佲","嫇","嶹","朙","榠","熐",
                     "猽","眀","眳","蓂","覭","詺","鄍","铭","颙",
                     "鸣"],
            ming_7  :[],

            #ㄇㄧㄥ
            miu_space:["唒"],
            ming_3  :[],
            ming_4  :["謬","繆","缪","谬"],
            ming_6  :[],
            ming_7  :[],
               
            #ㄇㄛ
            mo_space:["摸","帞","絈","臓"],
            mo_3  :["抹","懡"],
            mo_4  :["莫","末","默","墨","沫","魩","漠","沒","茉",
                    "瘼","陌","歿","寞","妺","貘","脈","秣","驀",
                    "磨","鏌","眽","纆","鄚","万","冒","嗼","嘜",
                    "嚜","圽","塻","嫼","帓","怽","慔","抹","昩",
                    "暯","枺","榒","歾","殁","没","洦","湐","爅",
                    "皌","瞙","粖","縸","耱","膜","莈","蓦","藦",
                    "爅","蛨","蟔","衇","袜","袹","覛","貃","貊",
                    "銆","镆","霡","霢","靺","饃","饳","鬕","黙"],
            
            mo_6  :["摩","模","魔","磨","膜","謨","饃","摹","蘑",
                    "糢","劘","嚩","嫫","擵","無","臓","臜","藦",
                    "謩","譕","谟","鉱","饝","馍","髍","麼"],
               
            mo_7  :["麼","尛","麽"],
            

            #ㄇㄡ
            mou_space:[],
            mou_3  :["某","冇","踇"],
            mou_4  :["愗"],
            
            mou_6  :["謀","牟","繆","眸","哞","鉾","蛑","侔","呣",
                    "劺","洠","缪","蝥","谋","赗","鍪","鞪","鴾",
                    "麰"],
               
            mou_7  :[],

            #ㄇㄨ
            mou_space:[],
            mou_3  :["母","姆","畝","牡","拇","亩","姥","娒","峔",
                     "牳","畆","畞","畮","砪","胟","鉧"],
            mou_4  :["木","目","墓","幕","慕","牧","穆","募","睦",
                     "沐","暮","苜","鉬","霂","仫","坶","幙","募",
                     "楘","樢","毣","炑","牟","狇","縸","莯","蚞",
                     "钼","雮","鞪","鶩"],
            
            
            mou_6  :["模","橅","氁","獏"],
               
            mou_7  :[],
            #ㄋㄚ
            na_space:["哪"],
            na_3  :["哪","那"],
            na_4  :["那","納","娜","嘜","杩","榪","獁","募","魶",
                     "妠","呐","哪","笝","纳","肭","吶","豽","貀",
                     "軜","钠"],
            
            
            na_6  :["拿","拏","挐","誽","镎"],
               
            na_7  :["哪"],
            #ㄋㄞ
            nai_space:[],
            nai_3  :["乃","奶","迺","氖","艿","奈","妳","嬭","尕",
                     "廼","氝","疓","舗","釢"],
            nai_4  :["奈","耐","鼐","柰","倷","渿","耏","萘","螚",
                     "褦","賎","辌","錼"],
            
            
            nai_6  :["孻","摨"],
               
            nai_7  :["奶"],
            #ㄋㄢ
            nan_space:["囝","囡"],
            nan_3  :["湳","腩","赧","戁","揇","罱","蝻"],
            nan_4  :["難","婻"],
            
            
            nan_6  :["南","難","男","楠","喃","萳","柟","蝻","囡",
                     "奻","娚","暔","枏","畘","莮","諵"],
               
            nan_7  :[],
            #ㄋㄤ
            nang_space:["囔","釒"],
            nang_3  :["曩","攮","灢","馕"],
            nang_4  :["儾","齉"],
            
            
            nang_6  :["囊","乪","欜","馕"],
               
            nang_7  :[],
            
            
            #ㄋㄠ
            nao_space:["孬","峱"],
            nao_3  :["腦","惱","瑙","匘","垴","嫐","恼","悩","碯",
                     "脑","镮"],
               
            nao_4  :["鬧","淖","舮","閙","闹"],
            
            
            nao_6  :["撓","橈","鐃","呶","猱","夒","峱","嶩","巎",
                     "巙","怓","憹","挠","獶","獿","硇","繷","蛲",
                     "譊","铙","髐"],
               
            nao_7  :[],

            #ㄋㄜ
            ne_space:["呢"],
            ne_3  :[],
               
            ne_4  :["抐","眲","訥","讷"],
            
            
            ne_6  :[],
               
            ne_7  :["呢"],
            
            #ㄋㄟ
            nei_space:[],
            nei_3  :["餒","哪","涹","脮","腇","餧","馁","鮾","鯘"],
               
            nei_4  :["內","内","那"],
            
            
            nei_6  :[],
               
            nei_7  :[],

            #ㄋㄣ
            nen_space:["黁"],
            nen_3  :[],
               
            nen_4  :["嫩","嫰","抐"],
            
            
            nen_6  :[],
               
            nen_7  :[],

            #ㄋㄥ
            neng_space:[],
            neng_3  :[],
               
            neng_4  :["挊","濘"],
            
            
            neng_6  :["能","薴","儜"],
               
            neng_7  :[],
            #ㄋㄧ
            ni_space:[],
            ni_3  :["你","你","擬","隬","旎","昵","伱","伲","儗",
                      "坭","孴","抳","拟","掜","柅","檷","狔","祢",
                      "禰","苨","薿","譺","鉨","馜"],
            
               
            ni_4  :["逆","膩","溺","匿","暱","睨","泥","堄","嫟",
                      "嬺","孨","屰","嶷","惄","愵","搻","昵","氼",
                      "痆","縌","胒","腻","艍","衵","迡","鷁","鷊"],
                 
            
            ni_6  :["尼","妮","泥","倪","霓","呢","怩","婗","兒",
                      "坭","埿","堄","屔","棿","淣","狋","狔","猊",
                      "秜","臡","虉","蚭","蜺","觬","貎","跜","輗",
                      "郳","鈮","铌","鯓","鯢","鲵","鲾","鶂","鶃",
                      "麑","齯"],
            
               
            ni_7  :[],
            #ㄋㄧㄢ
            nian_space:["蔫"],
            nian_3  :["輾","捻","碾","拈","輦","攆","撚","撵","涊",
                      "簐","艔","跈","蹨","躎","辇","鯰"],
            
               
            nian_4  :["念","唸","廿","埝","淰","艌","酿","鼰","齞"],
                 
            
            nian_6  :["年","黏","粘","哖","拈","鯰","姩","秊","秥",
                      "鮎","鲇","鲶","鲿"],
            
               
            nian_7  :[],
            #ㄋㄧㄤ
            niang_space:[],
            niang_3  :[],             
            niang_4  :["釀","酿"],           
            niang_6  :["娘","孃","嬢","酿"],
            
               
            niang_7  :["娘"],

            #ㄋㄧㄠ
            niao_space:[],
            niao_3  :["鳥","蔦","嬝","裊","嬲","嫋","褭","茑","茮",
                      "袅","鸟"],             
            niao_4  :["尿","脲","艍"],           
            niao_6  :[],
            
               
            niao_7  :[],
            #ㄋㄧㄝ
            nie_space:["捏","惗","揑","踗","鈢","錜","鑈"],
            nie_3  :[],             
            nie_4  :["聶","鎳","涅","顳","摰","孽","嚙","齧","鑷",
                      "囓","躡","囁","臬","隉","乜","啮","嗫","囐",
                      "圼","孼","嵲","巕","嶭","帇","攝","敜","枿",
                      "槷","櫱","疌","痆","篞","糱","糵","聂","臲",
                      "艝","艠","菍","蘗","蠥","踂","踙","蹑","鉨",
                      "鉩","钀","镊","镍","闑","陧","颞"],
            
            nie_6  :["苶"],
            
               
            nie_7  :[],

            #ㄋㄧㄣ
            nin_space:[],
            nin_3  :[],             
            nin_4  :["酿","釀"],
            
            nin_6  :["您","囜"],
            
               
            nin_7  :[],

            #ㄋㄧㄣ
            ning_space:[],
            ning_3  :["擰","拧","橣","矃"],             
            ning_4  :["佞","濘","寧","拧","擰","甯"],
            
            ning_6  :["寧","凝","甯","檸","嚀","寍","獰","咛","嬣",
                      "寕","寗","寜","拧","擰","狞","聍","聹","苎",
                      "薴","鑏","鬡","鸋"],
            
            
               
            ning_7  :[],
            #ㄋㄧㄡ
            niu_space:["妞"],
            niu_3  :["紐","扭","鈕","鈕","忸","沑","狃","纽",
                     "莥","钮","靵"],             
            niu_4  :["拗","衂"],
            
            niu_6  :["牛","汼"],
            
            
               
            niu_7  :[],

            #ㄋㄨㄥ
            nong_space:[],
            nong_3  :["繷"],             
            nong_4  :["弄","挊"],
            
            nong_6  :["農","濃","膿","儂","噥","穠","醲","侬","农",
                      "哝","憹","檂","欁","浓","癑","禯","脓","蕽",
                      "襛","赒","辳","鬞","齈"],        
               
            nong_7  :[],
  
            #ㄋㄨㄥ
            nong_space:[],
            nong_3  :["繷"],             
            nong_4  :["弄","挊"],
            
            nong_6  :["農","濃","膿","儂","噥","穠","醲","侬","农",
                      "哝","憹","檂","欁","浓","癑","禯","脓","蕽",
                      "襛","赒","辳","鬞","齈"],        
               
            nong_7  :[],
            #ㄋㄡ
            nou_space:[],
            nou_3  :["啂"],             
            nou_4  :["嗕","挊","槈","檽","耨","譨","鎒","鐞"],
            
            nou_6  :["譨","羺","獳"],        
               
            nou_7  :[],


            #ㄋㄨ
            nu_space:[],
            nu_3  :["努","弩","伮","砮","胬"],             
            nu_4  :["怒","搙","詉"],
            
            nu_6  :["奴","孥","駑","笯","蒘","驽"],        
               
            nu_7  :[],
            #ㄋㄩ
            nyu_space:[],
            nyu_3  :["女","釹","籹","钕"],             
            nyu_4  :["女","忸","恧","朒","衄"],            
            nyu_6  :[],                       
            nyu_7  :[],
            #ㄋㄨㄢ

            nuan_space:[],
            nuan_3  :["暖","煖","餪","渜","煗"],              
            nuan_4  :[],            
            nuan_6  :[],                       
            nuan_7  :[],

            #ㄋㄨㄛ

            nuo_space:[],
            nuo_3  :["娜","橠"],              
            nuo_4  :["諾","锘","糯","喏","懧","挼","掿","搦","稬",
                     "穤","糑","糥","诺","逽","锘"],            
            nuo_6  :["難","挪","儺","娜","那","傩","哪","捼","梛",
                     "郍"],                       
            nuo_7  :[],
            #ㄛ
            o_space:["喔","ㄛ","呵"],
            o_3  :[],              
            o_4  :[],            
            o_6  :["哦"],                       
            o_7  :[],
            #ㄡ
            ou_space:["歐","毆","鷗","甌","ㄡ","謳","嘔","剾","區",
                      "慪","櫙","欧","殴","沤","漚","熰","瓯","瞘",
                      "蓲","讴","鏂","鸥"],
               
            ou_3  :["偶","藕","嘔","耦","吘","呕","塸","湡","腢",
                    "蕅","髃"],
               
            ou_4  :["嘔","噢","漚","呕","怄","沤","膒"],            
            ou_6  :["吽"],                       
            ou_7  :["噢"],
            #ㄆㄚ
            pa_space:["趴","啪","葩","夿","嘛","嬷","犘","蚆"],
               
            pa_3  :[],
               
            pa_4  :["怕","帕","帊","汃","袙"],            
            pa_6  :["爬","扒","耙","杷","琶","潖","筢","跁","鈀",
                    "钯","魞"],                       
            pa_7  :[],

            #ㄆㄞ
            pai_space:["拍","啪"],
               
            pai_3  :["俖","排","矲"],
               
            pai_4  :["派","湃","汖","苆","蒎","鎃"],            
            pai_6  :["排","牌","徘","俳","棑","猅","簰","輫"],                       
            pai_7  :[],
            #ㄆㄢ
            pan_space:["潘","攀","眅","媻","番"],
               
            pan_3  :["坢"],
               
            pan_4  :["判","盼","畔","叛","泮","拚","冸","沜","溿",
                     "炍","牉","袢","襻","詊","鋬","鑻","頄","頖"],            
            pan_6  :["盤","磐","蟠","槃","跘","搫","胖","媻","幋",
                     "弁","柈","瀊","磻","縏","繁","般","蒰","媻",
                     "踫","蹒","蹣","鎜","鞶"],                       
            pan_7  :[],

            #ㄆㄢ
            pan_space:["潘","攀","眅","媻","番"],
               
            pan_3  :["坢"],
               
            pan_4  :["判","盼","畔","叛","泮","拚","冸","沜","溿",
                     "炍","牉","袢","襻","詊","鋬","鑻","頄","頖"],            
            pan_6  :["盤","磐","蟠","槃","跘","搫","胖","媻","幋",
                     "弁","柈","瀊","磻","縏","繁","般","蒰","媻",
                     "踫","蹒","蹣","鎜","鞶"],                       
            pan_7  :[],

            #ㄆㄤ
            pang_space:["潘","攀","眅","媻","番"],
               
            pang_3  :["坢"],
               
            pang_4  :["判","盼","畔","叛","泮","拚","冸","沜","溿",
                     "炍","牉","袢","襻","詊","鋬","鑻","頄","頖"],            
            pang_6  :["盤","磐","蟠","槃","跘","搫","胖","媻","幋",
                     "弁","柈","瀊","磻","縏","繁","般","蒰","媻",
                     "踫","蹒","蹣","鎜","鞶"],                       
            pang_7  :[],
            #ㄆㄠ
            pao_space:["拋","泡","抛","胞","脬"],
               
            pao_3  :["跑"],
               
            pao_4  :["砲","泡","砲","皰","奅","疱","礟","礮","靤",
                     "髱","麭"],            
            pao_6  :["袍","刨","匏","庖","咆","炮","炰","爮","狍",
                     "瓟","礟","軳","鞄","颮","麃","齙"],                       
            pao_7  :[],

            #ㄆㄠ
            pao_space:["拋","泡","抛","胞","脬"],
               
            pao_3  :["跑"],
               
            pao_4  :["砲","泡","砲","皰","奅","疱","礟","礮","靤",
                     "髱","麭"],            
            pao_6  :["袍","刨","匏","庖","咆","炮","炰","爮","狍",
                     "瓟","礟","軳","鞄","颮","麃","齙"],                       
            pao_7  :[],

            #ㄆㄟ
            pei_space:["胚","坯","呸","坏","垺","妚","娝","岯","柸",
                       "肧","衃","醅"],
               
            pei_3  :["昢","琣"],
               
            pei_4  :["配","佩","沛","珮","霈","姵","旆","轡","浿",
                     "帔","淠","伂","嶏","斾","昢","犻","翇","苝",
                     "辔","釡","馷"],            
            pei_6  :["陪","培","賠","裴","坏","毰","碚","荖","裵",
                     "赔","邳","锫","阫","陫"],                       
            pei_7  :[],
            #ㄆㄣ
            pen_space:["歕","噴","喯","喷","歕"],
               
            pen_3  :["翉","呠","翸"],
               
            pen_4  :["喷","噴"],            
            pen_6  :["盆","湓","瓫","葐","鍁"],                       
            pen_7  :[],

            #ㄆㄣ
            peng_space:["砰","烹","抨","怦","泙","澎","匉","恲","梈",
                        "漰","硑","磞","茓","軯","軿","閛","駍"],
               
            peng_3  :["捧","剻","奉","淎","皏"],
               
            peng_4  :["彭","鵬","踫","掽","堋","槰"],            
            peng_6  :["鵬","彭","棚","澎","朋","蓬","膨","篷","芃",
                      "硼","蟛","倗","傰","嘭","埄","塜","塳","篷",
                      "憉","樥","浲","淜","熢","痭","稝","竼","蘕",
                      "蟚","輣","逢","錋","鑝","韸","韼","髼","鬅",
                      "鬅","鹏"],                       
            peng_7  :[],

            #ㄆㄧ
            pi_space:["批","披","匹","丕","劈","霹","砒","秠","鈹",
                      "紕","伾","噼","坏","坯","怌","怶","悂","憵",
                      "抷","旇","炋","狉","狓","磇","礔","礕","秛",
                      "纰","翍","耚","被","豾","釽","鈈","鉟","銔",
                      "铍","駓","髬","鮍","鴄"],
               
            pi_3  :["匹","癖","痞","疋","圮","否","仳","噽","嚭",
                    "崥","庀","悂","脴","苤","諀"],
               
            pi_4  :["闢","屁","僻","癖","譬","癖","鷿","副","揊",
                    "擗","淠","渒","潎","澼","濞","甓","疈","礔",
                    "躃","辟","鎞","髲","鸊"],            
            pi_6  :["皮","埤","疲","毗","啤","琵","脾","陂","毘",
                      "枇","陴","蜱","郫","蚍","壀","朇","椑","毞",
                      "沘","焷","犤","猈","玭","笓","篺","紕","罴",
                      "罷","羆","膍","芘","藣","蚽","螕","螷",
                     "蠯","裨","豼","貔","軣","輌","鈚","鈹","錍",
                    "铍","阰","隦","鞞","骙","魮","魾","鼙"],                       
            pi_7  :[],

            #ㄆㄧㄢ
            pian_space:["篇","偏","翩","媥","扁","犏","萹","貵","頨",
                      "鶣"],
               
            pian_3  :[],
               
            pian_4  :["片","騙","遍","騗","骗"],            
            pian_6  :["便","胼","諞","駢","楩","平","琕","缏",
                      "腁","賆","跰","蹁","騈","骿"],                       
            pian_7  :[],

            
            #ㄆㄧㄠ
            pie_space:["飄","漂","慓","螵","僄","嘌","嫖","彯","旚",
                      "缥","翲","荙","飃","飘","薸","魒"],
               
            pie_3  :["瞟","漂","縹","殍","莩","摽","犥","摽","皫","篻",
                     "缥","荙","藨","醥","顠","颣","鷅"],
               
            pie_4  :["票","漂","驃","剽","勡","彯","徱","慓","篻",
                     "荙","蔈","顠","骠"],            
            pie_6  :["朴","嫖","瓢","淲","荝","闝"],                       
            pie_7  :[],

            #ㄆㄧㄣ
            pin_space:["飄","漂","慓","螵","僄","嘌","嫖","彯","旚",
                      "缥","翲","荙","飃","飘","薸","魒"],
               
            pin_3  :["品"],
               
            pin_4  :["聘","牝","朩"],            
            pin_6  :["頻","貧","蘋","嬪","顰","嚬","娦","嫔","瀕",
                     "獱","玭","矉","薲","蠙","贫","频","颦"],                       
            pin_7  :[],

            #ㄆㄧㄥ
            ping_space:["娉","乒","俜","甹","砯","聠","艵","覮","頩"],
               
            ping_3  :["絣"],
               
            ping_4  :["聘"],            
            ping_6  :["平","評","坪","屏","憑","瓶","萍","苹","蘋",
                     "枰","呯","玶","秤","俜","冯","凭","凴","屛",
                      "帡","幈","慿","泙","洴","淜","炾","甁","甹",
                      "竮","箳","簈","缾","胓","艵","荓","蓱","蚲",
                      "蛢","评","軿","郱","輧","馮","鮃","鱰","鲆",
                      "鵧"],                       
            ping_7  :[],

            #ㄆㄛ
            po_space:["波","坡","潑","泺","泼","癹","翍","鉕","鏺",
                      "钋","陂","颇","飅"],
               
            po_3  :["頗","叵","剖","尀","笸","箥","钷","駊"],
               
            po_4  :["破","迫","珀","粕","魄","釙","醱","狛","奤",
                    "屰","岶","朴","泊","炇","烞","砶","蒪","謈",
                    "霸"],            
            po_6  :["婆","皤","鄱","嘙","媻","櫇","繁","蔢"],                       
            po_7  :["婆"],

            #ㄆㄡ
            pou_space:["剖","吥"],
               
            pou_3  :["剖","勏","哣","培","婄","掊","棓","犃","瓿"],
               
            pou_4  :[],            
            pou_6  :["抔","抙","捊","掊","稖","裒","錇"],                       
            pou_7  :[],

            #ㄆㄨ
            pu_space:["鋪","舖","撲","噗","仆","扑","抪","擈","攴",
                      "攵","痡","瞨","醭","铺","鯆"],
               
            pu_3  :["普","埔","浦","譜","溥","圃","圤","暜","氆",
                    "潽","烳","誧","諩","谱","鐠","镨"],
               
            pu_4  :["鋪","舖","曝","瀑","暴","蒲","豧","铺","陠"],            
            pu_6  :["蒲","樸","葡","璞","脯","濮","僕","莆","菩",
                    "蹼","匍","朴","墣","幞","扶","檏","獛","穙",
                    "箁","纀","菐","蒱","襆","襥","轐","酺","醭",
                    "釙","鏷","镤"],                       
            pu_7  :[],


            #ㄆㄨ
            pu_space:["鋪","舖","撲","噗","仆","扑","抪","擈","攴",
                      "攵","痡","瞨","醭","铺","鯆"],
               
            pu_3  :["普","埔","浦","譜","溥","圃","圤","暜","氆",
                    "潽","烳","誧","諩","谱","鐠","镨"],
               
            pu_4  :["鋪","舖","曝","瀑","暴","蒲","豧","铺","陠"],            
            pu_6  :["蒲","樸","葡","璞","脯","濮","僕","莆","菩",
                    "蹼","匍","朴","墣","幞","扶","檏","獛","穙",
                    "箁","纀","菐","蒱","襆","襥","轐","酺","醭",
                    "釙","鏷","镤"],                       
            pu_7  :[],
            
            #ㄑㄧ
            qi_space:["七","妻","漆","棲","欺","戚","淒","悽","栖",
                      "鶈","凄","沏","萋","諆","緀","悊","柒","榿",
                     "嘁","娸","慼","鸂","倛","僛","咠","唭","墄",
                      "徛","慽","捿","攲","桤","桼","辒","欹","溪",
                      "磎","磩","紪","緁","莵","莻","谿","迉","郪",
                      "霋","顣","魌"],
               
            qi_3  :["起","啟","豈","綺","杞","乞","棨","啓","綮",
                    "屺","启","呇","唘","啔","婍","岂","敧","晵",
                    "盀","稽","绮","芑","芞","袳","諬","邔","闙"],
               
            qi_4  :["氣","器","企","棄","契","迄","汽","砌","泣",
                    "憩","緝","葺","訖","汔","磜","炁","磧","罊",
                    "亟","呚","呮","咠","噐","夡","妻","弃","忔",
                    "愒","憇","揭","摖","敌","暣","栔","气","湆",
                    "湇","哜","嚌","垍","盵","矵","碛","礘","缉",
                    "蚑","蟿","諿","讫","鏚","鼜"],            
            qi_6  :["其","期","騎","奇","旗","齊","琪","棋","崎",
                    "琦","祈","祺","淇","祇","麒","岐","錡","萁",
                    "騏","歧","鰭","碁","祁","耆","臍","畦","頎",
                    "旂","埼","錤","亓","蜞","衹","綦","碕","鮨",
                    "剘","圻","岓","帺","弜","忯","愭","懠","掑",
                    "斉","斊","枝","棊","檱","濝","櫀","猉","玂",
                    "璂","禥","稘","竒","粸","綥","綨","翗","脐",
                    "艩","芪","荠","萕","蕲","薺","藄","蚑","蚔",
                    "蛴","蜝","蠐","褀","踑","軝","鄿","铏","铔",
                    "陭","隑","颀","騹","骐","骑","鬐","鬾","鬿",
                    "鳍","鵸","鶀","麡","齐"],                       
            qi_7  :[],


            #ㄑㄧㄚ
            qia_space:["掐","跒","辺"],               
            qia_3  :["酎","卡","酠"],
               
            qia_4  :["洽","恰","圶","帢","愘","楬","殎","硈"],            
            qia_6  :[],                       
            qia_7  :[],

            #ㄑㄧㄢ
            qian_space:["千","簽","遷","牽","謙","鉛","籤","嵌","騫",
                        "芊","仟","扦","阡","慳","韆","奷","顅","佥",
                        "僉","圱","圲","婜","孯","岍","忏","悭","愆",
                        "拪","掔","搴","撁","攐","攑","攓","杄","檶",
                        "櫏","欦","臤","汘","褰","諐","譣","谦","谸",
                        "蹮","迁","鐱","钎","铅","顩","馯","骞","鬜",
                        "鵮","麉"],               
            qian_3  :["淺","遣","譴","繾","嗛","嵰","忏","撖","槏","遣",
                      "譴","浅","缱","蜸","谴","鼸"],
               
            qian_4  :["欠","倩","茜","塹","歉","蒨","芡","縴","棈",
                      "俔","綪","傔","儙","刋","嗛","蒨","壍","慊",
                      "椠","槧","皘","篟","纤","肷","萙","蔳","輤"],            
            qian_6  :["前","錢","潛","虔","墘","鉗","鈐","黔","箝",
                      "乾","掮","鉆","乹","仱","姏","媊","岒","忴",
                      "欠","拑","揵","榩","歬","漧","潜","濳","灊",
                      "燂","犍","羬","荨","葥","蚙","蠸","赶","軡",
                      "銭","钤","钱","钳","飗","騚","鬵","鰬","鳹",
                      "黚"],                       
            qian_7  :[],
            

            #ㄑㄧㄤ
            qiang_space:["槍","腔","羌","鏘","鎗","瑲","錆","蹌","呛",
                        "嗆","將","嶈","戗","抢","搶","斨","枪","椌",
                        "溬","牄","猐","矼","羗","羫","萚","蜣","謒",
                        "跄","蹡","鏹","锖","锵","镪"],
               
            qiang_3  :["淺","遣","繾","譴","嗛","嵰","忏","撖","槏",
                    "浅","缱","蜸","谴","鼸"],
               
            qiang_4  :["欠","倩","茜","塹","歉","蒨","歉","縴","棈",
                    "綪","俔","傔","儙","刋","嗛","堑","壍","慊",
                    "亟","槧","皘","篟","纤","肷","萙","蔳","輤"],            
            qiang_6  :["前","錢","潛","虔","墘","鉗","鈐","黔","箝",
                    "乾","掮","鉆","乹","仱","姏","媊","岒","忴",
                    "扲","拑","榩","揵","祁","耆","潜","濳","灊",
                    "燂","犍","羬","荨","葥","蚙","蠸","赶","軡",
                    "銭","钤","钱","钳","飗","騚","鬵","鰬","鳹",
                    "黚"],                       
            qiang_7  :[],


            #ㄑㄧㄤ
            qiang_space:["槍","腔","羌","鏘","鎗","瑲","錆","蹌","呛",
                        "嗆","將","嶈","戗","抢","搶","斨","枪","椌",
                        "溬","牄","猐","矼","羗","羫","萚","蜣","謒",
                        "跄","蹡","鏹","锖","锵","镪"],
               
            qiang_3  :["淺","遣","繾","譴","嗛","嵰","忏","撖","槏",
                    "浅","缱","蜸","谴","鼸"],
               
            qiang_4  :["欠","倩","茜","塹","歉","蒨","歉","縴","棈",
                    "綪","俔","傔","儙","刋","嗛","堑","壍","慊",
                    "亟","槧","皘","篟","纤","肷","萙","蔳","輤"],            
            qiang_6  :["前","錢","潛","虔","墘","鉗","鈐","黔","箝",
                    "乾","掮","鉆","乹","仱","姏","媊","岒","忴",
                    "扲","拑","榩","揵","祁","耆","潜","濳","灊",
                    "燂","犍","羬","荨","葥","蚙","蠸","赶","軡",
                    "銭","钤","钱","钳","飗","騚","鬵","鰬","鳹",
                    "黚"],                       
            qiang_7  :[],
            
            #ㄑㄧㄠ
            qiang_space:["敲","鍬","蹺","橇","蹻","悄","撬","毃","鍫",
                        "塙","墝","墧","墽","嵪","幧","庨","硗","磽",
                        "繑","缲","趬","跷","踍","郻","鄗","鄡","鄥",
                        "鏒","鐰","锹","鞽","頝","骹","髜"],
               
            qiang_3  :["巧","悄","愀","燋","釥","雀","頝","鵲"],
               
            qiang_4  :["俏","翹","鞘","撬","蹺","竅","峭","僺","噭",
                    "帩","撽","殼","礉","窍","翘","誚","诮","谯",
                    "踎","躈","陗","髚"],            
            qiang_6  :["橋","喬","僑","瞧","樵","譙","蕎","翹","憔",
                    "侨","劁","嘺","嫶","峤","嶣","敿","桥","槗",
                    "燆","癄","睄","礄","簥","翘","荍","荞","藮",
                    "谯","趫","趬","鐈","鞒","顦"],                       
            qiang_7  :[],
            #ㄑㄧㄝ
            qie_space:["切","沏","聺"],
               
            qie_3  :["且"],
               
            qie_4  :["竊","切","妾","鍥","篋","愜","挈","怯","唼",
                    "契","帹","悏","惬","慊","抾","朅","洯","淁",
                    "砌","穕","窃","笡","箧","緀","藒","蛪","謙",
                    "踥","躀","锲","鯜"],            
            qie_6  :["茄","伽","癿"],                       
            qie_7  :[],

            #ㄑㄧㄝ
            qie_space:["切","沏","聺"],
               
            qie_3  :["且"],
               
            qie_4  :["竊","切","妾","鍥","篋","愜","挈","怯","唼",
                    "契","帹","悏","惬","慊","抾","朅","洯","淁",
                    "砌","穕","窃","笡","箧","緀","藒","蛪","謙",
                    "踥","躀","锲","鯜"],            
            qie_6  :["茄","伽","癿"],                       
            qie_7  :[],
            #ㄑㄧㄣ
            qin_space:["親","欽","侵","衾","嶔","廞","駸","亲","众",
                       "儬","媇","寴","崯","梫","瀙","綅","誛","鋟",
                       "钦","顉","鮼"],
               
            qin_3  :["寢","坅","寑","昑","曋","螼","赺","鋟","顉"],
               
            qin_4  :["沁","吢","吣","唚","寴","抋","揿","搇","撳",
                    "臤","菣"],            
            qin_6  :["勤","琴","秦","禽","芹","擒","噙","芩","檎",
                     "懃","螓","嫀","嶜","庈","慬","捦","斳","澿",
                     "珡","琹","耹","肣","菳","蠄","蚙","覃","軡",
                     "鈙","锓","雂","靲","鳹","鵭"],                       
            qin_7  :[],
            #ㄑㄧㄥ
            qing_space:["清","輕","青","卿","傾","氫","氰","烴","鯖",
                       "蜻","倾","啨","圊","寈","氢","狅","軽","轻",
                       "郬","鑋","靑","頃","鲘","鲭"],
               
            qing_3  :["請","頃","傾","廎","请","顷"],
               
            qing_4  :["慶","罄","磬","親","謦","汫","亲","凊","媇",
                    "庆","掅","殸","漀","碃","綮","罊","鑋","靘"],            
            qing_6  :["情","晴","擎","黥","傾","剠","勍","夝","擏",
                     "暒","樈","檠","殌","殑","甠","葝"],                       
            qing_7  :[],
            #ㄑㄩㄥ
            qiong_space:["芎","穹","匔","宆","焪","熍","銎"],
               
            qiong_3  :["苘","顈"],
               
            qiong_4  :[],            
            qiong_6  :["瓊","窮","芎","邛","煢","儝","卭","嬛","惸",
                     "桏","棾","橩","焭","琼","璚","瞏","穷","穹",
                      "竆","笻","筇","舼","茕","蒆","藑","藭","蛩",
                      "赹","跫","輁","験"],                       
            qiong_7  :[],

            #ㄑㄩㄥ
            qing_space:["芎","穹","匔","宆","焪","熍","銎"],
               
            qing_3  :["苘","顈"],
               
            qing_4  :[],            
            qing_6  :["瓊","窮","芎","邛","煢","儝","卭","嬛","惸",
                     "桏","棾","橩","焭","琼","璚","瞏","穷","穹",
                      "竆","笻","筇","舼","茕","蒆","藑","藭","蛩",
                      "赹","跫","輁","験"],                       
            qing_7  :[],

            #ㄑㄧㄡ
            qiu_space:["邱","秋","丘","坵","萩","鶖","鰍","鞦","楸",
                       "蚯","恘","偢","媝","篍","緧","蓲","蝵","蟗",
                       "蠤","趥","鞧","鱃","鳅","鳒","龜","龝","龟"],
               
            qiu_3  :["叴","糗","搝"],
               
            qiu_4  :[],    
            qiu_6  :["球","求","裘","囚","逑","泅","酋","虯","毬",
                     "俅","銶","梂","釚","仇","僋","厹","唒","崷",
                      "巯","捄","扏","朹","殏","汓","浗","湭","渞",
                      "煪","犰","玌","玐","璆","皳","盚","紌","絿",
                     "脙","肍","艽","苬","莍","虬","蛷","蝤","蠤",
                     "觓","觩","訄","訅","賕","赇","輏","逎","遒",
                     "醔","頄","驲","鮂","鯄","鰌","鰽","鼽"],                       
            qiu_7  :[],
            #ㄑㄩ
            qu_space:["區","趨","曲","驅","屈","蛆","軀","祛","袪",
                       "嶇","蛐","胠","伹","佉","凵","区","呿","坥",
                       "岖","岨","岴","憈","抾","敺","瞿","砠","紶",
                       "虗","袦","觑","詘","誳","诎","趋","趍","躯",
                       "镼","阹","駆","駈","驱","髷","魼","鱋","鶌"],
               
            qu_3  :["取","曲","娶","齲","浀","竘","筁","紶","詓",
                     "龋"],
               
            qu_4  :["去","趣","覷","闃","刞","厺","娶","湨","漆",
                     "蒅","覰","覻","觑","閴","阒","麮","黢","鼁"],    
            qu_6  :["渠","麴","璩","瞿","衢","磲","鴝","癯","劬",
                     "蕖","佢","匷","懅","戵","斪","朐","欋","氍",
                      "淭","灈","爠","璖","籧","絇","翑","翵","胊",
                      "臞","菃","葋","蘧","蚼","蛐","螶","蟝","蠷",
                     "豞","豦","躣","軥","鑺","鸜","鸲","麯","鼩"],                       
            qu_7  :[],

                        
            #ㄑㄩㄢ
            qu_space:["圈","悛","圏","峑","弮","惓","桊","棬","箞",
                       "絟"],
               
            qu_3  :["犬","汱","綣","呟","圈","犭","琄","甽","畎",
                     "绻","葲","虇","詃"],
               
            qu_4  :["勸","券","劝","勧","圈","烇","牶","絭"],    
            qu_6  :["全","權","泉","拳","銓","醛","詮","荃","蜷",
                     "筌","鬈","痊","洤","佺","湶","恮","顴","灥",
                      "卷","埢","姾","婘","孉","巏","惓","搼","权",
                      "権","牷","犈","犬","踡","瑔","縓","腃","蒊",
                    
                     "蠸","觠","诠","跧","踡","輇","辁","酫","铨",
                    "颧","駩","騡","鰁","齤"],                       
            qu_7  :[],

            #ㄑㄩㄝ
            que_space:["缺","闕","炔","蒛","阙"],
               
            que_3  :[],
               
            que_4  :["卻","確","雀","闕","鵲","怯","怯","榷","埆",
                     "塙","恪","悫","愨","慤","搉","殼","毃","灍",
                     "燩","爵","皵","硞","确","碏","碻","礐","礭",
                     "舭","觳","闋","阕","阙","魥","鹊"],    
            que_6  :["瘸"],                       
            que_7  :[],

            #ㄑㄩㄣ
            qun_space:["逡","夋","峮","踆","輑"],
               
            qun_3  :[],
               
            qun_4  :[],    
            qun_6  :["群","裙","羣","宭","帬","裠","麏"],                       
            qun_7  :[],

            #ㄖㄢ
            ran_space:[],
               
            ran_3  :["染","冉","冄","苒","呥","姌","媣","嫨","橪",
                     "珃","髥","髯"],
               
               
            ran_4  :[],    
            ran_6  :["然","燃","髯","呥","嘫","肰","繎","蚦","蚺",
                     "蛅","衻","袡"],                       
            ran_7  :[],
            #ㄖㄤ
            rang_space:[],
               
            rang_3  :["壤","嚷","攘","爙","夯"],
               
               
            rang_4  :["讓","懹","让"],    
            rang_6  :["穰","攘","禳","瓤","儴","勷","瀼","獽","蘘",
                     "蠰","躟","鬤"],                       
            rang_7  :[],

            #ㄖㄠ
            rao_space:[],               
            rao_3  :["擾","娆","绕"],              
            rao_4  :["繞","遶","隢","绕"],    
            rao_6  :["饒","嬈","蟯","蕘","娆","桡","橈","荛","襓",                     
                     "饶"],                       
            rao_7  :[],

            
            #ㄖㄜ
            re_space:[],
               
            re_3  :["惹","喏","若"],
               
               
            re_4  :["熱","渃","热","爇"],    
            re_6  :["耴"],                       
            re_7  :[],

            #ㄖㄣ
            ren_space:[],
               
            ren_3  :["忍","稔","荏","栠","忹","栣","棯","儿","秹","腍",
                     "荵","馉"],
               
               
            ren_4  :["任","認","刃","韌","恁","軔","飪","仞","紉",
                     "衽","訒","妊","靭","賃","刄","姙","屻","杒",
                     "梕","牣","紝","絍","纫","肕","袵","认","軠",
                     "轫","韧","餁","饪","鵀"],    
            ren_6  :["人","仁","壬","芢","紝","銋","任","儿","姙",
                     "忎","朲","秂","鈓","魜","鵀"],                       
            ren_7  :[],


            #ㄖㄥ
            reng_space:["扔"],
               
            reng_3  :["扔"],
               
               
            reng_4  :["芿"],    
            reng_6  :["仍","礽","辸","陾"],                       
            reng_7  :[],


            #ㄖ
            reng_space:[],
               
            reng_3  :[],
               
               
            reng_4  :["日","囸","氜","衵","釰","鈤","馹"],    
            reng_6  :["仍","礽","辸","陾"],                       
            reng_7  :[],

            #ㄖㄨㄥ
            rong_space:[],
               
            rong_3  :["冗","傇","坈","宂","氄","茸","蓙","軵"],
               
               
            rong_4  :[],    
            rong_6  :["榮","融","容","蓉","榕","絨","溶","戎","鎔",
                      "熔","茸","嶸","瑢","蠑","毧","媶","峵","嵘",
                      "嵤","搑","曧","栄","榵","瀜","烿","爃","狨",
                      "穁","縙","绒","羢","肜","茙","荣","蝾","螎",
                      "褣","駥","髶","鰫","鱅","鷛"],                       
            rong_7  :[],

            #ㄖㄡ
            rou_space:[],
               
            rou_3  :["煣","粈","糅","鍕"],
               
               
            rou_4  :["肉","月","宍","蓜"],    
            rou_6  :["柔","揉","蹂","鞣","媃","葇","厹","楺","渘",
                      "瑈","瓇","禸","糅","脜","腬","蝚","輮","鍒",
                      "韖","騥","鰇","鶔"],                       
            rou_7  :[],


            #ㄖㄨ
            ru_space:[],
               
            ru_3  :["乳","汝","辱","侞","女","擩","肗"],
               
               
            ru_4  :["入","辱","褥","溽","縟","傉","嗕","媷","孺",
                    "擩","洳","缛","肉","茹","蓐","鄏"],    
            ru_6  :["如","儒","茹","濡","繻","蠕","孺","銣","嚅",
                      "薷","襦","帤","蕠","挐","曘","桇","侞","渪",
                      "燸","獳","筎","臑","蒘","袽","邚","醹","釈",
                      "鑐","铷","顬","颥","鱬","鴑","鴽"],                       
            ru_7  :[],

            #ㄖㄨㄢ
            ruan_space:[],
               
            ruan_3  :["軟","阮","偄","媆","愞","朊","瑌","瓀",
                    "碝","礝","緛","耎","腝","蝡","蠕","輭","软"],
               
               
            ruan_4  :[],    
            ruan_6  :["堧","壖","撋"],                       
            ruan_7  :[],


            #ㄖㄨㄟ
            rui_space:[],
               
            rui_3  :["軟","阮","偄","媆","愞","朊","瑌","瓀",
                    "碝","礝","緛","耎","腝","蝡","蠕","輭","软"],
               
               
            rui_4  :[],    
            rui_6  :["堧","壖","撋"],                       
            rui_7  :[],


            #ㄖㄨㄣ
            run_space:["犉"],
               
            run_3  :[],
               
               
            run_4  :["潤","閏","橍","润","闰"],    
            run_6  :["犉","瞤"],                       
            run_7  :[],


            #ㄖㄨㄛ
            ruo_space:[],
               
            ruo_3  :[],
               
               
            ruo_4  :["若","弱","偌","箬","蒻","箬","篛","鄀","叒",
                     "婼","楉","渃","焫","爇","蹃","鶸"],    
            ruo_6  :["挼","捼"],                       
            ruo_7  :[],

            #ㄖㄨㄛ
            ruo_space:[],
               
            ruo_3  :[],
               
               
            ruo_4  :["若","弱","偌","箬","蒻","箬","篛","鄀","叒",
                     "婼","楉","渃","焫","爇","蹃","鶸"],    
            ruo_6  :["挼","捼"],                       
            ruo_7  :[],

            #ㄙㄚ
            sa_space:["撒","仨","櫒"],
               
            sa_3  :["撒","灑","洒","櫒","靸"],
               
               
            sa_4  :["薩","卅","颯","攃","脎","萨","趿","躠","隡",
                     "飒","馺"],    
            sa_6  :[],                       
            sa_7  :[],

            #ㄙㄞ
            sai_space:["塞","腮","鰓","偲","思","愢","揌","毢","顋","鳃"],
               
            sai_3  :[],
               
               
            sai_4  :["賽","塞","僿","簺","赛"],    
            sai_6  :[],                       
            sai_7  :[],

            #ㄙㄢ
            san_space:["三","參","叁","参","叄","叅","嘇","弎","攕",
                       "毿","犙","鬖"],
               
            san_3  :["傘","散","繖","仐","伞","槮","糂","糝","糣",
                     "糤","鏾","饊","馓","鮴"],
               
               
            san_4  :["散","俕","潵","閐"],    
            san_6  :[],                       
            san_7  :[],

            #ㄙㄤ
            sang_space:["桑","喪","丧","桒"],               
            sang_3  :["嗓","搡","磉","褬","鎟","顙","颡"],              
            sang_4  :["喪","丧"],    
            sang_6  :[],                       
            sang_7  :[],

            #ㄙㄠ
            sao_space:["艘","騷","搔","臊","鰺","慅","溞","瘙","繅",
                       "缫","缲","颾","骚","臊","鱢","鳋","鳡"],               
            sao_3  :[],              
            sao_4  :["掃","埽","扫","氉","燥","瘙","臊"],    
            sao_6  :[],                       
            sao_7  :[],

            #ㄙㄜ
            se_space:[],               
            se_3  :[],              
            se_4  :["色","瑟","澀","圾","嗇","塞","璱","穡","銫",
                    "啬","懎","歮","歰","涩","渋","澁","濇","濏",
                    "瀒","犞","穑","穯","繬","翜","譅","趇","轖",
                    "鈒","铯","雭","飋","餏"],    
            se_6  :[],                       
            se_7  :[],

            #ㄙㄣ
            sen_space:["森","幓","曑","槮","穼","篸","罧","蔘","襂"],               
            sen_3  :[],              
            sen_4  :[],    
            sen_6  :[],                       
            sen_7  :[],

            #ㄙㄥ
            seng_space:["僧","鬙"],               
            seng_3  :[],              
            seng_4  :[],    
            seng_6  :[],                       
            seng_7  :[],

            #ㄕㄚ
            sha_space:["沙","殺","砂","莎","鯊","紗","煞","痧","逤",
                       "裟","鎩","唦","帴","摋","杉","桬","樧","猀",
                       "硰","粆","纱","蔱","铩","髿","魦","鮻","鯋",
                       "鲓","鲨"],               
            sha_3  :["傻","儍","訯"],              
            sha_4  :["煞","嗄","霎","剎","歃","唼","喢","廈","樧",
                     "箑","翜","翣","萐","閯"],    
            sha_6  :["啥"],                       
            sha_7  :[],

            #ㄕㄞ
            shai_space:["篩","筛","酾"],               
            shai_3  :["骰","繺","色"],              
            shai_4  :["曬","晒","殺","閷"],    
            shai_6  :[],                       
            shai_7  :[],

            #ㄕㄢ
            shan_space:["山","珊","衫","杉","刪","姍","舢","搧","羶",
                        "潸","煽","跚","挻","釤","笘","苫","傓","删",
                        "剼","埏","姗","扇","摻","檆","澘","烻","狦",
                        "穇","縿","羴","芟","蔶","襂","邓","邖","钐",
                        "髟"],               
            shan_3  :["閃","陝","掸","摻","晱","睒","覢","閄","闪",
                      "陜"],              
            shan_4  :["善","扇","擅","膳","汕","繕","訕","嬗","贍",
                      "鱔","疝","墡","鄯","禪","傓","僐","儃","剡",
                      "單","墠","彡","掞","掸","摲","撣","樿","灗",
                      "煔","煽","磰","禅","缮","蔶","蟮","蟺","謆",
                      "譱","讪","赡","赸","釤","钐","饍","騸","骟",
                      "鱓","鱣","鳝"],    
            shan_6  :[],                       
            shan_7  :[],

            #ㄕㄤ
            shang_space:["商","傷","殤","愓","觴","湯","伤","墒","慯",
                        "殇","汤","滳","漡","蔏","螪","觞","謪","鬺"],               
            shang_3  :["賞","晌","上","丄","赏"],              
            shang_4  :["上","尚","丄","仩","姠","尙","爙","绱"],    
            shang_6  :[],                       
            shang_7  :["裳"],

            #ㄕㄠ
            shao_space:["燒","稍","梢","捎","筲","艄","弰","莦","佋",
                        "娋","巶","旓","烧","焇","蕱","蛸","輎","髾",
                        "鮗","鮹"],               
            shao_3  :["少"],              
            shao_4  :["紹","邵","哨","少","劭","卲","召","捎","潲"],    
            shao_6  :["韶","杓","勺","玿","芍","圴","柖","牊","閊"],                       
            shao_7  :[],

            #ㄕㄜ
            she_space:["奢","檨","賒","奓","畬","畲","譇","賖","赊"],               
            she_3  :["捨","舍"],              
            she_4  :["設","社","涉","射","舍","攝","赦","麝","厍",
                     "厙","弽","慑","拾","捑","摄","摵","欇","歙",
                     "渉","滠","灄","猞","舎","葉","蔎","蠂","设",
                     "蹑","遪","韘","騇"],    
            she_6  :["蛇","什","舌","佘","甚","它","揲","虵","蛥",
                     "鉇","鉈","闍"],                       
            she_7  :[],
            
            #ㄕㄨㄟ
            shei_space:[],               
            shei_3  :["水"],              
            shei_4  :["稅","睡","說","涗","帨","挩","捝","涚","祱",
                     "税","蘔","蛻","蜕","裞","説","说"],    
            shei_6  :["脽","誰","谁"],                       
            shei_7  :[],

            #ㄕㄣ
            shen_space:["深","身","申","伸","蔘","砷","紳","燊","鯓",
                        "珅","參","甡","莘","呻","娠","侁","信","叁",
                        "参","叄","叅","妽","屾","峷","幓","扟","敒",
                        "柛","棽","氠","甧","瘮","眒","籶","籸","绅",
                        "胂","葠","薓","裑","訷","詵","诜","鉮","阠",
                        "駪","鮴","鵢"],               
            shen_3  :["沈","審","嬸","瀋","哂","寀","吲","婶","审",
                      "宷","弞","曋","渖","瞫","矤","矧","覾","訠",
                      "訦","諗","讅","谂","邥","魫"],              
            shen_4  :["甚","慎","腎","滲","蜃","葚","侺","愼","抻",
                     "昚","椹","沁","涁","渗","瘎","眘","罧","肾",
                     "脤","蜄","鋠"],    
            shen_6  :["脽","誰","谁"],                       
            shen_7  :[],


            #ㄕㄥ
            sheng_space:["生","聲","升","昇","陞","笙","牲","胜","甥",
                        "勝","鉎","湦","泩","呏","声","抍","斘","殅",
                        "殸","焺","狌","珄","窚","苼","阩","陹","鵿",
                        "鼪"],               
            sheng_3  :["省","冼","偗","眚","箵"],              
            sheng_4  :["勝","聖","剩","盛","賸","乘","嵊","乗","剰",
                     "圣","垩","墭","椉","琞","蕂","膡","貹"],    
            sheng_6  :["繩","憴","渑","溗","澠","縄","绳","譝","鱦"],                       
            sheng_7  :[],

            #ㄕ
            shi_space:["施","師","失","詩","獅","屍","濕","溼","蝨",
                        "虱","尸","蓍","ㄕ","螄","鰤","噓","师","湤",
                        "湿","溮","狮","瑡","箷","籭","絁","葹","蒒",
                        "褜","褷","襹","诗","迉","邿","酾","釶","鍦",
                        "魳","鯴","鲺","鳁","鳲","鶳","鸍"],               
            shi_3  :["省","冼","偗","眚","箵"],              
            shi_4  :["勝","聖","剩","盛","賸","乘","嵊","乗","剰",
                     "圣","垩","墭","椉","琞","蕂","膡","貹"],    
            shi_6  :["繩","憴","渑","溗","澠","縄","绳","譝","鱦"],                       
            shi_7  :[],


            #ㄕ
            shou_space:["收","収","荍"],               
            shou_3  :["手","首","守","艏","扌","垨","掱"],              
            shou_4  :["受","售","壽","瘦","授","獸","綬","狩","兽",
                     "嘼","嚋","寿","涭","璹","绶","鏉"],    
            shou_6  :["熟"],                       
            shou_7  :[],

            #ㄕㄨ
            shu_space:["書","輸","疏","舒","紓","殊","梳","蔬","樞",
                       "姝","抒","鵨","橾","殳","杸","书","俞","摅",
                       "摴","攄","枢","樗","櫖","毹","毺","疋","疎",
                       "祋","綀","纾","荼","藲","蘓","踈","軗","输",
                       "鄃","陎"],               
            shu_3  :["數","屬","署","鼠","薯","暑","蜀","藷","糬",
                     "潻","黍","婌","属","数","癙","薥","襩","钃",
                     "韣"],              
            shu_4  :["數","樹","術","述","束","恕","豎","墅","曙",
                     "署","澍","戍","庶","倏","漱","鉥","沭","侸",
                     "倐","儵","凁","尌","庻","怷","数","术","樜",
                     "潄","濖","疏","竖","竪","籔","絉","翛","腧",
                     "荗","蒁","虪","裋","錰","鏣","鶐"],    
            shu_6  :["淑","叔","孰","贖","塾","菽","熟","埱","尗",
                     "掓","焂","秫","虪","襡","跾","赎","饸","埱",
                    "鸀"],                       
            shu_7  :["叔"],

            #ㄕㄨㄚ
            shua_space:["刷","唰","鮛"],               
            shua_3  :["耍"],              
            shua_4  :["誜"],    
            shua_6  :[],                       
            shua_7  :[],
            
            
            #ㄕㄨㄞ
            shuai_space:["摔","衰","孈","縗"],               
            shuai_3  :["甩"],              
            shuai_4  :["率","帥","蟀","卛","咰","帅","繂"],    
            shuai_6  :[],                       
            shuai_7  :[],
            
            #ㄕㄨㄢ
            shuan_space:["栓","拴","閂","闩"],               
            shuan_3  :[],              
            shuan_4  :["涮"],    
            shuan_6  :[],                       
            shuan_7  :[],

            #ㄕㄨㄤ
            shuang_space:["雙","霜","双","孀","孇","欆","泷","滝","瀧",
                          "礵","艭","驦","鷞","鸘"],               
            shuang_3  :["爽","塽","慡","樉","漺","縔","騻","鷞"],              
            shuang_4  :["灀"],    
            shuang_6  :[],                       
            shuang_7  :[],
            

            #ㄕㄨㄟ
            shui_space:[],               
            shui_3  :["水"],              
            shui_4  :["说","稅","說","涗","帨","挩","捝","涚","祱",
                      "税","蘔","蛻","蜕","裞","説","说"],    
            shui_6  :["谁","脽","誰"],                       
            shui_7  :[],

            #ㄕㄨㄣ
            shun_space:[],               
            shun_3  :["吮","揗","楯","盾","賰"],              
            shun_4  :["順","舜","瞬","瞚","橓","蕣","蘒","顺","鬊"],    
            shun_6  :[],                       
            shun_7  :[],

            #ㄕㄨㄛ
            shuo_space:["說","哾","蘔","説","说"],               
            shuo_3  :[],              
            shuo_4  :["碩","朔","鑠","爍","妁","槊","欶","蒴","勺",
                      "卛","嗍","帥","揱","搠","數","烁","獡","蒴",
                      "矟","硕","箾","蟀","鎙","铄","飮"],    
            shuo_6  :[],                       
            shuo_7  :[],

            #ㄙ
            si_space:["斯","思","司","私","絲","撕","偲","嘶","廝",
                      "ㄙ","鷥","俬","鍶","楒","澌","虒","丝","凘",
                      "厮","厶","咝","媤","恖","榹","泀","磃","禗",
                      "禠","簛","緦","缌","罳","蕬","蛳","蜤","螄",
                      "螔","蟖","蟴","覗","謕","釃","鉰","鐁","鑓",
                      "锶","颸","騦","鷈","鸶","鼶"],               
            si_3  :["死"],              
            si_4  :["四","似","寺","賜","俟","祀","嗣","飼","肆",
                      "泗","巳","伺","駟","汜","禩","姒","耜","亖",
                      "佀","侣","儩","兕","娰","孠","怬","攺","杫",
                    "柶","洍","涘","瀃","牭","竢","笥","肂","蕼",
                    "貄","逘","釲","鈻","食","饲","驷"],    
            si_6  :[],                       
            si_7  :["厕","硛"],

            #ㄙ
            si_space:["斯","思","司","私","絲","撕","偲","嘶","廝",
                      "ㄙ","鷥","俬","鍶","楒","澌","虒","丝","凘",
                      "厮","厶","咝","媤","恖","榹","泀","磃","禗",
                      "禠","簛","緦","缌","罳","蕬","蛳","蜤","螄",
                      "螔","蟖","蟴","覗","謕","釃","鉰","鐁","鑓",
                      "锶","颸","騦","鷈","鸶","鼶"],               
            si_3  :["死"],              
            si_4  :["四","似","寺","賜","俟","祀","嗣","飼","肆",
                      "泗","巳","伺","駟","汜","禩","姒","耜","亖",
                      "佀","侣","儩","兕","娰","孠","怬","攺","杫",
                    "柶","洍","涘","瀃","牭","竢","笥","肂","蕼",
                    "貄","逘","釲","鈻","食","饲","驷"],    
            si_6  :[],                       
            si_7  :["厕","硛"],

            #ㄙㄨㄥ

            song_space:["松","鬆","崧","嵩","淞","菘","蜙","忪","倯",
                      "凇","娀","庺","憽","枀","柗","梥","檧","濍",
                      "硹","蘴","轪"],               
            song_3  :["聳","悚","慫","竦","傱","嵷","怂","惣","愯","捒","耸","駷"],              
            song_4  :["送","宋","頌","訟","誦","讼","蘰","诵","颂"],    
            song_6  :[],                       
            song_7  :[],

            #ㄙㄡ

            sou_space:["搜","蒐","餿","颼","廋","嗖","廀","捜","摗",
                      "溲","獀","螋","鄋","醙","鎪","鏉","锼","飕",
                      "馊","騪"],               
            sou_3  :["叟","藪","擻","傁","叜","嗾","擞","橾","櫢",
                     "瞍","籔","蓃","薮","謏","颋"],              
            sou_4  :["嗽","擞","瘶","膄"],    
            sou_6  :[],                       
            sou_7  :[],

            #ㄙㄨ

            su_space:["蘇","酥","甦","穌","囌","櫯","稣","苏","蘓",
                      "鯂"],               
            su_3  :[],              
            su_4  :["素","速","訴","塑","溯","肅","宿","夙","粟",
                    "愫","鋉","嫊","簌","傃","驌","僳","嗉","泝",
                    "蓿","涑","窣","塐","愬","憟","摍","數","栜",
                    "榡","樕","橚","殐","洬","溸","溹","潚","潥",
                    "玊","珟","璛","碿","粛","縤","縮","缩","肃",
                    "膆","蔌","藗","蘓","觫","誎","謖","诉","谡",
                    "趚","蹜","遡","遫","餗","鱐","鷫"],
               
            su_6  :["俗"],                       
            su_7  :[],

            #ㄙㄨㄢ

            suan_space:["酸","痠","狻","虄"],               
            suan_3  :["匴","篹"],              
            suan_4  :["算","蒜","祘","筭"],
               
            suan_6  :[],                       
            suan_7  :[],

            #ㄙㄨㄟ

            sui_space:["雖","綏","睢","荾","荽","倠","哸","夊","奞",
                       "娞","尿","毸","浽","滖","濉","熣","眭","虽",
                       "鞖"],               
            sui_3  :["髓","嶲","巂","瀡","膸","靃","髄"],              
            sui_4  :["歲","遂","碎","穗","隧","穗","祟","燧","檅",
                     "亗","埣","嬘","嵗","旞","檖","歳","澻","煫",
                     "璲","疩","睟","砕","禭","穂","穟","繀","繐",
                     "繸","襚","誶","譢","谇","賥","轊","鐆","鐩",
                     "韢"],
               
            sui_6  :["隨","隋","髓","瓍","绥","芕","遀","遂","随",
                     "雟"],                       
            sui_7  :[],

            #ㄙㄨㄣ

            sun_space:["孫","蓀","飧","猻","孙","槂","搎","狲","荪",
                       "蕵","薞","轌","飡","飱"],               
            sun_3  :["損","筍","榫","笋","损","箰","簨","鎨","阘"],              
            sun_4  :["愻","潠"],
               
            sun_6  :[],                       
            sun_7  :[],

            #ㄊㄚ

            ta_space:["他","她","它","牠","祂","塌","趿","鉈","禢",
                       "褟","鉇","铊","靸"],               
            ta_3  :["塔","墖","榙","獭","鎝","鳎"],              
            ta_4  :["踏","榻","躂","漯","沓","撻","獺","蹋","拓",
                    "遢","遝","錔","傝","嗒","嚃","塌","崉","挞",
                    "搨","橽","毾","涾","溻","澾","濌","眔","羍",
                    "蟽","誻","譶","蹹","躢","迏","达","迖","達",
                    "鎉","鑉","闒","闥","闼","阓","鞈","鞜","鞳",
                    "鮙","鰨","龖","龘"],
               
            ta_6  :[],                       
            ta_7  :[],

            #ㄊㄞ

            tai_space:["他","她","它","牠","祂","塌","趿","鉈","禢",
                       "褟","鉇","铊","靸"],               
            tai_3  :["塔","墖","榙","獭","鎝","鳎"],              
            tai_4  :["踏","榻","躂","漯","沓","撻","獺","蹋","拓",
                    "遢","遝","錔","傝","嗒","嚃","塌","崉","挞",
                    "搨","橽","毾","涾","溻","澾","濌","眔","羍",
                    "蟽","誻","譶","蹹","躢","迏","达","迖","達",
                    "鎉","鑉","闒","闥","闼","阓","鞈","鞜","鞳",
                    "鮙","鰨","龖","龘"],
               
            tai_6  :[],                       
            tai_7  :[],
            
            #ㄊㄢ

            tan_space:["攤","貪","灘","坍","癱","驒","怹","嘽","噒",
                       "抩","探","摊","灘","擹","瘫","緂","舑","舚",
                       "贪"],               
            tan_3  :["坦","毯","袒","忐","菼","贉","嗿","憳","憻",
                     "璮","禫","膻","裧","襢","醓","鉭","钽","憳"],              
            tan_4  :["炭","探","嘆","碳","歎","湠","僋","埮","羰",
                    "舕","賧"],
               
            tan_6  :[],                       
            tan_7  :[],

            #ㄊㄤ

            tang_space:["湯","蹚","鏜","蝪","汤","薚","鐋","铴","镗",
                       "鞺","鼞"],               
            tang_3  :["躺","倘","淌","帑","儻","伖","偒","傥","惝",
                     "戃","攩","曭","爣","矘","耥","鎲","钂"],              
            tang_4  :["趟","燙","摥","烫","鐋"],
               
            tang_6  :["堂","糖","唐","塘","棠","醣","膛","瑭","溏",
                      "搪","樘","螳","螗","榶","漟","煻","傏","啺",
                      "坣","摚","橖","磄","禟","篖","糃","糛","膅",
                      "蓎","薚","蚫","赯","踼","鄌","鎕","鏜","镗",
                      "镵","闛","隚","餹","饄","饧","鶶"],                       
            tang_7  :[],

            #ㄊㄠ

            tao_space:["饕","掏","韜","滔","搯","濤","慆","弢","縚",
                       "叨","夵","嫍","幍","槄","焘","瑫","絛","縧",
                       "绦","翢","蜪","詜","謟","鞱","韬","飸"],               
            tao_3  :["討","讨"],              
            tao_4  :["套"],
               
            tao_6  :["陶","濤","桃","逃","淘","萄","燾","啕","咷",
                      "匋","檮","洮","涛","祹","綯","蛍","蜪","裪",
                      "迯","醄","鋾","錭","鞀","駣","鞉","騊","鼗"],                       
            tao_7  :[],

            #ㄊㄜ

            te_space:["忒"],               
            te_3  :[],              
            te_4  :["特","忑","慝","匿","忒","脦","蚮","螣","蟘",
                    "貣","鋱","铽","鴏"],
               
            te_6  :[],                       
            te_7  :[],

            #ㄊㄥ

            teng_space:["膯","鼟"],               
            teng_3  :[],              
            teng_4  :[],
               
            teng_6  :["藤","騰","疼","籐","滕","謄","儯","幐","漛",
                      "籘","縢","腾","螣","誊","邆","駦"],                       
            teng_7  :[],


            #ㄊㄧ

            ti_space:["踢","梯","剔","掦","焍","銻","锑"],               
            ti_3  :["體","体","屉","綈","躰","軆","骵"],              
            ti_4  :["替","剃","惕","悌","涕","銻","薙","剔","屜",
                    "逖","倜","嚏","俶","嚔","屟","弟","悐","戻",
                    "挮","揥","擿","歒","殢","瓋","籊","绨","蛯",
                    "裼","褅","趯","迖","逷","鐟","髢","髰","鬀",
                    "鬄","鵜"],
               
            ti_6  :["提","題","堤","媞","緹","蹄","啼","鯷","醍",
                    "隄","禔","鵜","鷈","偍","厗","蹄","埞","崹",
                    "惿","漽","瑅","睼","碮","禵","稊","綈","绨",
                    "缇","罤","腣","荑","蕛","蝭","謕","趧","蹏",
                    "遆","鍗","题","騠","鮷","鴺","鶗","鶙","鷉",
                    "鷤","鹈"],                       
            ti_7  :[],
            
            #ㄊㄧㄢ

            tian_space:["天","添","倎","兲","婖","屇","沗","酟","靝",
                        "黇"],               
            tian_3  :["舔","晪","忝","腆","殄","唺","悿","淟","痶"
                      "睓","紾","蚕","覥","賟","銽","鍩","靦","餂"],              
            tian_4  :["瑱","掭","煔"],
               
            tian_6  :["田","填","甜","恬","沺","闐","塡","搷","湉",
                    "璳","甛","禔","盷","磌","窴","胋","菾","钿",
                    "阗","鷏"],                       
            tian_7  :[],
            
            #ㄊㄧㄠ

            tiao_space:["挑","祧","佻","庣","恌","旫","聎","莜","蓨",
                        "鮡"],               
            tiao_3  :["挑","窕","嬥","宨","晀","窱","誂"],              
            tiao_4  :["跳","眺","眺","朓","嬥","佻","粜","絩","脁",
                      "覜","鑃","頫"],
               
            tiao_6  :["條","調","迢","苕","髫","佻","鰷","岧","岹",
                    "条","樤","祒","笤","芀","萔","蜩","调","趒",
                    "銚","鋚","鎥","鞗","鲌","鲦","齠","龆"],                       
            tiao_7  :[],

            #ㄊㄧㄝ

            tie_space:["貼","怗","萜","帖","贴","跕"],               
            tie_3  :["鐵","帖","驖","僣","鉄","铁"],              
            tie_4  :["餮","帖","蛈","飻"],
               
            tie_6  :[],                       
            tie_7  :[],

            #ㄊㄧㄥ

            ting_space:["聽","廳","汀","桯","厅","听","庁","廰","朾",
                        "烃","綎","耓","耵","桯","聼","艼","鞓"],               
            ting_3  :["挺","艇","町","鋌","聴","侹","梃","侱","圢",
                      "涏","烶","脡","誔","铤","頲"],              
            ting_4  :["聽","听","忊","聴","聼"],
               
            ting_6  :["停","騰","庭","亭","婷","霆","蜓","葶","莛",
                      "渟","筳","楟","嵉","朾","榳","綎","聤","蝏",
                      "諪","邒","閮","鼮"],                       
            ting_7  :[],
            #ㄊㄨㄥ

            tong_space:["通","樋","蓪","嗵","囲","恫","炵","熥","狪",
                        "痌","醤"],               
            tong_3  :["統","桶","筒","捅","垌","姛","筩","统"],              
            tong_4  :["痛","慟","恸","憅","蘳","衕"],
               
            tong_6  :["同","童","桐","銅","彤","酮","瞳","硐","峒",
                      "仝","潼","佟","僮","烔","浵","曈","朣","茼",
                      "橦","侗","勭","哃","庝","挏","晍","氃","洞",
                      "燑","爞","犝","狪","獞","眮","砼","硧","秱",
                      "穜","筒","粡","絧","罿","膧","艟","蕫","蚒",
                      "衕","詷","赨","迵","鉖","鉵","铜","餇","鮦",
                      "鼨"],                       
            tong_7  :[],

            #ㄊㄡ

            tou_space:["偷","偸","媮","鍮"],               
            tou_3  :["鈄","妵","紏","蘣","钭","黈","筩","统"],              
            tou_4 :["透","斢"],
               
            tou_6  :["投","頭","疼","骰","坄","头","牏","緰","褕"],                       
            tou_7  :["頭","头"],

            #ㄊㄨ

            tu_space:["禿","凸","嶀","庩","廜","捸","涋","痜","秃",
                      "鵚"],               
            tu_3  :["土","吐","釷","唋","堍","鵵"],              
            tu_4 :["兔","吐","菟","兎","堍","鵵"],
               
            tu_6  :["圖","塗","徒","突","涂","途","凸","屠","凃",
                    "荼","椟","啚","図","图","圗","堗","宊","峹",
                    "嵞","廜","怢","悇","捈","揬","梌","湥","潳",
                    "瑹","瘏","稌","筡","腯","菟","葖","蒤","蝋",
                    "跿","酴","鈯","鍎","馟","駼","鵌","鶙","鷉",
                    "鶟","鷵","鼵"],                       
            tu_7  :[],


            #ㄊㄨㄢ

            tuan_space:["湍","貒","煓","猯"],               
            tuan_3  :["畽","疃","颴"],              
            tuan_4 :["彖","湪","褖"],
               
            tuan_6  :["團","糰","槫","漙","剸","团","団","圌","慱",
                    "抟","摶","檲","篿","鏄","鷒","鷻"],                       
            tuan_7  :[],

            
            #ㄊㄨㄟ

            tui_space:["推","煺","蓷","藬"],               
            tui_3  :["腿","俀","僓","蹆","骽"],              
            tui_4 :["退","蛻","娧","螁","駾"],
               
            tui_6  :["頹","僓","蹪","墤","尵","弚","橔","穨","藬",
                    "蘈","隤","頺","頽","颓","魋"],                       
            tui_7  :[],

            #ㄊㄨㄣ

            tun_space:["推","煺","蓷","藬"],               
            tun_3  :["腿","俀","僓","蹆","骽"],              
            tun_4 :["退","蛻","娧","螁","駾"],
               
            tun_6  :["頹","僓","蹪","墤","尵","弚","橔","穨","藬",
                    "蘈","隤","頺","頽","颓","魋"],                       
            tun_7  :[],

            #ㄊㄨㄛ

            tuo_space:["脫","拖","托","託","魠","侂","挩","侻","咃",
                       "堶","扥","拕","杔","楕","汑","沰","痑","矺",
                       "脱","蛇","訑","詑","飥","馲","驝"],               
            tuo_3  :["妥","庹","橢","媠","嫷","撱","佗","鋖","鰖",
                     "鵎"],              
            tuo_4 :["拓","涶","唾","侻","墌","柝","槖","毤","毻",
                    "涶","箨","莌","蘀","袥","跅","魄"],
               
            tuo_6  :["陀","駝","坨","鴕","馱","沱","佗","酡","砣",
                    "跎","岮","彵","柁","橐","沲","狏","砤","碢",
                     "紽","袉","鉇","鉈","铊","阤","陁","鞁","飥",
                     "駄","駞","驒","驮","鮀","驼","鱜","鸵","鼉",
                     "鼍","鼧"],                       
            tuo_7  :[],
            #ㄨㄚ

            wa_space:["挖","蛙","漥","哇","窪","洼","媧","劸","呱",
                       "嗗","娲","搲","攨","溛","畖","穵","窊","窐",
                       "聉","鼃"],               
            wa_3  :["瓦","佤","咓","邷"],              
            wa_4 :["襪","哇","嗢","腽","膃","袜","韈","韤"],
               
            wa_6  :["娃","挖"],                       
            wa_7  :["哇","娃"],
            #ㄨㄞ
            wai_space:["歪","竵"],               
            wai_3  :["歪","舀"],              
            wai_4 :["外","懀","蝿"],
               
            wai_6  :[],                       
            wai_7  :[],
            #ㄨㄢ
            wan_space:[],               
            wan_3  :["晚","碗","婉","挽","宛","琬","菀","浣","綰",
                     "皖","輓","畹","脘","腕","睌","莞","脕","倇",
                     "啘","埦","娩","捾","晩","晼","梚","椀","盌",
                     "睕","箢","綩","绾","萖","葂","蜿","踠","鋄",
                     "鋔","錽","鎫","锠","锽","鞔","鯇"],              
            wan_4 :["萬","腕","惋","玩","卍","翫","万","仴","卐",
                    "忨","捥","綄","薍","蟃","贃","踠","輐"],
               
            wan_6  :["玩","完","丸","頑","烷","紈","刓","婠","岏",
                     "忨","抏","捖","汍","纨","芄","貦","顽"],                       
            wan_7  :[],

            #ㄨㄤ
            wang_space:["汪","尪","尢","尣","尩","尫"],               
            wang_3  :["往","網","枉","罔","惘","魍","冈","徃","暀",
                     "棢","瀇","网","枉","臦","菵","蛧","誷","輞",
                     "辋","迬"],              
            wang_4 :["忘","望","旺","妄","朢","王","莣","螦","迋"],
               
            wang_6  :["王","亡","亾","兦","彺","莣","蚟"],                       
            wang_7  :[],

            #ㄨㄟ
            wei_space:["威","葳","崴","偎","萎","煨","隈","烓","燰",
                       "委","渨","葨","喴","媙","嵔","愄","揋","椳",
                       "楲","溾","癐","碨","蝛","螧","覣","詴","逶",
                       "隇","鰃","鰄"],               
            wei_3  :["委","偉","尾","瑋","緯","鮪","煒","暐","葦",
                     "萎","芛","韙","諉","猥","韡","娓","梶","洧",
                     "痿","艉","磈","隗","徫","椲","亹","伟","伪",
                     "儰","厃","唩","喡","壝","媁","寪","峗","崣",
                      "愇","斖","浘","瀢","炜","玮","痏","硊","纬",
                      "腲","苇","荱","蒍","蓶","蔿","薳","蘤","蜲",
                      "诿","踓","鍡","韑","韪","頠","颹","骩","骪",
                      "骫","鰖","鲔"],              
            wei_4 :["為","位","未","味","衛","魏","胃","餵","偽",
                    "蔚","謂","畏","慰","尉","渭","喂","蝟","餵",
                    "餧","为","亹","僞","卫","叞","媦","嬒","徻",
                    "爲","犚","犩","猬","磑","穌","叞","罻","苿",
                    "菋","薉","藯","蜼","螱","蟏","蟐","衞","褽",
                    "讆","谓","贀","躗","軎","遗","遺","錗","鏏",
                    "霨","鮇"],
               
            wei_6  :["為","維","圍","微","惟","薇","唯","帷","違",
                     "危","囗","巍","闈","桅","濰","幃","帷","癓",
                     "嵬","鍏","鮠","湋","为","围","峗","峞","帏",
                     "欈","沩","洈","涠","溦","潍","潙","潿","濻",
                     "瀢","犩","维","蓶","覹","违","鄬","醀","闱",
                     "陒","霺","韦"],
               
            wei_7  :[],


            #ㄨㄟ
            wen_space:["溫","塭","瘟","轀","昷","榅","殟","温","瑥",
                       "瞃","豱","輼","馧"],               
            wen_3  :["穩","吻","刎","脗","呡","懚","桽","歾","穏",
                     "肳"],              
            wen_4 :["問","汶","紊","搵","文","璺","免","妏","抆",
                    "揾","絻","纹","聞","问"],
               
            wen_6  :[],
               
            wen_7  :[],

            #ㄨㄥ
            weng_space:["翁","嗡","鶲","螉","鎓","霐"],               
            weng_3  :["蓊","聬","勜","塕","嵡","暡","浻","滃","瞈"],              
            weng_4 :["甕","瓮","罋","齆"],
               
            weng_6  :[],
               
            weng_7  :[],

            #ㄨㄛ
            wo_space:["窩","渦","倭","萵","喔","挝","涡","猧","窝",
                      "莴","蜗","渦"],               
            wo_3  :["我","婐","捰"],              
            wo_4 :["握","沃","臥","渥","斡","幄","齷","涴","偓",
                   "卧","喔","楃","濣","焥","腛","艧","鍄","龌"],
               
            wo_6  :[],
               
            wo_7  :["午","喔"],

            #ㄨ
            wu_space:["屋","烏","巫","汙","污","誣","嗚","鄔","ㄨ",
                      "鎢","圬","於","杇","乌","剭","匫","呜","媉",
                      "弙","恶","惡","歍","汚","洿","盓","窏","箼",
                      "腛","螐","诬","邬","钨","陓","鰞","鴮","鵐",
                      "鼿"],               
            wu_3  :["五","武","舞","午","伍","摀","侮","捂","鵡",
                    "仵","廡","忤","嵨","迕","嫵","憮","倵","儛",
                    "啎","墲","妩","娬","庑","怃","抚","旿","橆",
                    "潕","牾","玝","珷","甒","碔","膴","躌","陚",
                    "陚","鹉"],              
            wu_4 :["物","務","誤","勿","霧","惡","悟","晤","戊",
                   "塢","騖","兀","逜","鶩","寤","杌","婺","芴",
                   "鋈","乌","僫","务","匫","卼","噁","坞","埡",
                   "堊","奦","娪","屼","岉","嵍","忢","煟","熃",
                   "悞","扤","悪","敄","沕","溩","焐","溩","煟",
                   "瑦","痦","矹","窹","粅","蓩","蘁","误","軏",
                   "迕","遻","鎢","阢","雾","霚","靰","骛","鹜",
                   "齀"],
               
            wu_6  :["無","吳","吾","梧","毋","蕪","浯","唔","蜈",
                    "毌","鼯","俉","膴","誣","鋘","鋙","亡","亾",
                    "兦","吴","呉","峿","巫","无","洖","牾","珸",
                    "瞴","禑","芜","茣","莁","蟱","誈","譕","郚",
                    "鯃","鷡","麌"],
               
            wu_7  :[],


            #ㄨ
            wu_space:["屋","烏","巫","汙","污","誣","嗚","鄔","ㄨ",
                      "鎢","圬","於","杇","乌","剭","匫","呜","媉",
                      "弙","恶","惡","歍","汚","洿","盓","窏","箼",
                      "腛","螐","诬","邬","钨","陓","鰞","鴮","鵐",
                      "鼿"],               
            wu_3  :["五","武","舞","午","伍","摀","侮","捂","鵡",
                    "仵","廡","忤","嵨","迕","嫵","憮","倵","儛",
                    "啎","墲","妩","娬","庑","怃","抚","旿","橆",
                    "潕","牾","玝","珷","甒","碔","膴","躌","陚",
                    "陚","鹉"],              
            wu_4 :["物","務","誤","勿","霧","惡","悟","晤","戊",
                   "塢","騖","兀","逜","鶩","寤","杌","婺","芴",
                   "鋈","乌","僫","务","匫","卼","噁","坞","埡",
                   "堊","奦","娪","屼","岉","嵍","忢","煟","熃",
                   "悞","扤","悪","敄","沕","溩","焐","溩","煟",
                   "瑦","痦","矹","窹","粅","蓩","蘁","误","軏",
                   "迕","遻","鎢","阢","雾","霚","靰","骛","鹜",
                   "齀"],
               
            wu_6  :["無","吳","吾","梧","毋","蕪","浯","唔","蜈",
                    "毌","鼯","俉","膴","誣","鋘","鋙","亡","亾",
                    "兦","吴","呉","峿","巫","无","洖","牾","珸",
                    "瞴","禑","芜","茣","莁","蟱","誈","譕","郚",
                    "鯃","鷡","麌"],
               
            wu_7  :[],

            #ㄒㄧ
            xi_space:["溪","西","希","吸","熙","悉","攜","膝","嘻",
                      "稀","禧","析","兮","曦","蜥","奚","嬉","烯",
                      "熹","晰","羲","犧","犀","唏","硒","皙","晞",
                      "熺","谿","淅","僖","蹊","蟋","恓","鼷","浠",
                      "窸","蠵","巂","栖","樨","莃","俙","傒","僁",
                      "凞","卤","厀","唽","噏","娭","媐","嬆","屎",
                      "屖","嵆","嵠","巇","徆","徯","忚","忾","桸",
                      "怷","悕","惁","扱","扸","携","撕","擕","桸",
                      "棲","榽","橀","欷","歖","氥","潝","焁","焈",
                      "熈","熻","燨","爔","牺","狶","玺","琋","瓗",
                      "畦","疧","盻","睎","瞦","礂","粞","繥","纗",
                      "羛","胿","舾","菥","睎","螅","螇","螝","觹",
                      "觽","觿","誒","譆","讗","豀","豨","豯","貕",
                      "郋","酅","醯","釐","鏭","鑴","锡","闟","隵",
                      "饎","騒","騱","驨","鬹","鵗","鸂","黊"],               
            xi_3  :["喜","洗","囍","璽","徙","洒","屣","葸","禧",
                    "匚","匸","噧","壐","憘","憙","敼","暿","枲",
                    "漇","狶","玺","簁","縰","纚","葈","蓰","蟢",
                    "諰","蹝","躧","釃","鈪","鉨","鉩","钖","铣",
                    "霼","鰓"],              
            xi_4 :["系","係","戲","細","矽","潟","隙","夕","汐",
                   "繫","卌","屭","歙","鬩","傒","僁","呬","咥",
                   "嚊","嚱","妎","屓","忥","怬","恄","戏","戯",
                   "戱","扢","摡","晳","滊","潝","焃","熂","犔",
                   "盻","磶","禊","稧","穸","綌","緆","縘","细",
                   "翕","翖","肸","肹","舃","舄","蕮","虩","衋",
                   "褉","覤","謑","赥","赩","郄","郤","鄎","韢",
                   "酅","釳","釸","鎎","鑴","阋","隟","霫","韢",
                   "餼","饩","黖","齂"],
               
            xi_6  :["離","梨","黎","罹","犁","厘","釐","鱺","籬",
                    "璃","貍","狸","孋","漓","藜","驪","犛","麶",
                    "褵","蜊","蠡","鸝","犂","鑗","黧","蘺","灕",
                    "縭","蔾","麗","离","粍","喱","攡","刕","剓",
                    "剺","劙","卨","哩","嚟","囇","嫠","孷","廲",
                    "悡","梩","梸","棃","樆","氂","漦","猍","盠",
                    "睝","穲","篱","缡","艃","荲","菞","蓠","蟍",
                    "蟸","蠫","謧","邌","酦","醨","釃","鋫","錅",
                    "鏫","騹","骊","鯬","鲃","鲡","鵹","鹂","麶",
                    "黐"],
               
            xi_7  :["哩"],

            #ㄒㄧㄚ
            xia_space:["蝦","瞎","傄","岈","谺","鍜","颬","鰕"],               
            xia_3  :["閜"],              
            xia_4 :["下","夏","嚇","廈","昰","丅","厦","吓","夓",
                   "懗","暇","欱","煆","疜","罅","芐","諕","鏬",
                   "鶷"],
               
            xia_6  :["霞","轄","挾","俠","狹","呷","峽","匣","瑕",
                    "暇","遐","狎","陜","黠","侠","假","冾","峡",
                    "搳","斜","柙","洽","炠","烚","狭","珨","睱",
                    "硖","硤","碬","磍","祫","笚","筪","縀","縖",
                    "翈","舝","蕸","赮","辖","鍜","鎋","镠","陕",
                    "陝","陿","騢","魻","鰕","鶷"],
               
            xia_7  :[],

            #ㄒㄧㄢ
            xian_space:["先","仙","鮮","纖","掀","秈","暹","氙","珗",
                        "仚","屳","灦","奾","僊","嘕","姍","嬐","孅",
                        "廯","忺","憸","攕","杴","枮","硟","澖","祆",
                        "籼","纎","纤","苮","莶","蓒","褼","襳","跹",
                        "蹮","躚","酰","醶","銛","銽","錟","锨","韱",
                        "馦","鱻","鲜","鶱"],               
            xian_3  :["顯","險","癬","蜆","銑","搟","蘚","鮮","獮",
                       "燹","姺","尟","尠","嶮","幰","攇","显","毨",
                       "洒","洗","烍","猃","獫","玁","礆","禒","筅",
                      "箲","藓","蚬","譣","赻","跣","鍌","铣","险",
                      "韅","顕","鲜","鼸","齴"],              
            xian_4 :["縣","線","現","憲","限","獻","陷","餡","腺",
                   "羨","霰","莧","瀗","俔","僩","县","咞","哯",
                   "垷","姭","娊","宪","现","岘","悓","撊","晛",
                    "橌","櫶","涀","献","睍","粯","睍","絤","綫",
                     "线","臔","臽","苋","蜆","見","誢","见","豏",
                     "軐","轞","鋧","錎","鏾","饀","馅","麲"],
               
            xian_6  :["衔","嫌","閒","鹹","咸","嫻","弦","銜","絃",
                    "閑","諴","啣","嫺","鷴","舷","涎","癇","鷳",
                    "唌","娴","娹","婱","憪","燅","甉","痃","痫",
                    "礥","稴","羬","胘","臤","葴","藖","蚿","蛝",
                    "衔","衘","誸","贒","贤","輱","醎","闲","鹇"],
               
            xian_7  :[],

            #ㄒㄧㄤ
            xiang_space:["相","鄉","香","箱","廂","湘","襄","鑲","驤",
                        "薌","葙","緗","乡","厢","啌","忀","欀","瓖",
                        "皂","纕","缃","膷","舡","芗","袆","郷","鄊",
                        "鄕","镶","骧","麘"],               
            xiang_3  :["想","響","享","饗","餉","响","饟","鯗","亯",
                       "晑","珦","鄉","銄","鑜","飨","饷","鮝","鱶",
                       "鱽","鲞"],              
            xiang_4 :["向","項","像","象","巷","相","橡","嚮","勨",
                   "嶑","恦","曏","潒","缿","萫","蟓","蠁","襐",
                   "鄉","鐌","闀","项","鱌"],
               
            xiang_6  :["祥","翔","降","詳","庠","羊","佭","栙","样",
                    "絴","详","跭","鴹"],
               
            xiang_7  :[],

            #ㄒㄧㄠ
            xiao_space:["蕭","消","銷","霄","硝","削","宵","鴞","囂",
                        "瀟","梟","哮","簫","逍","驍","烋","蛸","魈",
                        "呺","哓","啋","嘋","嘐","嘵","嚣","嚻","婋",
                        "宯","庨","彇","憢","揱","撨","枭","枵","櫹",
                        "歊","毊","洨","涍","潇","潚","灱","枭","猇",
                        "獢","痚","痟","硣","穘","窙","箫","簘","綃",
                        "绡","翛","膮","萧","萷","藃","虈","虓","蟂",
                        "蟰","蠨","謼","踃","鑁","销","顤","颵","骁",
                        "髇","髐","鴵"],               
            xiao_3  :["小","曉","筱","篠","謏","晓","暁","皢","袯",
                       "袰"],              
            xiao_4 :["校","笑","孝","效","肖","嘯","酵","傚","咲",
                   "効","俲","关","啸","嘨","娎","恔","歗","涍",
                   "熽","皛","藠","誟","踍","鞩","韒"],
               
            xiao_6  :["姣","學","斈","洨","笅","胶","袮","誵","郩"],
               
            xiao_7  :[],

            #ㄒㄧㄝ
            xie_space:["些","歇","蠍","楔","嗋","揳","猲","蝎","褉"],               
            xie_3  :["寫","血","写","叶","藛"],              
            xie_4 :["謝","洩","蟹","卸","燮","屑","械","瀉","榭",
                   "泄","渫","懈","褻","邂","瀣","獬","解","亵",
                   "伳","偰","呭","契","妎","媟","屜","屧","嶰",
                   "廨","徢","揳","斺","暬","楔","榍","檞","泻",
                    "澥","灺","焎","爕","疶","碿","祄","糏","紲",
                    "絏","絬","緤","绁","缷","薢","薤","蠏","觧",
                    "谢","躞","躠","逹","阛","鞢","韰","駭","駴",
                    "骱","鰰","齘","齛","齥"],
               
            xie_6  :["協","鞋","斜","邪","偕","諧","脅","脇","劦",
                     "纈","拹","勰","嗋","垥","奊","恊","愶","慀",
                     "挟","挾","搚","撷","擷","攜","旪","熁","燲",
                     "瑎","籺","絜","綊","缬","翓","胁","脥","膎",
                     "蝢","衺","裃","裄","裇","裈","襭","谐","鞵",
                     "頡","颉","鮭","龤"],
               
            xie_7  :["謝"],



            #ㄒㄧㄣ
            xin_space:["新","心","欣","辛","馨","薪","鑫","芯","昕",
                       "鋅","歆","忻","欣","炘","鈊","妡","盺","俽",
                       "兟","噷","嬜","廞","忄","惞","訢","邤","锌"],               
            xin_3  :["伈"],              
            xin_4 :["信","囟","釁","舋","卂","妡","焮","煡","膷",
                   "芯","衅","訫","軐","阠","顖","馸"],
               
            xin_6  :["寻","尋","攳","杺","樳","襑","鄩","镡","鬵"],
               
            xin_7  :[],

            #ㄒㄧㄥ
            xing_space:["興","星","腥","猩","惺","煋","兴","垶","曐",
                       "瑆","皨","胜","蛵","觪","觲","鍟","馨","馫",
                       "騂","鮏","鯹"],               
            xing_3  :["醒","擤","省","渻","睲"],              
            xing_4 :["姓","性","幸","杏","興","倖","悻","行","莕",
                   "荇","婞","兴","咅","嬹","涬","睲","緈","臖",
                     "葕"],
               
            xing_6  :["型","行","形","刑","邢","洐","侀","坓","娙",
                      "滎","濴","烆","硎","筕","胻","荥","賯","郉",
                      "鈃","鉶","銒","鋞","陉","陘","餳","饧"],
               
            xing_7  :[],


            #ㄒㄩㄥ
            xiong_space:["胸","兇","兄","凶","匈","洶","汹","哅","忷",
                       "恟","胷","褄","訩","詾"],               
            xiong_3  :[],              
            xiong_4 :["夐","敻","詗"],
               
            xiong_6  :["雄","熊","熋","赨"],
               
            xiong_7  :[],

            #ㄒㄧㄡ
            xiu_space:["修","休","羞","咻","脩","貅","髹","鵂","庥",
                       "饈","俢","樇","滫","咻","烌","臹","茠","蓚",
                       "蓨","銝","鎀","鏅","馐","髤","鱃","鸺"],               
            xiu_3  :["宿","朽","滫","潃","糔","綇"],              
            xiu_4 :["秀","繡","袖","銹","鏽","琇","嗅","綉","岫",
                    "溴","玊","绣","臭","嘼","宿","殠","珛","璓",
                    "繍","臰","螑","褎","褏","鏥","锈","齅"],
               
            xiu_6  :[],
               
            xiu_7  :[],

            
            #ㄒㄩ
            xu_space:["需","須","虛","鬚","噓","墟","戌","胥","盱",
                       "吁","歔","嬬","鑐","倠","偦","呴","嘘","嬃",
                       "幁","揟","旴","晇","楈","欨","欰","殈","疞",
                      "稰","窢","竬","糈","縃","繻","蕦","虗","虚",
                      "蝑","褜","褝","訏","謣","譃","须","顼","驉",
                      "魖"],               
            xu_3  :["許","需","煦","昫","詡","喣","醑","俆","冔",
                    "咻","姁","浒","湑","珝","盨","糈","諝","许",
                    "诩","鄦"],              
            xu_4 :["續","旭","敘","序","緒","蓄","畜","絮","婿",
                    "恤","敍","酗","卹","壻","勖","頊","勗","慉",
                    "訹","漵","銊","怴","伵","侐","叙","嘼","垿",
                   "旮","昫","槒","殈","汿","沀","洫","潊","烅",
                   "獝","珬","盢","瞁","瞲","稸","窢","緖","绪",
                   "续","聟","肷","芧","藇","藚","賉","馘","魆",
                   "鱮"],
               
            xu_6  :["徐","余","蒣"],
               
            xu_7  :["逧"],



            #ㄒㄩㄢ
            xuan_space:["宣","軒","萱","瑄","煊","暄","喧","暖","媗",
                       "諠","愃","亘","佡","儇","吅","喛","塤","壎",
                        "嬛","弲","愋","懁","揎","昍","晅","暅","梋",
                        "煖","睻","矎","禤","箮","翧","翾","萲","蕿",
                        "藼","蘐","蠉","蝖","諼","譞","谖","轩","鋗",
                        "鍹","駽","鶱"],               
            xuan_3  :["選","烜","咺","癣","选"],              
            xuan_4 :["炫","鉉","眩","渲","絢","楦","泫","旋","鏇",
                    "眴","怰","敻","昡","楥","漩","琄","縼","繏",
                    "绚","蔙","衒","袨","讂","贙","铉","镟","鞙",
                   "駽"],
               
            xuan_6  :["懸","玄","璇","旋","玆","璿","漩","琁","伭",
                      "妶","嫙","悬","暶","檈","玹","盷","睘","琁",
                      "蜁","誸","還"],
               
            xuan_7  :[],


            #ㄒㄩㄝ
            xue_space:["薛","靴","噱","嶨","吙","辥","鞾"],               
            xue_3  :["雪","鱈","襅","鳕"],              
            xue_4 :["穴","削","雪","吷","坹","岤","桖","泬","狘",
                    "血","袕","謞","谑","趐"],
               
            xue_6  :["學","踅","鷽","壆","燢","乴","嶨","斅","斈",
                      "泶","澩","穴","褶","觷","雤"],
               
            xue_7  :[],


            #ㄒㄩㄣ
            xun_space:["勳","薰","勛","燻","熏","壎","醺","塤","焄",
                       "曛","勋","勲","坃","埙","壦","姰","峋","獯",
                       "矄","纁","臐","荤","葷","蔒","薫","蘍","襇"],               
            xun_3  :[],              
            xun_4 :["訊","訓","遜","汛","迅","巽","蕈","殉","侚",
                    "噀","巺","徇","潠","爋","訙","训","讯","賐",
                    "迿","逊","鑂","韗","顨","馴","鵔","鵕"],
               
            xun_6  :["巡","尋","循","詢","旬","蟳","馴","鱘","洵",
                      "珣","荀","恂","郇","潯","峋","蕁", "旬","枔", 
                     "峋","徇","鱘","伨","偱","咰","噚","寻","廵",
                     "撏","攳","杊","栒","槆","橁","毥","浔","燅",
                     "燖","狥","璕","璿","畃","紃","询","毥","駨",
                     "驯","鱏","鱾","狥","鲟"],
             
            xun_7  :[],

            #ㄧㄚ
            ya_space:["壓","押","鴨","呀","鴉","丫","椏","啞","劜",
                       "哑","唖","垭","孲","庘","曱","桠","煆","襕",
                       "雅","鵶","鸦","鸭"],               
            ya_3  :["雅","亞","啞","氬","雃","亚","厊","哑","唖",
                        "庌","掗","疋","痖","瘂","蕥"],
            ya_4 :["亞","訝","婭","迓","軋","揠","砑","亚","亜",
                    "俹","呀","圠","娅","掗","氩","氬","猰","玡",
                    "稏","窫","聐","襕","襾","讶","轧","錏","鐚",
                   "閕","鼼","齾"],
               
            ya_6  :["牙","芽","涯","衙","枒","犽","蚜","伢","厓",
                      "呀","堐","押","漄","猚","疨","笌","齖"],
             
            ya_7  :["呀"],

            #ㄧㄢ
            yan_space:["菸","燕","煙","淹","焉","醃","咽","閹","嫣",
                       "奄","烟","湮","鄢","蔫","珚","胭","堙","懨",
                       "厭","崦","殷","偣","嬮","恹","懕","漹","猒",
                       "硽","篶","腌","臙","襨","覀","酀","閼","阉",
                       "阏","黫"],               
            yan_3  :["眼","演","衍","掩","琰","儼","棪","偃","魘",
                     "渰","甗","龑","椼","鼴","乵","俨","兗","兖",
                     "剡","匽","厣","厴","噞","埯","夵","奄","姶",
                     "嬐","嬿","屵","嵃","嶖","巘","巚","广","弇",
                     "檿","惔","戭","扊","抁","揜","擪","晻","曮",
                     "躽","遃","郾","酓","铻","锧","隒","馣","魇",
                     "鰋","鶠","黤","黭","黶","鼹","齞","齴"],
            yan_4 :["驗","彥","燕","宴","艷","豔","堰","晏","雁",
                    "諺","焰","嚥","讞","厭","硯","燄","嬿","焱",
                    "唁","贋","灩","饜","讌","贗","牪","筵","姲",
                   "掞","鷰","俺","偐","傿","厌","咽","喭","噞",
                   "囐","墕","妟","婩","嬊","嵃","彦","懕","懨",
                    "敥","暥","曕","曣","婩","沿","淹","滟","灔",
                    "灧","烻","熌","爓","猒","研","砚","艶","莚",
                    "襷","覀","覎","觾","谚","谳","豓","豣","赝",
                    "酀","酽","醶","醼","釅","閆","隁","餍","騐",
                    "騴","驠","验","鬳","鰋","鳫","鴈","鴳","鷃",
                    "鹽"],
               
            yan_6  :["言","顏","嚴","沿","鹽","延","炎","研","癌",
                     "岩","巖","妍","閻","簷","筵","閆","檐","蜒",
                     "閰","埏","喦","郔","莚","严","厃","厈","厳",
                     "塩","壛","壧","姸","娮","孍","嵒","嵓","巌",
                     "巗","开","揅","昖","楌","櫩","狿","琂","盐",
                     "硏","碞","礹","綖","蔅","虤","襷","詽","鈆",
                     "鉛","鋋","铅","闫","阎","顃","顔","颜","鳽",   
                     "麙","麣"],
             
            yan_7  :[],
            

            #ㄧㄤ
            yang_space:["央","秧","鴦","殃","泱","胦","姎","佒","咉",
                       "坱","柍","楧","眏","紻","鉠","雵","鞅","鸯"],               
            yang_3  :["養","氧","仰","癢","痒","傟","养","勜","卬",
                     "坱","岟","慃","懩","抰","攁","氱","炴","蝆",
                     "詇","軮","鞅"],
            yang_4 :["樣","漾","恙","怏","様","瀁","煬","羕","詇",
                    "養"],
               
            yang_6  :["銀","吟","寅","淫","垠","鄞","狺","齦","崟",
                     "夤","霪","檭","釿","齗","冘","凐","噖","嚚",
                     "圁","垦","婬","斦","檐","殥","泿","滛","烎",
                     "犾","璌","碒","苂","荶","蔩","蟫","訔","訡",
                     "鶍","鸉"],
             
            yang_7  :[],

            #ㄧㄠ
            yao_space:["邀","腰","要","么","妖","喲","夭","吆","祅",
                       "哟","喓","枖","楆","狕","约","芺","葽","訞",
                       "鴁"],               
            yao_3  :["咬","邀","要","穾","杳","榚","窅","仸","偠",
                     "夭","婹","嫍","窈","宎","崾","抭","殀","溔",
                     "眑","窔","苭","蓔","闄","騕","鴢","鷕","齩"],
            yao_4 :["要","藥","耀","曜","躍","鑰","燿","葯","鷂",
                    "筄","樂","拗","熎","牰","獟","疟","矅","穾",
                    "窰","艞","药","薬","袎","覞","讑","趭","钥",
                    "靿","鼼"],
               
            yao_6  :["姚","窯","搖","瑤","堯","遙","肴","謠","餚",
                     "垚","爻","淆","媱","洮","堯","嶢","笅","銚",
                     "徭","繇","颻","鰩","侥","倄","僥","嗂","壵",
                     "尧","崤","嶤","幺","愮","摇","摿","暚","柼",
                     "榣","殽","烑","猇","猺","珧","瑶","窑","窕",
                     "蘨","蛍","訤","谣","軺","轺","遥","鎐","铫",
                     "陶","靔","顤","餆","鳐"],
             
            yao_7  :["哟"],



            #ㄧㄝ
            ye_space:["耶","噎","峫","曅","潱","蠮"],               
            ye_3  :["也","野","冶","埜","壄","漜"],
            ye_4 :["葉","業","夜","頁","液","燁","謁","曄","腋",
                    "拽","靨","咽","饁","嶪","瞱","业","亱","偞",
                    "僷","哗","嚈","墷","射","嶫","弽","抴","擛",
                    "擫","晔","曗","枼","枽","楪","殗","殜","澲",
                    "烨","煠","爗","牃","皣","瞸","礏","谒","邺",
                   "鄴","鍱","鎑","鐷","靥","页","餣","驜","鵺",
                   "鸈","黦"],
               
            ye_6  :["椰","爺","揶","捓","擨","斜","歋","爷","琊",
                     "瑘","耶","裄","邪","釾","鋣","鎁","铘"],
             
            ye_7  :["哟"],

            #ㄧ
            yi_space:["一","依","醫","伊","衣","禕","ㄧ","壹","漪",
                      "咿","揖","銥","繄","黟","噫","吚","圪","壱",
                      "夁","嫛","嬄","嶬","弌","旑","曀","椅","檹",
                      "欹","毉","泆","洢","溰","燚","猗","瑿","稦",
                      "蛜","觃","觍","訲","郼","鎄","铱","陭","鷖",
                      "黳"],               
            yi_3  :["以","已","乙","椅","蟻","矣","倚","苡","顗",
                    "旖","尾","扡","釔","礒","鉯","檥","佁","偯",
                    "吕","崺","嶬","庡","扆","掜","攺","晲","笖",
                    "肔","胣","舣","艤","苢","蚁","螘","裿","踦",
                    "輢","轙","迆","迤","逘","酏","鈘","鎄","钇",
                    "阤","陭","鳦","齮"],
            yi_4 :["一","億","義","亦","意","益","易","疫","藝",
                    "議","異","毅","役","憶","逸","溢","奕","裔",
                   "譯","翼","翊","懿","誼","邑","弈","抑","鎰",
                    "驛","俋","羿","熠","薏","刈","佾","挹","翌",
                    "曳","液","詣","繹","臆","埸","掖","佚","屹",
                   "翳","軼","杙","釴","弋","浥","鐿","晹","嶧",
                   "縊","蜴","謚","藙","懌","埶","囈","悒","玴",
                   "肄","蓺","枻","鶂","仡","墿","泄","洩","澺",
                   "瘞","繶","腋","乂","义","亄","亿","伇","伿",
                   "劓","劮","勩","医","呓","呹","唈","嗌","噫",
                   "圛","垼","嫕","嬑","嬟","寱","射","峄","帟",
                   "帠","幆","廙","异","忆","忔","怈","怿","悘",
                   "悥","抴","捙","撎","敡","斁","施","昳","曀",
                   "曎","曵","枍","栧","棭","槷","槸","檍","欭",
                   "殔","殪","殹","泆","洂","浂","浳","湙","潩",
                   "瀷","炈","焲","熤","熼","燡","燱","痬","瘗",
                   "瘱", "癔","睪","瞖","秇","穓","緆","绎","缢",
                   "羛","肊","膉","艗","艺","艾","芅","蘙","蛡",
                   "螠","衣","袣","裛","褹","訁","襼","詄","詍",
                   "譩","讛","议","译","诣","谊","豙","豛","豷",
                   "跇","転","轶","醳","醷","鈠","镒","镱","阝",
                   "阣","隿","霬","鷁","靾","食","饐","驿","骮",
                   "鯣","鳦","鴩","鷁","鷊","鷧","鷾","黓","齸"],
               
            yi_6  :["一","宜","移","怡","疑","儀","遺","誼","夷",
                     "沂","姨","頤","彝","貽","羡","飴","胰","詒",
                    "圯","咦","荑","迤","衪","迻","眙","痍","宧",
                    "萓","簃","珆","蛇","迆","訑","乁","仪","侇",
                    "冝","凒","匜","台","呲","宐","寲","峓","嶷",
                    "巸","弬","彛","恞","扅","暆","杝","枱","柂",
                    "狋","栘","桋","椸","歋","沵","沶","泤","洟",
                    "熪","瓵","眤","眱","竩","笫","箷","羠","苐",
                    "蛦","跠","螔","袘","袲","觺","謻","讉","诒",
                    "貤","贻","迱","遗","酏","鈶","鉹","銕","頉",
                    "頥","顊","颐","饴","鮧","鴺","鸃"],
             
            yi_7  :[],


            #ㄧㄣ
            yin_space:["因","音","殷","陰","茵","瘖","姻","韾","氤",
                      "湮","喑","慇","銦","愔","絪","侌","凐","噾",
                      "囙","垔","堙","婣","摿","栶","欭","歅","洇",
                     "洕","溵","磤","禋","秵","筃","緸","荫","蒑",
                      "裀","铟","諲","闉","阥","阴","陻","隂","隌",
                      "霒","霠","鞇","韽","駰","黫"],               
            yin_3  :["引","尹","飲","癮","隱","蚓","乚","听","嶾",
                    "廴","戭","檃","檼","櫽","殷","淾","濥","濦",
                    "瘾","磤","粌","紖","縯","蘟","螾","訚","讔",
                    "趛","鈏","隐","隠","靷","饮","馻"],
            yin_4 :["印","蔭","胤","廕","窨","乚","廕","堷","币",
                    "慭","憖","憗","朄","湚","猌","癊","茚","荫",
                    "訚","酳","阥","隱","飲","饮","鮣"],
               
            yin_6  :["龈","銀","寅","淫","垠","鄞","狺","齦","崟",
                     "夤","霪","檭","釿","齗","冘","凐","噖","嚚",
                    "圁","垦","婬","斦","檐","殥","泿","滛","烎",
                    "犾","璌","碒","苂","荶","蔩","蟫","訔","訡",
                    "誾","鈝","鏔","银","鷣","龈"],
             
            yin_7  :[],

            #ㄧㄥ
            ying_space:["應","英","鷹","嬰","櫻","瑛","鶯","瓔","纓",
                      "膺","霙","鸚","媖","嫈","嚶","攖","煐","韺",
                      "罌","偀","蠳","罃","嘤","噟","婴","孆","孾",
                     "应","応","撄","朠","樱","渶","瀴","璎","甇",
                      "甖","碤","礯","缨","罂","莺","蘡","蝧","褮",
                      "譻","鍈","鑍","铓","霒","鶧","鷪","鸎","鹦",
                      "鹰" ],               
            ying_3  :["影","穎","癭","潁","郢","巊","景","梬","浧",
                    "瀴","璄","瘿","矨","鐛","頴","颍","颖"],
            ying_4 :["應","硬","映","媵","应","摬","暎","濙","瀅",
                    "訳","譍","賏","鎣","鞕"],
               
            ying_6  :["營","贏","盈","迎","瑩","瀛","螢","瀅","蠅",
                     "濚","縈","熒","楹","嬴","塋","滎","瀠","僌",
                    "営","巆","廮","攍","櫿","滢","瀯","盁","籝",
                    "籯","耺","茔","荥","荧","萤","营","萦","萾",
                    "蓥","藀","蝇","褮","覮","謍","赢","闬"],
             
            ying_7  :[],

            #ㄧㄛ
            yo_space:["唷"],               
            yo_3  :[],
            yo_4 :[],               
            yo_6  :[],             
            yo_7  :[],

            #ㄩㄥ
            yo_space: ["傭","庸","鏞","雍","墉","蕹","壅","慵","癰",
                      "邕","佣","噰","臃","饔","嗈","廱","拥","擁",
                      "滽","澭","灉","牅","痈","癕","躻","郺","鄘",
                      "镛","雝","鳙","鷛"],               
            yo_3  :   ["永","勇","泳","湧","擁","詠","蛹","俑","踴",
                      "涌","甬","踊","咏","恿","埇","傛","勈","塎",
                      "壅","彮","悀","惥","愑","愹","慂","搈","柡",
                      "硧","禜","臃","銢"],
            yo_4 :["用","佣","禜","苚","醟"],               
            yo_6  :["嫆","喁","傛","傭","嫞","嬫","嵱","槦","牅",
                    "銿","顒"],             
            yo_7  :[],

            #ㄩㄥ
            yong_space: ["傭","庸","鏞","雍","墉","蕹","壅","慵","癰",
                      "邕","佣","噰","臃","饔","嗈","廱","拥","擁",
                      "滽","澭","灉","牅","痈","癕","躻","郺","鄘",
                      "镛","雝","鳙","鷛"],               
            yong_3  :   ["永","勇","泳","湧","擁","詠","蛹","俑","踴",
                      "涌","甬","踊","咏","恿","埇","傛","勈","塎",
                      "壅","彮","悀","惥","愑","愹","慂","搈","柡",
                      "硧","禜","臃","銢"],
            yong_4 :["用","佣","禜","苚","醟"],               
            yong_6  :["嫆","喁","傛","傭","嫞","嬫","嵱","槦","牅",
                    "銿","顒"],             
            yong_7  :[],

            #ㄧㄡ
            you_space: ["優","悠","憂","幽","攸","呦","优","蚴","懮",
                        "喲","纋","嚘","妋","怮","櫌","瀀","耰","鄾",
                        "麀"],               
            you_3  :   ["有","友","酉","黝","銪","槱","岰","牖","丣",
                        "卣","媨","峳","庮","懮","栯","梄","泑","湵",
                        "禉","羐","羑","苃","聈","蚴","蜏","莠","铕"],
            you_4 :["又","右","幼","佑","柚","祐","誘","釉","囿",
                    "宥","鈾","侑","莠","鼬","峟","姷","亴","卣",
                    "叹","唀","喲","忧","扰","有","牰","狖","蜏",
                    "褎","诱","貁","迶","酭","鴢"],               
            you_6  :["由","游","遊","油","尤","猶","郵","猷","魷",
                     "疣","逌","莤","秞","楢","斿","訧","鮋","优",
                     "偤","囮","怣","櫾","沋","浟","滺","犹","繇",
                     "肬","莸","蕕","蚰","蝣","輏","輶","逰","邎",
                     "邮","鈾","醔","铀","鞧","駀","鱿"],             
            you_7  :[],


            #ㄩ
            yu_space: ["淤","瘀","迂","ㄩ","紆","箊","扜","扝","毹",
                        "盓","穻","纡","虶","迃","騟"],               
            yu_3  :   ["有","友","酉","黝","銪","槱","岰","牖","丣",
                        "卣","媨","峳","庮","懮","栯","梄","泑","湵",
                        "禉","羐","羑","苃","聈","蚴","蜏","莠","铕"],
            yu_4 :["又","右","幼","佑","柚","祐","誘","釉","囿",
                    "宥","鈾","侑","莠","鼬","峟","姷","亴","卣",
                    "叹","唀","喲","忧","扰","有","牰","狖","蜏",
                    "褎","诱","貁","迶","酭","鴢"],               
            yu_6  :["由","游","遊","油","尤","猶","郵","猷","魷",
                     "疣","逌","莤","秞","楢","斿","訧","鮋","优",
                     "偤","囮","怣","櫾","沋","浟","滺","犹","繇",
                     "肬","莸","蕕","蚰","蝣","輏","輶","逰","邎",
                     "邮","鈾","醔","铀","鞧","駀","鱿"],             
            yu_7  :[],

            #ㄩㄢ
            yuan_space: ["淵","冤","鳶","鴛","灁","肙","剈","囦","嬽",
                        "宛","寃","惌","棩","渁","渆","蒝","眢","葾",
                        "蒬","蜎","蜵","裫","裷","鋺","駌","鵷","鸢",
                         "鸳","鼘","鼝"],               
            yuan_3  :   ["遠","妴","盶","逺","齳"],
            yuan_4 :["院","願","苑","怨","愿","瑗","遠","傆","厡",
                    "噮","夗","夘","媛","掾","禐","衏","褑","褤",
                    "謜","逺","镚"],               
            yuan_6  :["元","原","員","園","源","圓","援","緣","袁",
                     "媛","垣","沅","猿","爰","芫","蒝","轅","櫞",
                     "湲","嫄","榞","騵","溒","蝝","螈","円","厡",
                     "员","园","圆","圎","圜","妧","媴","暅","杬",
                     "榬","橼","猨","猭"",獂","笎","縁","缘","羱",
                     "萲","薗","蚖","蝯","貟","蝯","辕","邍","邧",
                     "鎱","魭","鱛","鶢","鶰","黿","鼋"],             
            yuan_7  :[],



            #ㄩㄝ
            yue_space: ["約","曰","噦","岄","焥","箹","约"],               
            yue_3  :   [],
            yue_4 :["月","越","樂","岳","閱","悅","躍","玥","嶽",
                    "粵","鉞","樾","趯","刖","乐","兌","哾","妜",
                    "恱","悦","戉","抈","捳","敫","曜","枂","栎",
                    "楽","櫟","泧","瀹","爚","狘","礿","禴","篗",
                    "籆","籥","籰","粤","耀","藥","蘥","蘔","蚎",
                    "蚏","說","说","跀","跃","軏","鈅","鑰","钥",
                    "钺","閲","阅","鸑","鸙","龠","龥"],               
            yue_6  :[],             
            yue_7  :[],


            #ㄩㄣ
            yun_space: ["傭","庸","鏞","雍","墉","蕹","壅","晕","氲",
                        "渁","渆","渊","蒀","蒕","蝹","輼"],               
            yun_3  :   ["允","殞","隕","鈗","傊","喗","愪","抎","揾",
                        "殒","渷","狁","玧","磒","荺","褞","賱","輑",
                        "运","阭","陥","陨","霣","馻"],
            yun_4 :["運","韻","孕","蘊","韞","熨","醞","慍","韵",
                    "惲","暈","员","員","夽","媪","忶","恽","愠",
                    "晕","枟","榲","煴","煾","熅","緷","緼","縕",
                    "腪","蕰","蕴","薀","藴","运","郓","鄆","酝",
                    "醖","鞰","韗","韫","餫","鶤"],               
            yun_6  :["雲","芸","云","筠","勻","耘","昀","澐","妘",
                     "畇","沄","紜","蕓","鋆","橒","鄖","荺","伝",
                     "匀","员","員","囩","枃","溳","熅","熉","眃",
                     "秐","篔","縜","纭","耺","蒷","読","誮","郧"],             
            yun_7  :[],


            #ㄗㄚ
            za_space: ["紮","匝","咂","唼","嘁","帀","抸","沞","迊",
                        "鉔","魳"],               
            za_3  :   ["鮺"],
            za_4 :[],               
            za_6  :["砸","雜","咱","偺","囐","磼","襍","雑","雥",
                     "韴"],             
            za_7  :[],

            #ㄗㄞ
            zai_space: ["災","栽","哉","渽","灾","烖","睵","葘","賳"],               
            zai_3  :   ["載","仔","宰","崽","儎","縡","载"],
            zai_4 :["在","再","載","饡","儎","扗","洅","縡","载",
                    "酨"],               
            zai_6  :[],             
            zai_7  :[],

            #ㄗㄢ
            zan_space: ["簪","兂","簮","鐕"],               
            zan_3  :   ["攢","昝","儹","礸","儧","喒","噆","寁","拶"
                        "揝","撍","攒","沯","禶","趱","趲"],
            zan_4 :["讚","贊","瓚","暫","欑","鏨","囋","暂","濽",
                    "灒","瓉","瓒","襸","覱","讃","賛","赞","趲",
                    "鄼","酇","錾","饡"],               
            zan_6  :["咱","偺","糌"],             
            zan_7  :[],

            #ㄗㄤ
            zang_space: ["簪","兂","簮","鐕"],               
            zang_3  :   ["攢","昝","儹","礸","儧","喒","噆","寁","拶"
                        "揝","撍","攒","沯","禶","趱","趲"],
            zang_4 :["讚","贊","瓚","暫","欑","鏨","囋","暂","濽",
                    "灒","瓉","瓒","襸","覱","讃","賛","赞","趲",
                    "鄼","酇","錾","饡"],               
            zang_6  :[],             
            zang_7  :[],

            #ㄗㄤ
            zao_space: ["遭","糟","蹧","慒","傮","醩"],               
            zao_3  :   ["早","棗","澡","藻","蚤","璪","枣","繰","缲"
                        "薻"],
            zao_4 :["造","灶","躁","皂","燥","噪","譟","唕","唣",
                    "喿","慥","梎","皁","矂","竈","簉","艁","趮",
                    "髞"],               
            zao_6  :["鑿","凿"],             
            zao_7  :[],

            #ㄗㄜ
            ze_space: [],               
            ze_3  :   ["怎"],
            ze_4 :["仄","昃","稄","庂","侧","側","唶","夨","崱",
                    "昗","歵","汄"],               
            ze_6  :["則","澤","責","擇","嘖","謮","咋","柞","賊",
                    "则","啧","岞","崱","帻","幘","戝","択","择",
                    "泽","溭","皟","瞔","矠","笮","窄","箦","簀",
                    "耫","舴","萴","蠈","蠌","襗","諎","賾","责",
                    "赜","迮","鱡","鰂","齰"],             
            ze_7  :[],


            #ㄗㄟ
            zei_space: [],               
            zei_3  :   [],
            zei_4 :[],               
            zei_6  :["賊","戝","蠈","贼"],             
            zei_7  :[],

            #ㄗㄣ
            zen_space: ["兂"],               
            zen_3  :   ["怎","諚"],
            zen_4 :["譖","谮"],               
            zen_6  :[],             
            zen_7  :[],

            #ㄗㄥ
            zeng_space: ["曾","增","憎","繒","罾","璔","磳","増","橧",
                        "熷","矰","缯","譄","驓"],               
            zeng_3  :   [],
            zeng_4 :["贈","甑","缯","赠","锃"],                
            zeng_6  :[],             
            zeng_7  :[],

            #ㄓㄚ
            zha_space: ["渣","扎","喳","楂","抯","偧","奓","挓","揸",
                        "摣","柤","查","樝","皻","觰","謯","譇","齄",
                        "齇"],               
            zha_3  :   ["眨","扠","鮓","厏","渣","砟","苲","踷"],
            zha_4 :["詐","炸","榨","乍","搾","柵","咤","搾","蚱",
                    "醡","咋","宱","咋","溠","灹","痄","砟","簎",
                    "膪","蜡","诈","鮓"],                
            zha_6  :["炸","札","紮","扎","閘","鍘","劄","鍘","哳","煠",
                     "牐","紥","蚻","蠿","譗","轧","铡","闸","铡","霅"],             
            zha_7  :[],

            #ㄓㄞ
            zhai_space: ["摘","齋","侧","夈","捚","斊","斋","斎","棏",
                        "榸","齊"],               
            zhai_3  :   ["窄","岝","鉙"],
            zhai_4 :["債","寨","债","瘵","砦","祭","責"],                
            zhai_6  :["宅","翟","择"],             
            zhai_7  :[],

            #ㄓㄢ
            zhan_space: ["詹","沾","瞻","霑","氈","譫","譠","占","覘",
                        "薝","詹","呫","厃","嶦","惉","旃","旜","栴",
                         "毡","氊","粘","蛅","詀","讝","谵","趈","邅",
                         "鉆","饘","驙","鱣","鸇"],               
            zhan_3  :   ["展","盞","斬","嶄","輾","嫸","崭","嶃","搌",
                         "斩","榐","樿","橏","琖","皽","盏","蹍","辗",
                         "醆","颭","魙"],
            zhan_4 :["站","戰","佔","占","暫","棧","湛","顫","綻",
                     "蘸","偡","嶘","战","戦","栈","碊","绽","菚",
                     "虥","虦","襢","蹔","輚","轏","颤","驏"],                
            zhan_6  :[],             
            zhan_7  :[],

            #ㄓㄤ
            zhang_space: ["張","章","彰","璋","樟","漳","蟑","傽","獐",
                        "鱆","暲","墇","嫜","张","弡","慞","粻","蔁",
                         "遧","鄣","餦","騿","麞"],               
            zhang_3  :   ["長","漲","掌","仉","仧","兏","涨","镸","长",
                         "鞝"],
            zhang_4 :["障","帳","仗","脹","丈","杖","賬","瘴","嶂",
                     "扙","幛","漲","兏","帐","涨","涱","痮","瘬",
                     "瞕","粀","胀","账","長","镸"],                
            zhang_6  :[],             
            zhang_7  :[],


            #ㄓㄠ
            zhao_space: ["朝","招","昭","召","釗","著","嘲","妱","晁",
                        "盄","着","窼","鉊","鍣","钊","駋"],               
            zhao_3  :   ["找","沼","爪","爫","瑵","菬"],
            zhao_4 :["照","趙","兆","罩","肇","詔","召","炤","棹",
                     "垗","旐","晁","曌","枛","櫂","燳","狣","瞾",
                     "笊","箌","肁","肈","诏","赵","跶","雿","鮡",
                     "鵫"],                
            zhao_6  :["著","着"],             
            zhao_7  :[],


            #ㄓㄜ
            zhe_space: [],               
            zhe_3  :   ["者","赭","鍺","堵","锗","褶"],
            zhe_4 :["這","蔗","浙","宅","柘","檡","淛","烢","礋",
                     "蟅","这","鷓","鹧"],                
            zhe_6  :["哲","折","輒","摺","喆","褶","懾","謫","晢",
                     "蜇","摘","轍","乇","厇","啠","嚞","埑","悊",
                     "慴","樀","檡","歽","瓋","砓","磔","籷","耴",
                     "虴","蛰","襵","謺","讁","讋","讘","谪","輙",
                     "辄","辙","適","銸","馲","驝","鮿","鸅"],             
            zhe_7  :["著","嫬","晢","着","遮"],

            #ㄓㄣ
            zhen_space: ["真","嗔","瞋","謓","偵","針","禎","臻","椹",
                         "楨","蓁","溱","砧","箴","榛","媜","斟","禛",
                         "湞","胗","鱵","鍼","侦","儬","唇","堻","嫃",
                         "寊","帪","揁","搸","昣","栕","桢","桭","樼",
                         "浈","潧","獉","珎","瑊","眞","碪","祯","籈",
                         "葴","蒖","蒧","薽","診","贞","轃","遉","酙",
                         "鉁","錱","针","闿","靕","駗","鷏"],               
            zhen_3  :   ["診","疹","枕","軫","畛","縝","稹","姫","屒",
                         "弫","抌","疹","軫","畛","眕","祳","笉","紾",
                         "絼","縥","缜","縥","袗","裖","覙","诊","轸",
                         "辴","飻","鬒","黕","黰"],
            zhen_4 :["鎮","振","震","陣","賑","朕","鴆","敶","侲",
                     "塦","娠","挋","揕","兏","涨","涱","痮","瘬",
                     "瞕","粀","胀","账","長","镸"],                
            zhen_6  :[],             
            zhen_7  :[],

            #ㄓㄥ
            zheng_space: ["爭","徵","蒸","睜","征","掙","箏","錚","鉦",
                         "癥","崢","諍","姃","正","烝","猙","怔","丁",
                         "争","佂","埩","崝","徰","徴","挣","炡","狰",
                         "眐","筝","睁","篜","聇","脀","鏳","钲","铮",
                         "鬇","鲘","鲭","鴊"],               
            zheng_3  :   ["整","氶","拯","愸","撜","糽"],
            zheng_4 :["正","政","鄭","證","症","証","幀","掙","帧",
                     "挣","证","诤","郑","鋥","铮"],                
            zheng_6  :[],             
            zheng_7  :[],

            #ㄓ
            zhi_space: ["之","隻","支","知","枝","汁","織","芝","肢",
                         "脂","祗","吱","蜘","梔","胝","衼","ㄓ","卮",
                         "只","倁","坧","巵","掷","搘","枳","栀","椥",
                         "榰","氏","汥","泜","疧","疷","祇","祬","秓",
                         "秖","秪","织","胑","跖","馶","鳷","鴟","鴲",
                        "鵄","鼅"],               
            zhi_3  :   ["只","指","紙","止","址","旨","芷","織","肢",
                        "酯","祉","枳","咫","阯","黹","晊","藢","劧",
                        "厎","坁","夂","帋","徵","恉","抧","栺","汦",
                        "沚","淽","滍","疻","砋","祇","纸","茋","襧",
                        "訨","軹","轵"],
            zhi_4 :["至","志","致","智","治","制","製","置","誌",
                     "緻","滯","雉","痣","稚","秩","炙","鋕","幟",
                    "郅","峙","痔","窒","輊","桎","質","躓","蛭",
                    "帙","銍","陟","知","騭","鴙","騭","忮","歭",
                    "娡","膣","豸","跱","偫","劕","厔","垁","妷",
                    "徝","恎","懥","懫","挃","挚","搱","旘","晊",
                    "栉","櫍","洔","洷","淛","滍","滞","熫","狾",
                    "猘","疐","礩","祑","秲","稺","穉","筫","紩",
                    "綕","翐","胵","臷","臸","芖","螲","袟","袠",
                    "覟","觗","觢","觯","觶","識","譲","识","豑",
                    "贄","质","贽","踬","轾","迣","遰","遲","鑕",
                    "阤","隲","饢","駤","騺","驇","骘","鯯","鴩",
                    "鷙","鸷"],                
            zhi_6  :["直","職","值","質","植","執","擲","殖","侄",
                     "姪","蟄","蹠","埴","摭","稙","躑","慹","跖",
                     "値","儨","嬂","懫","戠","执","挃","掷","擿",
                     "柣","桎","樴","漐","犆","瓆","瓡","礩","禃",
                     "秷","絷","縶","聀","职","膱","蘵","蟙","褁",
                     "譛","貭","踯","蹢","躓","軄","釞","馽","鰚",
                     ],             
            zhi_7  :[],

            #ㄓㄨㄥ
            zhong_space: ["中","忠","鐘","鍾","終","盅","衷","螽","忪",
                         "柊","煄","伀","刣","喠","妐","彸","汷","泈",
                         "潀","炂","籦","终","舯","蔠","衳","蹱","钟",
                         "锺","鴤","鼨"],               
            zhong_3  :   ["種","腫","塚","踵","冢","歱","瘇","肿"],
            zhong_4 :["種","重","眾","仲","中","乑","偅","堹","妕",
                     "媑","尰","湩","潨","狆","祌","筗","緟","茽",
                    "衆","衶","褈","諥"],                
            zhong_6  :[
                     ],             
            zhong_7  :[],

            #ㄓㄡ
            zhou_space: ["周","州","洲","週","舟","粥","珘","淍","啁",
                         "銂","賙","輈","輖","侜","喌","粥","婤","徟",
                         "洀","烐","盩","矪","譸","郮","霌","郮","騆",
                         "鵃"],               
            zhou_3  :   ["肘","帚","晭","疛","睭","箒","鯞"],
            zhou_4 :["咒","皺","宙","縐","晝","冑","紂","胄","咮",
                     "籀","伷","僽","呪","噣","怞","昼","甃","皱",
                    "籒","籕","粙","繇","纣","绉","荮","葤","詋",
                     "讏","轴","酎","駎"],                
            zhou_6  :["軸","妯","轴"
                     ],             
            zhou_7  :[],


            #ㄓㄨ
            zhu_space: ["朱","豬","珠","諸","株","茱","銖","蛛","櫫",
                         "洙","侏","誅","硃","瀦","藸","絑","劯","槠",
                         "橥","櫧","潴","猪","祩","蕏","蝫","藷","蠩",
                         "袾","觰","诛","诸","跦","蹽","馶","邾","铢","駯",
                        "鮢","鯺","鴸","鼄"],
                        
            zhu_3  :   ["帚","晭","疛","睭","箒","鯞"],
            zhu_4 :["咒","皺","宙","縐","晝","冑","紂","胄","咮",
                     "籀","伷","僽","呪","噣","怞","昼","甃","皱",
                    "籒","籕","粙","繇","纣","绉","荮","葤","詋",
                     "讏","轴","酎","駎"],                
            zhu_6  :["軸","妯","轴"
                     ],             
            zhu_7  :[],

            #ㄓㄨㄚ
            zhu_space: ["抓","挝","摣","撾","檛","簻","髽"],
                        
            zhu_3  :   ["爪","爫"],
            zhu_4  :[],                
            zhu_6  :[],             
            zhu_7  :[],


            #ㄓㄨㄞ
            zhuai_space: ["拽"],
                        
            zhuai_3    :   ["跩","转"],
            zhuai_4    :[],                
            zhuai_6    :[],             
            zhuai_7    :[],

            
            #ㄓㄨㄢ
            zhuan_space: ["專","磚","顓","嫥","膞","专","剸","劗","叀",
                          "塼","瑼","甎","砖","篿","耑","蟤","鄟","颛",
                          "鱄","鷒"],
                        
            zhuan_3    :   ["轉","囀","孨","转"],
            zhuan_4    :["傳","賺","饌","撰","篆","轉","縳","传","僎",
                         "啭","堟","灷","瑑","竱","籑","腞","蒃","襈",
                         "譔","赚","转","馔"],                
            zhuan_6    :[],             
            zhuan_7    :[],


            #ㄓㄨㄤ
            zhuang_space: ["裝","莊","樁","妝","庄","粧","梉","妆","娤",
                          "庒","桩","籹","糚","荘","装"],
                        
            zhuang_3    :   ["奘"],
            zhuang_4    :["撞","狀","壯","僮","壮","戆","戇","焋","状"],                
            zhuang_6    :[],             
            zhuang_7    :[],


            #ㄓㄨㄟ
            zhui_space: ["追","椎","錐","隹","騅","腄","锥","骓","鴭",
                         "鵻"], 
                        
            zhui_3    :   ["沝"],
            zhui_4    :["墜","綴","贅","惴","縋","餟","坠","娷","娺",
                        "甀","硾","礈","缀","缒","腏","膇","諈","赘",
                        "錣","鑆","隊"],                
            zhui_6    :[],             
            zhui_7    :[],

            #ㄓㄨㄣ
            zhui_space: ["諄","宒","屯","窀","衠","肫","訰","谆","迍"],
                        
            zhui_3    :   ["準","准","隼","鶽","凖","埻","綧"],
            zhui_4    :["稕","訰"],                
            zhui_6    :[],             
            zhui_7    :[],

            #ㄓㄨㄛ
            zhuo_space: ["桌","捉","涿","棹","穛","蠿"],
                        
            zhuo_3    :   [],
            zhuo_4    :[],                
            zhuo_6    :["卓","濁","酌","櫂","著","啄","倬","拙","斲",
                        "灼","禚","琢","茁","焯","擢","鐲","濯","斵",
                        "諑","圴","梲","鷟","啅","斫","丵","仢","剢",
                        "劅","勺","嚉","妰","彴","撯","擆","斀","斮",
                        "斱","晫","棁","棳","椓","槕","櫡","汋","泎",
                        "浊","浞","涿","灂","炪","烵","犳","琸","畷",
                        "硺","穛","篧","籗","籱","繳","缴","罬","蝃",
                        "蠗","謶","讱","诼","趠","踔","鉵","錣","鐯",
                        "镯"],             
            zhuo_7    :[],

            #ㄗ
            zi_space: ["資","茲","姿","滋","貲","諮","孜","咨","錙",
                       "孳","鎡","輜","髭","粢","淄","ㄗ","吱","孖",
                       "緇","觜","齜","仔","兹","姕","孶","崰","嵫",
                       "斊","氏","汥","泜","疧","疷","甾","禌","秶",
                       "稵","紎","缁","茊","菑","葘","薋","蠀","谘",
                       "豮","賫","賷","赀","资","趑","輺","辎","鄑",
                       "鈭","鍿","锱","頾","頿","鯑","鯔","鰦","鲻",
                       "鳂","鶅","鶿","鷀","鼒","齊","齍","龇"],
                        
            zi_3    :   ["子","仔","紫","籽","梓","秭","笫","訾","芓",
                         "滓","姊","吇","呰","啙","杍","榟","矷","秄",
                         "耔","胏","茈","茡","虸","訿","釨","饦"],
            zi_4    :["自","字","漬","恣","眥","牸","事","倳","剚",
                      "孳","扻","渍","眦","胔","胾","芓","髊"],                
            zi_6    :[],             
            zi_7    :["子"],


            #ㄗㄨㄥ
            zong_space: ["宗","蹤","棕","綜","縱","鬃","倧","鯮","踪",
                       "騣","嵏","嵕","嵷","嵸","從","惾","朡","椶",
                       "樅","熧","猣","磫","稯","緃","緵","繌","综",
                       "翪","腙","艐","苁","葼","蝬","豵","踨","鍐",
                       "騌","鬉","鬷","鯼"],
                        
            zong_3    :   ["總","傯","熜","偬","总","愡","憁","捴","揔",
                         "摠","朡","縂","蓗"],
            zong_4    :["粽","綜","縱","從","倊","昮","猔","瘲","糉",
                      "纵","综","苁"],                
            zong_6    :[],             
            zong_7    :[],

            #ㄗㄡ
            zou_space: ["鄒","諏","謅","陬","啁","媰","掫","棷","棸",
                       "箃","緅","菆","诌","诹","邹","郰","鄹","騶",
                       "驺","鯫","鲝","鲰","黀","齱","齺"],
                        
            zou_3    :   ["走","赱"],
            zou_4    :["奏","驟","揍","骤"],                
            zou_6    :[],             
            zou_7    :[],


            #ㄗㄨ
            zu_space: ["租","蒩"],
                        
            zu_3    :   ["租","蒩","阻","俎","詛","爼","珇","组","謯",
                         "祖","诅","靻"],
            zu_4    :["駔"],                
            zu_6    :["族","足","卒","鏃","嗾","傶","卆","哫","崒",
                      "崪","捽","稡","踤","踿","鉃","镞","顇"],             
            zu_7    :[],

            #ㄗㄨㄢ
            zuan_space: ["鑽","躦","攅","躜","钻"],
                        
            zuan_3    :   ["纂","纘","儹","穳","籫","纉","缵","鑽"],
            zuan_4    :["鑽","攥","揝","櫕","賺","赚","鑚","钻","饡"],                
            zuan_6    :[],             
            zuan_7    :[],

            #ㄗㄨㄟ
            zui_space: ["羧","厜","堆","嶉","樶","穝","纗","脧","蟕"],
                        
            zui_3    :   ["嘴","噿","嶉","嶊","濢","璻","觜"],
            zui_4    :["最","罪","醉","蕞","冣","墬","嶵","晬","栬",
                       "檇","檌","祽","醉","辠","酔","酻","鋷","錊",],                
            zui_6    :[],             
            zui_7    :[],

            #ㄗㄨㄣ
            zun_space: ["尊","遵","鱒","樽","鐏","墫","壿","嶟","繜",
                        "罇","鳟","鷷"],
                        
            zun_3    :   ["撙","僔","噂","墫","譐"],
            zun_4    :["圳","俊","捘","銌","燇","鱒"],                
            zun_6    :[],             
            zun_7    :[],

            #ㄗㄨㄛ
            zuo_space: ["嘬"],
                        
            zuo_3    :   ["左","佐","毑","繓"],
            zuo_4    :["做","作","座","坐","祚","酢","怍","侳","凿",
                       "夎","柞","糳","胙","葃","葄","袏","鑿","阼"],                
            zuo_6    :["昨","作","岝","椊","砟","秨","稓","筰","苲",
                       "莋","葃","鈼","飵"],             
            zuo_7    :[],
            })

def main():
    
    keys = bopomofoDict.keys()
    values = bopomofoDict.values()
    import sqlite3
    from PySide6.QtCore import QByteArray, QDataStream, QIODevice
    import os
    BASEDIR = os.path.join(os.getcwd(), "bopomofo.sqlite3")
    with sqlite3.connect(BASEDIR) as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS BOPOMOFO")        
        cur.execute("CREATE TABLE IF NOT EXISTS BOPOMOFO (NAME TEXT, DATA BLOB)")        
        
        for key, value in bopomofoDict.items():
            qb = QByteArray()
            out = QDataStream(qb, QIODevice.WriteOnly)
            out.writeQStringList(value)         
            cur.execute("INSERT INTO BOPOMOFO VALUES (?, ?)", (key.pattern, qb))  
        

        
  
        
        
                

if __name__ == "__main__":
    main()







