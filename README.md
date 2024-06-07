# calabiqiu-auto 2.7版本
# 卡拉彼丘自动挂机脚本

# 下载地址
    链接：https://pan.baidu.com/s/1lS4xHiENLzvmsLmrcNFKzQ?pwd=2233 
    提取码：2233

# 下载地址文件介绍
    calabiqiu-autox.x.exe
        无限团竞自动挂机脚本，默认奥黛丽
    calabiqiu-autox.x-bear.exe
        无限团竞自动挂机脚本，默认伊维特
    calabiqiu-autox.x-xiaohuajia.exe
        无限团竞自动挂机脚本，默认小画家
    TeamBrawlForMission.exe
        只进行一次团队死斗，为了完成75次技能任务的脚本
    pressQMultipleTimes.exe
        卡拉比丘75次技能使用脚本
        手动进入团队乱斗，手动锁定奥黛丽，打开脚本，会自动按300次Q，然后可以挂机等结束


# 使用方法
    1.下载：calabiqiu-auto.exe
    2.桌面或者卡拉比丘窗口大小调整为1920 X 1080
    3.游戏打开至无限团竞界面，不要点击开始
    4.右键calabiqiu-auto.exe文件，选择属性，选择兼容性，选择更改所有用户的设置，勾选以管理员身份运行此程序，并应用确定
    5.推荐右键以管理员身份运行calabiqiu-auto.exe，并切回卡拉比丘无限团竞界面
    6.脚本启动期间不要触碰鼠标键盘，不要离开卡拉比丘全屏界面，否则无法正常运行

# 以往版本更新介绍
    2.7
        1.由于7v7加快游戏节奏，导致还没开始识别比分就结束了，所以调整180s睡眠时间为120s
    2.6
        1.优化10分钟排队后取消的逻辑
        2.优化重复内容输出
        3.提供多种选择
    2.1
        1.更新错误处理代码。
        2.错误处理代码截图新增时间间隔，减少机器压力
        3.截图优化处理逻辑，遍历会有问题，只有‖才能点两次，其它通通1次
        4.修复测试错误，排了10min后关闭并没有开始匹配
    2.0 版本更新介绍
        1.对项目代码进行了重构，删除了大量冗余代码，精简函数
        2.新增错误处理机制
        3.新增日志记录
    1.5 修复已知bug
    1.4 修复已知bug，由于点击升级的返回按钮太快，导致没有加载出来就点击了，延长了点击前的加载时间
    1.3 新增多次点击，防止只点击一次无法成功返回
    1.2 惊喜礼盒活动结束，删除相关代码
    1.1 降低45-50的图像要求，防止检测不到    
    1.0 初始版本
    
    
    






# 项目背景
    需求分析：卡拉比丘有完成任务需求，和自动挂机升级需求，和好感度需求
    全自动挂机困境：完全不打伤害会被系统检测并不给予任务完成计算和升级经验和好感度

# 解决方案
    无限团竞，基于经验选中奥黛丽，当用户大约挂机 1min 中后会被系统检测到挂机，然后让 AI 打伤害，在最后 45/50 时候，输入按键或者移动鼠标，就会自动连回来，不会受到挂机处罚

# 自动化的步骤
    首先手动进入无限团竞界面， 自动点击开始，等待排进去，排进去后自动点击准备，自动点击奥黛丽，点击锁定
    挂机180s，并每间隔 5s 检测一次顶部双方战绩数字，
    然后当一方到达或者超过 45 后，输入 w+单击，
    等待对局结束，自动点击返回大厅，自动点击离开，
    然后开始第二次循环

# 代码实现
    main.py

# 打包语句
    cd src
    pyinstaller --add-data 'images:images' --onefile main.py
    pyinstaller --onefile pressQMultipleTimes.py
    pyinstaller --add-data 'images:images' --onefile testMain.py
    pyinstaller --add-data 'images:images' --onefile testPressQMultipleTimes.py
    pyinstaller --add-data 'images:images' --onefile testTeamBrawl.py
    pyinstaller --add-data 'images:images' --onefile testTeamBrawlForMission.py
    pyinstaller -y main.spec

# exe闪退
    解决:闪退的时候可以看到有报错，但是看不清就退出了，加上-c 参数，可以在控制台运行或者打开cmd或者powerhsell都行，在命令行直接运行它
    .\testMain.exe