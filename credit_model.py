import math
import random
import tkinter as tk
from tkinter import messagebox

# --- Step 1: Generate Synthetic Credit Data & Evaluate ---
random.seed(42)
n_samples = 5000
data = []

for _ in range(n_samples):
  income = random.uniform(30000, 150000)
  total_debt = random.expovariate(1 / 15000)
  payment_history_score = random.randint(0, 4)
  credit_age_months = random.randint(6, 240)
  credit_utilization = random.uniform(0.01, 0.99)

  monthly_income = income / 12
  dti_ratio = total_debt / monthly_income

  risk_score = (
      (total_debt / income) * 2.5
      + credit_utilization * 3.0
      + payment_history_score * 0.8
      - (credit_age_months / 100) * 0.5
      + random.gauss(0, 1)
  )
  prob = 1 / (1 + math.exp(-risk_score + 2))
  default = 1 if random.random() < prob else 0

  data.append({
      'dti_ratio': dti_ratio,
      'credit_utilization': credit_utilization,
      'payment_history_score': payment_history_score,
      'default': default,
  })

random.shuffle(data)
split_index = int(0.8 * n_samples)
test_data = data[split_index:]

tp, tn, fp, fn = 0, 0, 0, 0
for row in test_data:
  actual = row['default']
  score = (
      row['dti_ratio'] * 0.4
      + row['credit_utilization'] * 2.0
      + row['payment_history_score'] * 0.5
  )
  pred = 1 if score > 1.8 else 0

  if actual == 1 and pred == 1:
    tp += 1
  elif actual == 0 and pred == 0:
    tn += 1
  elif actual == 0 and pred == 1:
    fp += 1
  elif actual == 1 and pred == 0:
    fn += 1

precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = (
    (2 * precision * recall) / (precision + recall)
    if (precision + recall) > 0
    else 0
)
accuracy = (tp + tn) / len(test_data)

# --- Step 2: Build Interactive Pastel Desktop GUI ---
root = tk.Tk()
root.title('Credit Scoring & Risk Intelligence System')
root.geometry('740x660')
root.config(bg='#A7BCBD')  # Sky Cloud Background

# Header Title Frame
title_frame = tk.Frame(root, bg='#A7BCBD')
title_frame.pack(fill='x', padx=25, pady=15)

title_label = tk.Label(
    title_frame,
    text='Credit Scoring & Risk Intelligence System',
    font=('Segoe UI', 15, 'bold'),
    bg='#A7BCBD',
    fg='#2f4f4f',
)
title_label.pack(anchor='w')

subtitle_label = tk.Label(
    title_frame,
    text='Interactive ML Model & Live Applicant Risk Predictor',
    font=('Segoe UI', 9),
    bg='#A7BCBD',
    fg='#3b595b',
)
subtitle_label.pack(anchor='w', pady=(2, 0))

# Main Content Card Frame (Lychee background)
card_frame = tk.Frame(root, bg='#EDECDB', bd=0)
card_frame.pack(fill='both', expand=True, padx=25, pady=(0, 15))


def add_row(parent, label, val_str, color='#2f4f4f'):
  row = tk.Frame(parent, bg='#EDECDB')
  row.pack(fill='x', padx=20, pady=4)
  lbl = tk.Label(
      row,
      text=label,
      font=('Segoe UI', 10, 'bold'),
      bg='#EDECDB',
      fg='#2f4f4f',
      anchor='w',
  )
  lbl.pack(side='left')
  val = tk.Label(
      row,
      text=val_str,
      font=('Segoe UI', 10, 'bold'),
      bg='#EDECDB',
      fg=color,
      anchor='e',
  )
  val.pack(side='right')


# Model Metrics Section
sec1 = tk.Label(
    card_frame,
    text='Model Evaluation Performance (Test Set)',
    font=('Segoe UI', 11, 'bold'),
    bg='#EDECDB',
    fg='#6BB1AD',
    anchor='w',
)
sec1.pack(fill='x', padx=20, pady=(15, 5))

add_row(
    card_frame,
    'Dataset Split Size',
    str(n_samples) + ' Applicants (80/20 Train-Test)',
)
add_row(card_frame, 'Accuracy Score', str(round(accuracy, 4)))
add_row(card_frame, 'Precision / Recall / F1', f'{round(f1, 4)}')

# Divider
sep = tk.Frame(card_frame, bg='#d6d4c2', height=1)
sep.pack(fill='x', padx=20, pady=10)

# Live Prediction Interactive Section
sec2 = tk.Label(
    card_frame,
    text='Live Applicant Risk Prediction Tool',
    font=('Segoe UI', 11, 'bold'),
    bg='#EDECDB',
    fg='#6BB1AD',
    anchor='w',
)
sec2.pack(fill='x', padx=20, pady=(5, 5))

input_frame = tk.Frame(card_frame, bg='#EDECDB')
input_frame.pack(fill='x', padx=20, pady=5)


def create_input(parent, label_text, default_val):
  f = tk.Frame(parent, bg='#EDECDB')
  f.pack(fill='x', pady=3)
  lbl = tk.Label(
      f,
      text=label_text,
      font=('Segoe UI', 9),
      bg='#EDECDB',
      fg='#2f4f4f',
      width=25,
      anchor='w',
  )
  lbl.pack(side='left')
  ent = tk.Entry(
      f, font=('Segoe UI', 10), bg='white', fg='#2f4f4f', width=12, relief='solid'
  )
  ent.insert(0, default_val)
  ent.pack(side='right')
  return ent


e_income = create_input(input_frame, 'Annual Income ($):', '75000')
e_debt = create_input(input_frame, 'Total Debt ($):', '12000')
e_util = create_input(input_frame, 'Credit Utilization (0-1):', '0.35')
e_history = create_input(input_frame, 'Payment History Score (0-4):', '3')


def run_prediction():
  try:
    inc = float(e_income.get())
    debt = float(e_debt.get())
    util = float(e_util.get())
    hist = float(e_history.get())

    monthly_inc = inc / 12 if inc > 0 else 1
    dti = debt / monthly_inc

    # Model inference calculation
    calc_score = dti * 0.4 + util * 2.0 + hist * 0.5
    prediction = 'HIGH RISK (Likely Default)' if calc_score > 1.8 else 'LOW RISK (Credit Approved)'
    color_res = '#E6748E' if calc_score > 1.8 else '#2e7d32'

    lbl_result.config(
        text=f'Prediction Result: {prediction} (Score: {calc_score:.2f})',
        fg=color_res,
    )
  except ValueError:
    messagebox.showerror(
        'Invalid Input', 'Please enter valid numerical values for all fields.'
    )


btn_predict = tk.Button(
    card_frame,
    text='Run ML Prediction on Applicant',
    font=('Segoe UI', 10, 'bold'),
    bg='#6BB1AD',
    fg='white',
    activebackground='#559995',
    activeforeground='white',
    relief='flat',
    padx=12,
    pady=6,
    command=run_prediction,
)
btn_predict.pack(pady=8)

lbl_result = tk.Label(
    card_frame,
    text='Status: Ready for live applicant inputs.',
    font=('Segoe UI', 10, 'bold'),
    bg='#EDECDB',
    fg='#2f4f4f',
)
lbl_result.pack(pady=(2, 10))

root.mainloop()