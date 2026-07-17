# Pokemon VGC Simulator

A CLI-based double battle simulator designed to replicate the core mechanics of competitive Pokémon VGC (Video Game Championships). Built entirely in Python, it features standard Level 50 competitions with Pokémon from the Scarlet & Violet DLC.

---

## Features

- **Double Battles (2v2)**: True VGC format where you bring 4 Pokémon out of a pool of 6.
- **Mega Evolution**: Mega Evolve your Pokémon (e.g., Charizard into Mega Charizard Y) mid-battle to change stats and activate weather abilities.
- **Weather Synergies**:
  - **Sun (Drought)**: Boosts Fire-type moves, triggers *Chlorophyll* (doubles Speed), and activates *Protosynthesis* (increases Attack/Special Attack).
  - **Rain (Drizzle)**: Boosts Water-type moves, triggers *Swift Swim* (doubles Speed), and enables *Electro Shot* to charge instantly.
- **Speed Control & Field Hazards**:
  - **Tailwind**: Doubles team speed for 4 turns.
  - **Trick Room**: Reverses the speed order for 5 turns, allowing slower Pokémon to move first.
- **Abilities & Stat Buffs**:
  - **Intimidate**: Lowers opponents' Attack stage on entry.
  - **Stamina**: Boosts Defense when hit by attacks.
  - **Download**: Boosts Attack or Special Attack based on the opponent's weaker defense stat.
  - **Blaze**: Boosts Fire-type moves at low HP.
- **Status Conditions**:
  - **Burn**: Halves physical attack power and drains HP at the end of each turn.
  - **Paralysis**: Halves speed and introduces a chance to be fully paralyzed.
- **Post-Match Performance Board**: Track damage dealt, KOs achieved, and crown a match MVP!

---

## Team Preview Pools

### Your Team Pool (Sun/Offense Focused)
1. **Charizard** (Fire/Flying) + *Mega Stone (Charizardite Y)*: High Special Attack, activates Drought upon Mega Evolution.
2. **Venusaur** (Grass/Poison) + *Chlorophyll*: High Speed in Sun, uses Sludge Bomb and Giga Drain.
3. **Torkoal** (Fire) + *Drought*: Sets sun immediately on entry, utilizes high-power Eruption and Earth Power.
4. **Whimsicott** (Grass/Fairy) + *Prankster*: Priority Tailwind speed control.
5. **Roaring Moon** (Dragon/Dark) + *Protosynthesis*: High physical attacker, boosted by Sun.
6. **Great Tusk** (Ground/Fighting) + *Protosynthesis*: Physical powerhouse with Close Combat and Headlong Rush.

### Opponent Pool (Rain/Trick Room Focused)
1. **Politoed** (Water) + *Drizzle*: Sets rain on entry.
2. **Kingdra** (Water/Dragon) + *Swift Swim*: Dangerous sweeper with Hurricane and Draco Meteor.
3. **Archaludon** (Steel/Dragon) + *Stamina*: Steel tank that fires instant Electro Shots in rain.
4. **Porygon2** (Normal) + *Download* + *Eviolite*: Bulk boosted by 1.5x, sets up Trick Room.
5. **Ludicolo** (Water/Grass) + *Swift Swim*: Rain sweeper with Hydro Pump and Giga Drain.
6. **Incineroar** (Fire/Dark) + *Intimidate*: Lowers your physical damage on entry, utilizes Flare Blitz and Snarl.

---

## How to Run

Ensure you have Python 3.8+ installed. Navigate to the repository root directory and run the simulator using:

```bash
python -m PokemonVGC
```

Alternatively, run the script directly:

```bash
python PokemonVGC/__init__.py
```

---

## Mechanics Reference

- **Move Priority**: High-priority moves (like `Protect`) execute before normal moves regardless of speed.
- **Switching**: Switching a Pokémon out occurs before normal attacks.
- **Type Effectiveness**: Implements full type matchups, immunities (e.g. Ground vs Flying, Ghost vs Normal), and double weaknesses/resistances.
