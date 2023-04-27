# General

This repository was used to create the following corpus with data from the website _personality-database.com_.

This project was carried out as part of a master's degree course at the [University of Regensburg](https://www.uni-regensburg.de/en).

The scraping was performed using Python 3.10 in a Jupyter Notebook environment with the aid of Python's Request module.

The analysis was performed using Pandas, Seaborn, Matplotlib, scikit-learn and SciPy using Python 3.10 in a Jupyter Notebook environment.

<p align="center">
<b>NO ACTUAL DATA IS INCLUDED IN THIS REPOSITORY</b>
</p>

# Repository Structure

```
.
├── README.md
├── LICENSE                                         Repository is licensed the MIT license
├── resources
│   ├── complete.feather                            Stores all data, used for analysis (DUMMY FILE)
│   ├── profiles_with_actors.csv                    Profile IDs which require additional scraping (DUMMY FILE)
│   └── templates
│       ├── corpus_template.json                    Data scheme for publication
│       └── internal_template.json                  (Reduced) data scheme for first analysis
├── src
│   ├── data-analysis
│   │   └── general_analysis.ipynb                  Analyses corpus
│   └── scraping
│       ├── Colab_Scraping_w_Requests.ipynb         Scrapes Profiles
│       ├── Actor_Scraping.ipynb                    Scrapes additional infos about profiles
│       └── data                                    Target folder for scraping
└── utils
    ├── json_formatter.py                           Transforms raw data
    └── movietelevision_ids.ipynb                   Scrapes IDs which require additional data
                                                    output: profiles_with_actors.csv
```

# Installation

### For local usage:

1. Clone git repository

```
git clone https://github.com/NiciSc/dh-personality-corpus.git
```

2. Install requirements from requirements.txt

```
pip install -r requirements.txt
```

3. Navigate to src/scraping/Scraping.ipynb and adjust according to needs:

- URL: Put desired API-Url here, the script will append the {id} to the String
- TIMEOUT: Time after which an API call is considered timed out. It's recommended not to change this setting.
- DELAY_AFTER_ERROR: Delay before retrying after HTTP response returns error status code
- DELAY_BETWEEN_REQUESTS: Delay between to reduce load on server. It's recommended not to change this setting.
- LOWER_LIMIT: {id} to start requests with
- UPPER_LIMIT: {id} to end requests on
- ENABLE_REMOTE_LOGGING: Enable if remote logging is required. Default: False.
- PATH_TO_SAVE_LOCATION: Put the path where you want to store the JSON files here.
- [OPTIONAL] REMOTE_LOGGER_HOST: Put Url to remote logging provider here.
- [OPTIONAL] REMOTE_LOGGER_PORT: Put Port of remote logging provider here.

4. Execute all cells to run scraping

# Corpus Description

The Corpus includes 518,481 profiles as of March 15th 2023.

## Distriution

The Corpus is made up of:

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

## File Format

Each profile has the following properties:

| Key                         |  Value  | Purpose                                                                                    | Notes                                      | Used for Analysis |
| :-------------------------- | :-----: | :----------------------------------------------------------------------------------------- | :----------------------------------------- | :---------------: |
| "id"                        | Integer | Unique profile ID                                                                          | ascending                                  |        \*         |
| "mbti_profile"              | String  | Name of character                                                                          |                                            |        \*         |
| "profile_name_searchable"   | String  | Different spelling of mbti_profile                                                         | often lowercase and as one word            |                   |
| "allow_commenting"          | Boolean | Whether members are allowed to comment on profile                                          | True for 99.98% of profiles                |                   |
| "allow_voting"              | Boolean | Whether members are allowed to vote on profile                                             | True for 99,76% of profiles                |                   |
| "user_id"                   | Integer | Unique submittor ID                                                                        |                                            |                   |
| "display_order"             | Integer | Unknown                                                                                    | 81,10% of profles with value "0"           |                   |
| "edit_lock"                 |  0\|1   | Whether community member can edit profiles or not                                          | True for 99,23% of profiles                |                   |
| "edit_lock_picture"         |  0\|1   | Whether member can change picture of profiles                                              | True for 98,87% of pictures                |                   |
| "is_active"                 |  True   | If profile is marked for deletion                                                          | True for 100% of profiles                  |                   |
| "is_approved"               | Boolean | Whether this profile went through some kind of approval process already                    | True for 99,97% of profiles                |                   |
| "mbti_enneagram_type"       | String  | MBTI and Enneagram type                                                                    | Can be ""                                  |                   |
| "mbti_type"                 | String  | MBTI and Enneagram type                                                                    | same as mbti_enneagram_type                |        \*         |
| "pdb_comment_access"        |  True   | Whether comments can be accessed or not                                                    | True for 100% of profiles                  |                   |
| "pdb_page_owner"            |    0    | Unknown                                                                                    | 0 for 100% of profiles                     |                   |
| "pdb_public_access"         | Boolean | Whether profile can be accessed by everyone                                                | True for 100% of profiles                  |                   |
| "wiki_description"          | String  | Description of character                                                                   | Optional                                   |                   |
| "watch_count"               | Integer | How many members bookmarked this profile                                                   |                                            |        \*         |
| "comment_count"             | Integer | Number of comments on profile                                                              |                                            |        \*         |
| "vote_count"                | Integer | Number of votes for MBTI type                                                              |                                            |                   |
| "vote_count_enneagram"      | Integer | Number of votes for Enneagram type                                                         |                                            |                   |
| "vote_count_mbti"           | Integer | Number of votes for MBTI type                                                              | Same as vote_count                         |        \*         |
| "total_vote_counts"         | Integer | Sum of all votes                                                                           |                                            |        \*         |
| "personality_type"          | String  | Personality type for all personality systems except MBTI and Enneagram                     | Can be empty                               |                   |
| "type_updated_date"         |  Date   | Date where some type has been updated                                                      | YYYY-MM-DD HH:MM:SS                        |                   |
| "enneagram_vote"            |   ""    | Unknown                                                                                    | "" for 100% of profiles                    |                   |
| "enneagram_vote_id"         |    0    | Unknown                                                                                    | 0 for 100% of profiles                     |                   |
| "mbti_vote"                 |   ""    | Unknown                                                                                    | "" for 100% of profiles                    |                   |
| "mbti_vote_id"              |    0    | Unknown                                                                                    | 0 for 100% of profiles                     |                   |
| "is_watching"               |  False  | Unknown                                                                                    | False for 100% of profiles                 |                   |
| "image_exists"              | Boolean | Unknown, has nothing to do with profile picture                                            | False for 99,83% of profiles               |                   |
| "profile_image_url"         |   URL   | Link to image on personality-database server                                               | Optional                                   |                   |
| "profile_image_credit"      | String  | Source of profile image if provided by community member                                    | Optional                                   |                   |
| "profile_image_credit_id"   | Integer | Unknown                                                                                    |                                            |                   |
| "profile_image_credit_type" | Integer | Whether profile image is fair use (0), public domain (1) or licensed for reuse (2)         | Default 0                                  |                   |
| "profile_image_credit_url"  | String  | Unknown                                                                                    |                                            |                   |
| "alt_subcategory"           | String  | Whenever the sucategory has an alternative name (translation, etc.) it's displayed here    | "" for 96,47% of profiles                  |                   |
| "related_subcategories"     | String  | Other subcategories when a profile belongs to more than one subategory                     | "" for 98,71% of profiles                  |                   |
| "cat_id"                    | Integer | ID of category                                                                             |                                            |        \*         |
| "category"                  | String, | Name of category                                                                           |                                            |        \*         |
| "category_is_fictional"     | Boolean | Whether category is fictional                                                              | True for 83,54% of profiles                |        \*         |
| "sub_cat_id"                | Integer | ID of subcategory                                                                          |                                            |        \*         |
| "subcategory"               | String  | Name of subcategory                                                                        |                                            |        \*         |
| "subcat_link_info"          |  Array  | Further information about subcategory (name/sub_cat_id/cat_id)                             | mostly redundant                           |                   |
| "related_subcat_link_info"  |  Array  | Further information about related_subcategories (name/sub_cat/cat_id)                      | mostly redundant                           |                   |
| "related_profiles"          |  Array  | Information about profiles to display on the websites sidebar, when viewing profile        | information not related to current profile |                   |
| "functions"                 |  Array  | Most voted Dom/Aux/Tert/Inf functions, derived from Harold Grant Function Stacks           |                                            |        \*         |
| "systems"                   |  Array  | Contains sum of votes for each personality systems (MBTI, Enneagram, Tritype, etc.)        |                                            |                   |
| "breakdown_systems"         |  Array  | Contains votes for every single option in each personality system (ISFJ, 6w7, sp/sp, etc.) |                                            |        \*         |
| "breakdown_config"          |  Array  | Possibly some configuration for displaying information on the website                      | contains no usable information             |                   |
| "mbti_letter_stats"         |  Array  | Agreement percentage of userbase over each MBTI letter                                     |                                            |        \*         |
| "topic_info"                |  Array  | Information on discussion board about character and related discussion boards              | information not related to current profile |                   |

# Contact

For access to the complete corpus (for **research purposes only**) or regarding any questions please contact:

- Thomas.Schmidt@ur.de
- michelle.lanzinge@student.ur.de
- nicole.schoenwerth@student.ur.de
- raphael.wagner@student.ur.de
