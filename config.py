from nonebot import logger, get_driver
import random

config = get_driver().config.dict()

if 'cool_group' not in config:
    logger.warning('未发现配置项 `cool_group` , 采用默认值: []')

if 'cool_time' not in config:
    logger.warning('未发现配置项 `cool_time` , 采用默认值: 100')

cool_group = config.get('cool_group', [])
cool_time = config.get('cool_time', 1)

if cool_time == 'random':
    cool_time = random.randint(100, 150)

cool_message = "不觉得很酷吗？\n" \
               "作为一个QQ Bot，我觉得这实在是太酷了，\n" \
               "很符合我对未来生活的想象，科技并带着趣味。"
