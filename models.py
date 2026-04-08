import random
from models import Observation, Action, Reward

class StudentEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.state_data = {
            "money": 5000,
            "savings": 2000,
            "investments": 3000,
            "income": 2000,
            "expenses": 1500,
            "happiness": 70,
            "month": 1
        }
        return Observation(**self.state_data)

    def state(self):
        return Observation(**self.state_data)

    def step(self, action: Action):
        prev_money = self.state_data["money"]

        # monthly update
        self.state_data["money"] += self.state_data["income"]
        self.state_data["money"] -= self.state_data["expenses"]

        act = action.action

        if act == "save":
            self.state_data["money"] -= 500
            self.state_data["savings"] += 500

        elif act == "invest_low":
            self.state_data["investments"] += random.randint(100, 300)

        elif act == "invest_high":
            if random.random() > 0.5:
                self.state_data["investments"] += 800
            else:
                self.state_data["investments"] -= 800

        elif act == "spend":
            self.state_data["money"] -= 500
            self.state_data["happiness"] += 10

        elif act == "learn":
            self.state_data["income"] += 500

        self.state_data["month"] += 1

        # reward
        reward_val = (self.state_data["money"] - prev_money) / 1000
        reward_val = max(min(reward_val, 1), -1)

        done = self.state_data["money"] <= 0 or self.state_data["month"] > 12

        return (
            Observation(**self.state_data),
            Reward(value=reward_val),
            done,
            {}
        )