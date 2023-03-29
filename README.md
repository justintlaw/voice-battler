# Voice Final Project ASR

## Summary
This python program runs two processes at once:
  - A websocket server that the game can connect to
  - A voice recognition pipeline that takes commands from the user

Commands are place into `q_commands` from the recoginition process, and the
websocket server reads commands from that queue.

## Testing
To test the voice aspect of the project by itself, enter the following into
your terminal and run it: `voiceonly=true python index.py`.

## Command Structure

### **Overview**
Commands should be placed into the queue as a json object with the following
structure:
```javascript
{
  "target": "minions", // The part of the game that will be affected
  "action": "buy", // The action the game will take
  "amount": 1, // (optional) A number input when applicable
  "item": "warrior" // (optional) A value that the target will use
}
```

Not every command needs each property. The following two examples are also
acceptable:
```javascript
// example 1
{
  "target": "volume",
  "action": "turn up"
}

// example 2
{
  "target": "game",
  "action": "start"
}
```

### **Command Properties**
Targets:
  - "minions" (the part of the game that spawns people to attack)
  - "volume" (control the volume)
  - "game" (the overall game process, i.e., "start/pause/stop")

## Desired Commands:
Minions:
  - spawn/buy/order `{num}` `{soldier_type}`
    - "warrior", also known as:
      - "melee"
      - "axeman"
      - "axemen"
    - "rider", also known as:
      - "horseman"
      - "horse"
      - "bear dwarf"
      - "bear"
    - "ranged", also know as:
      - "crossbowman"
      - "crossbowmen"
      - "archer"

Game:
  - Start the game
  - Pause the game
  - Stop the game

Volume:
  - Turn up the volume
  - Turn down the volume
  - Turn off the volume
  - Turn on the volume
