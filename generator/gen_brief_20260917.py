# -*- coding: utf-8 -*-
"""每日资讯工作台 简报生成器（自动同步线上模式）。
生成 09-16 补跑(早报+晚报全套) 与 09-17 晚报全套。
严格遵循 prefs.md v7：去标识化、链接铁律、六板块结构、配色固定。
"""
import os

BASE = r"D:\WorkBuddy\Projects\VCPE每日咨询工作台"
ARCH = os.path.join(BASE, "archive")

CSS = """<style>
:root{--green:#20BDA5;--green-d:#138A76;--navy:#304373;--blue:#2c5282;--amber:#d69e2e;--plum:#9b2c5c;--forest:#276749;--gray:#4a5568;--line:#eceff2;}
*{box-sizing:border-box;}
body{margin:0;background:#f4f6f8;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:#1a1a1a;line-height:1.62;}
.wrap{max-width:800px;margin:0 auto;background:#fff;padding:18px 16px 44px;}
.hd{margin:6px 0 28px;}
.hd .d{font-size:13px;color:#8896a8;margin-bottom:4px;}
.hd .ti{font-size:36px;font-weight:800;color:#111;letter-spacing:-0.5px;padding-bottom:8px;border-bottom:6px solid var(--green);display:inline-block;}
.hd .mo{background:#eafaf6;border-left:4px solid var(--green);padding:10px 12px;border-radius:0 8px 8px 0;font-size:14px;color:#1f3d36;margin-top:16px;}
.sec{margin:20px 0 6px;}
.sec-h{display:inline-block;font-size:16px;font-weight:700;color:#fff;padding:9px 18px;border-radius:10px;margin:0 0 10px;}
.sec-h.c1{background:var(--navy);}
.sec-h.c2{background:var(--green);}
.sec-h.c3{background:var(--blue);}
.sec-h.c4{background:var(--amber);}
.sec-h.c5{background:var(--plum);}
.sec-h.c6{background:var(--forest);}
.sec-h.c7{background:var(--gray);}
.item{padding:12px 2px;border-bottom:1px solid var(--line);}
.item .t{font-weight:700;font-size:15.5px;color:#111;}
.item .s{font-size:12px;color:#9aa3ad;margin:4px 0 4px;}
.item .dd{font-size:14px;color:#37404a;}
.item a{color:var(--green-d);font-size:12px;text-decoration:none;border-bottom:1px dotted var(--green-d);margin-left:4px;}
.ft{margin-top:28px;font-size:11.5px;color:#9aa3ad;text-align:center;border-top:1px solid #eee;padding-top:13px;}
.up{color:#d6453d;font-weight:700;} .down{color:#1b8a5a;font-weight:700;}
</style>"""

def item(t, s, d, link=None, linktext=None):
    a = ''
    if link and linktext:
        a = ' <a href="%s" target="_blank">%s</a>' % (link, linktext)
    return ('<div class="item"><div class="t">%s</div><div class="s">来源：%s</div>'
            '<div class="dd">%s%s</div></div>') % (t, s, d, a)

def render_html(title, date_cn, mo, sections, footer):
    secs = []
    for (h, cls, items) in sections:
        inner = "".join(items)
        secs.append('<div class="sec"><div class="sec-h %s">%s</div>%s</div>' % (cls, h, inner))
    return ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1.0">'
            '<title>%s %s</title>%s</head><body><div class="wrap">'
            '<div class="hd"><div class="d">%s</div><div class="ti">%s</div>'
            '<div class="mo">%s</div></div>%s'
            '<div class="ft">%s</div></div></body></html>') % (
        title, date_cn, CSS, date_cn, title, mo, "".join(secs), footer)

def render_wechat(title, date_cn, mo, sections, footer):
    secs = []
    for (h, cls, items) in sections:
        inner = "".join(items)
        secs.append('<h2 style="font-size:17px;color:#138A76;border-left:5px solid #20BDA5;padding-left:8px;margin:22px 0 8px;">%s</h2>%s' % (h, inner))
    return ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1.0">'
            '<title>%s %s</title></head><body style="font-family:-apple-system,\'PingFang SC\',\'Microsoft YaHei\',sans-serif;'
            'font-size:16px;line-height:1.7;color:#222;max-width:680px;margin:0 auto;padding:16px;">'
            '<h1 style="font-size:26px;font-weight:800;border-bottom:5px solid #20BDA5;padding-bottom:6px;display:inline-block;">%s</h1>'
            '<p style="background:#eafaf6;border-left:4px solid #20BDA5;padding:10px 12px;font-size:14px;color:#1f3d36;">%s</p>'
            '%s<p style="font-size:12px;color:#9aa3ad;border-top:1px solid #eee;padding-top:12px;margin-top:24px;">%s</p>'
            '</body></html>') % (title, date_cn, title, mo, "".join(secs), footer)

def render_xhs(title_candidates, body, tags, footer):
    cand = "\n".join("· " + c for c in title_candidates)
    return ("【标题备选】\n%s\n\n【正文】\n%s\n\n【话题标签】\n%s\n\n%s") % (cand, body, tags, footer)

# ============================================================
# 数据：09-17 晚报
# ============================================================
FOOTER_E = "每日晚报（训练期草稿）｜本简报基于公开信息整理，仅供内部参考与学习，不构成任何投资建议。市场有风险，决策需独立。"
FOOTER_M = "每日早报（训练期草稿）｜本简报基于公开信息整理，仅供内部参考与学习，不构成任何投资建议。市场有风险，决策需独立。"

e0917 = {
"title": "每日晚报", "date_cn": "2026.09.17 周四",
"mo": "● 美联储三年来首次加息25bp至3.75%–4.00%、点阵图鹰派，全球股债承压、美元站上100、10Y美债逼近5%；A股低开收跌（沪指-0.41%），港股-0.44%；国办强化烟花爆竹全链条监管、沪深北交易所公布中秋国庆休市；地瓜机器人4亿美元C轮领跑硬科技融资。",
"sections": [
 ("政策与监管", "c2", [
   item("国办印发《关于进一步加强烟花爆竹全链条安全监管的意见》（国办发〔2026〕26号）",
        "中国政府网",
        "生产/储存/经营/运输/燃放全链条严监管，淘汰落后工艺、严禁委托代加工，对发生伤亡事故单位一律停产整顿。",
        "https://www.gov.cn/zhengce/content/202609/content_7081356.htm", "中国政府网(意见全文)"),
   item("沪深北交易所公布2026中秋国庆休市安排",
        "上交所 / 深交所 / 北交所",
        "9/25–9/27、10/1–10/7休市，9/28、10/8起照常开市；港股通同步暂停与恢复。节前资金、持仓安排需提前。",
        "https://www.163.com/dy/article/L720TS0R0519C6T9.html", "中新经纬(休市安排)"),
   item("广电总局“十五五”推一体化电视等新型终端，2项部门规章即将发布",
        "国新办发布会 / 每日经济新闻",
        "部署超千万插入式微型机顶盒；有线电视、IPTV运营服务管理规定即将发布；治理“套娃”收费与虚假医药广告。",
        "https://www.163.com/dy/article/L72EJJGA0512B07B.html", "每日经济新闻"),
   item("文旅部印发《文化和旅游发展“十五五”规划》",
        "文化和旅游部 / 新华每日重点信息",
        "部署8方面任务、设计54个重点工程项目，推动科技赋能文化和旅游发展。",
        "https://www.sohu.com/a/1077307111_121696613", "文旅部规划"),
 ]),
 ("VC/PE 与 IPO 投融资", "c4", [
   item("地瓜机器人完成4亿美元C轮（具身智能/机器人计算芯片）",
        "证券时报 / 深圳新闻网 / 中国证券网",
        "未来资产领投、美团战投等联合跟投；年内累计6.7亿美元，旭日系列芯片累计出货破800万片，具身智能客户覆盖率超50%。",
        "https://www.sznews.com/news/content/mb/2026-09/17/content_32173727.htm", "深圳新闻网"),
   item("帕西尼感知数亿元B轮、视塔机器人Pre-A、上海造父智能（哈啰Robotaxi）约1亿美元新一轮",
        "证券时报",
        "帕西尼累计融资破40亿；视塔由哈勃投资等投Pre-A（触觉感知）；造父智能由上海国投先导领投，估值近30亿美元。",
        "https://www.163.com/dy/article/L722OBIT053469RG.html", "证券时报"),
   item("AI制药AnewLabs（新生实验室，原字节AI for Science团队）首轮独立融资2.9亿美元",
        "证券时报",
        "红杉中国、IDG资本、高瓴创投、五源资本、高榕资本等参投，投后估值约15亿美元。",
        "https://www.163.com/dy/article/L722OBIT053469RG.html", "证券时报"),
   item("IPO进展：沈鼓集团(601091)今日主板上市、博迈医疗创业板过会、长川科技筹划H股",
        "沪深北交易所 / 港交所披露易 / 公司公告",
        "沈鼓募12.61亿；博迈医疗为近三年深交所首家过会医疗器械IPO；星环科技H股定价、纳真科技招股截止、欢创科技过聆讯。",
        "https://ipofinance.eastmoney.com/", "东方财富IPO频道"),
 ]),
 ("特殊机会投资", "c5", [
   item("最高法印发《全国法院审理房地产开发企业破产案件座谈会纪要》（法〔2026〕137号）",
        "最高人民法院",
        "统一房企破产法律适用，稳妥处置房地产项目债务风险，保障购房人等各方权益；自印发日起施行。",
        "https://www.court.gov.cn/fabu/xiangqing/511091.html", "最高人民法院"),
   item("地产不良成银行对公不良第一大压力源",
        "行业研究",
        "风险从民营房企向全行业、开发贷向全品类蔓延；抵押物“有价无市”、法拍流拍率上升，传统催收诉讼核销失效。",
        "https://news.qq.com/rain/a/20260917A055H800", "地产事件汇总"),
   item("房企动态：招商局置地佛山地块收回补偿5.69亿、华侨城售常熟实业、新城拟发4亿公司债、电建63.83亿REIT反馈",
        "腾讯新闻 / 公司公告",
        "新华社强调楼市回稳新政“有力有序”落地；头部房企窗口期降价清库存保现金流。",
        "https://news.qq.com/rain/a/20260917A055H800", "地产事件汇总"),
   item("法拍案例：云南仟浩尚城项目第三批未售不动产破产强清拍卖",
        "全国企业破产重整案件信息网",
        "130间商铺、6车位及35套住宅于淘宝破产强清平台拍卖，9/21–9/22竞价；标的以现状为准、瑕疵自负。",
        "https://pccz.court.gov.cn/pcajxxw/pcgg/ggxq?id=19333661059051520", "破产重整信息网"),
 ]),
 ("汽车检测行业", "c6", [
   item("机动车环保检测全面趋严：OBD成年检必检项",
        "公安部 / 生态环境部 / 行业政策",
        "除免检车外新购营运车、面包车、7座+须过排放关；OBD故障灯/故障码直接不过；六部门专项整治中580家机构被取消资质、110家追责。",
        "https://k.sina.com.cn/article_7879996579_1d5af34a306801j5eg.html", "检测新规解读"),
   item("新能源专属检验推进：电池健康度/绝缘/电控故障码扫描",
        "行业政策",
        "截至2025年底全国新能源车保有量3140万辆（占8.9%），多地检测站改造设备，增加电池健康度读取、充电接口绝缘测试。",
        "https://k.sina.com.cn/article_7879996579_1d5af34a306801j5eg.html", "检测新规解读"),
   item("行业影响：数据联网闭环淘汰黄牛、倒逼设备升级与合规",
        "机动车检测新规解读",
        "数据联网+严刑处罚使“包过”失去空间；未完成硬件改造站点暂停环保检测；须建检测台账双人复核、数据留存。",
        "https://szjj.sz.gov.cn/gkmlpt/content/12/12681/post_12681296.html", "深圳交警(年检周期)"),
 ]),
 ("二级市场收盘复盘", "c3", [
   item("A股9/17：沪指3875.60（-0.41%）、深成指13409.91（-0.33%）、创业板3298.31（-0.40%）",
        "中新经纬",
        "成交1.84万亿、超2800股飘绿；海运领涨，汽车/农业/生物科技涨幅居前；贵金属、稀土、油气、半导体下跌（美联储加息拖累）。",
        "https://www.chinanews.com.cn/cj/2026/09-17/10698225.shtml", "中新经纬(收评)"),
   item("港股9/17：恒指24604.29（-0.44%）、恒科4310.74（-0.34%）、国指8175.36（-0.38%）",
        "新华社",
        "主板成交1855.86亿港元；腾讯-1.71%、港交所-1.77%、中石化-2.17%、中海油-1.97%。",
        "https://my-h5news.app.xinhuanet.com/h5/article.html?articleId=2026091769b6891804df4729af582e267e29350f", "新华社(港股)"),
   item("隔夜美股（9/16美东=9/17凌晨）：美联储加息25bp，道指-1.21%、标普-0.45%、纳指-0.01%",
        "央视财经 / 新浪财经",
        "10Y美债逼近5%、美元站上100；费城半导体盘中涨超2%后回落，英伟达/AMD/英特尔收涨。",
        "https://finance.sina.com.cn/jjxw/2026-09-17/doc-inisaiet0363337.shtml", "新浪财经(加息)"),
 ]),
 ("今日要闻与热点现象", "c7", [
   item("美联储时隔三年重启加息、点阵图鹰派：年内或再加息一次",
        "央视财经 / 新浪财经",
        "联邦基金利率升至3.75%–4.00%；COMEX黄金期货-0.70%报4302.5，但现货一度重回4300上方（央行购金支撑）。",
        "https://finance.sina.com.cn/jjxw/2026-09-17/doc-inisaiet0363337.shtml", "新浪财经(加息)"),
   item("商务部回应欧委会《公共采购法》草案“欧洲优先”条款",
        "商务部例行新闻发布会",
        "中方高度关切，敦促欧方遵守世贸规则、保持市场开放、修改歧视性条款，为企业营造公平透明非歧视营商环境。",
        None, None),
   item("香港特区政府发布首份五年规划（2026–2030），AI列为战略产业",
        "华尔街见闻 / 新华社",
        "强化全球最大离岸人民币枢纽功能，优化股票债券市场、构建大宗商品交易生态圈，拟修订特专科技上市制度、人民币柜台纳入港股通。",
        "https://wallstreetcn.com/livenews/3166551", "华尔街见闻"),
   item("华为发布《智能世界2035》报告：预测2035年全球年度Token消耗增10万倍",
        "华为 / 华尔街见闻",
        "智能体流量占比超90%，并首次提出通往智能世界的十大关键命题。",
        "https://wallstreetcn.com/livenews/3166551", "华尔街见闻"),
 ]),
],
}

# ============================================================
# 数据：09-16 早报（补跑）
# ============================================================
m0916 = {
"title": "每日早报", "date_cn": "2026.09.16 周三",
"mo": "● 美股9/16（北京时间凌晨）三大指数集体收跌（道指-1.21%、纳指-0.01%），美联储9/17凌晨加息预期压制；A股9/16放量大涨（沪指+0.71%、创业板+1.96%、科创50涨超4%、成交1.84万亿），半导体/光通信/存储领涨；潘功胜求是文章谈金融结构、文旅部与电子信息制造业“十五五”规划出炉。",
"sections": [
 ("隔夜速览", "c1", [
   item("美股9/16：道指-1.21%报51461.90、标普-0.45%报7551.81、纳指-0.01%报25978.42",
        "市场数据",
        "费城半导体指数盘中涨超2%后回落；英特尔盘中涨超7%；市场预期美联储9/17凌晨加息25bp。",
        "https://finance.sina.com.cn/jjxw/2026-09-17/doc-inisaiet0363337.shtml", "新浪财经(加息)"),
   item("商品/汇率：美油-3.6%报102.02、布油-2.9%报105.6；COMEX黄金-0.70%报4302.5",
        "市场数据",
        "沙特修复遭袭输油管道、调整出口路线缓解供应担忧；LME基本金属多数上涨（锡+1.41%、铜+1.18%）。",
        "https://finance.sina.com.cn/jjxw/2026-09-17/doc-inisaiet0363337.shtml", "新浪财经(加息)"),
   item("汇率/美债：在岸人民币16:30收6.7064（+70bp）；10Y美债逼近5%、美元站上100",
        "外汇交易中心 / 市场数据",
        "人民币中间价6.7628（调升42bp）；美联储加息预期推升美元与长端美债收益率。",
        None, None),
 ]),
 ("今日大事件（宏观统计）", "c2", [
   item("潘功胜《求是》文章：不能简单以信贷增速衡量金融支持实体经济力度",
        "求是 / 人民银行",
        "科技型企业早期主要靠私募股权和创业投资；金融市场对技术前沿、高风险创新产业提供融资，带来对贷款的良性替代与分流。",
        "https://www.sohu.com/a/1077307111_121696613", "求是文章解读"),
   item("国家统计局《统计改革发展“十五五”规划》：探索数字经济供给使用表试编",
        "国家统计局",
        "研究推进数据资产等知识产权产品核算、开展试点试算；探索新兴支柱产业和未来产业统计监测。",
        None, None),
   item("全球金融中心指数：纽约/伦敦/香港/新加坡/上海/东京居前10",
        "中英文研究机构联合报告",
        "中国内地上榜城市整体表现亮眼，亚太地区平均评分增幅最大。",
        None, None),
 ]),
 ("二级市场聚焦", "c3", [
   item("A股9/16：沪指3891.60（+0.71%）、深成指13454.74（+1.26%）、创业板3311.47（+1.96%）、科创50涨超4%",
        "市场数据 / 腾讯财经",
        "成交1.84万亿、超4100股涨；半导体、光通信、存储领涨，宁德时代-6%；工程机械、农业、银行、地产休整。",
        "https://gu.qq.com/resources/shy/news/detail-v2/index.html?t=1#/index?_tentrees_trans=0&id=SN20260916150354985c0b11", "腾讯财经(收评)"),
   item("港股9/16：恒指24713.78（+0.19%）、恒科4325.45（+0.79%），南向净买20.99亿港元",
        "市场数据",
        "脑机接口、光通信、存储涨幅居前；锂电池、重型机械、石油股下跌。",
        None, None),
   item("两融与IPO：截至9/15两市融资余额25900亿；Q3 IPO达44家募1374亿",
        "Wind / 市场数据",
        "长鑫科技与华润新能源两只巨型IPO合计募约911亿，占全季募资66.3%，创2023年以来新高。",
        None, None),
 ]),
 ("VC/PE 与投融资", "c4", [
   item("宁德时代子公司认缴11.2亿设创投基金；润泽科技10亿设创投基金（AI/具身智能）",
        "央广网",
        "产业资本密集做LP，主要投向人工智能、具身智能等硬科技赛道。",
        "https://www.cnr.cn/jingji/ycbd/20260916/t20260916_527815041.shtml", "央广网"),
   item("先正达集团向港交所保密递交IPO（募资约50亿美元，拟明年上市）",
        "路透 / 搜狐",
        "若推进顺利，将是香港市场近年来规模最大的IPO项目之一。",
        "https://www.sohu.com/a/1076599239_99992453", "陆家嘴早餐"),
   item("天承科技筹划发行H股；星巴克拟售日本业务多数股权（约30亿美元）",
        "央广网 / 路透",
        "天承科技拟赴港上市；星巴克据称正考虑出售日本业务多数股权。",
        "https://www.cnr.cn/jingji/ycbd/20260916/t20260916_527815041.shtml", "央广网"),
 ]),
 ("特殊机会投资", "c5", [
   item("房企动态（9/16）：招商局置地佛山地块收回补偿5.69亿、华侨城售常熟实业、新城拟发4亿公司债",
        "腾讯新闻 / 公司公告",
        "电建地产63.83亿REIT获反馈；云南城投重组无实质进展；新华社强调楼市回稳新政“有力有序”落地。",
        "https://news.qq.com/rain/a/20260917A055H800", "地产事件汇总"),
   item("地产不良全景：银行对公不良第一大压力源，风险向全行业蔓延",
        "行业研究",
        "抵押物“有价无市”、法拍流拍率上升；保交楼约束下传统司法处置失效，纾困重组与AMC接盘成主流。",
        "https://news.qq.com/rain/a/20260917A055H800", "地产事件汇总"),
 ]),
 ("汽车检测行业", "c6", [
   item("年检周期与OBD：2018年后车辆上线检须连OBD，9座以下非营运小客车10年内第6/10年上线",
        "公安部交通管理局",
        "免检期内每2年线上申领电子标志；OBD故障码需先维修再年检，避免白跑。",
        "https://szjj.sz.gov.cn/gkmlpt/content/12/12681/post_12681296.html", "深圳交警(年检周期)"),
   item("新能源专属检验推进：电池健康度/绝缘/电控故障码扫描",
        "行业政策",
        "纯电免尾气检测、重点查三电；新能源车保有量攀升倒逼检测站设备改造。",
        "https://szjj.sz.gov.cn/gkmlpt/content/12/12681/post_12681296.html", "深圳交警(年检周期)"),
 ]),
],
}

# ============================================================
# 数据：09-16 晚报（补跑）
# ============================================================
e0916 = {
"title": "每日晚报", "date_cn": "2026.09.16 周三",
"mo": "● 9/16 A股放量大涨（创业板+1.96%、科创50涨超4%），半导体/光通信/存储领涨；先正达秘密递表港交所（募约50亿美元）领衔IPO储备；文旅部、电子信息制造业“十五五”规划发布；蓝箭航天朱雀二号改遥七成功组网（民营商业航天迈入批量组网）；美联储加息前夕市场谨慎。",
"sections": [
 ("政策与监管", "c2", [
   item("文旅部印发《文化和旅游发展“十五五”规划》",
        "文化和旅游部 / 新华每日重点信息",
        "部署8方面任务、设计54个重点工程项目，推动科技赋能文化和旅游发展。",
        "https://www.sohu.com/a/1077307111_121696613", "文旅部规划"),
   item("电子信息制造业“十五五”规划：到2030规模以上营收破30万亿",
        "工信部 / 央视",
        "推动集成电路全链条攻关，统筹推进产能规划与预警；推动光电融合平台、加快太空计算全链条布局。",
        "https://www.sohu.com/a/1076599239_99992453", "陆家嘴早餐"),
   item("市场监管总局+文旅部对美团/抖音/京东/携程/同程/飞猪行政指导（反内卷）",
        "市场监管总局",
        "要求落实合规主体责任，防范独家合作、“全网最低价”等内卷与竞争风险，营造优质优价秩序。",
        "https://www.sohu.com/a/1076599239_99992453", "陆家嘴早餐"),
   item("钢铁行业全面开展自律控产降库存倡议",
        "中国钢铁工业协会",
        "坚决落实产量调控、谴责超产；坚持自律控产降库存，尽快降低高企库存。",
        "https://www.sohu.com/a/1076599239_99992453", "陆家嘴早餐"),
 ]),
 ("VC/PE 与 IPO 投融资", "c4", [
   item("先正达集团向港交所保密递交IPO（募资约50亿美元）",
        "路透 / 搜狐",
        "计划明年上市，若推进顺利为香港近年最大IPO之一。",
        "https://www.sohu.com/a/1076599239_99992453", "陆家嘴早餐"),
   item("宁德时代子公司11.2亿设创投基金；润泽科技10亿设创投基金（AI/具身智能）",
        "央广网",
        "产业资本密集做LP，硬科技优先。",
        "https://www.cnr.cn/jingji/ycbd/20260916/t20260916_527815041.shtml", "央广网"),
   item("星巴克拟售日本业务多数股权（约30亿美元）；天承科技筹划H股",
        "路透 / 央广网",
        "星巴克日本估值约30亿美元；天承科技拟赴港上市。",
        "https://www.cnr.cn/jingji/ycbd/20260916/t20260916_527815041.shtml", "央广网"),
 ]),
 ("特殊机会投资", "c5", [
   item("房企动态（9/16）：招商局置地佛山地块收回补偿5.69亿、华侨城售常熟实业、新城拟发4亿公司债",
        "腾讯新闻 / 公司公告",
        "电建地产63.83亿REIT获反馈；云南城投重组无实质进展；新华社强调楼市回稳新政有力有序落地。",
        "https://news.qq.com/rain/a/20260917A055H800", "地产事件汇总"),
   item("地产不良全景：银行对公不良第一大压力源",
        "行业研究",
        "风险从民营房企向全行业、开发贷向全品类蔓延；法拍流拍率上升、抵押物有价无市。",
        "https://news.qq.com/rain/a/20260917A055H800", "地产事件汇总"),
 ]),
 ("汽车检测行业", "c6", [
   item("机动车环保检测专项整治：580家机构被取消资质、110家追责",
        "公安部 / 生态环境部",
        "六部门联合整治机动车排放检验领域，斩断数据造假链条；不合格车辆不予上牌。",
        "https://k.sina.com.cn/article_7879996579_1d5af34a306801j5eg.html", "检测新规解读"),
   item("年检新规/OBD必检：故障灯或故障码直接不过",
        "公安部交通管理局",
        "2018年后车辆上线检须连OBD；纯电免尾气、重点查三电。",
        "https://szjj.sz.gov.cn/gkmlpt/content/12/12681/post_12681296.html", "深圳交警(年检周期)"),
 ]),
 ("二级市场收盘复盘", "c3", [
   item("A股9/16：沪指3891.60（+0.71%）、深成指13454.74（+1.26%）、创业板3311.47（+1.96%）",
        "市场数据 / 腾讯财经",
        "成交1.84万亿、超4100股涨；半导体、光通信、存储领涨，科创50涨超4%。",
        "https://gu.qq.com/resources/shy/news/detail-v2/index.html?t=1#/index?_tentrees_trans=0&id=SN20260916150354985c0b11", "腾讯财经(收评)"),
   item("港股9/16：恒指24713.78（+0.19%）、恒科4325.45（+0.79%），南向净买20.99亿",
        "市场数据",
        "半导体、光通信、存储涨幅居前；锂电池、石油股下跌。",
        None, None),
   item("美股加息前夕（9/16美东）：道指-1.21%、标普-0.45%、纳指-0.01%",
        "市场数据",
        "美联储9/17凌晨公布利率决议，交易员近乎完全定价25bp加息。",
        "https://finance.sina.com.cn/jjxw/2026-09-17/doc-inisaiet0363337.shtml", "新浪财经(加息)"),
 ]),
 ("今日要闻与热点现象", "c7", [
   item("蓝箭航天朱雀二号改进型遥七发射成功，首次承担大型卫星互联网星座组网",
        "央视新闻 / 行业",
        "将千帆极轨19组共10颗卫星送入预定轨道，标志中国民营商业航天正式迈入批量组网阶段。",
        None, None),
   item("美联储加息前瞻：9/17凌晨落地，市场已定价25bp",
        "新浪财经",
        "决议与点阵图将直接影响港股流动性与外资配置节奏；存储涨价潮延续。",
        "https://finance.sina.com.cn/jjxw/2026-09-17/doc-inisaiet0363337.shtml", "新浪财经(加息)"),
   item("香港五年规划（李家超9/16公布）：AI列为战略产业、强化离岸人民币枢纽",
        "华尔街见闻 / 新华社",
        "拟修订特专科技上市制度、人民币柜台纳入港股通；构建大宗商品交易生态圈。",
        "https://wallstreetcn.com/livenews/3166551", "华尔街见闻"),
   item("SK海力士英特尔赴美生产存储芯片传闻；马斯克暗示特斯拉与SpaceX合并",
        "路透 / 今日头条",
        "SK海力士回应“尚无定论”；马斯克表态引发两家业务协同想象，隔夜SpaceX一度涨超4%。",
        "https://www.toutiao.com/article/7686293322256450057/", "今日头条"),
 ]),
],
}

# ============================================================
# 写盘
# ============================================================
def write_all(brief, date, kind):
    d = os.path.join(ARCH, date)
    os.makedirs(d, exist_ok=True)
    title = brief["title"]
    if kind == "evening":
        base = "evening-" + date
    else:
        base = "morning-" + date
    html = render_html(title, brief["date_cn"], brief["mo"], brief["sections"], FOOTER_E if kind=="evening" else FOOTER_M)
    with open(os.path.join(d, base + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    wc = render_wechat(title, brief["date_cn"], brief["mo"], brief["sections"], FOOTER_E if kind=="evening" else FOOTER_M)
    with open(os.path.join(d, "wechat-" + base + ".html"), "w", encoding="utf-8") as f:
        f.write(wc)
    # xhs 浓缩
    if kind == "evening":
        xhs_body = ("【%s %s】\n" % (title, date) +
            brief["mo"].replace("● ", "") +
            "\n\n六板块速览：\n" +
            "\n".join("· %s：%s" % (h, secs[0].replace("来源：", "（")) for (h, cls, items) in brief["sections"] for secs in [items[0].split("</div>")[2].split(">",1)[1]] if False) )
        # 简化：用每板块首条标题拼接
        lines = []
        for (h, cls, items) in brief["sections"]:
            first = items[0]
            # 取 title
            t0 = first.split('<div class="t">')[1].split("</div>")[0]
            lines.append("· %s：%s" % (h, t0))
        xhs_body = ("【%s %s】\n%s\n\n核心要点：\n%s\n\n（完整版见 HTML 简报）") % (
            title, date, brief["mo"].replace("● ", ""), "\n".join(lines))
        tags = "#每日晚报 #VCPE #宏观 #半导体 #新能源 #特殊机会投资 #汽车检测 #二级市场"
        cand = ["%s｜美联储加息落地，A股收跌、硬科技融资火热" % date,
                "%s晚报｜六板块速览：政策、融资、地产不良、收盘复盘" % date,
                "一日资讯｜加息潮下的A股与港股，地瓜机器人4亿美元C轮"]
        xhs = render_xhs(cand, xhs_body, tags, FOOTER_E)
    else:
        lines = []
        for (h, cls, items) in brief["sections"]:
            t0 = items[0].split('<div class="t">')[1].split("</div>")[0]
            lines.append("· %s：%s" % (h, t0))
        xhs_body = ("【%s %s】\n%s\n\n核心要点：\n%s\n\n（完整版见 HTML 简报）") % (
            title, date, brief["mo"].replace("● ", ""), "\n".join(lines))
        tags = "#每日早报 #隔夜 #宏观 #半导体 #新能源 #VCPE #汽车检测"
        cand = ["%s｜A股放量大涨、美联储加息前夕" % date,
                "%s早报｜六板块：隔夜、宏观、二级、融资、地产、检测" % date]
        xhs = render_xhs(cand, xhs_body, tags, FOOTER_M)
    with open(os.path.join(d, "xhs-" + base + ".md"), "w", encoding="utf-8") as f:
        f.write(xhs)
    print("written:", d, base)

if __name__ == "__main__":
    write_all(e0917, "2026-09-17", "evening")
    write_all(m0916, "2026-09-16", "morning")
    write_all(e0916, "2026-09-16", "evening")
    print("DONE")
