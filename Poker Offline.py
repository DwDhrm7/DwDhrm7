import tkinter as tk
import random
from collections import Counter

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_values = {r: i for i, r in enumerate(ranks, start=2)}
hand_ranks = ['High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = rank_values[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]


def evaluate_hand(cards):
    values = sorted([c.value for c in cards], reverse=True)
    suits_list = [c.suit for c in cards]
    counts = Counter(values)
    values_by_count = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
    flush = [c for c in cards if suits_list.count(c.suit) >= 5]
    flush_vals = sorted([c.value for c in flush], reverse=True)

    def is_straight(vals):
        vals = sorted(set(vals))
        for i in range(len(vals) - 4):
            if vals[i + 4] - vals[i] == 4:
                return True, vals[i + 4]
        if set([14, 2, 3, 4, 5]).issubset(set(vals)):
            return True, 5
        return False, None

    if len(flush) >= 5:
        is_sf, sf_high = is_straight(flush_vals)
        if is_sf:
            if sf_high == 14:
                return (9, [14])  # Royal Flush
            return (8, [sf_high])  # Straight Flush

    if values_by_count[0][1] == 4:
        return (7, [values_by_count[0][0]])  # Four of a Kind
    if values_by_count[0][1] == 3 and values_by_count[1][1] >= 2:
        return (6, [values_by_count[0][0], values_by_count[1][0]])  # Full House
    if len(flush) >= 5:
        return (5, flush_vals[:5])  # Flush
    is_str, high = is_straight(values)
    if is_str:
        return (4, [high])  # Straight
    if values_by_count[0][1] == 3:
        return (3, [values_by_count[0][0]])  # Three of a Kind
    if values_by_count[0][1] == 2 and values_by_count[1][1] == 2:
        return (2, [values_by_count[0][0], values_by_count[1][0]])  # Two Pair
    if values_by_count[0][1] == 2:
        return (1, [values_by_count[0][0]])  # One Pair
    return (0, values[:5])  # High Card

def estimate_win(player_hand, opponent_hand, community_cards):
    full_player = player_hand + community_cards
    full_opponent = opponent_hand + community_cards
    p_score = evaluate_hand(full_player)
    o_score = evaluate_hand(full_opponent)
    if p_score > o_score:
        return "High"
    elif p_score == o_score:
        return "Medium"
    else:
        return "Low"

class Player:
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.cards = []
        self.folded = False

    def reset_for_round(self):
        self.cards = []
        self.folded = False


class PokerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Texas Hold'em Poker")
        self.master.geometry("700x500")
        self.setup_gui()
        self.new_game()

    def setup_gui(self):
        font_large = ("Courier", 20, "bold")
        font_med = ("Courier", 16)
        font_small = ("Courier", 14)

        tk.Label(self.master, text="Your Cards:", font=font_med).pack(pady=5)
        self.label_player_cards = tk.Label(self.master, font=font_large)
        self.label_player_cards.pack()

        tk.Label(self.master, text="Community Cards:", font=font_med).pack(pady=5)
        self.label_community_cards = tk.Label(self.master, font=font_large)
        self.label_community_cards.pack()

        self.label_computer_cards = tk.Label(self.master, font=font_small)
        self.label_computer_cards.pack(pady=5)

        self.status_text = tk.StringVar()
        tk.Label(self.master, textvariable=self.status_text, font=font_small).pack(pady=10)

        self.win_chance_label = tk.Label(self.master, text="", font=font_small)
        self.win_chance_label.pack()

        self.money_label = tk.Label(self.master, text="", font=font_small)
        self.money_label.pack()

        self.pot_label = tk.Label(self.master, text="", font=font_small)
        self.pot_label.pack()

        self.buttons = tk.Frame(self.master)
        self.buttons.pack(pady=10)
        self.call_btn = tk.Button(self.buttons, text="Call", width=10, font=font_small, command=self.call)
        self.call_btn.grid(row=0, column=0, padx=5)
        self.raise_btn = tk.Button(self.buttons, text="Raise", width=10, font=font_small, command=self.raise_bet)
        self.raise_btn.grid(row=0, column=1, padx=5)
        self.fold_btn = tk.Button(self.buttons, text="Fold", width=10, font=font_small, command=self.fold)
        self.fold_btn.grid(row=0, column=2, padx=5)

        self.next_btn = tk.Button(self.master, text="Next", font=font_small, width=20, command=self.next_stage)
        self.next_btn.pack(pady=10)

    def new_game(self):
        self.deck = Deck()
        self.stage = 0
        self.pot = 0
        self.small_blind = 25
        self.big_blind = 50
        self.player = Player("You")
        self.computer = Player("Computer")
        self.community_cards = []

        self.player.money -= self.small_blind
        self.computer.money -= self.big_blind
        self.pot += self.small_blind + self.big_blind

        self.player.cards = self.deck.deal(2)
        self.computer.cards = self.deck.deal(2)
        self.update_display()
        self.status_text.set("Game started. Pre-Flop.")

        self.enable_buttons()
        self.next_btn.config(text="Next", command=self.next_stage)

    def update_display(self):
        self.label_player_cards.config(text=' '.join(str(c) for c in self.player.cards))
        self.label_community_cards.config(text=' '.join(str(c) for c in self.community_cards))
        self.money_label.config(text=f"Your money: ${self.player.money}")
        self.pot_label.config(text=f"Pot: ${self.pot}")
        if self.stage == 4:
            self.label_computer_cards.config(text=f"Computer Cards: {' '.join(str(c) for c in self.computer.cards)}")
        else:
            self.label_computer_cards.config(text="")
        if self.stage >= 1:
            win_est = estimate_win(self.player.cards, self.computer.cards, self.community_cards)
            self.win_chance_label.config(text=f"Estimated Win Chance: {win_est}")
        else:
            self.win_chance_label.config(text="")

    def call(self):
        bet = 50
        if self.player.money >= bet and self.computer.money >= bet:
            self.player.money -= bet
            self.computer.money -= bet
            self.pot += bet * 2
            self.status_text.set("Both players called.")
            self.update_display()

    def raise_bet(self):
        raise_amt = 100
        if self.player.money >= raise_amt:
            self.player.money -= raise_amt
            self.computer.money -= 50
            self.pot += raise_amt + 50
            self.status_text.set("You raised, Computer called.")
            self.update_display()

    def fold(self):
        self.player.folded = True
        self.status_text.set("You folded. Computer wins.")
        self.computer.money += self.pot
        self.end_round()

    def next_stage(self):
        if self.stage == 0:
            self.community_cards += self.deck.deal(3)
        elif self.stage in [1, 2]:
            self.community_cards += self.deck.deal(1)
        elif self.stage == 3:
            self.showdown()
            return
        self.stage += 1
        self.status_text.set(f"Stage: {['Pre-Flop','Flop','Turn','River','Showdown'][self.stage]}")
        self.update_display()

    def showdown(self):
        if self.player.folded:
            return
        self.stage = 4
        p_score = evaluate_hand(self.player.cards + self.community_cards)
        c_score = evaluate_hand(self.computer.cards + self.community_cards)
        result = f"Your hand: {hand_ranks[p_score[0]]}\nComputer's hand: {hand_ranks[c_score[0]]}\n"

        if p_score > c_score:
            result += f"You win ${self.pot}!"
            self.player.money += self.pot
        elif p_score < c_score:
            result += "Computer wins!"
            self.computer.money += self.pot
        else:
            result += "Draw."
            self.player.money += self.pot // 2
            self.computer.money += self.pot // 2

        self.status_text.set(result)
        self.update_display()
        self.end_round()

    def end_round(self):
        self.disable_buttons()
        self.next_btn.config(text="Play Again", command=self.new_game)

    def disable_buttons(self):
        self.call_btn.config(state="disabled")
        self.raise_btn.config(state="disabled")
        self.fold_btn.config(state="disabled")

    def enable_buttons(self):
        self.call_btn.config(state="normal")
        self.raise_btn.config(state="normal")
        self.fold_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = PokerGame(root)
    root.mainloop()
