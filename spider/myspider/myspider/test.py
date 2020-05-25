depList = {'哲学':{'哲学':'zhexue'}
            ,'经济学':{'理论经济学':'lilunjingjixue','应用经济学':'yingyongjingjixue'}
           ,'法学':{'法学':'faxue','政治学':'zhengzhixue','社会学':'shehuixue','民族学':'minzuxue','马克思主义理论':'makesizhuyililun'}
           ,'教育学':{'教育学':'jiaoyuxue','心理学':'xinlixue','体育学':'tiyuxue'}
           ,'文学':{'中国语言文学':'zhongguoyuyanwenxue','外国语言文学':'waiguoyuyanwenxue','新闻传播学':'xinwenchuanboxue'}
           ,'历史学':{'考古学':'kaoguxue','中国史':'zhongguoshi','世界史':'shijieshi'}
           ,'理学':{'数学':'shuxue','物理学':'wulixue','化学':'huaxue','天文学':'tianwenxue','地理学':'dilixue','大气科学':'daqikexue',
                    '海洋科学':'haiyangkexue','地球物理学':'diqiuwulixue','地质学':'dizhixue','生物学':'shengwuxue','生态学':'shengtaixue','统计学':'tongjixue'}
           ,'工学':{'力学':'lixue','机械工程':'jixiegongcheng','仪器科学与技术':'yiqikexueyujishu','材料科学与工程':'cailiaokexueyugongcheng',
                    '冶金工程':'yejingongcheng','动力工程及工程热物理':'dongligongchengjigongchengrewuli','电气工程':'dianqigongcheng',
                    '电子科学与技术':'dianzikexueyujishu','信息与通信工程':'xinxiyutongxingongcheng','控制科学与工程':'kongzhikexueyugongcheng',
                    '计算机科学与技术':'jisuanjikexueyujishu','建筑学':'jianzhuxue','土木工程':'tumugongcheng','水利工程':'shuiligongcheng',
                    '测绘科学与技术':'cehuikexueyujishu','化学工程与技术':'huaxuegongchengyujishu','地质资源与地质工程':'dizhiziyuanyudizhigongcheng',
                    '矿业工程':'kuangyegongcheng','石油与天然气工程':'shiyouyutianranqigongcheng','纺织科学与工程':'fangzhikexueyugongcheng',
                    '轻工技术与工程':'qinggongjishuyugongcheng','交通运输工程':'jiaotongyunshugongcheng','船舶与海洋工程':'chuanboyuhaiyanggongcheng',
                    '航空宇航科学与技术':'hangkongyuhangkexueyujishu','核科学与技术':'hekexueyujishu','农业工程':'nongyegongcheng',
                    '环境科学与工程':'huanjingkexueyugongcheng','生物医学工程':'shengwuyixuegongcheng','食品科学与工程':'shipinkexueyugongcheng',
                    '城乡规划学':'chengxiangguihuaxue','软件工程':'ruanjiangongcheng','安全科学与工程':'anquankexueyugongcheng'}
           ,'农学':{'作物学':'zuowuxue','园艺学':'yuanyixue','农业资源与环境':'nongyeziyuanyuhuanjing','植物保护':'zhiwubaohu',
                    '畜牧学':'chumuxue','兽医学':'shouyixue','林学':'linxue','水产':'shuichan','草学':'caoxue'}
           ,'医学':{'基础医学':'jichuyixue','临床医学':'linchuangyixue','口腔医学':'kouqiangyixue','公共卫生与预防医学':'gonggongweishengyuyufangyixue',
                    '中医学':'zhongyixue','中西医结合':'zhongxiyijiehe','药学':'yaoxue','中药学':'zhongyaoxue','特种医学':'tezhongyixue',
                    '护理学':'hulixue'}
            ,'管理学':{'管理科学与工程':'guanlikexueyugongcheng','工商管理':'gongshangguanli','农林经济管理':'nonglinjingjiguanli',
                    '公共管理':'gonggongguanli','图书情报与档案管理':'tushuqingbaoyudanganguanli'}        
            ,'艺术学':{'艺术学理论':'yishuxuelilun','音乐与舞蹈学':'yinyueyuwudaoxue','戏剧与影视学':'xijuyuyingshixue','美术学':'meishuxue',
                    '设计学':'shejixue'}
            }

spList = ['哲学','经济学']
for i in range(2017,2020,1):
    for j in range(0,len(spList),1):
        sp = spList[j]
        # print (str(sp))
        dep = depList.get(str(sp))
        pinyin = list(dep.values())
        for k in range(0,len(pinyin),1):
            url = 'http://www.zuihaodaxue.com/BCSR/'+str(pinyin[k])+str(i)+'.html'
            print (url)
    