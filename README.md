# Empire-Builder
Working on building a  digital version of the semi-obscure boardgame

This project is presently incomplete, and is just a hobby update project. It will likely remain that way, as I would like to experiment with other languages and libraries to potentially add websocket support, and make this playable online.

The current build includes:

- non-functional buttons for selecting player color and number of players
- functional button for starting a game
- a map of normal mileposts and mountain-type mileposts that is randomly generated
- A* pathfinding to find the cheapest path between any two points. Cost is generated from distance traveled and cost of building track between two points. (It costs 1 to build to a normal milepost and 2 to build to a mountain milepost)
- Pathfinding updates based on existing track. If a player has already laid track somewhere, the track will not build through that track. 

Future development goals: 
-Implement color-transitions as turns begin and end. Update pathfinding appropriately so that tracks a player has already built count as 0 cost. 
- Implement track renting according to the rules so that a player knows if it would be cheapest to just use another player's track to get to a city vs. building their own.
- Include money counters for the player, and allow them to build only what they have the funds for. 
- Build train objects to track where each player's train is, what its movement speed is, what its current loads are, etc.
- Work in online play (likely will have to be done with another language)
