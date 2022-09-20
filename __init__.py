from nonebot import on_message
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from . import config
import re

cool_group = config.cool_group
cool_time = config.cool_time
cool_message = config.cool_message

message_times = {}
for i in cool_group:
    message_times[i] = 0

logger.success(f"何同学的Cooool插件加载完成，这实在太酷了。响应频率：每{cool_time}条")

cool = on_message(priority=20, block=False)


@cool.handle()
async def repeater(bot: Bot, event: GroupMessageEvent):
    gid = str(event.group_id)
    if gid in cool_group:
        global message_times
        message_times[gid] += 1
        if message_times.get(gid) == config.cool_time:
            logger.success(f'已发送Cooool的消息。不觉得很酷吗？')
            await bot.send_group_msg(group_id=event.group_id, message=cool_message, auto_escape=False)
