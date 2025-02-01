import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Thông số hình tròn
R_big = 20  # Bán kính hình tròn lớn
R_small = 10  # Bán kính hình tròn nhỏ
num_frames = 360  # Số khung hình (1 độ mỗi bước)

# Hàm vẽ hình tròn
def draw_circle(ax, center, radius, color='b', lw=2):
    circle = plt.Circle(center, radius, fill=False, color=color, linewidth=lw)
    ax.add_patch(circle)

# Hàm cập nhật animation
def update(frame):
    ax.clear()
    ax.set_xlim(-35, 35)
    ax.set_ylim(-35, 35)
    ax.set_aspect('equal')
    ax.axis('off')

    # Vẽ hình tròn lớn
    draw_circle(ax, (0, 0), R_big, color='black', lw=2)

    # Góc quay của hình tròn nhỏ quanh hình tròn lớn (theo chiều kim đồng hồ)
    theta = np.radians(frame)  # Quay theo chiều kim đồng hồ

    # Xác định tâm của hình tròn nhỏ
    x_center = (R_big + R_small) * np.sin(theta)  # Đảm bảo bắt đầu từ 12h
    y_center = (R_big + R_small) * np.cos(theta)

    # Góc quay của hình tròn nhỏ (cùng chiều kim đồng hồ)
    phi = theta * (R_big / R_small)  # Đảm bảo quay cùng chiều kim đồng hồ

    # Vẽ hình tròn nhỏ
    draw_circle(ax, (x_center, y_center), R_small, color='blue', lw=2)

    # Vẽ mũi tên chỉ 12h trên hình tròn nhỏ
    arrow_x = x_center + R_small * np.sin(phi)  # Ban đầu chỉ thẳng lên
    arrow_y = y_center + R_small * np.cos(phi)
    ax.arrow(x_center, y_center, arrow_x - x_center, arrow_y - y_center,
             head_width=1, head_length=1.5, fc='red', ec='red')

# Tạo khung vẽ
fig, ax = plt.subplots(figsize=(6, 6))

# Animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20)

# Hiển thị animation
plt.show()
