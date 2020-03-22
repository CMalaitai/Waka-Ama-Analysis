# Waka Ama Spirit Nationals Analysis
## Digital Technologies & Hangarau Matihiko Level 3

**Standard title**: Develop a complex computer program

**Credits**: 6

**Resource title**: Waka Ama Spirit Nationals Analysis

**Resource reference**: Digital Technologies & Hangarau Matihiko 3.7B

### Introduction/Kupu Aratak
This assessment activity requires you to create a computer program, using complex techniques, to read in the raw data from the Waka Ama Sprint Nationals race results and award scoring for the competition.  In addition to reading from and writing to files, your program must also demonstrate one or more of the following complex programming techniques:
- creating a graphical user interface (GUI)
- defining class(es) and creating objects
- defining and using custom type(s)
- uses third party or non-coreAPI, library or framework 
- using complex data structures (e.g. stacks, queues, trees).

This assessment is developed with support of Nga Kaihoe o Aotearoa, Waka Ama New Zealand, www.wakaama.co.nz. Approval has been given to use the data associated with this assessment task.

You will be assessed on how effectively you develop, test and refine your program, so that it is a well-structured, logical response to the task.  While developing, testing and refining your program:
- write code that meetsall the task specifications
- set out the program code clearly, following conventions of your chosen programming language
- document the program with appropriate variable/module names and organised comments that describe code function and behaviour
- comprehensively test and debug your program in an organised way, to ensure that it works on a sample of both expected cases, relevant boundary cases, and invalid cases 
- ensure that the program is a well-structured, logical response to the task
- make the program flexible and robust

## Task/Hei Mahi
### Scenario
At the beginning of each year Nga Kaihoe o Aotearoa, Waka Ama New Zealand hold their annual Sprint Nationals. There is a mixture of events at the competition in which regional associations compete for medals as well as for the overall association of the competition.
The Club Points Trophy recognises a club’s paddling excellence and achievement throughout the week. Points are accumulated throughout the week from all finals, and the club with the most points at the end of the week is awarded this Club Points Trophy. The requirements for the competition points mean thata computer program is required to analyse all the races in order to:
- find theresults of the finals out of the batch of data 
- assign points based onplacing against the correct regional association. 

You are required to develop a computer program, using complex programming techniques, to read in the raw data from the race results, award scoring for the competition and determine the overall winning regional association. 
All times are recorded through the FinishLynx system. This is a camera and software that allow times to be recorded based on an image capture. The files are saved to the system as .lif files, very similar to .csv files.  The Waka Ama database records the progressions, results, disqualifications, places and times. 

### Flexibility in your programming
The program must be able to be flexible enough to handle different input parameters each year.  For example, 
- different regional associations may compete each year
- the number of lanes may differ each year based on where the Sprint Nationals are held
- if the competition is held overseas for Waka Ama worlds, different places and points may be awarded.

### Reading from files
You will have access to a folder of all the .lif files.  Your program must be able to connect to the finals files and read the raw data. You must ensure that no files are deleted from the folder. 
You may have to modify some files to enable testing and debugging.
Testing can be done by making a brief screencast showing the outcome being comprehensively tested.  If desired, you can take screenshots of your screencast and annotate them.  This is often easier than trying to screenshot whilst testing where it is easy to ‘forget’ to screenshot a key part of the test.  If you prefer, you are welcome to talk us through your testing and simply submit a brief screencast (screencasts should be 3 minutes or less in length).

### Waka Ama Sprint Nationals Scoring Program Specifications:
- The program must be able to determine the regional association that wins the Waka Ama New Zealand Club Points Trophy and displays the number of points for each association sorted in descending order and produce a .csv file with this information as output.
- On startup, the program should display what folder (2017 or 2018) it is analysing and the number of files in that folder.
- The program should find the finals files and analyse just those files. It should leave the other files alone.
- The program should show the file it is analysing. If there is an error while processing, it should display the error.
- The program should record the regional association and determine the points for all finals. These include bowl, plate, cup champ, straight finals.

### Rules for Assigning Points

1st place -8 points

2nd place -7 points

3rd place -6 points

4th place -5 points

5th place -4 points

6th place -3 points

7th place -2 points

8th place -1 point

any placing onward, 1 point.

### Other considerations for awarding of points
- If a resultis DQ/Disqualified or DNS (Did Not Start), no points are awarded.
- There may be some cases within the data that the same place is awarded to 2 or 3 teams, as they received the same finish time. This is not an error and they should each receive the same number of points.
- In the W12 category, where two regional associations are paddling in the same waka, the same points are to be given to both regional associations.

## Example (input of .lif file)
```045,Champ Final,1,Mid Women -W6 250,,,,,,250,9:04:36.5444,,,,,,,```

```1,56470,1,Puketirini Puhi,,Rahui Pokeka Waka Sports,1:30.11,,1:30.11,,,9:04:36.55,,,,1:30.11,1:30.11```

```2,53948,3,Rangiatea,,Otaki Waka Hoe Charitable Trust,1:32.39,,2.28,,,9:04:36.55,,,,2.28,2.28```

```3,55109,4,Tamaki Nga Taonga Iti,,TamakiOutrigger Canoe Club,1:33.33,,0.94,,,9:04:36.55,,,,0.94,0.94```

```4,56908,7,Hine Ataahua,,Horouta Waka Hoe Club Inc.,1:36.71,,3.38,,,9:04:36.55,,,,3.38,3.38```

```5,55852,2,Mauri Midgets,,Nga Hoe Horo Outrigger Canoe Cl,1:37.04,,0.33,,,9:04:36.55,,,,0.33,0.33```

```6,56121,6,Hilo,,Ruamata Waka Ama Club,1:37.76,,0.72,,,9:04:36.55,,,,0.72,0.72```

```7,56434,5,Midge Angels,,Waitakere Outrigger Canoe Club ,1:38.10,,0.34,,,9:04:36.55,,,,0.34,0.34```

```8,54498,8,Waipuna(R),,Te Toki Voyaging Trust,1:42.42,,4.32,,,9:04:36.55,,,,4.32,4.32```

The program will need to be able to establish whether a file is relevant (is it a final or not) and, for each file that is relevant, allocate the appropriate number of points to the regional association.

## Description of what is in each row
The top most row gives data about the race:race number, race type, heat, title, unused, unused, unused, unused, unused, length, start time, unused, unused, unused, unused, unused, unused 
eg. 

```045,Champ Final,1,Mid Women -W6 250,,,,,,250,9:04:36.5444,,,,,,,```

The rows that follow provide data about the placings of the teams, in finishing order. Notice that the same data may appear in several places in each row, and each row may repeat data found in a previous row. The final columns in first placing provides elapsed time, and subsequent rows the time difference between first and the subsequent places.
on subsequent rows:
place, team id, lane, team name, unused, regional association, elapsed time, unused, elapsed time, unused, unused, start time, unused, unused, unused, elapsed time, elapsed time

```1,56470,1,Puketirini Puhi,,Rahui Pokeka Waka Sports,1:30.11,,1:30.11,,,9:04:36.55,,,,1:30.11,1:30.11```

subsequent rows -place, team id, lane, team name, unused, regional association, elapsed time, unused, difference, unused, unused, start time, unused, unused, unused, difference, difference

```2,53948,3,Rangiatea,,Otaki Waka Hoe Charitable Trust,1:32.39,,2.28,,,9:04:36.55,,,,2.28,2.28```

### Example of a possible output: 
A table of values listing the associations and the points won in rank order, from highest to lowest, including an appropriate title. The table is formatted so that the column widths are appropriate for the text.

## FULL CLUB POINTS
| Association | Points |
| --- | --- |
| Horouta Waka Hoe Club Inc. | 418 |
| Manukau Outrigger Canoe Club | 154 |
| Ruamata Waka Ama Club | 145 |
| Mareikura Waka Ama Club Incorporated | 133 |
| Taniwha Outrigger Canoe Club Inc | 115 |
| Te Au Rere Waka Ama Club | 107 | 
| Kaihoe o Ngati Rehia Trust | 101.5 | 
| Haeata Ocean Sports Inc | 101 | 
| Otaki Waka Hoe Charitable Trust | 89 | 
| Hei Matau Paddlers | 88 | 
| Rahui Pokeka Waka Sports | 88 | 
| Mitamitaga o le Pasefika Va'a-alo Canoe Club | 77 | 
| Waitakere Outrigger Canoe Club Inc | 75.5 | 
| Turangawaewae Waka Sports | 75 |
| Te Paerangi Waka Ama Inc | 68.5 | 
| Akarana | 62 | 
| Parihaka Waka AmaInc | 56 | 
| Aratika Tamaki Waka Ama Club Incorporated | 52 | 
| Cook Islands Outriggers Association | 47 | 
| Nga Hoe Horo Outrigger Canoe Club | 43.5 | 
| Te Toki Voyaging Trust | 31.5 | 
| Whakatu Marae Waka-Ama Club| 31 |
| Te Rau Oranga O Ngati Kahungunu Waka Ama Club | 31 | 
| Wairarapa Waka Ama Canoe Club | 30 | 
| Te Waka Pounamu | 29 | 
| TOA Waka Ama Club | 28 | 
| Heretaunga Ararau O Ngati Kahungunu Waka Ama Roopu | 27 | 
| Waka Ama O Whakatane | 27 |
| Tauranga Moana Outrigger Canoe Club Inc. | 22.5 |
| Te Awa Haku | 20 | 
| Hawaiki Nui Tuarua Waka Ama | 19 | 
| Hoe Aroha Whanau o Mauao | 18.5 | 
| Porirua Canoe Kayak Club Inc. | 17 | 
| YMP Waka Ama | 17 | 
| Waikato Dragon Boat & Waka Ama Association | 12 | 
| Maraenui Rugby & Sports Association | 10 | 
| Whaingaroa Whanau Hoe Waka | 10 | 
| Te Pou Herenga Waka Ama Club Inc. | 9 | 
| Tarawera Outrigger Canoe Club | 8 | 
| Hoe Tonga Pacifica Waka Ama Association | 7 | 
| Tu Tangi Ora -South Kaipara Collective Inc | 6 | 
| Taranaki Outrigger Canoe Club | 6 | 
| Wakatipu Waka Ama Club | 6 |
| Ocean Blue Sports Club | 5 | 
| Hikoikoi Waka Club | 4 |
| Pakuranga Outrigger Canoe Club | 4 |
| Te Ringa Miti Tai Heke Whanganui Waka Ama Club Incorporated | 4 |
| Maketu Hoe Waka | 3.5 |
| Orakei Water Sports | 3 |
| Rangaunu Sports Club | 3 |
| Whanganui River Outrigger Canoe Club Inc. | 2 |
| Nga Tai Whakarongo | 1 |
| Te Puu Ao | 1 |
