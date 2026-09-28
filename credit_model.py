import math
import random
import tkinter as tk

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

# --- Step 2: Build Modern Styled Desktop GUI ---
root = tk.Tk()
root.title('Credit Scoring & Risk Intelligence Dashboard')
root.geometry('700x560')
root.config(bg='#0f172a')  # Modern dark slate background

# Header Title
title_frame = tk.Frame(root, bg='#0f172a')
title_frame.pack(fill='x', padx=25, pady=20)

title_label = tk.Label(
    title_frame,
    text='Credit Scoring & Risk Intelligence System',
    font=('Segoe UI', 16, 'bold'),
    bg='#0f172a',
    fg='#f8fafc',
)
title_label.pack(anchor='w')

subtitle_label = tk.Label(
    title_frame,
    text='Machine Learning Pipeline & Performance Evaluation Suite',
    font=('Segoe UI', 10),
    bg='#0f172a',
    fg='#94a3b8',
)
subtitle_label.pack(anchor='w', pady=(2, 0))

# Main Content Card Frame
card_frame = tk.Frame(root, bg='#1e293b', bd=0)
card_frame.pack(fill='both', expand=True, padx=25, pady=(0, 15))


# Helper function to create metric rows inside the card
def add_metric_row(parent, label, value, color='#38bdf8'):
  row = tk.Frame(parent, bg='#1e293b')
  row.pack(fill='x', padx=25, pady=6)
  lbl = tk.Label(
      row,
      text=label,
      font=('Segoe UI', 11),
      bg='#1e293b',
      fg='#cbd5e1',
      anchor='w',
  )
  lbl.pack(side='left')
  val = tk.Label(
      row,
      text=value,
      font=('Segoe UI', 11, 'bold'),
      bg='#1e293b',
      fg=color,
      anchor='e',
  )
  val.pack(side='right')


# Section 1 Header
sec1 = tk.Label(
    card_frame,
    text='Model Performance Metrics',
    font=('Segoe UI', 12, 'bold'),
    bg='#1e293b',
    fg='#f8fafc',
    anchor='w',
)
sec1.pack(fill='x', padx=25, pady=(20, 5))

add_metric_row(
    card_frame,
    'Dataset Split Size (Train / Test)',
    str(n_samples) + ' Total Applicants (80/20)',
    '#f8fafc',
)
add_metric_row(card_frame, 'Accuracy Score', str(round(accuracy, 4)))
add_metric_row(card_frame, 'Precision Score', str(round(precision, 4)))
add_metric_row(card_frame, 'Recall Score', str(round(recall, 4)))
add_metric_row(card_frame, 'F1-Harmonic Score', str(round(f1, 4)), '#4ade80')

# Divider Line
sep = tk.Frame(card_frame, bg='#334155', height=1)
sep.pack(fill='x', padx=25, pady=15)

# Section 2 Header
sec2 = tk.Label(
    card_frame,
    text='Confusion Matrix Breakdown',
    font=('Segoe UI', 12, 'bold'),
    bg='#1e293b',
    fg='#f8fafc',
    anchor='w',
)
sec2.pack(fill='x', padx=25, pady=(0, 5))

add_metric_row(
    card_frame, 'True Negatives (Accurate Non-Defaults)', str(tn)
)
add_metric_row(card_frame, 'False Positives (Type I Error)', str(fp), '#f87171')
add_metric_row(card_frame, 'False Negatives (Type II Error)', str(fn), '#f87171')
add_metric_row(card_frame, 'True Positives (Accurate Defaults)', str(tp))

# Footer Button Frame
btn_frame = tk.Frame(root, bg='#0f172a')
btn_frame.pack(fill='x', padx=25, pady=(0, 20))


def trigger_simulation():
  pass  # Add actions if needed


btn = tk.Button(
    btn_frame,
    text='Pipeline Executed Successfully',
    font=('Segoe UI', 10, 'bold'),
    bg='#0284c7',
    fg='white',
    activebackground='#0369a1',
    activeforeground='white',
    relief='flat',
    padx=15,
    pady=8,
)
btn.pack(side='right')

root.mainloop()