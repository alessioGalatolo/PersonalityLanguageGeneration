# Text-only Study data
This folder contains the dialogues used in the text-only study as well as the data collected and the statistics done

## Folder structure
```bash
.
├── text_study_data                   # Includes all the data used, collected and analysis from the text-only study
│   ├── plots                         # Some plots obtained from the data collected
│   │   └── ...
│   ├── inputs                        # Original dialogues used before the personality shaping
│   ├── outputs_handcrafted           # The dialogues personalised according to literature
│   ├── outputs_gpt3                  # The dialogues personalised by GPT-3 with one-shot learning
│   ├── outputs_strap                 # The dialogues personalised by STRAP
│   ├── data_raw.csv                  # Data collected from the text-only study
│   ├── before_jasp.ipynb             # Simple per-processing of data for JASP (remove failed attention checks, etc.)
│   ├── expert_d1.csv                 # Stats done considering only Expert condition and the first dialogue
│   ├── expert_d2.csv                 # Stats done considering only Expert condition and the second dialogue
│   ├── expert_d3.csv                 # Stats done considering only Expert condition and the third dialogue
│   ├── expert_all.csv                # Stats done considering only Expert condition and all the dialogues together
│   ├── gpt3_d1.csv                   # Stats done considering only GPT-3 condition and the first dialogue
│   ├── gpt3_d2.csv                   # Stats done considering only GPT-3 condition and the second dialogue
│   ├── gpt3_d3.csv                   # Stats done considering only GPT-3 condition and the third dialogue
│   ├── gpt3_all.csv                  # Stats done considering only GPT-3 condition and all the dialogues together
│   ├── strap_d1.csv                  # Stats done considering only STRAP condition and the first dialogue
│   ├── strap_d2.csv                  # Stats done considering only STRAP condition and the second dialogue
│   ├── strap_d3.csv                  # Stats done considering only STRAP condition and the third dialogue
│   ├── strap_all.csv                 # Stats done considering only STRAP condition and all the dialogues together
│   └── other_stats.jasp              # Other analysis done
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
These are other attention checks used in the text-only study.
Attention checks were shown with checkboxs.

What were the dialogues about (select one or more)?

0. An introduction of a companion robot  (Correct one)
1. A talk on humanities  (Correct one)
2. A conversation between a student and their supervisor
3. A presentation of a vaccum cleaner
4. A talk on STEM subjects
5. A dialogue between two people working together  (Correct one)
