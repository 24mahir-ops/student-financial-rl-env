name: Student Financial Decision Environment

entrypoint: app.py

observation:
  money: float
  savings: float
  investments: float
  income: float
  expenses: float
  happiness: float
  month: int

actions:
  - save
  - invest_low
  - invest_high
  - spend
  - learn

reward: float