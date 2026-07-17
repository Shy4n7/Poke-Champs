# Pokemon VGC Simulator

A CLI-based double battle simulator designed to replicate the core mechanics of competitive Pokémon VGC (Video Game Championships). Built entirely in Python, it features standard Level 50 competitive spreads, multiple weather and terrain synergies, speed control tactics, and Mega Evolution.

---

## 🎮 Features

- **Double Battles (2v2)**: True VGC format where you select 4 Pokémon out of a pool of 6 to bring into battle.
- **Multiple Team Archetypes**: Pick a strategy or randomize your draft! Both player and opponent select/randomize from 4 VGC archetypes or a fully random draft pool.
- **Mega Evolution**: Mega Evolve your Pokémon (e.g., Charizard into Mega Charizard Y) mid-battle to change stats and activate weather abilities.
- **Weather & Terrain Synergies**:
  - ☀️ **Sun (Drought)**: Boosts Fire-type moves, triggers *Chlorophyll* (doubles Speed), and activates *Protosynthesis* (increases Attack/Special Attack).
  - 🌧️ **Rain (Drizzle)**: Boosts Water-type moves, triggers *Swift Swim* (doubles Speed), and enables *Electro Shot* to charge instantly.
  - 🪨 **Sandstorm (Sand Stream)**: Boosts Rock-type Special Defense by 1.5x, triggers *Sand Rush* (doubles Speed), and deals damage at the end of each turn to non-Rock/Ground/Steel Pokémon.
  - 🔮 **Psychic Terrain (Psychic Surge)**: Boosts Psychic-type moves by 1.3x and blocks priority moves (like *Sucker Punch* and *Aqua Jet*) against grounded targets.
- **Abilities & Stat Buffs**:
  - **Intimidate**: Lowers opponents' Attack stage on entry.
  - **Stamina**: Boosts Defense when hit by attacks.
  - **Download**: Boosts Attack or Special Attack based on the opponent's weaker defense stat.
  - **Blaze**: Boosts Fire-type moves at low HP.
  - **Mirror Armor**: Reflects stat reduction attempts (like *Snarl* or *Intimidate*) back at the opponent.
  - **Unseen Fist**: Contact moves bypass protect options.
  - **Storm Drain**: Draws in and absorbs all Water-type attacks to boost Special Attack.
  - **Guts (Flame Orb)**: Activates a burn condition on entry, boosting physical damage by 1.5x and ignoring the attack drop of status conditions.
  - **Good as Gold**: Complete immunity to enemy status moves.
  - **Supreme Overlord**: Grants a damage boost for each fainted ally.
  - **Rough Skin**: Physical attackers take recoil damage on contact.
- **Status Conditions**:
  - **Burn**: Halves physical attack power (unless using *Guts*) and drains HP at the end of each turn.
  - **Paralysis**: Halves speed and introduces a chance to be fully paralyzed.
- **Post-Match Performance Board**: Track damage dealt, KOs achieved, and crown a match MVP!

---

## 📋 Strategy Pools & Roster

### 🟡 Sun Team (Sun & Protosynthesis Offense)
*   **Charizard** (Fire/Flying) + *Mega Stone (Charizardite Y)*: Activates Drought on Mega Evolution.
*   **Venusaur** (Grass/Poison) + *Chlorophyll*: Fast sweeper in Sun, utilizes *Weather Ball* changes.
*   **Torkoal** (Fire) + *Drought*: Sets sun immediately on entry, utilizes high-power *Eruption*.
*   **Whimsicott** (Grass/Fairy) + *Prankster*: Priority *Tailwind* speed control.
*   **Roaring Moon** (Dragon/Dark) + *Protosynthesis*: Physical powerhouse boosted by Sun.
*   **Great Tusk** (Ground/Fighting) + *Protosynthesis*: High Defense physical attacker.
*   **Flutter Mane** (Ghost/Fairy) + *Protosynthesis*: Blazing fast special attacker.

### 🔵 Rain Team (Rain & Swift Swim Control)
*   **Politoed** (Water) + *Drizzle*: Sets rain on entry.
*   **Kingdra** (Water/Dragon) + *Swift Swim*: Fast special sweep under rain.
*   **Archaludon** (Steel/Dragon) + *Stamina*: Steel tank that fires instant *Electro Shots* in rain.
*   **Ludicolo** (Water/Grass) + *Swift Swim*: Rain sweeper with *Hydro Pump* and *Giga Drain*.
*   **Pelipper** (Water/Flying) + *Drizzle*: Alternative rain setter and Tailwind controller.
*   **Urshifu-Rapid** (Water/Fighting) + *Unseen Fist*: Contact moves bypass *Protect*, strikes hard with *Surging Strikes* and *Aqua Jet*.

### 🟣 Trick Room Team (Slow, High-Bulk Heavy Hitters)
*   **Porygon2** (Normal) + *Download* + *Eviolite*: Ultra bulky, sets up *Trick Room*.
*   **Indeedee-F** (Psychic/Normal) + *Psychic Surge*: Activates Psychic Terrain, supports allies with *Helping Hand*.
*   **Ursaluna** (Ground/Normal) + *Guts* + *Flame Orb*: Heavy-hitting attacker utilizing boosted *Facade*.
*   **Armarouge** (Fire/Psychic) + *Flash Fire*: Sweeps with terrain-boosted *Expanding Force*.
*   **Kingambit** (Dark/Steel) + *Supreme Overlord*: Late-game cleaner with *Kowtow Cleave* and *Sucker Punch*.
*   **Incineroar** (Fire/Dark) + *Intimidate*: Cycles *Intimidate* and *Snarl* to lower foe offensive threat.

### 🟢 Sandstorm Team (Sand Stream & Rock/Steel Synergy)
*   **Tyranitar** (Rock/Dark) + *Sand Stream*: Sets Sandstorm on entry, gains 1.5x Special Defense boost.
*   **Excadrill** (Ground/Steel) + *Sand Rush*: Doubles speed under Sandstorm.
*   **Garchomp** (Dragon/Ground) + *Rough Skin*: High speed dragon with area damage *Earthquake*.
*   **Gastrodon** (Water/Ground) + *Storm Drain*: Immune to water moves, redirects opponent's Water-type attacks.
*   **Corviknight** (Flying/Steel) + *Mirror Armor*: Deflects stat drops, uses *Brave Bird* and *Roost*.
*   **Gholdengo** (Steel/Ghost) + *Good as Gold*: Immune to status moves, attacks with *Make It Rain*.

---

## 🚀 How to Run

Ensure you have Python 3.8+ installed. Navigate to the repository root directory and run the simulator using:

```bash
python -m PokemonVGC
```

Alternatively, run the script directly:

```bash
python PokemonVGC/__init__.py
```

---

## 🛠️ Mechanics Reference

- **Move Priority**: High-priority moves (like `Protect`, `Sucker Punch`, `Aqua Jet`) execute before normal moves.
- **Switching**: Switching a Pokémon out occurs before normal attacks.
- **Type Effectiveness**: Implements full type matchups, immunities (e.g. Ground vs Flying, Ghost vs Normal), and double weaknesses/resistances.
