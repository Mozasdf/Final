import psutil
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import time

# 프로세스 목록 가져오기 (정렬 포함)
def get_top_processes(limit=10):
    # 첫 번째 호출로 예열
    for p in psutil.process_iter():
        try:
            p.cpu_percent()
        except psutil.NoSuchProcess:
            continue

    time.sleep(1)

    total_cpu = psutil.cpu_count(logical=True) * 100
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = p.info
            if info['name'] == 'System Idle Process':
                continue  # 제외 처리
            # CPU%를 전체 시스템 기준으로 정규화
            info['cpu_percent'] = min((info['cpu_percent'] / total_cpu) * 100, 100)
            procs.append(info)
        except psutil.NoSuchProcess:
            continue

    procs.sort(key=lambda x: x['cpu_percent'], reverse=True)
    return procs[:limit]

# GUI에 리스트 삽입
def update_process_list():
    for row in tree.get_children():
        tree.delete(row)
    top_procs = get_top_processes()
    for proc in top_procs:
        tree.insert('', tk.END, values=(
            proc['pid'],
            proc['name'],
            f"{proc['cpu_percent']:.1f}",
            f"{proc['memory_percent']:.1f}"
        ))
    root.after(1000, update_process_list)  # 1초마다 자동 갱신

# 그래프 출력
def show_graph():
    top_procs = get_top_processes()
    names = [p['name'].replace('.exe', '') for p in top_procs]
    cpu_vals = [p['cpu_percent'] for p in top_procs]
    ram_vals = [p['memory_percent'] for p in top_procs]

    fig, ax1 = plt.subplots(figsize=(12, 5))

    ax1.bar(names, cpu_vals, label='CPU %', alpha=0.7)
    ax1.set_ylabel('CPU %', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_ylim(0, 100)

    ax2 = ax1.twinx()
    ax2.plot(names, ram_vals, color='green', marker='o', label='RAM %')
    ax2.set_ylabel('RAM %', color='green')
    ax2.tick_params(axis='y', labelcolor='green')
    ax2.set_ylim(0, 100)

    plt.title("Top Processes: CPU & RAM Usage (0~100%)")
    plt.xticks(rotation=45)
    fig.tight_layout()
    plt.show()

# GUI 설정
root = tk.Tk()
root.title("프로세스 자원 소비 분석기")
root.geometry("700x420")

columns = ('PID', '이름', 'CPU%', 'RAM%')
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor='center', width=150, stretch=True)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="그래프로 보기", command=show_graph, width=20).pack()

update_process_list()
root.mainloop()
