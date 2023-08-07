import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import *

plt.rcParams['axes.prop_cycle'] = plt.cycler(
    color=["blue", "lightblue", "darkblue", "aquamarine", "cyan"]
)

# Chart 1: Bar chart of sales data 
fig1, ax1 = plt.subplots()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Sales by Product")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
# plt.show()

# Chart 2: Horizontal bar chart of inventory data 
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Inventory by Product")

ax2.set_xlabel("Product")
ax2.set_ylabel("Quantity")
# plt.show()

# Chart 3: Pie chart of product data 
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title("Product Data")
# plt.show()

# Chart 4: Line chart of sales by year 
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales Year Data")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")
# plt.show()

# Chart 5: Area chart of inventory by month 
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")
# plt.show()

# Create a window and add charts 
root = tk.Tk()
root.title("Dashboard")
# zoomed = maximized 
root.state("zoomed")

# Create the lefthand side frame
side_frame = tk.Frame(root, bg="purple")
side_frame.pack(side="left", fill="y")

# Side frame label to title dashboard 
label = tk.Label(side_frame, text="Dashboard", bg="purple", fg="white", font=35)
label.pack(pady=50, padx=20)

# Create a frame that will house the frames 
charts_frame = tk.Frame(root)
charts_frame.pack()

# Create upper frame 
upper_frame = tk.Frame(charts_frame)
# fill = both fills both the x and y axis, expand allows it to expand 
upper_frame.pack(fill="both", expand=True)

# Add the first chart into upper_frame using FigureCanvasTkAgg 
canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

# Add the second chart into upper_frame 
canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

# Add the third chart into upper frame 
canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

# Create lower frame 
lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

# Add the fourth chart into the lower frame 
canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

# Add the fifth chart into the lower frame 
canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.draw()
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

# Eventloop 
root.mainloop()
