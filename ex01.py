from khl import Bot, Message

# 新建机器人，token 就是机器人的身份凭证
bot = Bot(token='你的机器人token')


# 注册指令
# @ 是「装饰器」语法，大家可以网上搜搜教程，我们这里直接用就行
# bot 是我们刚刚新建的机器人，声明这个指令是要注册到 bot 中的
# name 标示了指令的名字，名字也被用于触发指令，所以我们 /hello 才会让机器人有反应
# async def 说明这是一个异步函数，khl.py 是异步框架，所以指令也需要是异步的
# world 是函数名，可以自选；函数第一个参数的类型固定为 Message

@bot.command(name='hello')
async def world(msg: Message):
    # msg 指的是我们所发送的那句 `/hello`
    # 所以 msg.reply() 就是回复我们那句话，回复的内容是 `world!`
    await msg.reply('world!')

@bot.command(name='小可爱')
async def world(msg: Message):  # when `name` is not set, the function name will be used
    await msg.reply('咋啦，我在呢!😘')  # 当然也可以输入/小可爱，机器人回复：咋啦，我在呢!😘


# 运行日志
import logging
logging.basicConfig(level='INFO')
# 期望输出：INFO:khl.receiver:[ init ] launched

# 凭证传好了、机器人新建好了、指令也注册完了
# 接下来就是运行我们的机器人了，bot.run() 就是机器人的起跑线
bot.run()
# 教程来自：https://github.com/TWT233/khl.py/tree/main/example/ex01_helloworld
