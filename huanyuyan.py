import os
import yaml
#放在英雄联盟文件夹下
file1=r'./LeagueClient/system.yaml'
file2=r'./LeagueClient/Config/LeagueClientSettings.yaml'
file3=r'./Riot Client/system.yaml'
file4=r'./Riot Client Data/User Data/Config/RiotClientSettings.yaml'

# 'en_SG'：新加坡
# ’zh_CN'  中文
language='en_SG'


filelist=[file1,file2,file3,file4]

print(filelist)
for file in filelist:
    with open(file,'r') as f:
        config=yaml.safe_load(f)

    if file.endswith('system.yaml'):
        config['region_data']['TENCENT']['default_locale'] = 'language'
    else:
        config['install']['globals']['locale'] = 'language'

    with open(file,'w') as f:
        yaml.dump(config,f)




