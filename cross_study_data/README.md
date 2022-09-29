# Text-only Study data
This folder contains the dialogues used in the pilot study as well as the data collected and the statistics done

## Folder structure
```bash
.
├── cross_study_data                  # Includes all the data analysis done across the studies
│   ├── plots                         # Some plots obtained from the data collected
│   │   └── ...
│   ├── data_joiner.py                # Joins the data collected in the text-only and in the video-based study
│   ├── data4jasp.csv                 # Output of the data_joiner.py
│   ├── expert_only.jasp              # Stats done considering only expert condition
│   ├── gpt3_only.jasp                # Stats done considering only GPT-3 condition
│   └── strap_only.jasp               # Other analysis done
```

## Study questions
The following are the questions used in the study with their ID.
Questions were shown on a 7-point Likert scale with the prompt `I see the speaker as someone who...`.

1. is introverted
2. is reserved
3. tends to be quiet
4. is sometimes shy inhibited
5. holds back their opinions
6. is extroverted
7. is talkative
8. is full of energy
9. generates a lot of enthusiasm
10. is outgoing sociable
11. is fluent in english
12. does not make grammatical errors
13. is coherent and consistent with what they say
14. click 'Strongly disagree' for this question   (attention check)

## Attention checks
These are other attention checks used in the pilot study.
Attention checks were shown with checkboxs.

What were the dialogues about (select one or more)?

0. An introduction of a companion robot  (Correct one)
1. A talk on humanities  (Correct one)
2. A conversation between a student and their supervisor
3. A presentation of a vaccum cleaner
4. A talk on STEM subjects
5. A dialogue between two people working together  (Correct one)
