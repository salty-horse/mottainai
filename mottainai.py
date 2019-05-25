#!/usr/bin/env python3

import re
import random
from dataclasses import dataclass
from enum import Enum, auto
from functools import total_ordering

def prompt_choice(player_name, instruction, options, n=1, allow_cancel=True):
    if isinstance(n, int) and len(options) == n and not allow_cancel:
        if n > 1:
            return list(range(n))
        else:
            return 0
    print(f'{player_name} - {instruction}:')
    for i, c in enumerate(options):
        print(f'  {i+1}. {c}')
    if allow_cancel:
        print(f'  0. Cancel')
    while True:
        choice = input('> ').strip()
        if n == 1:
            try:
                choice = int(choice) - 1
                if allow_cancel and choice == -1:
                    return -1
                if 0 <= choice < len(options):
                    return choice
            except:
                pass
        else:
            try:
                if not choice:
                    l = []
                else:
                    l = list(set(int(x) - 1 for x in re.split('[, ]', choice)))
                if isinstance(n, tuple):
                    # Allow a range of choices
                    # cancel must be on its own
                    if allow_cancel and l == [-1]:
                        return -1
                    if allow_cancel and len(l) > 1 and -1 in l:
                        pass
                    elif n[0] <= len(l) <= n[1] and all(0 <= x < len(options) for x in l):
                        return l
                else:
                    if len(set(l)) == n and all(0 <= x < len(options) for x in l):
                        return l
            except:
                pass
        print('Invalid choice')


@dataclass(frozen=True)
class Material:
    id: int
    name: str
    value: int
    symbol: str
    task: str
    description: str

    def __eq__(self, other):
        if isinstance(other, Material):
            return self.id == other.id
        else:
            return False

    def __repr__(self):
        return self.name

PAPER = Material(1, 'Paper', 1, '📜', 'Clerk', 'Sell a material')
STONE = Material(2, 'Stone', 2, '🗿', 'Monk', 'Hire a helper')
CLOTH = Material(3, 'Cloth', 2, '🧵', 'Tailor', 'Refill your hand')
CLAY = Material(4, 'Clay', 3, '🧱', 'Potter', 'Collect a material')
METAL = Material(5, 'Metal', 3, '🔧', 'Smith', 'Complete any work')

@dataclass(frozen=True)
@total_ordering
class Card:
    id: int
    name: str
    material: Material

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return (self.id, self.name) < (other.id, other.name)

    def __repr__(self):
        return f'{self.name} {self.material.symbol}'

CRANE = Card(1, 'Crane', PAPER)
CURTAIN = Card(2, 'Curtain', PAPER)
DECK_OF_CARDS = Card(3, 'Deck of Cards', PAPER)
DOLL = Card(4, 'Doll', PAPER)
FAN = Card(5, 'Fan', PAPER)
LAMPSHADE = Card(6, 'Lampshade', PAPER)
PINWHEEL = Card(7, 'Pinwheel', PAPER)
PLANE = Card(8, 'Plane', PAPER)
POEM = Card(9, 'Poem', PAPER)
SCROLL = Card(10, 'Scroll', PAPER)
SKETCH = Card(11, 'Sketch', PAPER)
STRAW = Card(12, 'Straw', PAPER)
STATUE = Card(13, 'Statue', STONE)
PILLAR = Card(14, 'Pillar', STONE)
FROG = Card(15, 'Frog', STONE)
TABLET = Card(16, 'Tablet', STONE)
STOOL = Card(17, 'Stool', STONE)
GO_SET = Card(18, 'Go Set', STONE)
FOUNTAIN = Card(19, 'Fountain', STONE)
TOWER = Card(20, 'Tower', STONE)
DAITORO = Card(21, 'Daitoro', STONE)
AMULET = Card(22, 'Amulet', STONE)
BENCH = Card(23, 'Bench', STONE)
KITE = Card(24, 'Kite', CLOTH)
UMBRELLA = Card(25, 'Umbrella', CLOTH)
SOCKS = Card(26, 'Socks', CLOTH)
QUILT = Card(27, 'Quilt', CLOTH)
ROBE = Card(28, 'Robe', CLOTH)
FLAG = Card(29, 'Flag', CLOTH)
TAPESTRY = Card(30, 'Tapestry', CLOTH)
HANDKERCHIEF = Card(31, 'Handkerchief', CLOTH)
PUPPET = Card(32, 'Puppet', CLOTH)
MASK = Card(33, 'Mask', CLOTH)
CLOAK = Card(34, 'Cloak', CLOTH)
VASE = Card(35, 'Vase', CLAY)
HANIWA = Card(36, 'Haniwa', CLAY)
TEAPOT = Card(37, 'Teapot', CLAY)
DICE = Card(38, 'Dice', CLAY)
BOWL = Card(39, 'Bowl', CLAY)
JAR = Card(40, 'Jar', CLAY)
BRICK = Card(41, 'Brick', CLAY)
FIGURINE = Card(42, 'Figurine', CLAY)
BANGLE = Card(43, 'Bangle', CLAY)
CUP = Card(44, 'Cup', CLAY)
RING = Card(45, 'Ring', METAL)
FLUTE = Card(46, 'Flute', METAL)
SWORD = Card(47, 'Sword', METAL)
SHURIKEN = Card(48, 'Shuriken', METAL)
GONG = Card(49, 'Gong', METAL)
PIN = Card(50, 'Pin', METAL)
COIN = Card(51, 'Coin', METAL)
TURTLE = Card(52, 'Turtle', METAL)
BELL = Card(53, 'Bell', METAL)
CHOPSTICKS = Card(54, 'Chopsticks', METAL)

CARDS = [
    CRANE, CURTAIN, DECK_OF_CARDS, DOLL, FAN, LAMPSHADE, PINWHEEL, PLANE,
    POEM, SCROLL, SKETCH, STRAW, STATUE, PILLAR, FROG, TABLET, STOOL,
    GO_SET, FOUNTAIN, TOWER, DAITORO, AMULET, BENCH, KITE, UMBRELLA, SOCKS,
    QUILT, ROBE, FLAG, TAPESTRY, HANDKERCHIEF, PUPPET, MASK, CLOAK, VASE,
    HANIWA, TEAPOT, DICE, BOWL, JAR, BRICK, FIGURINE, BANGLE, CUP, RING,
    FLUTE, SWORD, SHURIKEN, GONG, PIN, COIN, TURTLE, BELL, CHOPSTICKS
]


@dataclass
@total_ordering
class HandCard:
    card: Card
    visible: bool = False

    def __repr__(self):
        return f'{self.card}{" 👁" if self.visible else ""}'

    def __cmp__(self, other):
        return self.card.__cmp__(other.card)

    def __lt__(self, other):
        return self.card.__lt__(other.card)


class Hand(list):
    def add_to_hand(self, cards):
        for c in cards:
            self.append(HandCard(c))
        self.sort()

    def hide(self):
        for c in self:
            c.visible = False

    def format_hand(self, is_active=False):
        if is_active:
            return str(self)
        else:
            items = ', '.join(sorted(c.card if c.visible else '?' for c in self))
            return f'[{items}]'


class Player:
    def __init__(self, i):
        self.name = f'Player {i}'
        self.hand = Hand()
        self.gallery = []
        self.gift_shop = []
        self.helpers = []
        self.craft_bench = []
        self.sales = []
        self.waiting_area = []
        self.task = None
        self.initial_task = None


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return repr(self.cards)

    def __len__(self):
        return len(self.cards)

    def draw(self, n=1):
        # TODO: Handle end of game whenever a draw is possible
        if n == 1:
            return self.cards.pop(0)
        else:
            return [self.cards.pop(0) for _ in range(n)]

    def return_cards(self, cards):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(card)


class State(Enum):
    CHECK_HAND_SIZE = auto()
    REDUCE_HAND = auto()
    MORNING_EFFECTS = auto()
    DISCARD_OLD_TASK = auto()
    CHOOSE_NEW_TASK = auto()
    PERFORM_OPPONENT_TASK = auto()
    PERFORM_OWN_TASK = auto()
    PERFORM_TASK = auto()
    PERFORM_ACTION = auto()
    PERFORM_CLERK = auto()
    PERFORM_MONK = auto()
    PERFORM_TAILOR = auto()
    PERFORM_POTTER = auto()
    PERFORM_SMITH = auto()
    NIGHT_EFFECTS = auto()
    DRAW_WAITING_AREA = auto()
    GAME_OVER = auto()


class Game:
    def __init__(self):
        self.floor = []
        self.active_player_ix = None

        # These are for the state machine move selection
        self.possible_moves = None
        self.possible_moves_internal = None
        self.instruction = None
        self.number_of_moves_to_choose = None
        self.allow_cancel = False
        self.submitted_moves = None

        self.opponents_with_tasks = None
        self.current_task_to_perform = None
        self.current_action_num = None
        self.actions_to_perform = None
        self.next_states = []

    def reset_possible_moves(self):
        self.possible_moves = None
        self.allow_cancel = False

    def start_game(self, player_count=1):
        self.players = [Player(i + 1) for i in range(player_count)]
        self.deck = Deck(random.sample(CARDS, len(CARDS)))
        for p in self.players:
            p.hand.add_to_hand(self.deck.draw(5))
            p.initial_task = self.deck.draw()
            self.floor.append(self.deck.draw())
        self.active_player_ix = sorted(enumerate(self.floor), key=lambda x: x[1].name.lower())[0][0]
        self.first_player_ix = self.active_player_ix
        self.turn_number = 1
        self.log('goes first')
        self.print_state()
        self.state = State.DISCARD_OLD_TASK
        while self.state != State.GAME_OVER:
            if self.possible_moves:
                self.submitted_moves = prompt_choice(
                    self.active_player.name,
                    self.instruction,
                    self.possible_moves,
                    self.number_of_moves_to_choose,
                    self.allow_cancel)
            print(f'State is {self.state}')
            self.handle_state()

    def log(self, message, player_name=True, space=True):
        print('LOG: ', end='')
        if player_name:
            print(f'{self.active_player.name}{" " if space else ""}', end='')
        print(f'{message}.')

    @property
    def active_player(self):
        return self.players[self.active_player_ix]

    def handle_state(self):
        if self.state == State.CHECK_HAND_SIZE:
            self.log("'s turn", space=False)
            if len(self.active_player.hand) <= 5:
                self.state = State.MORNING_EFFECTS
            else:
                n = len(self.active_player.hand) - 5
                self.instruction = f'Choose {n} card{"s" if n > 1 else ""} from your hand to return'
                self.possible_moves = self.active_player.hand
                self.number_of_moves_to_choose = n
                self.state = State.REDUCE_HAND
        elif self.state == State.REDUCE_HAND:
            if isinstance(self.submitted_moves, int):
                self.submitted_moves = [self.submitted_moves]
            returned_cards = [self.active_player.hand[i].card for i in self.submitted_moves]
            self.active_player.hand = Hand(x for i, x in enumerate(self.active_player.hand) if i not in self.submitted_moves)
            self.reset_possible_moves()
            self.deck.return_cards(returned_cards)
            self.active_player.hand.hide()
            self.log(f'returns {len(returned_cards)} card{"s" if len(returned_cards) > 1 else ""}')
            self.state = State.MORNING_EFFECTS
        elif self.state == State.MORNING_EFFECTS:
            # TODO
            self.log('TODO: morning effects', player_name=False)
            self.state = State.DISCARD_OLD_TASK
        elif self.state == State.DISCARD_OLD_TASK:
            if self.active_player.initial_task:
                self.floor.append(self.active_player.initial_task)
                self.log(f'initial task {self.active_player.initial_task} added to floor')
                self.active_player.initial_task = None
            elif self.active_player.task:
                self.floor.append(self.active_player.task)
                self.log(f'previous task {self.active_player.task} added to floor')
                self.active_player.task = None

            if not self.active_player.hand:
                self.log('chooses no new task')
                self.state = State.PERFORM_OPPONENT_TASK
            else:
                self.instruction = 'Choose task'
                self.possible_moves = [f'{x.card.material.task} ({x.card.material.description}) - {x.card}' for x in self.active_player.hand]
                self.possible_moves.append('Pray')
                self.number_of_moves_to_choose = 1
                self.state = State.CHOOSE_NEW_TASK
        elif self.state == State.CHOOSE_NEW_TASK:
            if self.submitted_moves == len(self.possible_moves) - 1:
                self.active_player.task = None
                self.log('chooses no new task')
            else:
                self.active_player.task = self.active_player.hand[self.submitted_moves].card
                self.log(f'chooses new task {self.active_player.task.material.task} - {self.active_player.task}')
                self.active_player.hand.pop(self.submitted_moves)
            self.reset_possible_moves()
            self.state = State.PERFORM_OPPONENT_TASK
        elif self.state == State.PERFORM_OPPONENT_TASK:
            self.print_state()
            if self.opponents_with_tasks is None:
                opponents_with_tasks = self.players[(self.active_player_ix+1):] + self.players[:self.active_player_ix]
            if not self.opponents_with_tasks:
                self.opponents_with_tasks = None
                self.state = State.PERFORM_OWN_TASK
            else:
                opp = self.opponents_with_tasks.pop(0)
                if opp.task:
                    self.log(f"performs opponent {opp.name}'s {opp.task.material.task} task")
                    self.current_task_to_perform = opp.task
                    self.current_task_is_of_opponent = True
                    self.state = State.PERFORM_TASK
                    self.next_states.append(State.PERFORM_OPPONENT_TASK)
                else:
                    self.log(f'Opponent {opp.name} has no task', player_name=False)

        elif self.state == State.PERFORM_TASK:
            task = self.current_task_to_perform
            if not task:
                self.log('prays')
                self.active_player.waiting_area.append(self.deck.draw())
                self.state = self.next_states.pop()
            else:
                if self.actions_to_perform is None:
                    # TODO: Calc cover
                    self.actions_to_perform = 1 + sum(1 for helper in self.active_player.helpers
                                     if helper.material == task.material)
                    self.log(f'- {self.actions_to_perform} {task.material.task} action{"s" if self.actions_to_perform > 1 else ""} available')
                    self.current_action_num = 1

                if self.current_action_num > self.actions_to_perform:
                    self.actions_to_perform = None
                    self.state = self.next_states.pop()
                else:
                    self.instruction = f'Choose how to perform action #{self.current_action_num} of {self.actions_to_perform}'
                    self.possible_moves_internal = []
                    self.possible_moves = []

                    # TODO: Check if works can be completed before allowing CRAFT or SMITH

                    if task.material == PAPER and not self.active_player.craft_bench:
                        self.log(f'cannot {task.material.task} with an empty craft bench')
                    elif task.material in (STONE, CLAY) and not self.floor:
                        self.log(f'cannot {task.material.task} with an empty floor')
                    elif task.material == CLOTH and len(self.active_player.waiting_area) >= 5:
                        self.possible_moves_internal.append(task.material)
                        self.possible_moves.append(f'{task.material.task} (PASS since the waiting area is full)')
                    elif task.material == METAL and not self.active_player.hand:
                        self.log(f'cannot {task.material.task} with an empty hand')
                    else:
                        self.possible_moves_internal.append(task.material)
                        self.possible_moves.append(f'{task.material.task} ({task.material.description})')

                    # This test is disabled as it reveals information about hand to opponents
                    # (even without the log, by the speed in which the fallback prayer is done)
                    #
                    # if not any(card.card.material == task.material for card in self.active_player.hand):
                    #     self.log(f'cannot Craft {task.material.name} with no matching cards in hand')
                    # else:

                    self.possible_moves_internal.append('craft')
                    self.possible_moves.append(f'Craft ({task.material.name})')

                    self.possible_moves_internal.append('pray')
                    self.possible_moves.append('Pray')
                    self.state = State.PERFORM_ACTION
                    self.next_states.append(State.PERFORM_TASK)

        elif self.state == State.PERFORM_ACTION:
            action = self.possible_moves_internal[self.submitted_moves]
            self.reset_possible_moves()

            if action == PAPER:
                self.state = State.PERFORM_CLERK
                self.instruction = 'Select a material from the craft bench to sell'
                self.possible_moves = []
                self.possible_moves.extend(self.active_player.craft_bench)
                self.allow_cancel = True
                self.number_of_moves_to_choose = 1
                return
            elif action == STONE:
                self.state = State.PERFORM_MONK
                self.instruction = 'Select a card from the floor to become a helper'
                self.possible_moves = []
                self.possible_moves.extend(self.floor)
                self.allow_cancel = True
                self.number_of_moves_to_choose = 1
                return
            elif action == CLOTH:
                self.log('TODO: Tailor')
                self.state = State.PERFORM_TAILOR
                room_in_waiting_area = max(0, 5 - len(self.active_player.waiting_area))
                hand_size = len(self.active_player.hand)
                max_cards = min(room_in_waiting_area, hand_size)
                self.instruction = f'Select 0–{max_cards} cards from your hand to return'
                self.possible_moves = []
                self.possible_moves.extend(self.active_player.hand)
                self.allow_cancel = True
                self.number_of_moves_to_choose = (0, max_cards)
                return
            elif action == CLAY:
                self.state = State.PERFORM_POTTER
                self.instruction = 'Select a card from the floor to collect in the craft bench'
                self.possible_moves = []
                self.possible_moves.extend(self.floor)
                self.allow_cancel = True
                self.number_of_moves_to_choose = 1
                return
            elif action == METAL:
                self.log('TODO: Smith')
            elif action == 'craft':
                self.log('TODO: Craft')
            elif action == 'pray':
                self.log('prays')
                self.active_player.waiting_area.append(self.deck.draw())
                self.possible_moves = []
                if self.current_action_num:
                    self.current_action_num += 1
            else:
                raise Exception(f'Unknown action {action}')

            self.state = self.next_states.pop()

        elif self.state == State.PERFORM_CLERK:
            if self.submitted_moves != -1:
                card = self.active_player.craft_bench[self.submitted_moves]
                self.active_player.sales.append(card)
                self.active_player.craft_bench.pop(self.submitted_moves)
                self.log(f'moves {card} from craft bench to sales')
                if self.current_action_num:
                    self.current_action_num += 1
            self.reset_possible_moves()
            self.state = self.next_states.pop()

        elif self.state == State.PERFORM_MONK:
            if self.submitted_moves != -1:
                card = self.floor[self.submitted_moves]
                self.active_player.helpers.append(card)
                self.floor.pop(self.submitted_moves)
                self.log(f'moves {card} from floor to helpers')
                if self.current_action_num:
                    self.current_action_num += 1
            self.reset_possible_moves()
            self.state = self.next_states.pop()

        elif self.state == State.PERFORM_TAILOR:
            if self.submitted_moves != -1:
                if not self.submitted_moves:
                    self.log(f'returns 0 cards')
                else:
                    returned_cards = [self.active_player.hand[i].card for i in self.submitted_moves]
                    self.active_player.hand = Hand(x for i, x in enumerate(self.active_player.hand) if i not in self.submitted_moves)
                    self.deck.return_cards(returned_cards)
                    self.active_player.hand.hide()
                    self.log(f'returns {len(returned_cards)} card{"s" if len(returned_cards) > 1 else ""}')

                cards_to_refill = max(0, 5 - len(self.active_player.hand) - len(self.active_player.waiting_area))
                if cards_to_refill:
                    self.log(f'draws {cards_to_refill} card{"s" if cards_to_refill > 1 else ""} into the waiting area')
                    for _ in range(cards_to_refill):
                        self.active_player.waiting_area.append(self.deck.draw())
                if self.current_action_num:
                    self.current_action_num += 1
            self.reset_possible_moves()
            self.state = self.next_states.pop()
        elif self.state == State.PERFORM_POTTER:
            if self.submitted_moves != -1:
                card = self.floor[self.submitted_moves]
                self.active_player.craft_bench.append(card)
                self.floor.pop(self.submitted_moves)
                self.log(f'moves {card} from floor to craft bench')
                if self.current_action_num:
                    self.current_action_num += 1
            self.reset_possible_moves()
            self.state = self.next_states.pop()

        elif self.state == State.PERFORM_OWN_TASK:
            if self.active_player.task:
                self.log(f'performs own {self.active_player.task.material.task} task')
            else:
                self.log('performs own missing task')
            self.current_task_to_perform = self.active_player.task
            self.current_task_is_of_opponent = False
            self.state = State.PERFORM_TASK
            self.next_states.append(State.NIGHT_EFFECTS)

        elif self.state == State.NIGHT_EFFECTS:
            # TODO
            self.log('TODO: night effects', player_name=False)
            self.state = State.DRAW_WAITING_AREA
        elif self.state == State.DRAW_WAITING_AREA:
            if self.active_player.waiting_area:
                waiting_area_size = len(self.active_player.waiting_area)
                self.log(f'draws {waiting_area_size} card{"s" if waiting_area_size > 1 else ""} from the waiting area')
                self.active_player.hand.add_to_hand(self.active_player.waiting_area)
                self.active_player.waiting_area = []
            self.active_player_ix = (self.active_player_ix + 1) % len(self.players)
            if self.active_player_ix == self.first_player_ix:
                self.turn_number += 1
            self.state = State.CHECK_HAND_SIZE
            self.print_state()
        else:
            raise Exception(f'Unknown state {self.state}')

    def print_state(self):
        print()
        print(f'Turn {self.turn_number}, {self.active_player.name} active')
        print(f'Deck: {len(self.deck)} card{"s" if len(self.deck) > 1 else ""}')
        print(f'Floor: {self.floor}')
        for i, p in enumerate(self.players):
            print(f'Player {i+1}')
            print(f'\tHand: {p.hand.format_hand(i == self.active_player_ix)}')
            if p.initial_task:
                print('\tTask: Hidden')
            elif p.task:
                print(f'\tTask: {p.task.material.task if p.task else "None"} - {p.task}')
            else:
                print('\tTask: None')
            if p.helpers:
                print(f'\tHelpers: {p.helpers}')
            if p.craft_bench:
                print(f'\tCraft Bench: {p.craft_bench}')
            if p.sales:
                print(f'\tSales: {p.sales}')
            if p.waiting_area:
                print(f'Waiting Area: {len(p.waiting_area)}')
        print()

if __name__ == '__main__':
    game = Game()
    game.start_game()
