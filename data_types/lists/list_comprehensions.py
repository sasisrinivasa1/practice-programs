players = ['Dhoni-7', 'Ronaldo-7', 'ABDe-17', 'Rishabt-17','Kohli-18','Sachin-10','Messi-10']

jersey_7 = [players[i] for i in range(len(players)) if (players[i].endswith("-7"))]
print("Sports players with jersey number 7 - ", jersey_7)

jersey_18 = [players[i] for i in range(len(players)) if (players[i].endswith("18"))]
print("\nSports players with jersey number 18 - ", jersey_18)

jersey_17 = [players[i] for i in range(len(players)) if (players[i].endswith("17"))]
print("\nSports players with jersey number 17 - ", jersey_17)

jersey_10 = [players[i] for i in range(len(players)) if (players[i].endswith("10"))]
print("\nSports players with jersey number 10 - ", jersey_10)

# Output:-
# Sports players with jersey number 7 -  ['Dhoni-7', 'Ronaldo-7']

# Sports players with jersey number 18 -  ['Kohli-18']

# Sports players with jersey number 17 -  ['ABDe-17', 'Rishabt-17']

# Sports players with jersey number 10 -  ['Sachin-10', 'Messi-10']