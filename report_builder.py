def build_report(headcount, opt, chm212, chm213, eng, gst):
    return (
        "============ STUDENT PERFORMANCE REPORT ============\n"
        f"Total Students Processed: {headcount}\n\n"
        f"Average OPT211 Score: {opt:.2f}\n"
        f"Average CHM212 Score: {chm212:.2f}\n"
        f"Average CHM213 Score: {chm213:.2f}\n"
        f"Average ENG211 Score: {eng:.2f}\n"
        f"Average GST212 Score: {gst:.2f}\n"
        "====================================================\n"
    )
