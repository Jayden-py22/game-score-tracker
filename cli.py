import argparse
import crud
from datetime import datetime

parser = argparse.ArgumentParser(description="Player Score Manager")

subparsers = parser.add_subparsers(dest="command")

# Add a new player
add_player_parser = subparsers.add_parser("add-player")
add_player_parser.add_argument("name")

# Add a new score for a player
add_score_parser = subparsers.add_parser("add-score")
add_score_parser.add_argument("player_id", type=int)
add_score_parser.add_argument("score", type=int)
add_score_parser.add_argument("date")

# List all scores
subparsers.add_parser("list-scores")

# Update a score by ID
update_score_parser = subparsers.add_parser("update-score")
update_score_parser.add_argument("score_id", type=int)
update_score_parser.add_argument("new_score", type=int)

# Delete a score by ID
delete_score_parser = subparsers.add_parser("delete-score")
delete_score_parser.add_argument("score_id", type=int)

# Query scores within a date range
date_range_parser = subparsers.add_parser("query-by-date")
date_range_parser.add_argument("start_date")
date_range_parser.add_argument("end_date")

args = parser.parse_args()

if args.command == "add-player":
    crud.add_player(args.name)
    print(f"✅ Added player: {args.name}")

elif args.command == "add-score":
    crud.add_score(args.player_id, args.score, args.date)
    print(f"✅ Added score {args.score} for player ID {args.player_id} on {args.date}")

elif args.command == "list-scores":
    scores = crud.get_all_scores()
    for row in scores:
        print(row)

elif args.command == "update-score":
    crud.update_score(args.score_id, args.new_score)
    print(f"✅ Updated score ID {args.score_id} to {args.new_score}")

elif args.command == "delete-score":
    crud.delete_score(args.score_id)
    print(f"✅ Deleted score ID {args.score_id}")

elif args.command == "query-by-date":
    results = crud.get_scores_in_date_range(args.start_date, args.end_date)
    for row in results:
        print(row)

else:
    parser.print_help()