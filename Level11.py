#imports pandas and gives it the name of pd
import pandas as pd

#reads the csv file and sets that as the name game_info
game_info = pd.read_csv("video_games_raw.csv")
valid_choice = False
change = False

print("Video Game Catalog Manager.")

# Loop that asks the user to give a row number and makes sure that they give a valid number. 
while valid_choice == False:
    try:
        user_choice = int(input(f"Please enter a row number that you would like to inspect between 0 and {len(game_info)-1}: "))
        if 0 <= user_choice <= (len(game_info)-1):
            valid_choice = True
        else:
            print(f"Please enter a row number between 0 and {len(game_info)-1}")
            continue
    except ValueError:
        print(f"Please enter a row number between 0 and {len(game_info)-1}")
        continue


#shows the line that the person chose. 
display = game_info.iloc[user_choice]
print(display)

# Tells the user to change the status for the game that they chose. 
while change == False:
    new_status = input("Please enter a new status for the game, Backlog, Playing, Completed, Dropped: ").strip().title()
    if new_status in ["Backlog", "Playing", "Completed", "Dropped"]:
        change = True
    else:
        print("Please enter Backlog, Playing, Completed, or Dropped")
        continue

# updates the games status with accordance to the user's choice. 
game_info.at[user_choice,"Status"] = new_status

#sets all the things in the recommended column to no. 
game_info["Recommended"] = "No"

#sets the games that have a rating greater than or equal to 8 and price less than or equal to 40 as recommended to yes. 
game_info.loc[(game_info["Rating"] >= 8) & (game_info["Price"] <= 40), "Recommended"] = "Yes"

#prints the games and info with recommended as yes. 
print("Recommended Games: ")
print(game_info.query("Recommended == 'Yes'"))


#puts the new data unto the video games cleaned csv. 
game_info.to_csv("video_games_cleaned.csv", index = False)


print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv.")





