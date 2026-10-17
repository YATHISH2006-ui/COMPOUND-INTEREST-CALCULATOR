import tkinter as tk
from tkinter import ttk

bank_rates = {"SBI": 6.50, "HDFC Bank": 7.00, "ICICI Bank": 6.80, "Axis Bank": 6.90, "PNB": 6.60}

mutual_funds = {"HDFC Equity Fund": 12.5, "SBI Bluechip Fund": 11.8, "ICICI Prudential Fund": 12.0, "Axis Growth Fund": 11.5}

govt_schemes = {"PPF": 7.10, "NSC": 7.70, "Sukanya Samriddhi": 8.20}

loan_rates = {
    "SBI": {"Personal": 11.00, "Home": 8.50, "Car": 8.70, "Education": 8.30},
    "HDFC Bank": {"Personal": 11.50, "Home": 8.60, "Car": 8.90, "Education": 8.50},
    "ICICI Bank": {"Personal": 11.25, "Home": 8.55, "Car": 8.80, "Education": 8.40},
    "Axis Bank": {"Personal": 11.75, "Home": 8.65, "Car": 8.95, "Education": 8.60},
    "PNB": {"Personal": 10.90, "Home": 8.40, "Car": 8.60, "Education": 8.20}
}

purpose_to_loan = {
    "Home Purchase": "Home",
    "Car Purchase": "Car",
    "Education": "Education",
    "Other / General Purchase": "Personal"
}

r = tk.Tk()
r.title("Compound Interest Calculator")
r.geometry("560x760")
r.configure(bg = "#f4f5f7")
r.option_add("*TCombobox*Listbox.font", ("Segoe UI", 14))

navbar = tk.Frame(r, bg = "#2c3e50", height = 50)
navbar.pack(fill = "x")

landing_frame = tk.Frame(r, bg = "#f4f5f7")
home_frame = tk.Frame(r, bg = "#f4f5f7")
bank_frame = tk.Frame(r, bg = "#f4f5f7")
loan_frame = tk.Frame(r, bg = "#f4f5f7")


def create_scrollable_container(parent_frame):
    canvas = tk.Canvas(parent_frame, bg="#f4f5f7", highlightthickness=0)
    scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
    scrollable_content = tk.Frame(canvas, bg="#f4f5f7")

    scrollable_content.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    window_id = canvas.create_window((0, 0), window=scrollable_content, anchor="nw")

   
    canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    def _on_mousewheel(event):
        if event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")
        else:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_mousewheel(event):
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_mousewheel)
        canvas.bind_all("<Button-5>", _on_mousewheel)

    def _unbind_mousewheel(event):
        canvas.unbind_all("<MouseWheel>")
        canvas.unbind_all("<Button-4>")
        canvas.unbind_all("<Button-5>")

    canvas.bind("<Enter>", _bind_mousewheel)
    canvas.bind("<Leave>", _unbind_mousewheel)

    return scrollable_content

def set_active(active_btn):
    for btn in (nav_btn0, nav_btn1, nav_btn2, nav_btn3):
        btn.config(bg = "#2c3e50")
    active_btn.config(bg = "#3b6ea5")

def show_landing():
    home_frame.pack_forget()
    bank_frame.pack_forget()
    loan_frame.pack_forget()
    landing_frame.pack(fill = "both", expand = True)
    set_active(nav_btn0)

def show_home():
    landing_frame.pack_forget()
    bank_frame.pack_forget()
    loan_frame.pack_forget()
    home_frame.pack(fill = "both", expand = True)
    set_active(nav_btn1)

def show_bank():
    landing_frame.pack_forget()
    home_frame.pack_forget()
    loan_frame.pack_forget()
    bank_frame.pack(fill = "both", expand = True)
    set_active(nav_btn2)

def show_loan():
    landing_frame.pack_forget()
    home_frame.pack_forget()
    bank_frame.pack_forget()
    loan_frame.pack(fill = "both", expand = True)
    set_active(nav_btn3)

nav_btn0 = tk.Button(navbar, text = "Home", bg = "#2c3e50", fg = "white", bd = 0, font = ("Segoe UI", 12), command = show_landing)
nav_btn0.pack(side = "left", padx = 15, pady = 10)

nav_btn1 = tk.Button(navbar, text = "Calculator", bg = "#2c3e50", fg = "white", bd = 0, font = ("Segoe UI", 12), command = show_home)
nav_btn1.pack(side = "left", padx = 15, pady = 10)

nav_btn2 = tk.Button(navbar, text = "Bank Rates", bg = "#2c3e50", fg = "white", bd = 0, font = ("Segoe UI", 12), command = show_bank)
nav_btn2.pack(side = "left", padx = 15, pady = 10)

nav_btn3 = tk.Button(navbar, text = "Loan Checker", bg = "#2c3e50", fg = "white", bd = 0, font = ("Segoe UI", 12), command = show_loan)
nav_btn3.pack(side = "left", padx = 15, pady = 10)

landing_card = tk.Frame(landing_frame, bg = "white", highlightbackground = "#d1d5db", highlightthickness = 1)
landing_card.pack(pady = 60, padx = 50, fill = "x")

landing_heading = tk.Label(landing_card, text = "Finance Toolkit", font = ("Playfair Display", 24, "bold"), bg = "white", fg = "#1e293b")
landing_heading.pack(pady = (30, 5))

landing_sub = tk.Label(landing_card, text = "Choose what you would like to explore", font = ("Segoe UI", 12), bg = "white", fg = "#6b7280")
landing_sub.pack(pady = (0, 25))

landing_btn1 = tk.Button(landing_card, text = "Compound Interest Calculator", width = 30, font = ("Segoe UI", 12), bg = "#3b6ea5", fg = "white", bd = 0, command = show_home)
landing_btn1.pack(pady = 8, ipady = 6)

landing_btn2 = tk.Button(landing_card, text = "Bank Rates & Investments", width = 30, font = ("Segoe UI", 12), bg = "#3b6ea5", fg = "white", bd = 0, command = show_bank)
landing_btn2.pack(pady = 8, ipady = 6)

landing_btn3 = tk.Button(landing_card, text = "Loan Eligibility Checker", width = 30, font = ("Segoe UI", 12), bg = "#3b6ea5", fg = "white", bd = 0, command = show_loan)
landing_btn3.pack(pady = (8, 30), ipady = 6)


home_card = tk.Frame(home_frame, bg = "white", highlightbackground = "#d1d5db", highlightthickness = 1)
home_card.pack(pady = 40, padx = 50, fill = "x")

heading = tk.Label(home_card, text = "Compound Interest Calculator", font = ("Playfair Display", 22, "bold"), bg = "white", fg = "#1e293b")
heading.pack(pady = (25, 20))

l1 = tk.Label(home_card, text = "Enter Your Principle Amount:", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l1.pack()
e1 = tk.Entry(home_card, font = ("Segoe UI", 13), relief = "flat", bg = "#f9fafb", highlightthickness = 1, highlightbackground = "#d1d5db", highlightcolor = "#3b6ea5")
e1.pack(pady = 5, padx = 30, fill = "x", ipady = 6)

l2 = tk.Label(home_card, text = "Enter Your offered interest rate:", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l2.pack()
e2 = tk.Entry(home_card, font = ("Segoe UI", 13), relief = "flat", bg = "#f9fafb", highlightthickness = 1, highlightbackground = "#d1d5db", highlightcolor = "#3b6ea5")
e2.pack(pady = 5, padx = 30, fill = "x", ipady = 6)

l3 = tk.Label(home_card, text = "Enter the Time Period (in Years):", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l3.pack()
e3 = tk.Entry(home_card, font = ("Segoe UI", 13), relief = "flat", bg = "#f9fafb", highlightthickness = 1, highlightbackground = "#d1d5db", highlightcolor = "#3b6ea5")
e3.pack(pady = 5, padx = 30, fill = "x", ipady = 6)

res = tk.Label(home_card, text = "", font = ("Segoe UI", 14, "bold"), bg = "white", fg = "#1e40af", wraplength = 350, justify = "left")
res.pack(pady = 10)

def go_to_interest(event):
    e2.focus()

def go_to_time(event):
    e3.focus()

def enter_pressed(event):
    calculate()

e1.bind("<Return>", go_to_interest)
e2.bind("<Return>", go_to_time)
e3.bind("<Return>", enter_pressed)

def calculate():
    try:
        principle = float(e1.get())
        interest = float(e2.get())
        time = float(e3.get())
    except ValueError:
        res.config(text = "Please enter valid numbers only")
        return

    if principle <= 0:
        res.config(text = "Your Principle Amount can't be Less than or Equal to zero")
        return

    if interest <= 0:
        res.config(text = "The Rate of Interest can't be Less than or Equal to zero")
        return

    if time <= 0:
        res.config(text = "Time can't be Less than or Equal to zero")
        return

    total = principle * pow((1 + interest/100), time)
    interest_amount = total - principle

    best_bank = ""
    best_rate = 0
    for bank in bank_rates:
        if bank_rates[bank] > best_rate:
            best_rate = bank_rates[bank]
            best_bank = bank

    if interest > best_rate:
        diff = interest - best_rate
        advice = f"Your rate beats {best_bank}'s FD rate by {diff:.2f}%"
    elif interest < best_rate:
        diff = best_rate - interest
        alt_total = principle * pow((1 + best_rate/100), time)
        extra = alt_total - total
        advice = f"{best_bank} offers {diff:.2f}% more. You could earn ₹{extra:.2f} more there"
    else:
        advice = f"Your rate matches {best_bank}'s FD rate"

    res.config(text = f"Balance: ₹{total:.2f}\nInterest: ₹{interest_amount:.2f}\n\n{advice}")

btn_row = tk.Frame(home_card, bg = "white")
btn_row.pack(pady = (10, 25))

b = tk.Button(btn_row, text = "Calculate", width = 15, font = ("Segoe UI", 11), bg = "#3b6ea5", fg = "white", bd = 0, command = calculate)
b.pack(side = "left", padx = 5)

def reset():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    res.config(text = "")

b3 = tk.Button(btn_row, text = "Reset", width = 15, font = ("Segoe UI", 11), bg = "#e5e7eb", bd = 0, command = reset)
b3.pack(side = "left", padx = 5)

bank_scroll_content = create_scrollable_container(bank_frame)

bank_card = tk.Frame(bank_scroll_content, bg = "white", highlightbackground = "#d1d5db", highlightthickness = 1)
bank_card.pack(pady = 40, padx = 50, fill = "x")

bank_heading = tk.Label(bank_card, text = "Bank FD Interest Rate Comparison", font = ("Playfair Display", 22, "bold"), bg = "white", fg = "#1e293b")
bank_heading.pack(pady = (25, 20))

bank_res = tk.Label(bank_card, text = "", font = ("Segoe UI", 13), bg = "white", fg = "#374151", justify = "left")
bank_res.pack(pady = 10)

def show_bank_rates():
    text = ""
    for bank in bank_rates:
        text = text + bank + ": " + str(bank_rates[bank]) + "%\n"
    bank_res.config(text = text)

bank_btn_row = tk.Frame(bank_card, bg = "white")
bank_btn_row.pack(pady = 5)

bank_button = tk.Button(bank_btn_row, text = "Show Bank FD Rates", width = 18, font = ("Segoe UI", 11), bg = "#3b6ea5", fg = "white", bd = 0, command = show_bank_rates)
bank_button.pack(side = "left", padx = 5)

def close_bank_rates():
    bank_res.config(text = "")

bank_close_button = tk.Button(bank_btn_row, text = "Close", width = 10, font = ("Segoe UI", 11), bg = "#e5e7eb", bd = 0, command = close_bank_rates)
bank_close_button.pack(side = "left", padx = 5)

mf_heading = tk.Label(bank_card, text = "Mutual Fund Plans (Avg. Annual Returns)", font = ("Segoe UI", 14, "bold"), bg = "white", fg = "#334155")
mf_heading.pack(pady = (25, 10))

mf_note = tk.Label(bank_card, text = "Market-linked, returns are not guaranteed", font = ("Segoe UI", 9), bg = "white", fg = "#6b7280")
mf_note.pack()

mf_res = tk.Label(bank_card, text = "", font = ("Segoe UI", 13), bg = "white", fg = "#374151", justify = "left")
mf_res.pack(pady = 10)

def show_mutual_funds():
    text = ""
    for fund in mutual_funds:
        text = text + fund + ": " + str(mutual_funds[fund]) + "%\n"
    mf_res.config(text = text)

mf_btn_row = tk.Frame(bank_card, bg = "white")
mf_btn_row.pack(pady = 5)

mf_button = tk.Button(mf_btn_row, text = "Show Mutual Fund Plans", width = 20, font = ("Segoe UI", 11), bg = "#3b6ea5", fg = "white", bd = 0, command = show_mutual_funds)
mf_button.pack(side = "left", padx = 5)

def close_mutual_funds():
    mf_res.config(text = "")

mf_close_button = tk.Button(mf_btn_row, text = "Close", width = 10, font = ("Segoe UI", 11), bg = "#e5e7eb", bd = 0, command = close_mutual_funds)
mf_close_button.pack(side = "left", padx = 5)

govt_heading = tk.Label(bank_card, text = "Government Savings Schemes", font = ("Segoe UI", 14, "bold"), bg = "white", fg = "#334155")
govt_heading.pack(pady = (25, 10))

govt_res = tk.Label(bank_card, text = "", font = ("Segoe UI", 13), bg = "white", fg = "#374151", justify = "left")
govt_res.pack(pady = 10)

def show_govt_schemes():
    text = ""
    for scheme in govt_schemes:
        text = text + scheme + ": " + str(govt_schemes[scheme]) + "%\n"
    govt_res.config(text = text)

govt_btn_row = tk.Frame(bank_card, bg = "white")
govt_btn_row.pack(pady = (5, 25))

govt_button = tk.Button(govt_btn_row, text = "Show Govt. Schemes", width = 18, font = ("Segoe UI", 11), bg = "#3b6ea5", fg = "white", bd = 0, command = show_govt_schemes)
govt_button.pack(side = "left", padx = 5)

def close_govt_schemes():
    govt_res.config(text = "")

govt_close_button = tk.Button(govt_btn_row, text = "Close", width = 10, font = ("Segoe UI", 11), bg = "#e5e7eb", bd = 0, command = close_govt_schemes)
govt_close_button.pack(side = "left", padx = 5)

loan_scroll_content = create_scrollable_container(loan_frame)

loan_card = tk.Frame(loan_scroll_content, bg = "white", highlightbackground = "#d1d5db", highlightthickness = 1)
loan_card.pack(pady = 40, padx = 50, fill = "x")

loan_heading = tk.Label(loan_card, text = "Loan Eligibility Checker", font = ("Playfair Display", 22, "bold"), bg = "white", fg = "#1e293b")
loan_heading.pack(pady = (25, 20))

l6 = tk.Label(loan_card, text = "Enter Your Monthly Income:", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l6.pack()
e4 = tk.Entry(loan_card, font = ("Segoe UI", 13), relief = "flat", bg = "#f9fafb", highlightthickness = 1, highlightbackground = "#d1d5db", highlightcolor = "#3b6ea5")
e4.pack(pady = 5, padx = 30, fill = "x", ipady = 6)

l7 = tk.Label(loan_card, text = "Enter Required Loan Amount:", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l7.pack()
e5 = tk.Entry(loan_card, font = ("Segoe UI", 13), relief = "flat", bg = "#f9fafb", highlightthickness = 1, highlightbackground = "#d1d5db", highlightcolor = "#3b6ea5")
e5.pack(pady = 5, padx = 30, fill = "x", ipady = 6)

l8 = tk.Label(loan_card, text = "Select Your Bank:", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l8.pack()
bank_var = tk.StringVar()
bank_dropdown = ttk.Combobox(loan_card, textvariable = bank_var, values = list(loan_rates.keys()), state = "readonly", font = ("Segoe UI", 14))
bank_dropdown.pack(pady = 5, padx = 30, fill = "x", ipady = 4)

l9 = tk.Label(loan_card, text = "Purpose of Loan:", font = ("Segoe UI", 13), bg = "white", fg = "#374151")
l9.pack()
purpose_var = tk.StringVar()
purpose_dropdown = ttk.Combobox(loan_card, textvariable = purpose_var, values = list(purpose_to_loan.keys()), state = "readonly", font = ("Segoe UI", 13))
purpose_dropdown.pack(pady = 5, padx = 30, fill = "x")

loan_res = tk.Label(loan_card, text = "", font = ("Segoe UI", 13, "bold"), bg = "white", fg = "#1e40af", wraplength = 350, justify = "left")
loan_res.pack(pady = 10)

def check_loan():
    try:
        income = float(e4.get())
        loan_amount = float(e5.get())
    except ValueError:
        loan_res.config(text = "Please enter valid numbers only")
        return

    if income <= 0:
        loan_res.config(text = "Income can't be zero or negative")
        return

    if loan_amount <= 0:
        loan_res.config(text = "Loan amount can't be zero or negative")
        return

    bank = bank_var.get()
    purpose = purpose_var.get()

    if bank not in loan_rates:
        loan_res.config(text = "Please select a bank")
        return

    if purpose not in purpose_to_loan:
        loan_res.config(text = "Please select a loan purpose")
        return

    max_loan = income * 60

    if loan_amount <= max_loan:
        eligibility_msg = "You are eligible for this loan amount"
    else:
        shortfall = loan_amount - max_loan
        eligibility_msg = f"You are eligible up to ₹{max_loan:.2f}, which is ₹{shortfall:.2f} less than requested"

    loan_type = purpose_to_loan[purpose]
    personal_rate = loan_rates[bank]["Personal"]

    if loan_type == "Personal":
        recommendation = "For a general purchase, a Personal Loan is your best available option here"
    else:
        specific_rate = loan_rates[bank][loan_type]
        diff = personal_rate - specific_rate
        recommendation = f"A {loan_type} Loan is more efficient than a Personal Loan here. It offers {diff:.2f}% lower interest at {bank} ({specific_rate}% vs {personal_rate}%)"

    loan_res.config(text = f"Maximum Eligible Amount: ₹{max_loan:.2f}\n{eligibility_msg}\n\n{recommendation}")

loan_button = tk.Button(loan_card, text = "Check Eligibility", width = 25, font = ("Segoe UI", 11), bg = "#3b6ea5", fg = "white", bd = 0, command = check_loan)
loan_button.pack(pady = (5, 25))

show_landing()

r.mainloop()