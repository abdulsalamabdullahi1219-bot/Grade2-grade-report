from loader import load_data
from dataset_info import get_headcount
from opt import opt_mean
from chm212 import chm212_mean
from chm213 import chm213_mean
from eng import eng_mean
from gst import gst_mean
from report_builder import build_report

# Step 1: Load data
df = load_data()

# Step 2: Headcount
headcount = get_headcount(df)

# Step 3: Calculate means
opt = opt_mean(df)
chm212 = chm212_mean(df)
chm213 = chm213_mean(df)
eng = eng_mean(df)
gst = gst_mean(df)

# Step 4: Build report
report = build_report(headcount, opt, chm212, chm213, eng, gst)

# Step 5: Save report
with open("report.txt", "w") as f:
    f.write(report)

# Step 6: Display
print("Report successfully generated as 'report.txt'!")
print("\n--- Displaying Generated Report ---")
print(open("report.txt").read())
