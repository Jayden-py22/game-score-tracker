import crud

# Add a new player
crud.add_player("TestPlayer")
# Add a new score for a player
crud.add_score(4, 123, "2025-05-08")  # player_id adjust as needed

# List all scores
for score in crud.get_all_scores():
    print(score)

# Update a score by ID
crud.update_score(1, 200)
# Delete a score by ID
crud.delete_score(2)