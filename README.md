# Linx，一个Nonebot插件

Linx，你的群聊小管家

# 使用教程

1. 在你的`src\plugins`（或`BOTNAME\plugins`）目录下执行
```bash
git clone git@github.com:lanbinshijie/nonebot_plugin_linx.git
```

2. 在`bot.py`（如图所示）位置添加如下命令

```python
import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

# 插入代码开始位置
nonebot.load_plugins('src/plugins/linx')
# 插入代码结束位置


nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")

```
**注意！结尾的linx要修改成clone下来的文件夹名称**

3. 运行 `nb run` 和 驱动器（如`go-cqhttp.exe`）

# 使用截图

![每日一言](https://cdn.jsdelivr.net/gh/lanbinshijie/image-cdn/picgo-img/202210222354143.png)

![今日人品](https://cdn.jsdelivr.net/gh/lanbinshijie/image-cdn/picgo-img/202210222356821.png)

![帮助页面](https://cdn.jsdelivr.net/gh/lanbinshijie/image-cdn/picgo-img/202210222357781.png)


# 投喂&赞助
小本经营，开发不易，如果可以的话请给蓝冰打赏一杯可乐吧w

![微信扫码](https://cdn.jsdelivr.net/gh/lanbinshijie/image-cdn/picgo-img/202210230029302.png)

|  名称   | 金额  | 日期|
|  ----  | ----  | ---- |
| 蓝冰世界  | 20.00元 | 2022年10月22日 |
| 蓝冰世界  | 20.00元 | 2022年10月23日 |
| 感谢 | 以上 | 大大

***TIPS：打赏列表每周更新一次***
