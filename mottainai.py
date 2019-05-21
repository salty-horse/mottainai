#!/usr/bin/env python3

import re
import random
from dataclasses import dataclass
from enum import Enum, auto
from functools import total_ordering

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
        self.sales = []
        self.craft_bench = []
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
        print('Returning cards', cards)
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(card)


class State(Enum):
    REDUCE_HAND = auto()
    MORNING_EFFECTS = auto()
    DISCARD_AND_CHOOSE_TASK = auto()
    PERFORM_OPPONENT_TASK = auto()
    PERFORM_OWN_TASK = auto()
    NIGHT_EFFECTS = auto()
    DRAW_WAITING_AREA = auto()
    GAME_OVER = auto()


class Game:
    def __init__(self):
        self.floor = []
        self.active_player_ix = None

    def start_game(self, player_count=2):
        self.players = [Player(i + 1) for i in range(player_count)]
        self.deck = Deck(random.sample(CARDS, len(CARDS)))
        for p in self.players:
            p.hand.add_to_hand(self.deck.draw(5))
            p.initial_task = self.deck.draw()
            self.floor.append(self.deck.draw())
        self.active_player_ix = sorted(enumerate(self.floor), key=lambda x: x[1].name.lower())[0][0]
        self.log('goes first')
        self.print_state()
        self.state = State.REDUCE_HAND
        while self.state != State.GAME_OVER:
            self.handle_state()

    def log(self, message, player_name=True, space=True):
        print('LOG: ', end='')
        if player_name:
            print(f'{self.active_player.name}{" " if space else ""}', end='')
        print(f'{message}.')

    @property
    def active_player(self):
        return self.players[self.active_player_ix]

    def prompt_choice(self, instruction, options, n=1):
        if len(options) == n:
            if n > 1:
                return list(range(n))
            else:
                return 0
        print(f'Player {self.active_player_ix + 1} - {instruction}:')
        for i, c in enumerate(options):
            print(f'  {i+1}. {c}')
        while True:
            choice = input('> ').strip()
            if n == 1:
                try:
                    choice = int(choice) - 1
                    if 0 <= choice < len(options):
                        return choice
                except:
                    pass
            else:
                try:
                    l = [int(x) - 1 for x in re.split('[, ]', choice)]
                    if len(set(l)) == n and all(0 <= x < len(options) for x in l):
                        return l
                except:
                    pass
            print('Invalid choice')

    def handle_state(self):
        if self.state == State.REDUCE_HAND:
            self.log("'s turn", space=False)
            if len(self.active_player.hand) > 5:
                n = len(self.active_player.hand) - 5
                choices = self.prompt_choice(f'Choose {n} cards to return', self.active_player.hand, n=n)
                returned_cards = [self.active_player.hand[i].card for i in choices]
                self.active_player.hand = Hand(x for i, x in enumerate(self.active_player.hand) if i not in choices)
                self.deck.return_cards(returned_cards)
                self.active_player.hand.hide()
                self.log(f'returns {n} card{"s" if n > 1 else ""}')
            self.state = State.MORNING_EFFECTS
        elif self.state == State.MORNING_EFFECTS:
            # TODO
            self.log('TODO: morning effects', player_name=False)
            self.state = State.DISCARD_AND_CHOOSE_TASK
        elif self.state == State.DISCARD_AND_CHOOSE_TASK:
            if self.active_player.initial_task:
                self.floor.append(self.active_player.initial_task)
                self.log(f'initial task {self.active_player.initial_task} added to floor')
                self.active_player.initial_task = None
            elif self.active_player.task:
                self.floor.append(self.active_player.task)
                self.log(f'previous task {self.active_player.task} added to floor')
                self.active_player.task = None

            if self.active_player.hand:
                choices = [f'{x.card.material.task} - {x.card}' for x in self.active_player.hand]
                choices.append('Pray')
                chosen_task_ix = self.prompt_choice('Choose task', choices)
                if chosen_task_ix == len(choices) - 1:
                    self.active_player.task = None
                    self.log('chooses no new task')
                else:
                    self.active_player.task = self.active_player.hand[chosen_task_ix].card
                    self.log(f'chooses new task {self.active_player.task.material.task} - {self.active_player.task}')
                    self.active_player.hand.pop(chosen_task_ix)
            self.state = State.PERFORM_OPPONENT_TASK
            self.print_state()
        elif self.state == State.PERFORM_OPPONENT_TASK:
            opponents = self.players[(self.active_player_ix+1):] + self.players[:self.active_player_ix]
            for opp in opponents:
                if opp.task:
                    self.log(f"performs opponent {opp.name}'s {opp.task.material.task} task")
                    self.perform_task(opp.task, belongs_to_active_player=False)
                else:
                    self.log(f'Opponent {opp.name} has no task', player_name=False)
            self.state = State.PERFORM_OWN_TASK
        elif self.state == State.PERFORM_OWN_TASK:
            if self.active_player.task:
                self.log(f'performs own {self.active_player.task.material.task} task')
            else:
                self.log('performs own missing task')
            self.perform_task(self.active_player.task)
            self.state = State.NIGHT_EFFECTS
        elif self.state == State.NIGHT_EFFECTS:
            # TODO
            self.log('TODO: night effects', player_name=False)
            self.state = State.DRAW_WAITING_AREA
        elif self.state == State.DRAW_WAITING_AREA:
            if self.active_player.waiting_area:
                waiting_area_size = len(self.active_player.waiting_area)
                self.log(f'draws {waiting_area_size} card{"s" if waiting_area_size > 1 else ""} from waiting area')
                self.active_player.hand.add_to_hand(self.active_player.waiting_area)
                self.active_player.waiting_area = []
            self.active_player_ix = (self.active_player_ix + 1) % len(self.players)
            self.state = State.REDUCE_HAND
            self.print_state()
        else:
            raise Exception(f'Unknown state {self.state}')
    
    def perform_task(self, task, belongs_to_active_player=True):
        if not task:
            self.log('prays')
            self.active_player.waiting_area.append(self.deck.draw())
            return

        # TODO: Calc cover
        amount = 1 + sum(1 for helper in self.active_player.helpers
                         if helper.material == task.material)
        self.log(f'- {amount} {task.material.task} action{"s" if amount > 1 else ""} available')
        for action_number in range(amount):
            available_actions = []
            action_descriptions = []

            if task.material == PAPER and not self.active_player.craft_bench:
                self.log(f'cannot {task.material.task} with an empty craft bench')
            elif task.material in (STONE, CLAY) and not self.floor:
                self.log(f'cannot {task.material.task} with an empty floor')
            elif task.material == CLOTH and len(self.active_player.waiting_area) == 5:
                self.log(f'cannot {task.material.task} with a full waiting area')
            elif task.material == METAL and not self.active_player.hand:
                self.log(f'cannot {task.material.task} with an empty hand')
            else:
                available_actions.append(task.material)
                action_descriptions.append(f'{task.material.task} ({task.material.description})')

            # This test is disabled as it reveals information about hand to opponents
            # (even without the log, by the speed in which the fallback prayer is done)
            #
            # if not any(card.card.material == task.material for card in self.active_player.hand):
            #     self.log(f'cannot Craft {task.material.name} with no matching cards in hand')
            # else:

            available_actions.append('craft')
            action_descriptions.append(f'Craft ({task.material.name})')

            available_actions.append('pray')
            action_descriptions.append('Pray')

            action_performed = False
            while not action_performed:
                chosen_action = self.prompt_choice(f'Choose how to perform action #{action_number + 1}', action_descriptions)
                action_performed = self.perform_action(available_actions[chosen_action], task)

    def perform_action(self, action, card):
        if action == PAPER:
            self.log('TODO: Clerk')
            return True
        elif action == STONE:
            self.log('TODO: Monk')
            return True
        elif action == CLOTH:
            self.log('TODO: Tailor')
            return True
        elif action == CLAY:
            self.log('TODO: Potter')
            return True
        elif action == METAL:
            self.log('TODO: Smith')
            return True
        elif action == 'craft':
            self.log('TODO: Craft')
            return True
        elif action == 'pray':
            self.log('prays')
            self.active_player.waiting_area.append(self.deck.draw())
            return True
        else:
            raise Exception(f'Unknown action {action}')

        return True

    def print_state(self):
        print()
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
            if p.waiting_area:
                print(f'Waiting area: {len(p.waiting_area)}')
        print()

if __name__ == '__main__':
    game = Game()
    game.start_game()
