# 一次性补跑清理：修正早报文件中的禁语与根域名链接（仅处理 morning/wechat-morning/xhs-morning）
import os

base = r"D:\WorkBuddy\Projects\VCPE每日咨询工作台\archive"
dates = ["2026-09-11", "2026-09-12", "2026-09-13", "2026-09-14"]

# 顺序敏感：先替换长短语，再替换单字
reps = [
    ("一级市场募资结构化上移", "私募股权市场募资门槛结构化上移"),
    ("一级市场", "私募股权市场"),
    ("中信证券关注", "中信证券聚焦"),
    ("资本关注", "资本青睐"),
    ("延续关注", "延续受青睐"),
    ("重点增三电", "新增三电"),
    ("全球高估值成长", "高估值成长"),
    ("全球", ""),
    ("https://www.citicamc.com/", "https://www.cnfin.com/hb-lb/detail/20260901/4463341_1.html"),
    ("AMC动态(公司IR)", "AMC动态(中国金融信息网)"),
    ("https://www.yindeng.com.cn/", "https://m.cls.cn/detail/2419000"),
    ("不良流转(银登中心)", "不良处置(财联社)"),
]

for d in dates:
    for suf in ["morning-" + d + ".html", "wechat-morning-" + d + ".html", "xhs-morning-" + d + ".md"]:
        p = os.path.join(base, d, suf)
        if not os.path.exists(p):
            print("SKIP", p)
            continue
        with open(p, encoding="utf-8") as f:
            t = f.read()
        for a, b in reps:
            t = t.replace(a, b)
        with open(p, "w", encoding="utf-8") as f:
            f.write(t)
        print("OK", p)
print("DONE")
