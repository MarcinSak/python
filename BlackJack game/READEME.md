# Blackjack Game - Simplified Rules

This is a basic implementation of a Blackjack game, developed as part of an exercise from the course: [Complete Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/). This program was created by me as part of an exercise for learning Python.

## Game Objective:
- The goal is to have a higher value in your hand than the dealer, but without exceeding 21.
- If your hand exceeds 21, it's called a **BUST**, and you lose.

## Card Values:
- Cards 2-10 are worth their face value.
- Jack, Queen, and King are each worth 10.
- Ace can be worth either 1 or 11, chosen by the player before the game starts.

## Game Play:
1. The dealer deals one card face up to each player and themselves.
2. Next, each player gets another card face up, while the dealer takes a card face down.
3. If a player has 21 (Blackjack) after two cards, they automatically win 2.5 times their bet.
   - If both the dealer and a player have 21, it's a **PUSH** (tie), and the player gets their original bet back.

## Player Actions:
- **HIT**: The player requests another card (dealt face down).
- **STAY**: The player is satisfied with their hand and does not receive more cards.

## Dealer Actions:
- The dealer flips their face-down card after all players finish.
- If the dealer's total is 16 or less, they must **HIT** (take another card).
- If the dealer's total is 17 or higher, they must **STAY**.
- If the dealer **BUSTS**, all remaining players win 2 times their bet.

## PUSH:
- A **PUSH** occurs when both the player and dealer have the same hand value at the end (without exceeding 21). The round ends in a tie, and the player receives their original bet back.

## Special Case:
- If two players have 21, both win their respective bets independently.
- If the dealer has 18 and two players have 20, both players win.

## Additional Notes:
- Players’ first two cards are face up.
- The dealer’s first card is face up, and their second card is face down.
- Any cards dealt after a **HIT** are face down and remain hidden until the end of the game.
