# FIRST Energize Match Data Grabber
This repo has a series of scripts for obtaining useful data for the FIRST Charged Up game. This data can be useful for scouting, comparing to scouting data, or determining match strategies. Use the scripts as you please. 

## epa_data.py
This script gets EPA data for the current year from each team in a specified district and writes it to the "epa_data.csv" file. The data written includes the team number, overall EPA, autonomous, teleop, and endgame EPAs, and the team's win rate.
## epa_data_event.py
Does the same thing as epa_data.py but only for the list of teams specified in the file "event_teams.txt" which is created by get_teams_at_event.py
## get_event_match_data.py
Gets the data for each team in each match at a specified event. The data includes mobility, autonomous and endgame charge station, autonomous and teleop cycles. Note that the autonomous and teleop cycles are a combined total of the alliances cycles, not the individual teams as FIRST does not collect individual team cycles. The data is output to "data.csv"
## get_scout_accuracy.py
This one requires a spreadsheet input, but basically takes TBA data and the team's data and returns the scouting accuracy of each scout. This is not a definitive calculation and does have some problems. The spreadsheet for this is also broken right now and not on GitHub. 
## get_teams_at_event.py
Gets a list of the teams at the specified event and creates the "event_teams.txt" file with one team per line.
## match_data.py
A set of classes for holding match data collected from The Blue Alliance API by get_event_match_data.py
