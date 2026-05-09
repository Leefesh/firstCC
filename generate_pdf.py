# -*- coding: utf-8 -*-
from fpdf import FPDF

codes = {
    "conveyor": (
        '// 变量: 移动方向 = 1\n'
        '事件: 游戏开始\n'
        '  动作: 重复执行\n'
        '    等待 0.1 秒\n'
        '    如果 传送带平台1 的 X坐标 > 15 则\n'
        '      设置 移动方向 = -1\n'
        '    如果 传送带平台1 的 X坐标 < -15 则\n'
        '      设置 移动方向 = 1\n'
        '    移动 传送带平台1 方向: (移动方向, 0, 0) 速度: 3\n'
        '    移动 传送带平台2 方向: (移动方向, 0, 0) 速度: 5\n'
        '    移动 传送带平台3 方向: (-移动方向, 0, 0) 速度: 4'
    ),
    "candy": (
        '// 实体: 糖果障碍物预制体\n'
        '事件: 游戏开始\n'
        '  动作: 重复执行\n'
        '    等待 3 秒\n'
        '    在坐标 (随机数(-20,20), 30, 随机数(-10,10)) 生成 糖果障碍物\n'
        '    等待 0.5 秒\n'
        '    在坐标 (随机数(-20,20), 30, 随机数(-10,10)) 生成 糖果障碍物\n\n'
        '事件: 玩家碰撞 糖果障碍物\n'
        '  动作:\n'
        '    播放音效 碰撞\n'
        '    将 糖果障碍物 销毁\n'
        '    对 碰撞玩家 造成伤害 30\n\n'
        '事件: 糖果障碍物 的 Y坐标 < -10\n'
        '  动作: 将 糖果障碍物 销毁'
    ),
    "spring": (
        '// 实体: 果冻弹簧 x4\n'
        '事件: 玩家进入 果冻弹簧区域\n'
        '  动作:\n'
        '    播放音效 弹簧\n'
        '    设置 玩家 的 Y方向速度 = 15\n'
        '    等待 1 秒\n'
        '    设置 果冻弹簧 的 缩放 = (1.2, 0.5, 1.2)\n'
        '    等待 0.2 秒\n'
        '    设置 果冻弹簧 的 缩放 = (1, 1, 1)'
    ),
    "finish": (
        '// 实体: 终点区域触发器\n'
        '事件: 玩家进入 终点区域\n'
        '  动作:\n'
        '    对 该玩家 显示文字 恭喜通关!\n'
        '    播放音效 胜利\n'
        '    重复 10 次:\n'
        '      在坐标 (随机数(-5,5), 随机数(5,15), 随机数(-5,5)) 生成 烟花粒子\n'
        '      等待 0.3 秒\n'
        '    设置 该玩家 为胜利状态\n'
        '    广播 游戏结束\n\n'
        '事件: 收到广播 游戏结束\n'
        '  动作:\n'
        '    停止所有 障碍物 的移动\n'
        '    对 所有玩家 显示排行榜'
    ),
    "timer": (
        '// 变量: 通关用时 = 0, 计时中 = 假\n'
        '事件: 游戏开始\n'
        '  动作: 设置 通关用时 = 0; 设置 计时中 = 真\n\n'
        '事件: 每帧执行\n'
        '  条件: 计时中 == 真\n'
        '  动作: 设置 通关用时 = 通关用时 + 0.016\n\n'
        '事件: 玩家通关\n'
        '  动作: 设置 计时中 = 假\n'
        '  对 该玩家 显示文字 用时: + 通关用时 + 秒'
    ),
}


class MapPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("yh", "", 8)
            self.cell(0, 8, "蛋仔派对 - 糖果工厂大冒险地图设计", align="C", new_x="LMARGIN", new_y="NEXT")
            self.line(10, 14, 200, 14)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("yh", "", 8)
        self.cell(0, 10, f"第 {self.page_no()} 页", align="C")

    def section_title(self, title):
        self.set_font("yh", "B", 14)
        self.set_fill_color(255, 200, 100)
        self.cell(0, 12, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def sub_title(self, title):
        self.set_font("yh", "B", 11)
        self.set_text_color(220, 80, 50)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def body_text(self, text):
        self.set_font("yh", "", 10)
        self.multi_cell(0, 6, text)
        self.ln(1)

    def code_block(self, text):
        self.set_fill_color(240, 240, 240)
        self.set_font("yh", "", 8)
        self.set_text_color(30, 30, 30)
        for line in text.split("\n"):
            self.cell(0, 5, line, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(3)

    def table_row(self, cells, bold=False, fill=False):
        self.set_font("yh", "B" if bold else "", 9)
        if bold:
            self.set_fill_color(230, 180, 100)
        elif fill:
            self.set_fill_color(250, 240, 220)
        widths = [80, 50, 60] if len(cells) == 3 else [40, 150]
        for i, cell in enumerate(cells):
            self.cell(widths[i], 7, cell, border=1, fill=(bold or fill), new_x="RIGHT")
        self.ln()


def build():
    pdf = MapPDF()
    pdf.add_font("yh", "", "C:/Windows/Fonts/msyh.ttc")
    pdf.add_font("yh", "B", "C:/Windows/Fonts/msyhbd.ttc")

    pdf.add_page()

    # ── 封面 ──
    pdf.ln(40)
    pdf.set_font("yh", "B", 28)
    pdf.set_text_color(255, 120, 50)
    pdf.cell(0, 15, "糖果工厂大冒险", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.set_font("yh", "", 16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "蛋仔派对 - 自定义地图设计", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_font("yh", "", 12)
    pdf.cell(0, 10, "类型: 竞速闯关  |  推荐人数: 4-8人  |  难度: ★★★☆☆", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)

    pdf.add_page()

    # ── 1. 地图概述 ──
    pdf.section_title("一、地图概述")
    pdf.body_text(
        "糖果工厂大冒险是一张趣味生存闯关地图。玩家置身于一个巨大的糖果加工厂中，需要穿越传送带区域、"
        "躲避从天而降的糖果雨、利用果冻弹簧弹跳过障碍，最终抵达终点。"
    )

    pdf.sub_title("整体布局")
    pdf.set_draw_color(200, 120, 50)
    pdf.set_fill_color(255, 240, 200)
    pdf.rect(15, pdf.get_y(), 180, 25, style="DF")
    y = pdf.get_y()
    pdf.set_font("yh", "", 10)
    pdf.set_xy(18, y + 4)
    pdf.set_fill_color(255, 255, 200)
    pdf.cell(35, 8, "起点", border=1, align="C", fill=True)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(40, 8, "传送带区", border=1, align="C", fill=True)
    pdf.set_fill_color(220, 255, 200)
    pdf.cell(40, 8, "糖果雨区", border=1, align="C", fill=True)
    pdf.set_fill_color(255, 220, 200)
    pdf.cell(40, 8, "果冻弹簧区", border=1, align="C", fill=True)
    pdf.set_fill_color(255, 200, 200)
    pdf.cell(25, 8, "终点", border=1, align="C", fill=True)
    pdf.ln(30)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_draw_color(0, 0, 0)

    # ── 2. 关卡设计 ──
    pdf.section_title("二、关卡设计")
    pdf.body_text("整张地图共分为 4 个关卡区域，各具特色:")

    pdf.table_row(["关卡", "名称", "核心机制"], bold=True)
    pdf.table_row(["1", "传送带跳跃", "移动平台 + 周期性切换方向"], fill=True)
    pdf.table_row(["2", "糖果雨", "天花板掉落糖果障碍物"], fill=True)
    pdf.table_row(["3", "果冻弹簧", "弹跳到移动平台上"], fill=True)
    pdf.table_row(["4", "终点", "烟花庆祝 + 排行榜"], fill=True)
    pdf.ln(3)

    # ── 3. 蛋码 ──
    pdf.section_title("三、蛋码逻辑实现")

    pdf.sub_title("3.1 传送带 - 左右循环移动")
    pdf.body_text("设计 3 个传送带平台，呈阶梯状排列，每个平台左右往返移动，玩家需找准时机跳跃通过。")
    pdf.code_block(codes["conveyor"])

    pdf.sub_title("3.2 糖果雨 - 从天而降的障碍物")
    pdf.body_text("每隔 3 秒从天花板随机位置生成糖果障碍物，高速落下，被砸中会受到伤害。")
    pdf.code_block(codes["candy"])

    pdf.sub_title("3.3 果冻弹簧区 - 弹跳机关")
    pdf.body_text("设置 4 个果冻弹簧，玩家踩上后会被弹到高空，落在前进平台上。弹簧会伴随压缩动画。")
    pdf.code_block(codes["spring"])

    pdf.sub_title("3.4 终点 - 烟花庆祝")
    pdf.body_text("首个抵达终点的玩家触发烟花特效，全屏显示排名。")
    pdf.code_block(codes["finish"])

    pdf.sub_title("3.5 通关计时器")
    pdf.code_block(codes["timer"])

    # ── 4. 配置参数 ──
    pdf.section_title("四、地图参数配置")
    pdf.ln(2)
    pdf.table_row(["参数", "值"], bold=True)
    pdf.table_row(["地图类型", "竞速 / 闯关"], fill=True)
    pdf.table_row(["推荐人数", "4 - 8 人"], fill=True)
    pdf.table_row(["难度评级", "★★★☆☆ (中等)"], fill=True)
    pdf.table_row(["预计通关时间", "60 - 90 秒"], fill=True)
    pdf.table_row(["存档点", "每关结束处各 1 个"], fill=True)
    pdf.ln(5)

    # ── 5. 搭建建议 ──
    pdf.section_title("五、搭建建议")
    pdf.body_text(
        "1. 地图尺寸建议 60x40 单位，高度 40 单位\n"
        "2. 传送带使用金属质感方块，搭配红/蓝动态灯光\n"
        "3. 糖果雨区使用彩色圆形方块作为糖果，大小 1.5 单位\n"
        "4. 果冻弹簧区使用半透明材质，配合绿色调\n"
        "5. 终点区域用金色方块围成拱门形状\n"
        "6. 整体配色: 粉色 / 橙色 / 黄色为主色调"
    )

    pdf.output("D:/firstCC/糖果工厂大冒险_地图设计.pdf")
    print("PDF 生成成功: D:/firstCC/糖果工厂大冒险_地图设计.pdf")


if __name__ == "__main__":
    build()
