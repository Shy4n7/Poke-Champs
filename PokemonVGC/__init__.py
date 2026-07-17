import random
import os
import sys

# Terminal Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"

# Type Effectiveness Database
TYPE_EFFECTIVENESS = {
    'Normal': {'Rock': 0.5, 'Ghost': 0.0, 'Steel': 0.5},
    'Fire': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ice': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Dragon': 0.5, 'Steel': 2.0},
    'Water': {'Fire': 2.0, 'Water': 0.5, 'Grass': 0.5, 'Ground': 2.0, 'Rock': 2.0, 'Dragon': 0.5},
    'Grass': {'Fire': 0.5, 'Water': 2.0, 'Grass': 0.5, 'Poison': 0.5, 'Ground': 2.0, 'Flying': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Dragon': 0.5, 'Steel': 0.5},
    'Electric': {'Water': 2.0, 'Grass': 0.5, 'Electric': 0.5, 'Ground': 0.0, 'Flying': 2.0, 'Dragon': 0.5},
    'Ice': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ice': 0.5, 'Ground': 2.0, 'Flying': 2.0, 'Dragon': 2.0, 'Steel': 0.5},
    'Fighting': {'Normal': 2.0, 'Ice': 2.0, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Ghost': 0.0, 'Dark': 2.0, 'Steel': 2.0, 'Fairy': 0.5},
    'Poison': {'Grass': 2.0, 'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0.0, 'Fairy': 2.0},
    'Ground': {'Fire': 2.0, 'Grass': 0.5, 'Electric': 2.0, 'Poison': 2.0, 'Flying': 0.0, 'Bug': 0.5, 'Rock': 2.0, 'Steel': 2.0},
    'Flying': {'Grass': 2.0, 'Electric': 0.5, 'Fighting': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Steel': 0.5},
    'Psychic': {'Fighting': 2.0, 'Poison': 2.0, 'Psychic': 0.5, 'Dark': 0.0, 'Steel': 0.5},
    'Bug': {'Fire': 0.5, 'Grass': 2.0, 'Fighting': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Psychic': 2.0, 'Ghost': 0.5, 'Dark': 2.0, 'Steel': 0.5, 'Fairy': 0.5},
    'Rock': {'Fire': 2.0, 'Ice': 2.0, 'Fighting': 0.5, 'Ground': 0.5, 'Flying': 2.0, 'Bug': 2.0, 'Steel': 0.5},
    'Ghost': {'Normal': 0.0, 'Psychic': 2.0, 'Ghost': 2.0, 'Dark': 0.5},
    'Dragon': {'Dragon': 2.0, 'Steel': 0.5, 'Fairy': 0.0},
    'Dark': {'Fighting': 0.5, 'Psychic': 2.0, 'Ghost': 2.0, 'Dark': 0.5, 'Fairy': 0.5},
    'Steel': {'Water': 0.5, 'Electric': 0.5, 'Ice': 2.0, 'Rock': 2.0, 'Steel': 0.5, 'Fairy': 2.0, 'Fire': 0.5},
    'Fairy': {'Fire': 0.5, 'Fighting': 2.0, 'Poison': 0.5, 'Dragon': 2.0, 'Dark': 2.0, 'Steel': 0.5}
}

# Moves Database
# Protect has priority 4. Other moves have priority 0.
# Moves Database
# Protect has priority 4. Other moves have priority 0.
MOVE_DB = {
    'Heat Wave': {'power': 95, 'type': 'Fire', 'category': 'Special', 'target': 'All Enemies', 'accuracy': 90, 'priority': 0},
    'Solar Beam': {'power': 120, 'type': 'Grass', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Air Slash': {'power': 75, 'type': 'Flying', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 95, 'priority': 0},
    'Protect': {'power': 0, 'type': 'Normal', 'category': 'Status', 'target': 'Self', 'accuracy': 100, 'priority': 4},
    'Giga Drain': {'power': 75, 'type': 'Grass', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Sludge Bomb': {'power': 90, 'type': 'Poison', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Weather Ball': {'power': 50, 'type': 'Normal', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Eruption': {'power': 150, 'type': 'Fire', 'category': 'Special', 'target': 'All Enemies', 'accuracy': 100, 'priority': 0},
    'Earth Power': {'power': 90, 'type': 'Ground', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Moonblast': {'power': 95, 'type': 'Fairy', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Shadow Ball': {'power': 80, 'type': 'Ghost', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Dazzling Gleam': {'power': 80, 'type': 'Fairy', 'category': 'Special', 'target': 'All Enemies', 'accuracy': 100, 'priority': 0},
    'Acrobatics': {'power': 110, 'type': 'Flying', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Knock Off': {'power': 97, 'type': 'Dark', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Dragon Claw': {'power': 80, 'type': 'Dragon', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Headlong Rush': {'power': 120, 'type': 'Ground', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Close Combat': {'power': 120, 'type': 'Fighting', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Rock Slide': {'power': 75, 'type': 'Rock', 'category': 'Physical', 'target': 'All Enemies', 'accuracy': 90, 'priority': 0},
    
    # AI Moves
    'Scald': {'power': 80, 'type': 'Water', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Icy Wind': {'power': 55, 'type': 'Ice', 'category': 'Special', 'target': 'All Enemies', 'accuracy': 95, 'priority': 0},
    'Muddy Water': {'power': 90, 'type': 'Water', 'category': 'Special', 'target': 'All Enemies', 'accuracy': 85, 'priority': 0},
    'Draco Meteor': {'power': 130, 'type': 'Dragon', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 90, 'priority': 0},
    'Hurricane': {'power': 110, 'type': 'Flying', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 70, 'priority': 0},
    'Electro Shot': {'power': 130, 'type': 'Electric', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Flash Cannon': {'power': 80, 'type': 'Steel', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Body Press': {'power': 80, 'type': 'Fighting', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Trick Room': {'power': 0, 'type': 'Psychic', 'category': 'Status', 'target': 'Self', 'accuracy': 100, 'priority': 0},
    'Recover': {'power': 0, 'type': 'Normal', 'category': 'Status', 'target': 'Self', 'accuracy': 100, 'priority': 0},
    'Tri Attack': {'power': 80, 'type': 'Normal', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Ice Beam': {'power': 90, 'type': 'Ice', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Hydro Pump': {'power': 110, 'type': 'Water', 'category': 'Special', 'target': 'Single Enemy', 'accuracy': 80, 'priority': 0},
    'Snarl': {'power': 55, 'type': 'Dark', 'category': 'Special', 'target': 'All Enemies', 'accuracy': 95, 'priority': 0},
    'Flare Blitz': {'power': 120, 'type': 'Fire', 'category': 'Physical', 'target': 'Single Enemy', 'accuracy': 100, 'priority': 0},
    'Tailwind': {'power': 0, 'type': 'Flying', 'category': 'Status', 'target': 'Self', 'accuracy': 100, 'priority': 0}
}

# Pokémon Database (Standard Neutral Level 50 competitive spreads)
POKEMON_DB = {
    # Player Pool
    'Charizard': {
        'types': ['Fire', 'Flying'],
        'stats': {'hp': 153, 'atk': 104, 'def': 98, 'spa': 129, 'spd': 105, 'spe': 120},
        'ability': 'Blaze',
        'moves': ['Heat Wave', 'Solar Beam', 'Air Slash', 'Protect'],
        'mega_stone': 'Charizardite Y',
        'mega_form': {
            'name': 'Mega Charizard Y',
            'stats': {'hp': 153, 'atk': 104, 'def': 98, 'spa': 211, 'spd': 135, 'spe': 152},
            'ability': 'Drought'
        }
    },
    'Venusaur': {
        'types': ['Grass', 'Poison'],
        'stats': {'hp': 155, 'atk': 92, 'def': 103, 'spa': 152, 'spd': 120, 'spe': 132},
        'ability': 'Chlorophyll',
        'moves': ['Giga Drain', 'Sludge Bomb', 'Weather Ball', 'Protect']
    },
    'Torkoal': {
        'types': ['Fire'],
        'stats': {'hp': 145, 'atk': 95, 'def': 160, 'spa': 137, 'spd': 90, 'spe': 40},
        'ability': 'Drought',
        'moves': ['Eruption', 'Earth Power', 'Solar Beam', 'Protect']
    },
    'Whimsicott': {
        'types': ['Grass', 'Fairy'],
        'stats': {'hp': 135, 'atk': 77, 'def': 105, 'spa': 97, 'spd': 95, 'spe': 136},
        'ability': 'Prankster',
        'moves': ['Tailwind', 'Moonblast', 'Giga Drain', 'Protect']
    },
    'Roaring Moon': {
        'types': ['Dragon', 'Dark'],
        'stats': {'hp': 180, 'atk': 191, 'def': 91, 'spa': 65, 'spd': 121, 'spe': 171},
        'ability': 'Protosynthesis',
        'moves': ['Acrobatics', 'Knock Off', 'Tailwind', 'Protect']
    },
    'Great Tusk': {
        'types': ['Ground', 'Fighting'],
        'stats': {'hp': 190, 'atk': 183, 'def': 151, 'spa': 63, 'spd': 73, 'spe': 139},
        'ability': 'Protosynthesis',
        'moves': ['Headlong Rush', 'Close Combat', 'Rock Slide', 'Protect']
    },
    
    # AI Opponent Pool (Rain/Trick Room)
    'Politoed': {
        'types': ['Water'],
        'stats': {'hp': 165, 'atk': 85, 'def': 95, 'spa': 142, 'spd': 120, 'spe': 90},
        'ability': 'Drizzle',
        'moves': ['Scald', 'Icy Wind', 'Muddy Water', 'Protect']
    },
    'Kingdra': {
        'types': ['Water', 'Dragon'],
        'stats': {'hp': 150, 'atk': 105, 'def': 115, 'spa': 147, 'spd': 115, 'spe': 137},
        'ability': 'Swift Swim',
        'moves': ['Muddy Water', 'Draco Meteor', 'Hurricane', 'Protect']
    },
    'Archaludon': {
        'types': ['Steel', 'Dragon'],
        'stats': {'hp': 165, 'atk': 115, 'def': 150, 'spa': 177, 'spd': 85, 'spe': 105},
        'ability': 'Stamina',
        'moves': ['Electro Shot', 'Flash Cannon', 'Draco Meteor', 'Body Press']
    },
    'Porygon2': {
        'types': ['Normal'],
        'stats': {'hp': 160, 'atk': 90, 'def': 110, 'spa': 157, 'spd': 115, 'spe': 80},
        'ability': 'Download',
        'moves': ['Trick Room', 'Recover', 'Tri Attack', 'Ice Beam']
    },
    'Ludicolo': {
        'types': ['Water', 'Grass'],
        'stats': {'hp': 155, 'atk': 90, 'def': 90, 'spa': 142, 'spd': 120, 'spe': 132},
        'ability': 'Swift Swim',
        'moves': ['Hydro Pump', 'Giga Drain', 'Ice Beam', 'Protect']
    },
    'Incineroar': {
        'types': ['Fire', 'Dark'],
        'stats': {'hp': 170, 'atk': 135, 'def': 110, 'spa': 80, 'spd': 110, 'spe': 80},
        'ability': 'Intimidate',
        'moves': ['Flare Blitz', 'Knock Off', 'Snarl', 'Protect']
    }
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_stage_multiplier(stage):
    if stage >= 0:
        return (2 + stage) / 2
    else:
        return 2 / (2 - stage)


def get_effective_stat(pokemon, stat_name, state, ignore_negative_stages=False, ignore_positive_stages=False):
    base_val = pokemon['stats'][stat_name]
    stage = pokemon['stat_stages'].get(stat_name, 0)
    if ignore_negative_stages and stage < 0:
        stage = 0
    if ignore_positive_stages and stage > 0:
        stage = 0
    multiplier = get_stage_multiplier(stage)
    val = base_val * multiplier
    
    # Weather and Ability Speed scaling
    weather = state['weather']
    if stat_name == 'spe':
        if pokemon['ability'] == 'Chlorophyll' and weather == 'Sun':
            val *= 2.0
        elif pokemon['ability'] == 'Swift Swim' and weather == 'Rain':
            val *= 2.0
        elif pokemon['ability'] == 'Protosynthesis' and weather == 'Sun' and pokemon['name'] == 'Flutter Mane':
            val *= 1.5
        # Tailwind speed multiplier
        if pokemon['is_player'] and state.get('player_tailwind', 0) > 0:
            val *= 2.0
        elif not pokemon['is_player'] and state.get('opponent_tailwind', 0) > 0:
            val *= 2.0
        # Status Paralysis Speed drop
        if pokemon['status'] == 'Paralyzed':
            val *= 0.5
            
    # Weather and Ability Attack scaling
    elif stat_name == 'atk':
        if pokemon['ability'] == 'Protosynthesis' and weather == 'Sun' and pokemon['name'] in ['Roaring Moon', 'Great Tusk']:
            val *= 1.3
        # Burn reduces physical attack damage
        if pokemon['status'] == 'Burn':
            val *= 0.5
            
    # Porygon2 Eviolite bulk boost
    if pokemon['name'] == 'Porygon2' and stat_name in ['def', 'spd']:
        val *= 1.5
        
    return val


def get_effectiveness(move_type, target):
    effectiveness = 1.0
    for t in target['types']:
        effectiveness *= TYPE_EFFECTIVENESS.get(move_type, {}).get(t, 1.0)
    return effectiveness


def make_hp_bar(hp, max_hp, length=10):
    if max_hp <= 0:
        return ""
    pct = hp / max_hp
    filled = int(round(pct * length))
    empty = length - filled
    bar_str = "=" * filled + "-" * empty
    if pct > 0.5:
        color = GREEN
    elif pct > 0.2:
        color = YELLOW
    else:
        color = RED
    return f"{color}[{bar_str}]{RESET}"


def init_pokemon(name, is_player):
    db_entry = POKEMON_DB[name]
    return {
        'name': name,
        'types': db_entry['types'],
        'stats': db_entry['stats'].copy(),
        'max_hp': db_entry['stats']['hp'],
        'hp': db_entry['stats']['hp'],
        'ability': db_entry['ability'],
        'moves': db_entry['moves'],
        'status': None,  # None, 'Burn', 'Paralyzed'
        'stat_stages': {'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0},
        'protected_this_turn': False,
        'last_move_used': None,
        'is_charging': False,
        'charging_move': None,
        'charging_target': None,
        'is_player': is_player,
        'is_mega': False,
        'mega_stone': db_entry.get('mega_stone'),
        'mega_form': db_entry.get('mega_form')
    }


def trigger_entrance_ability(pokemon, allies, foes, state):
    name = pokemon['name']
    ability = pokemon['ability']
    if ability == 'Drought':
        state['weather'] = 'Sun'
        state['weather_turns'] = 5
        print(f"{YELLOW}[Weather] {name}'s Drought intensified the Sun!{RESET}")
    elif ability == 'Drizzle':
        state['weather'] = 'Rain'
        state['weather_turns'] = 5
        print(f"{BLUE}[Weather] {name}'s Drizzle summoned the Rain!{RESET}")
    elif ability == 'Download':
        # Compare SpD vs Def of active opponents
        total_def = sum(get_effective_stat(p, 'def', state) for p in foes if p and p['hp'] > 0)
        total_spd = sum(get_effective_stat(p, 'spd', state) for p in foes if p and p['hp'] > 0)
        if total_spd < total_def:
            pokemon['stat_stages']['spa'] = min(6, pokemon['stat_stages']['spa'] + 1)
            print(f"{YELLOW}[Ability] {name}'s Download boosted its Special Attack! (SpA: {pokemon['stat_stages']['spa']:+d}){RESET}")
        else:
            pokemon['stat_stages']['atk'] = min(6, pokemon['stat_stages']['atk'] + 1)
            print(f"{YELLOW}[Ability] {name}'s Download boosted its Attack! (Atk: {pokemon['stat_stages']['atk']:+d}){RESET}")
    elif ability == 'Intimidate':
        print(f"{YELLOW}[Ability] {name}'s Intimidate cut the Attack of foes!{RESET}")
        for foe in foes:
            if foe and foe['hp'] > 0:
                foe['stat_stages']['atk'] = max(-6, foe['stat_stages']['atk'] - 1)
                print(f"  {foe['name']}'s Attack fell! (Atk: {foe['stat_stages']['atk']:+d})")


def perform_switch(is_player, active_idx, bench_idx, state):
    active_list = state['player_active'] if is_player else state['opponent_active']
    bench_list = state['player_bench'] if is_player else state['opponent_bench']
    
    old_pkmn = active_list[active_idx]
    new_pkmn = bench_list[bench_idx]
    
    if old_pkmn:
        # Reset stages and statuses before placing back to bench
        old_pkmn['stat_stages'] = {'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0}
        old_pkmn['protected_this_turn'] = False
        old_pkmn['last_move_used'] = None
        old_pkmn['is_charging'] = False
        bench_list[bench_idx] = old_pkmn
    else:
        bench_list.pop(bench_idx)
        
    active_list[active_idx] = new_pkmn
    
    side_str = f"{GREEN}Player{RESET}" if is_player else f"{RED}Opponent{RESET}"
    if old_pkmn:
        print(f"{YELLOW}[Switch] {side_str} withdrew {old_pkmn['name']} and sent out {new_pkmn['name']}!{RESET}")
    else:
        print(f"{YELLOW}[Switch] {side_str} sent out {new_pkmn['name']}!{RESET}")
        
    # Trigger entrance ability
    allies = state['player_active'] if is_player else state['opponent_active']
    foes = state['opponent_active'] if is_player else state['player_active']
    trigger_entrance_ability(new_pkmn, allies, foes, state)


def trigger_start_entrance_abilities(state):
    starters = []
    for p in state['player_active']:
        if p: starters.append(p)
    for p in state['opponent_active']:
        if p: starters.append(p)
        
    # Sort starters by Spe to resolve weather abilities accurately
    starters.sort(key=lambda p: get_effective_stat(p, 'spe', state), reverse=True)
    
    for p in starters:
        foes = state['opponent_active'] if p['is_player'] else state['player_active']
        allies = state['player_active'] if p['is_player'] else state['opponent_active']
        trigger_entrance_ability(p, allies, foes, state)


def get_dashboard_active_line(pos_str, p, is_player):
    if p is None:
        text = f"  {pos_str:5}: [Empty]"
        pad = " " * (56 - len(text))
        return f"  {pos_str:5}: {GRAY}[Empty]{RESET}{pad}"
        
    hp_bar_raw = "[" + "=" * int(round(p['hp']/p['max_hp']*10)) + "-" * (10 - int(round(p['hp']/p['max_hp']*10))) + "]"
    stages_list = [f"{k}{v:+d}" for k, v in p['stat_stages'].items() if v != 0]
    stages_str = f" ({','.join(stages_list)})" if stages_list else ""
    status_str = f" [{p['status']}]" if p['status'] else ""
    charging_str = f" (Chg:{p['charging_move']})" if p['is_charging'] else ""
    
    # Compute padding
    plain_start = f"  {pos_str:5}: {p['name']:12} - HP: {p['hp']:3}/{p['max_hp']:3} "
    plain_end = f"{hp_bar_raw}{status_str}{stages_str}{charging_str}"
    pad = " " * max(0, 56 - (len(plain_start) + len(plain_end)))
    
    # Colorize name
    name_color = GREEN if is_player else RED
    colored_name = f"{name_color}{p['name']:12}{RESET}"
    
    # Colorize HP bar
    pct = p['hp'] / p['max_hp']
    bar_color = GREEN if pct > 0.5 else (YELLOW if pct > 0.2 else RED)
    colored_bar = f"{bar_color}{hp_bar_raw}{RESET}"
    
    # Colorize status
    colored_status = f" [{RED}{p['status']}{RESET}]" if p['status'] else ""
    
    # Colorize stages
    colored_stages = ""
    if stages_list:
        parts = []
        for k, v in p['stat_stages'].items():
            if v != 0:
                s_color = GREEN if v > 0 else RED
                sign = "+" if v > 0 else ""
                parts.append(f"{s_color}{k}:{sign}{v}{RESET}")
        colored_stages = f" ({','.join(parts)})"
        
    colored_charging = f" {YELLOW}(Charging {p['charging_move']}){RESET}" if p['is_charging'] else ""
    
    return f"  {pos_str:5}: {colored_name} - HP: {p['hp']:3}/{p['max_hp']:3} {colored_bar}{colored_status}{colored_stages}{colored_charging}{pad}"


def draw_dashboard(state):
    clear_screen()
    # Header box top border
    print(f"{CYAN}+----------------------------------------------------------+{RESET}")
    
    # Weather and Trick Room Indicators
    weather_str = "NONE"
    if state['weather'] == 'Sun':
        weather_str = "SUN"
    elif state['weather'] == 'Rain':
        weather_str = "RAIN"
        
    weather_text = f"WEATHER: {weather_str}"
    if state['weather'] != 'None':
        weather_text += f" ({state['weather_turns']}t)"
        
    tr_text = ""
    if state['trick_room'] > 0:
        tr_text = f" | TRICK ROOM ({state['trick_room']}t)"
        
    full_weather_plain = f" {weather_text}{tr_text}"
    weather_pad = " " * max(0, 56 - len(full_weather_plain))
    
    # Colorize weather text
    w_color = YELLOW if state['weather'] == 'Sun' else (BLUE if state['weather'] == 'Rain' else WHITE)
    colored_weather_str = f"{w_color}{weather_str}{RESET}"
    
    colored_weather_text = f"WEATHER: {colored_weather_str}"
    if state['weather'] != 'None':
        colored_weather_text += f" ({state['weather_turns']}t)"
        
    colored_tr_text = ""
    if state['trick_room'] > 0:
        colored_tr_text = f" | {PURPLE}TRICK ROOM ({state['trick_room']}t){RESET}"
        
    print(f"{CYAN}|{RESET} {colored_weather_text}{colored_tr_text}{weather_pad} {CYAN}|{RESET}")
    print(f"{CYAN}+----------------------------------------------------------+{RESET}")
    
    # Opponents Active
    opp_header = " [FOE FIELD]"
    opp_pad = " " * (56 - len(opp_header))
    print(f"{CYAN}|{RESET} {RED}{opp_header}{RESET}{opp_pad} {CYAN}|{RESET}")
    for i, p in enumerate(state['opponent_active']):
        pos_str = "Left" if i == 0 else "Right"
        line = get_dashboard_active_line(pos_str, p, is_player=False)
        print(f"{CYAN}|{RESET} {line} {CYAN}|{RESET}")
        
    print(f"{CYAN}+----------------------------------------------------------+{RESET}")
    
    # Allies Active
    allied_header = " [ALLIED FIELD]"
    allied_pad = " " * (56 - len(allied_header))
    print(f"{CYAN}|{RESET} {GREEN}{allied_header}{RESET}{allied_pad} {CYAN}|{RESET}")
    for i, p in enumerate(state['player_active']):
        pos_str = "Left" if i == 0 else "Right"
        line = get_dashboard_active_line(pos_str, p, is_player=True)
        print(f"{CYAN}|{RESET} {line} {CYAN}|{RESET}")
        
    print(f"{CYAN}+----------------------------------------------------------+{RESET}")
    
    # Bench displays
    bench_p = [p['name'] for p in state['player_bench'] if p['hp'] > 0]
    bench_o = [p['name'] for p in state['opponent_bench'] if p['hp'] > 0]
    
    bench_p_str = f"Player Bench: {', '.join(bench_p) if bench_p else '[None]'}"
    bench_o_str = f"Opponent Bench: {', '.join(bench_o) if bench_o else '[None]'}"
    
    p_bench_pad = " " * max(0, 56 - len(bench_p_str))
    o_bench_pad = " " * max(0, 56 - len(bench_o_str))
    
    colored_bench_p = f"Player Bench: {GREEN}{', '.join(bench_p) if bench_p else '[None]'}{RESET}"
    colored_bench_o = f"Opponent Bench: {RED}{', '.join(bench_o) if bench_o else '[None]'}{RESET}"
    
    print(f"{CYAN}|{RESET} {colored_bench_p}{p_bench_pad} {CYAN}|{RESET}")
    print(f"{CYAN}|{RESET} {colored_bench_o}{o_bench_pad} {CYAN}|{RESET}")
    print(f"{CYAN}+----------------------------------------------------------+{RESET}\n")


def execute_move(attacker, move_name, target_idx, allies, foes, state):
    # Paralysis check
    if attacker['status'] == 'Paralyzed' and random.random() < 0.25:
        print(f"  {YELLOW}[Status] {attacker['name']} is paralyzed! It can't move!{RESET}")
        attacker['is_charging'] = False
        return
        
    move = MOVE_DB[move_name]
    
    # Charging mechanic check (Solar Beam and Electro Shot)
    if move_name == 'Solar Beam':
        if state['weather'] != 'Sun':
            if not attacker['is_charging']:
                attacker['is_charging'] = True
                attacker['charging_move'] = 'Solar Beam'
                attacker['charging_target'] = target_idx
                print(f"  {YELLOW}[Status] {attacker['name']} is absorbing sunlight!{RESET}")
                attacker['last_move_used'] = move_name
                return
            else:
                attacker['is_charging'] = False
        else:
            attacker['is_charging'] = False
            
    elif move_name == 'Electro Shot':
        if state['weather'] != 'Rain':
            if not attacker['is_charging']:
                attacker['is_charging'] = True
                attacker['charging_move'] = 'Electro Shot'
                attacker['charging_target'] = target_idx
                attacker['stat_stages']['spa'] = min(6, attacker['stat_stages']['spa'] + 1)
                print(f"  {YELLOW}[Ability] {attacker['name']} is absorbing electricity! Sp. Atk rose!{RESET}")
                attacker['last_move_used'] = move_name
                return
            else:
                attacker['is_charging'] = False
        else:
            if not attacker['is_charging']:
                attacker['stat_stages']['spa'] = min(6, attacker['stat_stages']['spa'] + 1)
                print(f"  {YELLOW}[Ability] {attacker['name']}'s Special Attack rose from Electro Shot!{RESET}")
            attacker['is_charging'] = False

    # Protect Move check
    if move_name == 'Protect':
        if attacker['last_move_used'] == 'Protect':
            print(f"  {YELLOW}{attacker['name']} tried to Protect, but it failed!{RESET}")
            attacker['protected_this_turn'] = False
        else:
            print(f"  {GREEN if attacker['is_player'] else RED}{attacker['name']}{RESET} protected itself!")
            attacker['protected_this_turn'] = True
        attacker['last_move_used'] = 'Protect'
        return
        
    # Normal move used
    attacker['last_move_used'] = move_name
    print(f"\n{GREEN if attacker['is_player'] else RED}{attacker['name']}{RESET} used {CYAN}{move_name}{RESET}!")
    
    # Locate valid targets
    targets = []
    if move['target'] == 'Self':
        targets = [attacker]
    elif move['target'] == 'All Enemies':
        targets = [p for p in foes if p and p['hp'] > 0]
    else:  # Single Enemy
        target_pkmn = foes[target_idx]
        if target_pkmn is None or target_pkmn['hp'] <= 0:
            # Retarget to the other active opponent if available
            other_idx = 1 - target_idx
            other_pkmn = foes[other_idx]
            if other_pkmn and other_pkmn['hp'] > 0:
                target_pkmn = other_pkmn
                print(f"  {YELLOW}[System] Retargeted to {target_pkmn['name']}.{RESET}")
            else:
                target_pkmn = None
        if target_pkmn:
            targets = [target_pkmn]
            
    if not targets:
        print(f"  {GRAY}But there was no target...{RESET}")
        return
        
    # Spread moves modifiers
    is_spread = move['target'] == 'All Enemies'
    spread_mult = 0.75 if (is_spread and len(targets) > 1) else 1.0
    
    # Execute against each target
    for target in targets:
        # Check Protect
        if target['protected_this_turn'] and move['target'] != 'Self':
            print(f"  {YELLOW}{target['name']} protected itself!{RESET}")
            continue
            
        # Check Accuracy
        move_acc = move['accuracy']
        if move_name == 'Hurricane':
            if state['weather'] == 'Rain':
                move_acc = 100
            elif state['weather'] == 'Sun':
                move_acc = 50
            else:
                move_acc = 70
                
        if random.random() * 100 > move_acc:
            print(f"  {GRAY}The attack missed {target['name']}!{RESET}")
            continue
            
        # Type effectiveness check
        eff = 1.0
        if move['target'] != 'Self':
            eff = get_effectiveness(move['type'], target)
            if eff == 0.0:
                print(f"  {GRAY}It doesn't affect {target['name']}...{RESET}")
                continue
                
        # Status Moves
        if move['category'] == 'Status':
            if move_name == 'Recover':
                heal = target['max_hp'] // 2
                target['hp'] = min(target['max_hp'], target['hp'] + heal)
                print(f"  {target['name']} recovered {heal} HP! ({target['hp']}/{target['max_hp']})")
            elif move_name == 'Trick Room':
                if state['trick_room'] > 0:
                    state['trick_room'] = 0
                    print(f"  {PURPLE}[Trick Room] The twisted dimensions returned to normal!{RESET}")
                else:
                    state['trick_room'] = 5
                    print(f"  {PURPLE}[Trick Room] {attacker['name']} twisted the dimensions!{RESET}")
            elif move_name == 'Tailwind':
                if attacker['is_player']:
                    state['player_tailwind'] = 4
                    print(f"  {YELLOW}[Tailwind] A tailwind blew from behind your team!{RESET}")
                else:
                    state['opponent_tailwind'] = 4
                    print(f"  {YELLOW}[Tailwind] A tailwind blew from behind the opposing team!{RESET}")
            continue
            
        # Attack Damage calculations
        power = move['power']
        move_type = move['type']
        
        # Weather Ball adjustments
        if move_name == 'Weather Ball':
            if state['weather'] == 'Sun':
                move_type = 'Fire'
                power = 100
            elif state['weather'] == 'Rain':
                move_type = 'Water'
                power = 100
            else:
                move_type = 'Normal'
                power = 50
                
        # Eruption scales with HP percentage
        if move_name == 'Eruption':
            power = int(150 * (attacker['hp'] / attacker['max_hp']))
            power = max(1, power)
            
        # Check Critical Hit (1/24 standard Pokemon crit rate)
        is_crit = random.random() < (1.0 / 24.0)
        
        # Pick offensive stats
        if move_name == 'Body Press':
            # Critical hits ignore attacker negative stages
            A = get_effective_stat(attacker, 'def', state, ignore_negative_stages=is_crit)
        elif move['category'] == 'Physical':
            A = get_effective_stat(attacker, 'atk', state, ignore_negative_stages=is_crit)
        else:
            A = get_effective_stat(attacker, 'spa', state, ignore_negative_stages=is_crit)
            
        # Pick defensive stats
        if move['category'] == 'Physical':
            # Critical hits ignore defender positive stages
            D = get_effective_stat(target, 'def', state, ignore_positive_stages=is_crit)
        else:
            D = get_effective_stat(target, 'spd', state, ignore_positive_stages=is_crit)
            
        # Clamp defense
        D = max(1.0, D)
        
        # Standard Damage Math
        base_dmg = ((22 * power * A / D) / 50) + 2
        
        if is_crit:
            base_dmg *= 1.5
            
        # Weather damage adjustments
        if move_type == 'Fire':
            if state['weather'] == 'Sun':
                base_dmg *= 1.5
            elif state['weather'] == 'Rain':
                base_dmg *= 0.5
        elif move_type == 'Water':
            if state['weather'] == 'Rain':
                base_dmg *= 1.5
            elif state['weather'] == 'Sun':
                base_dmg *= 0.5
                
        # STAB (Same Type Attack Bonus)
        if move_type in attacker['types']:
            base_dmg *= 1.5
            
        # Apply type effectiveness
        base_dmg *= eff
        
        # Apply spread move reductions
        base_dmg *= spread_mult
        
        # Apply random damage variance (0.85 - 1.00)
        base_dmg *= random.uniform(0.85, 1.0)
        
        damage = max(1, int(base_dmg))
        
        # Apply damage to target
        was_alive = target['hp'] > 0
        target['hp'] = max(0, target['hp'] - damage)
        print(f"  {target['name']} took {damage} damage! ({target['hp']}/{target['max_hp']} HP)")
        
        # Track statistics
        attacker_name = attacker['name']
        state['damage_dealt'][attacker_name] = state['damage_dealt'].get(attacker_name, 0) + damage
        if was_alive and target['hp'] == 0:
            state['kos_achieved'][attacker_name] = state['kos_achieved'].get(attacker_name, 0) + 1
            
        if is_crit:
            print(f"  {YELLOW}A critical hit!{RESET}")
            
        if eff > 1:
            print(f"  {GREEN}It's super effective!{RESET}")
        elif eff < 1 and eff > 0:
            print(f"  {YELLOW}It's not very effective...{RESET}")
            
        # Stamina Ability checks
        if target['ability'] == 'Stamina' and target['hp'] > 0:
            target['stat_stages']['def'] = min(6, target['stat_stages']['def'] + 1)
            print(f"  {YELLOW}[Ability] Archaludon's Stamina boosted its Defense! (Def: {target['stat_stages']['def']:+d}){RESET}")
            
        # Giga Drain heals 50% damage
        if move_name == 'Giga Drain' and attacker['hp'] > 0:
            heal = damage // 2
            attacker['hp'] = min(attacker['max_hp'], attacker['hp'] + heal)
            print(f"  {attacker['name']} recovered {heal} HP! ({attacker['hp']}/{attacker['max_hp']} HP)")
            
        # Scald: 30% Burn chance (Fire-types are immune to burn)
        if move_name == 'Scald' and target['hp'] > 0 and target['status'] is None:
            if 'Fire' not in target['types'] and random.random() < 0.3:
                target['status'] = 'Burn'
                print(f"  {RED}[Status] {target['name']} was burned!{RESET}")
                
        # Snarl: lowers target's SpA by 1 stage
        if move_name == 'Snarl' and target['hp'] > 0:
            target['stat_stages']['spa'] = max(-6, target['stat_stages']['spa'] - 1)
            print(f"  {target['name']}'s Special Attack fell! (SpA: {target['stat_stages']['spa']:+d})")
            
        # Icy Wind: lowers target's Speed by 1 stage
        if move_name == 'Icy Wind' and target['hp'] > 0:
            target['stat_stages']['spe'] = max(-6, target['stat_stages']['spe'] - 1)
            print(f"  {target['name']}'s Speed fell! (Spe: {target['stat_stages']['spe']:+d})")
            
        # Flare Blitz: 33% recoil damage
        if move_name == 'Flare Blitz' and target['hp'] > 0 and attacker['hp'] > 0:
            recoil = damage // 3
            attacker['hp'] = max(0, attacker['hp'] - recoil)
            print(f"  {attacker['name']} took {recoil} recoil damage! ({attacker['hp']}/{attacker['max_hp']} HP)")
                
        # Tri Attack: 10% Paralysis chance
        if move_name == 'Tri Attack' and target['hp'] > 0 and target['status'] is None:
            if random.random() < 0.10:
                target['status'] = 'Paralyzed'
                print(f"  {YELLOW}[Status] {target['name']} was paralyzed!{RESET}")
                
    # Attacker recoil/stat drops
    if move_name == 'Draco Meteor' and attacker['hp'] > 0:
        attacker['stat_stages']['spa'] = max(-6, attacker['stat_stages']['spa'] - 2)
        print(f"  {YELLOW}{attacker['name']}'s Special Attack fell sharply! (SpA: {attacker['stat_stages']['spa']:+d}){RESET}")
        
    elif move_name in ['Close Combat', 'Headlong Rush'] and attacker['hp'] > 0:
        attacker['stat_stages']['def'] = max(-6, attacker['stat_stages']['def'] - 1)
        attacker['stat_stages']['spd'] = max(-6, attacker['stat_stages']['spd'] - 1)
        print(f"  {YELLOW}{attacker['name']}'s Defense and Sp. Def fell! (Def: {attacker['stat_stages']['def']:+d}, SpD: {attacker['stat_stages']['spd']:+d}){RESET}")


def check_faints(state):
    # Check Player Active slots
    for i in range(2):
        p = state['player_active'][i]
        if p and p['hp'] <= 0:
            print(f"\n{RED}[Faint] Allied {p['name']} fainted!{RESET}")
            state['player_active'][i] = None
            
    # Check Opponent Active slots
    for i in range(2):
        p = state['opponent_active'][i]
        if p and p['hp'] <= 0:
            print(f"\n{RED}[Faint] Foe {p['name']} fainted!{RESET}")
            state['opponent_active'][i] = None


def get_player_actions(state):
    actions = []
    chosen_bench_indices = set()
    
    for i, p in enumerate(state['player_active']):
        if p is None or p['hp'] <= 0:
            continue
            
        # Auto action if charging
        if p['is_charging']:
            actions.append({
                'type': 'move',
                'pokemon': p,
                'move_name': p['charging_move'],
                'target_idx': p['charging_target'],
                'is_player': True,
                'active_idx': i,
                'mega_evolve': False
            })
            continue
            
        # Check Mega Evolution eligibility
        can_mega = (p.get('mega_stone') is not None) and (not p.get('is_mega')) and (not state.get('player_mega_used'))
        mega_select = False
        
        while True:
            print(f"\nWhat will {GREEN}{p['name']}{RESET} do? (Position: {'Left' if i == 0 else 'Right'})")
            print("1. Fight")
            print("2. Switch")
            if can_mega:
                print("3. Mega Evolve")
                choice = input("Select option (1-3): ").strip().lower()
            else:
                choice = input("Select option (1-2): ").strip().lower()
            
            if choice in ['3', 'mega', 'm'] and can_mega:
                mega_select = True
                print(f"  {YELLOW}[System] Mega Evolution armed for {p['name']}! Choose a move to activate.{RESET}")
                choice = '1'
                
            if choice in ['1', 'fight', 'f']:
                # Show moves
                print("\nMoves:")
                for idx, m_name in enumerate(p['moves']):
                    move = MOVE_DB[m_name]
                    eff_parts = []
                    if move['category'] != 'Status' and move['target'] != 'Self':
                        for opp in state['opponent_active']:
                            if opp and opp['hp'] > 0:
                                eff = get_effectiveness(move['type'], opp)
                                if eff > 1.0:
                                    eff_str = f"{GREEN}{eff}x{RESET}"
                                elif eff == 0.0:
                                    eff_str = f"{GRAY}0.0x{RESET}"
                                elif eff < 1.0:
                                    eff_str = f"{RED}{eff}x{RESET}"
                                else:
                                    eff_str = f"{WHITE}1.0x{RESET}"
                                eff_parts.append(f"vs {opp['name']}: {eff_str}")
                    eff_display = f" [{', '.join(eff_parts)}]" if eff_parts else ""
                    cat_color = RED if move['category'] == 'Physical' else (CYAN if move['category'] == 'Special' else PURPLE)
                    colored_cat = f"{cat_color}{move['category']:7}{RESET}"
                    power_str = str(move['power']) if move['power'] > 0 else '-'
                    print(f"  {idx + 1}. {m_name:14} ({move['type']:8} | {colored_cat} | Power: {power_str:3}){eff_display}")
                print("  5. Back")
                
                m_choice = input("Select a move (1-5): ").strip().lower()
                
                # Check move matching by name or index
                move_name = None
                is_back = False
                if m_choice in ['5', 'back', 'b']:
                    is_back = True
                else:
                    for m_name in p['moves']:
                        if m_choice in m_name.lower() and len(m_choice) >= 2:
                            move_name = m_name
                            break
                            
                if not move_name and not is_back:
                    try:
                        m_idx = int(m_choice) - 1
                        if 0 <= m_idx < 4:
                            move_name = p['moves'][m_idx]
                        elif m_idx == 4:
                            is_back = True
                    except ValueError:
                        pass
                        
                if is_back:
                    mega_select = False
                    continue
                if not move_name:
                    print("Invalid move option.")
                    continue
                    
                move = MOVE_DB[move_name]
                
                # Check single target targeting
                if move['target'] == 'Single Enemy':
                    print("\nSelect target:")
                    target_options = []
                    
                    opp_left = state['opponent_active'][0]
                    if opp_left and opp_left['hp'] > 0:
                        target_options.append((0, f"Left: {opp_left['name']} ({opp_left['hp']}/{opp_left['max_hp']} HP)"))
                        
                    opp_right = state['opponent_active'][1]
                    if opp_right and opp_right['hp'] > 0:
                        target_options.append((1, f"Right: {opp_right['name']} ({opp_right['hp']}/{opp_right['max_hp']} HP)"))
                        
                    target_options.append((-1, "Back"))
                    
                    for opt_idx, opt in enumerate(target_options):
                        print(f"  {opt_idx + 1}. {opt[1]}")
                        
                    t_choice = input(f"Select target (1-{len(target_options)}): ").strip().lower()
                    selected_target = None
                    try:
                        t_opt_idx = int(t_choice) - 1
                        if 0 <= t_opt_idx < len(target_options):
                            selected_target = target_options[t_opt_idx]
                    except ValueError:
                        # Match name
                        for opt in target_options:
                            if opt[0] != -1:
                                opp_name = state['opponent_active'][opt[0]]['name'].lower()
                                if t_choice in opp_name and len(t_choice) >= 2:
                                    selected_target = opt
                                    break
                            else:
                                if t_choice in "back":
                                    selected_target = opt
                                    break
                                    
                    if not selected_target:
                        print("Invalid choice.")
                        continue
                        
                    if selected_target[0] == -1:
                        mega_select = False
                        continue  # Back
                        
                    target_idx = selected_target[0]
                else:
                    target_idx = 0
                    
                actions.append({
                    'type': 'move',
                    'pokemon': p,
                    'move_name': move_name,
                    'target_idx': target_idx,
                    'is_player': True,
                    'active_idx': i,
                    'mega_evolve': mega_select
                })
                break
                
            elif choice in ['2', 'switch', 's']:
                # Switch check
                available_bench = [idx for idx, bp in enumerate(state['player_bench']) if bp['hp'] > 0 and idx not in chosen_bench_indices]
                if not available_bench:
                    print("No other active Pokemon ready to fight on the bench!")
                    continue
                    
                print("\nSelect Pokemon to switch in:")
                bench_options = []
                for bp_idx in available_bench:
                    bp = state['player_bench'][bp_idx]
                    bench_options.append((bp_idx, f"{bp['name']} ({bp['hp']}/{bp['max_hp']} HP)"))
                bench_options.append((-1, "Back"))
                
                for opt_idx, opt in enumerate(bench_options):
                    print(f"  {opt_idx + 1}. {opt[1]}")
                    
                b_choice = input(f"Select option (1-{len(bench_options)}): ").strip().lower()
                selected_bench = None
                try:
                    b_opt_idx = int(b_choice) - 1
                    if 0 <= b_opt_idx < len(bench_options):
                        selected_bench = bench_options[b_opt_idx]
                except ValueError:
                    # Match name
                    for opt in bench_options:
                        if opt[0] != -1:
                            bp_name = state['player_bench'][opt[0]]['name'].lower()
                            if b_choice in bp_name and len(b_choice) >= 2:
                                selected_bench = opt
                                break
                        else:
                            if b_choice in "back":
                                selected_bench = opt
                                break
                                
                if not selected_bench:
                    print("Invalid choice.")
                    continue
                    
                if selected_bench[0] == -1:
                    continue  # Back
                    
                chosen_bench_idx = selected_bench[0]
                chosen_bench_indices.add(chosen_bench_idx)
                
                actions.append({
                    'type': 'switch',
                    'pokemon': p,
                    'bench_idx': chosen_bench_idx,
                    'is_player': True,
                    'active_idx': i
                })
                break
            else:
                if can_mega:
                    print("Invalid input. Select 1, 2, or 3.")
                else:
                    print("Invalid input. Select 1 or 2.")
    return actions


def get_ai_actions(state):
    actions = []
    for i, p in enumerate(state['opponent_active']):
        if p is None or p['hp'] <= 0:
            continue
            
        # Auto-action if charging
        if p['is_charging']:
            actions.append({
                'type': 'move',
                'pokemon': p,
                'move_name': p['charging_move'],
                'target_idx': p['charging_target'],
                'is_player': False,
                'active_idx': i
            })
            continue
            
        best_move = None
        best_target = 0
        best_score = -9999
        
        # Speeds for Trick Room evaluation
        ai_avg_spe = sum(get_effective_stat(pk, 'spe', state) for pk in state['opponent_active'] if pk and pk['hp'] > 0)
        pl_avg_spe = sum(get_effective_stat(pk, 'spe', state) for pk in state['player_active'] if pk and pk['hp'] > 0)
        
        for move_name in p['moves']:
            move = MOVE_DB[move_name]
            
            possible_targets = []
            if move['target'] == 'Self':
                possible_targets = [0]
            elif move['target'] == 'All Enemies':
                possible_targets = [0]
            else:
                possible_targets = [idx for idx, pl in enumerate(state['player_active']) if pl and pl['hp'] > 0]
                
            for target_idx in possible_targets:
                score = 0
                
                # Protect evaluation
                if move_name == 'Protect':
                    if p['last_move_used'] == 'Protect':
                        score = -9999
                    else:
                        score = 40
                        if p['hp'] < p['max_hp'] * 0.4:
                            score += 60
                            
                # Recover evaluation
                elif move_name == 'Recover':
                    if p['hp'] == p['max_hp']:
                        score = -9999
                    else:
                        score = 20
                        if p['hp'] < p['max_hp'] * 0.5:
                            score += 100
                            
                # Trick Room evaluation
                elif move_name == 'Trick Room':
                    if state['trick_room'] > 0:
                        score = -9999
                    else:
                        score = 10
                        if pl_avg_spe > ai_avg_spe:
                            score += 120
                        else:
                            score -= 80
                            
                # Attack Moves evaluation
                else:
                    power = move['power']
                    move_type = move['type']
                    
                    if move_name == 'Weather Ball':
                        if state['weather'] == 'Sun':
                            move_type = 'Fire'
                            power = 100
                        elif state['weather'] == 'Rain':
                            move_type = 'Water'
                            power = 100
                        else:
                            move_type = 'Normal'
                            power = 50
                            
                    if move_name == 'Eruption':
                        power = int(150 * (p['hp'] / p['max_hp']))
                        power = max(1, power)
                        
                    target_pk = state['player_active'][target_idx]
                    if target_pk and target_pk['hp'] > 0:
                        if move_name == 'Body Press':
                            A = get_effective_stat(p, 'def', state)
                        elif move['category'] == 'Physical':
                            A = get_effective_stat(p, 'atk', state)
                        else:
                            A = get_effective_stat(p, 'spa', state)
                            
                        if move['category'] == 'Physical':
                            D = get_effective_stat(target_pk, 'def', state)
                        else:
                            D = get_effective_stat(target_pk, 'spd', state)
                            
                        D = max(1.0, D)
                        base_dmg = ((22 * power * A / D) / 50) + 2
                        
                        # Weather modifier
                        if move_type == 'Fire':
                            if state['weather'] == 'Sun': base_dmg *= 1.5
                            elif state['weather'] == 'Rain': base_dmg *= 0.5
                        elif move_type == 'Water':
                            if state['weather'] == 'Rain': base_dmg *= 1.5
                            elif state['weather'] == 'Sun': base_dmg *= 0.5
                            
                        # STAB
                        if move_type in p['types']:
                            base_dmg *= 1.5
                            
                        # Type effectiveness
                        eff = get_effectiveness(move_type, target_pk)
                        base_dmg *= eff
                        
                        est_damage = int(base_dmg)
                        score = est_damage
                        
                        # Multiplier bonus
                        if eff > 1.0:
                            score += 40
                        elif eff == 0.0:
                            score -= 300
                        elif eff < 1.0:
                            score -= 40
                            
                        # Weather synergy
                        if move_type == 'Fire' and state['weather'] == 'Sun':
                            score += 30
                        elif move_type == 'Water' and state['weather'] == 'Rain':
                            score += 30
                            
                        # STAB bonus
                        if move_type in p['types']:
                            score += 15
                            
                        # KO security
                        if est_damage >= target_pk['hp']:
                            score += 150
                            
                    # Charging moves penalty outside weather
                    if move_name == 'Electro Shot' and state['weather'] != 'Rain':
                        score -= 20
                    elif move_name == 'Solar Beam' and state['weather'] != 'Sun':
                        score -= 20
                        
                    # Burn penalty
                    if p['status'] == 'Burn' and move['category'] == 'Physical':
                        score -= 30
                        
                score += random.uniform(-5, 5)
                
                if score > best_score:
                    best_score = score
                    best_move = move_name
                    best_target = target_idx
                    
        if best_move is None:
            best_move = random.choice(p['moves'])
            best_target = 0
            
        actions.append({
            'type': 'move',
            'pokemon': p,
            'move_name': best_move,
            'target_idx': best_target,
            'is_player': False,
            'active_idx': i
        })
    return actions


def resolve_actions(player_actions, ai_actions, state):
    all_actions = player_actions + ai_actions
    
    # 1. Resolve manual switches first (Priority +6)
    switches = [a for a in all_actions if a['type'] == 'switch']
    for s in switches:
        perform_switch(s['is_player'], s['active_idx'], s['bench_idx'], state)
        
    # 1.5. Resolve Mega Evolutions before moves speed calculation
    for m in [a for a in all_actions if a['type'] == 'move']:
        if m.get('mega_evolve') and m['is_player']:
            p = m['pokemon']
            if not p['is_mega']:
                print(f"\n{YELLOW}[Mega Evolution] {p['name']}'s {p['mega_stone']} reacted to the Mega Ring!{RESET}")
                mega_data = p['mega_form']
                p['name'] = mega_data['name']
                p['stats'] = mega_data['stats'].copy()
                p['ability'] = mega_data['ability']
                p['is_mega'] = True
                state['player_mega_used'] = True
                print(f"  {GREEN}{p['name']} Mega Evolved!{RESET}")
                # Trigger Drought weather ability immediately
                trigger_entrance_ability(p, state['player_active'], state['opponent_active'], state)
        
    # 2. Resolve moves (Sort by Move Priority, then Speed based on Trick Room)
    moves = [a for a in all_actions if a['type'] == 'move']
    for m in moves:
        pkmn = m['pokemon']
        pri = MOVE_DB[m['move_name']]['priority']
        if pkmn['ability'] == 'Prankster' and MOVE_DB[m['move_name']]['category'] == 'Status':
            pri += 1
        m['priority'] = pri
        m['speed'] = get_effective_stat(pkmn, 'spe', state)
        
    # Speed sorting logic: descending normally, ascending in Trick Room
    moves.sort(key=lambda x: (
        x['priority'], 
        x['speed'] if state['trick_room'] == 0 else -x['speed'], 
        random.random()
    ), reverse=True)
    
    for m in moves:
        attacker = m['pokemon']
        if attacker['hp'] <= 0:
            continue
            
        if m['is_player']:
            allies = state['player_active']
            foes = state['opponent_active']
        else:
            allies = state['opponent_active']
            foes = state['player_active']
            
        execute_move(attacker, m['move_name'], m['target_idx'], allies, foes, state)
        check_faints(state)


def resolve_end_of_turn(state):
    print(f"\n{YELLOW}--- End of Turn status update ---{RESET}")
    
    # 1. Burn damage resolution
    for p in state['player_active'] + state['opponent_active']:
        if p and p['hp'] > 0 and p['status'] == 'Burn':
            burn_dmg = max(1, p['max_hp'] // 16)
            p['hp'] = max(0, p['hp'] - burn_dmg)
            print(f"  {RED}[Status] {p['name']} took {burn_dmg} damage from its burn! ({p['hp']}/{p['max_hp']} HP){RESET}")
            
    check_faints(state)
    
    # 2. Weather decays
    if state['weather_turns'] > 0:
        state['weather_turns'] -= 1
        if state['weather_turns'] == 0:
            print(f"  {YELLOW}[Weather] The weather returned to normal!{RESET}")
            state['weather'] = 'None'
            
    # 3. Trick Room decays
    if state['trick_room'] > 0:
        state['trick_room'] -= 1
        if state['trick_room'] == 0:
            print(f"  {PURPLE}[Trick Room] The Trick Room wore off!{RESET}")
            
    # 3.5. Tailwind decays
    if state.get('player_tailwind', 0) > 0:
        state['player_tailwind'] -= 1
        if state['player_tailwind'] == 0:
            print(f"  {YELLOW}[Tailwind] Your Tailwind wore off!{RESET}")
    if state.get('opponent_tailwind', 0) > 0:
        state['opponent_tailwind'] -= 1
        if state['opponent_tailwind'] == 0:
            print(f"  {YELLOW}[Tailwind] Foe's Tailwind wore off!{RESET}")
            
    # 4. Replacement switch-in phase (mandatory if active space is empty and bench has valid pokemon)
    # Player Replacement
    for i in range(2):
        if state['player_active'][i] is None:
            available_bench = [idx for idx, bp in enumerate(state['player_bench']) if bp['hp'] > 0]
            if available_bench:
                pos_str = "Left" if i == 0 else "Right"
                print(f"\n{GREEN}[Faint replacement] Your {pos_str} position is empty!{RESET}")
                for opt_idx, bp_idx in enumerate(available_bench):
                    bp = state['player_bench'][bp_idx]
                    print(f"  {opt_idx + 1}. {bp['name']} (HP: {bp['hp']}/{bp['max_hp']})")
                while True:
                    rep_choice = input(f"Select Pokemon (1-{len(available_bench)}): ").strip().lower()
                    chosen_idx = None
                    try:
                        opt_idx = int(rep_choice) - 1
                        if 0 <= opt_idx < len(available_bench):
                            chosen_idx = available_bench[opt_idx]
                    except ValueError:
                        # Match name
                        for bp_idx in available_bench:
                            bp_name = state['player_bench'][bp_idx]['name'].lower()
                            if rep_choice in bp_name and len(rep_choice) >= 2:
                                chosen_idx = bp_idx
                                break
                                
                    if chosen_idx is None:
                        print("Invalid choice. Please choose a number or type a Pokemon name.")
                        continue
                        
                    chosen_pkmn = state['player_bench'][chosen_idx]
                    if chosen_pkmn['hp'] <= 0:
                        print("That Pokemon is fainted!")
                        continue
                    perform_switch(is_player=True, active_idx=i, bench_idx=chosen_idx, state=state)
                    break
                        
    # AI Replacement
    for i in range(2):
        if state['opponent_active'][i] is None:
            available_bench = [idx for idx, bp in enumerate(state['opponent_bench']) if bp['hp'] > 0]
            if available_bench:
                # Automatically choose first healthy bench member
                perform_switch(is_player=False, active_idx=i, bench_idx=available_bench[0], state=state)


def print_match_summary(state):
    print(f"\n{CYAN}+----------------------------------------------------------+{RESET}")
    print(f"{CYAN}|                    MATCH SCOREBOARD                      |{RESET}")
    print(f"{CYAN}+----------------------------------------------------------+{RESET}")
    
    # Track all participants that entered battle
    player_names = set(p['name'] for p in state['player_active'] if p) | set(p['name'] for p in state['player_bench'] if p)
    opponent_names = set(p['name'] for p in state['opponent_active'] if p) | set(p['name'] for p in state['opponent_bench'] if p)
    
    print(f"\n{GREEN}YOUR TEAM PERFORMANCE:{RESET}")
    for name in sorted(player_names):
        dmg = state['damage_dealt'].get(name, 0)
        kos = state['kos_achieved'].get(name, 0)
        print(f"  * {name:18} | Damage Dealt: {dmg:4} | KOs: {kos}")
        
    print(f"\n{RED}OPPONENT TEAM PERFORMANCE:{RESET}")
    for name in sorted(opponent_names):
        dmg = state['damage_dealt'].get(name, 0)
        kos = state['kos_achieved'].get(name, 0)
        print(f"  * {name:18} | Damage Dealt: {dmg:4} | KOs: {kos}")
        
    all_participants = list(player_names | opponent_names)
    if all_participants:
        all_participants.sort(key=lambda n: (state['kos_achieved'].get(n, 0), state['damage_dealt'].get(n, 0)), reverse=True)
        mvp = all_participants[0]
        mvp_kos = state['kos_achieved'].get(mvp, 0)
        mvp_dmg = state['damage_dealt'].get(mvp, 0)
        print(f"\n{YELLOW}👑 MATCH MVP: {mvp} ({mvp_kos} KOs, {mvp_dmg} Damage dealt){RESET}")
        
    print(f"{CYAN}+----------------------------------------------------------+{RESET}\n")


def check_battle_end(state):
    player_healthy = sum(1 for p in state['player_active'] if p and p['hp'] > 0) + sum(1 for p in state['player_bench'] if p and p['hp'] > 0)
    opponent_healthy = sum(1 for p in state['opponent_active'] if p and p['hp'] > 0) + sum(1 for p in state['opponent_bench'] if p and p['hp'] > 0)
    
    if player_healthy == 0 and opponent_healthy == 0:
        print(f"\n{YELLOW}=== BATTLE COMPLETED ==={RESET}")
        print("The battle ended in a DRAW!")
        print_match_summary(state)
        return True
    elif player_healthy == 0:
        print(f"\n{YELLOW}=== BATTLE COMPLETED ==={RESET}")
        print(f"{RED}You lost! The opponent is victorious!{RESET}")
        print_match_summary(state)
        return True
    elif opponent_healthy == 0:
        print(f"\n{YELLOW}=== BATTLE COMPLETED ==={RESET}")
        print(f"{GREEN}You won! Congratulations, champion!{RESET}")
        print_match_summary(state)
        return True
    return False


def run_simulator():
    clear_screen()
    print("=" * 60)
    print(f"         {GREEN}WELCOME TO THE POKEMON VGC SIMULATOR{RESET}         ")
    print("=" * 60)
    
    # Team Selection Phase
    pool = ['Charizard', 'Venusaur', 'Torkoal', 'Whimsicott', 'Roaring Moon', 'Great Tusk']
    opp_pool = ['Politoed', 'Kingdra', 'Archaludon', 'Porygon2', 'Ludicolo', 'Incineroar']
    selected_names = []
    
    print("=" * 60)
    print(f"                     {RED}TEAM PREVIEW{RESET}                     ")
    print("=" * 60)
    print(f"\n{GREEN}YOUR TEAM POOL:{RESET}")
    for idx, name in enumerate(pool):
        db = POKEMON_DB[name]
        types = "/".join(db['types'])
        stats = db['stats']
        print(f"  {idx + 1}. {GREEN}{name:12}{RESET} [{types:14}] | HP:{stats['hp']:3} Spe:{stats['spe']:3} | Ability: {db['ability']}")
        
    print(f"\n{RED}OPPONENT TEAM POOL:{RESET}")
    for idx, name in enumerate(opp_pool):
        db = POKEMON_DB[name]
        types = "/".join(db['types'])
        stats = db['stats']
        print(f"  {idx + 1}. {RED}{name:12}{RESET} [{types:14}] | HP:{stats['hp']:3} Spe:{stats['spe']:3} | Ability: {db['ability']}")
    print("=" * 60)
    
    print("\nChoose exactly 4 Pokemon to bring into battle:")
    for i in range(4):
        while True:
            choice = input(f"Select Pokemon {i+1} (1-6 or by name): ").strip()
            
            # Match by name first
            chosen_name = None
            for p_name in pool:
                if choice.lower() in p_name.lower() and len(choice) >= 2:
                    chosen_name = p_name
                    break
                    
            # If name didn't match, check index
            if not chosen_name:
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < 6:
                        chosen_name = pool[idx]
                except ValueError:
                    pass
                    
            if not chosen_name:
                print("Invalid input. Please choose a number from 1 to 6, or type a Pokemon's name.")
                continue
                
            if chosen_name in selected_names:
                print("You have already selected this Pokemon!")
                continue
                
            selected_names.append(chosen_name)
            print(f"Added {GREEN}{chosen_name}{RESET} to your team!")
            break
                
    # Setup initial rosters
    # Player
    player_team = [init_pokemon(name, is_player=True) for name in selected_names]
    player_active = [player_team[0], player_team[1]]
    player_bench = [player_team[2], player_team[3]]
    
    # AI randomly selects 4 from its pool of 6
    opponent_selected = random.sample(opp_pool, 4)
    opponent_team = [init_pokemon(name, is_player=False) for name in opponent_selected]
    opponent_active = [opponent_team[0], opponent_team[1]]
    opponent_bench = [opponent_team[2], opponent_team[3]]
    
    # Global state dictionary
    state = {
        'weather': 'None',
        'weather_turns': 0,
        'trick_room': 0,
        'player_mega_used': False,
        'player_tailwind': 0,
        'opponent_tailwind': 0,
        'player_active': player_active,
        'player_bench': player_bench,
        'opponent_active': opponent_active,
        'opponent_bench': opponent_bench,
        'damage_dealt': {},
        'kos_achieved': {}
    }
    
    print(f"\n{YELLOW}[System] The battle is beginning! Sending out lead Pokemon...{RESET}\n")
    # Trigger start of battle entrance abilities
    trigger_start_entrance_abilities(state)
    
    turn = 1
    while True:
        # Reset protects
        for p in state['player_active'] + state['opponent_active']:
            if p:
                p['protected_this_turn'] = False
                
        # Draw Field Layout
        draw_dashboard(state)
        print(f"--- Turn {turn} ---")
        
        # 1. Player action input
        player_actions = get_player_actions(state)
        
        # 2. AI action input
        ai_actions = get_ai_actions(state)
        
        # 3. Resolve actions
        resolve_actions(player_actions, ai_actions, state)
        
        # 4. End of turn cleanup
        resolve_end_of_turn(state)
        
        # 5. Victory check
        if check_battle_end(state):
            break
            
        turn += 1
        input(f"\n{YELLOW}Press [Enter] to proceed to the next turn...{RESET}")
        clear_screen()


if __name__ == '__main__':
    try:
        run_simulator()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[Exit] Emergency office exit activated. Goodbye!{RESET}")
        sys.exit(0)
