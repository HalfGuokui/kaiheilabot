import json
import requests

playername = input('请输入你的Origin ID：')

url = f'https://api.gametools.network/bfv/stats/?format_values=true&name={playername}&platform=pc&skip_battlelog=false&lang=zh-CN'

r= requests.get(url)
print("状态码：",r.status_code)#返回api状态码
#print(f"返回状态码：{r.status_code}")#返回api状态码第二种写法
#print(data['userName'], data['rank'], data['id'])

respones_dict = r.json()

#print(respones_dict.keys())#打印键值

#print(f"头像图片文件：{respones_dict['avatar']}")
print(f"玩家昵称：{respones_dict['userName']}")
#print("玩家昵称：", respones_dict['userName'])
print(f"游戏时长：{respones_dict['timePlayed']}")
print(f"等级：{respones_dict['rank']}")
#print(f"等级图片文件：{respones_dict['rankImg']}")
print(f"KD：{respones_dict['killDeath']}")
print(f"KMP：{respones_dict['killsPerMinute']}")
print(f"SPM：{respones_dict['scorePerMinute']}")
print(f"命中率：{respones_dict['accuracy']}")
print(f"爆头率：{respones_dict['headshots']}")
print(f"爆头数：{respones_dict['headShots']}")
print(f"击杀数：{respones_dict['kills']}")
print(f"助攻数：{respones_dict['killAssists']}")
print(f"死亡数：{respones_dict['deaths']}")
print(f"救援数：{respones_dict['revives']}")
print(f"最高连杀数：{respones_dict['highestKillStreak']}")
print(f"最远爆头距离：{respones_dict['longestHeadShot']}米")
#print(f"已完成对局：{respones_dict['roundsPlayed']}")
print(f"胜场：{respones_dict['wins']}")
print(f"负场：{respones_dict['loses']}")
print(f"胜率：{respones_dict['winPercent']}")
print(f"最佳兵种：{respones_dict['bestClass']}")

