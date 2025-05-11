import crud

crud.add_player("TestPlayer")
crud.add_score(4, 123, "2025-05-08")  # player_id 根据实际调整

for score in crud.get_all_scores():
    print(score)

crud.update_score(1, 200)
crud.delete_score(2)