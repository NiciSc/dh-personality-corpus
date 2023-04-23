# General

This repository was used to create the following corpus with data from personality-database.com

<!-- HIER DIE WERTE FÜR DEN GANZEN KORPUS NACHTRAGEN-->

| Famous People: |       |
| -------------- | ----- |
| Pop Culture    | 15298 |
| Musician       | 14001 |
| Kpop           | 1939  |
| The Arts       | 5725  |
| Philosophy     | 1027  |
| Science        | 2841  |
| Sports         | 7830  |
| Business       | 1195  |
| Internet       | 19172 |
| Noteworthy     | 3051  |
| Historical     | 4031  |
| Religion       | 2345  |
| Political      | 3739  |

**∑: 82194**

| Fictional Characters: |       |
| --------------------- | ----- |
| Superheroes           | 4958  |
| Movies                | 51230 |
| Television            | 78084 |
| Anime & Manga         | 55235 |
| Gaming                | 79745 |
| Cartoons              | 29266 |
| Literature            | 37105 |
| Comics                | 3345  |
| Web Comics            | 18469 |
| Theatre               | 3104  |

**∑: 360541**

| Memes:                 |       |
| ---------------------- | ----- |
| Music                  | 39938 |
| Archetypes             | 8031  |
| Interests              | 10414 |
| Settings               | 2682  |
| Plots                  | 1576  |
| Franchises             | 3628  |
| Theories               | 2359  |
| Polls (If you...)      | 1992  |
| Your Experience        | 263   |
| Type Combo (Your Type) | 701   |
| Ask PDB                | 1025  |
| PDB Community          | 3137  |

**∑: 75746**

# File Structure

```
.
├── README.md
├── resources
│   ├── complete.feather                            Stores all data, used for analysis
│   ├── profiles_with_actors.csv                    Profile IDs which require additional scraping
│   └── templates
│       ├── corpus_template.json                    Data scheme for publication
│       └── internal_template.json                  (Reduced) data scheme for first analysis
├── src
│   ├── data-analysis
│   │   └── general_analysis.ipynb                  Analyses corpus
│   └── scraping
│       ├── Colab_Scraping_w_Requests.ipynb         Scrapes Profiles
│       ├── Actor_Scraping.ipynb                    Scrapes additional infos about profiles
│       └── data                                    Target folder for scraping
└── utils
    ├── json_formatter.py                           Transforms raw data
    └── movietelevision_ids.ipynb                   Scrapes IDs which require additional data
                                                    output: profiles_with_actors.csv
```

# Requirements
