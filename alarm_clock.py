import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
import winsound
from datetime import datetime
import json
import os

DATA_FILE = "alarms.json"


class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("闹钟")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.alarms = self.load_alarms()
        self.alarm_thread_running = True
        self.current_alarm_index = None

        self.setup_ui()
        self.update_clock()
        threading.Thread(target=self.check_alarm, daemon=True).start()

    # ── UI ──
    def setup_ui(self):
        # 当前时间
        self.time_label = tk.Label(self.root, font=("Arial", 48), fg="#333")
        self.time_label.pack(pady=20)

        self.date_label = tk.Label(self.root, font=("Arial", 14), fg="#666")
        self.date_label.pack()

        # 设置闹钟区域
        frame = tk.LabelFrame(self.root, text="设置闹钟", padx=10, pady=10)
        frame.pack(pady=10, fill="x", padx=20)

        tk.Label(frame, text="时:").grid(row=0, column=0, padx=2)
        self.hour_spin = ttk.Spinbox(frame, from_=0, to=23, width=5, format="%02.0f")
        self.hour_spin.grid(row=0, column=1, padx=2)
        self.hour_spin.set("08")

        tk.Label(frame, text="分:").grid(row=0, column=2, padx=2)
        self.min_spin = ttk.Spinbox(frame, from_=0, to=59, width=5, format="%02.0f")
        self.min_spin.grid(row=0, column=3, padx=2)
        self.min_spin.set("00")

        tk.Label(frame, text="标签:").grid(row=0, column=4, padx=2)
        self.label_entry = tk.Entry(frame, width=10)
        self.label_entry.grid(row=0, column=5, padx=2)
        self.label_entry.insert(0, "起床")

        ttk.Button(frame, text="添加闹钟", command=self.add_alarm).grid(row=0, column=6, padx=5)

        # 闹钟列表
        list_frame = tk.LabelFrame(self.root, text="闹钟列表", padx=10, pady=10)
        list_frame.pack(fill="both", expand=True, padx=20, pady=5)

        self.listbox = tk.Listbox(list_frame, height=6, font=("Arial", 11))
        self.listbox.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(list_frame)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(btn_frame, text="删除选中", command=self.delete_alarm).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="启用/禁用", command=self.toggle_alarm).pack(side="left", padx=5)

        self.refresh_listbox()

    # ── 时钟更新 ──
    def update_clock(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.date_label.config(text=now.strftime("%Y-%m-%d %A"))
        self.root.after(1000, self.update_clock)

    # ── 闹钟数据管理 ──
    def load_alarms(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_alarms(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.alarms, f, ensure_ascii=False, indent=2)

    def add_alarm(self):
        h = int(self.hour_spin.get())
        m = int(self.min_spin.get())
        label = self.label_entry.get().strip() or "闹钟"
        if not (0 <= h <= 23 and 0 <= m <= 59):
            messagebox.showerror("错误", "时间格式不正确")
            return
        self.alarms.append({"hour": h, "minute": m, "label": label, "enabled": True})
        self.save_alarms()
        self.refresh_listbox()

    def delete_alarm(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            del self.alarms[idx]
            self.save_alarms()
            self.refresh_listbox()

    def toggle_alarm(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            self.alarms[idx]["enabled"] = not self.alarms[idx]["enabled"]
            self.save_alarms()
            self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for a in self.alarms:
            status = "ON" if a["enabled"] else "OFF"
            self.listbox.insert(tk.END, f"[{status}] {a['hour']:02d}:{a['minute']:02d} - {a['label']}")
            color = "#333" if a["enabled"] else "#aaa"
            self.listbox.itemconfig(tk.END, fg=color)

    # ── 闹钟检测线程 ──
    def check_alarm(self):
        while self.alarm_thread_running:
            now = datetime.now()
            for i, a in enumerate(self.alarms):
                if a["enabled"] and a["hour"] == now.hour and a["minute"] == now.minute:
                    self.root.after(0, self.ring_alarm, i)
                    time.sleep(60)
            time.sleep(1)

    # ── 响铃 ──
    def ring_alarm(self, idx):
        alarm = self.alarms[idx]
        top = tk.Toplevel(self.root)
        top.title("闹钟响了!")
        top.geometry("350x200")
        top.resizable(False, False)

        tk.Label(top, text="⏰", font=("Arial", 40)).pack(pady=10)
        tk.Label(top, text=f"{alarm['label']}", font=("Arial", 20, "bold")).pack()
        tk.Label(top, text=f"{alarm['hour']:02d}:{alarm['minute']:02d}", font=("Arial", 16)).pack()

        def stop_alarm():
            if hasattr(stop_alarm, "playing") and stop_alarm.playing:
                stop_alarm.playing = False
            top.destroy()

        def snooze():
            if hasattr(stop_alarm, "playing") and stop_alarm.playing:
                stop_alarm.playing = False
            # 5分钟后再响
            snooze_time = datetime.now()
            snooze_time = snooze_time.replace(second=0) + __import__("datetime").timedelta(minutes=5)
            new_alarm = {
                "hour": snooze_time.hour,
                "minute": snooze_time.minute,
                "label": f"{alarm['label']}(贪睡)",
                "enabled": True
            }
            self.alarms.append(new_alarm)
            self.save_alarms()
            self.refresh_listbox()
            top.destroy()

        btn_frame = tk.Frame(top)
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="贪睡 (5分钟)", command=snooze).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="关闭", command=stop_alarm).pack(side="left", padx=10)

        # 响铃线程
        def play_beep():
            stop_alarm.playing = True
            while stop_alarm.playing:
                try:
                    winsound.PlaySound("*", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
                except:
                    for _ in range(20):
                        if not stop_alarm.playing:
                            break
                        winsound.Beep(800, 400)
                        time.sleep(0.3)
                time.sleep(0.5)

        t = threading.Thread(target=play_beep, daemon=True)
        t.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
