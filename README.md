# Roomba-AI
Reinforcement Learning agent learns to clean up a room, like a Roomba.

### Method of computing total area agent covered
 * Just calculate the square area of the most separated 4 points the agent has travelled.
   - It's a naive approximation. 
   - Probably works unless the values are really similar, which is most likely the case in the beginning...
