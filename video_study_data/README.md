# Video-based Study data
This folder contains the videos used in the study as well as the data collected and the stats done

## Folder structure
```bash
.
├── video_study_data                  # Includes all the data used, collected and analysis from the main study
│   ├── plots                         # Some plots obtained from the data collected
│   │   └── ...
│   ├── videos                        # The videos used in the study
│   │   └── ...
│   ├── data_raw.csv                  # Data collected from the main study unprocessed
│   ├── before_jasp.ipynb             # Simple pre-processing of data for JASP (remove failed attention checks, etc.)
│   ├── data4jasp.csv                 # Data that has been pre-processed for JASP
│   ├── gpt3_only.jasp                # Stats done considering only GPT-3 condition
│   ├── strap_only.jasp               # Stats done considering only STRAP condition
│   ├── expert_only.jasp              # Stats done considering only Expert condition
│   └── Stats.jasp                    # Contains most of the analysis done
```

## Study questions
The following are the questions used in the study with their ID.

Personality questions, shown on a 7-point Likert scale with the prompt `I see myself (the speaker of the video) as someone who:`:
1. is introverted  (not used when asked own personality)
2. is reserved
3. tends to be quiet
4. is sometimes shy inhibited
5. holds back their opinions
6. is extroverted  (not used when asked own personality)
7. is talkative
8. is full of energy
9. generates a lot of enthusiasm
10. is outgoing sociable
11. is fluent in english  (not used when asked own personality)
12. does not make grammatical errors  (not used when asked own personality)
13. is coherent and consistent with what they say  (not used when asked own personality)
14. click 'Strongly agree' for this question   (attention check)

Godspeed questions, shown on a 5-point Likert scale with the prompt `Please indicate the extent you think the robot is...`:

 Anthropomorphism

1. Fake - Natural
2. Machinelike - Humanlike
3. Unconscious - Conscious
4. Artificial - Lifelike
5. Moving rigidly - Moving elegantly

 Likeability

6. Dislikable - Likable
7. Unfriendly - Friendly
8. Unkind - Kind
9. Unpleasant - Pleasant
10. Awful - Nice

 Perceived safety

11. Anxious - Relaxed
12. Calm - Agitated
13. Quiescent - Surprised

RoSAS questions, shown on a 5-point Likert scale with the prompt `I think the robot in the video is:`:

 Warmth

1. Happy
2. Feeling
3. Social
4. Organic
5. Compassionate
6. Emotional 

 Attention check

7. Click 'disagree' for this question

 Discomfort

8. Scary
9. Strange
10. Awkward
11. Dangerous
12. Awful
13. Aggressive

## Attention checks
These are other attention checks used in the video-based study.

What was the name of the robot in the video you just watched?

0. Matthew
1. Emma
2. Robert
3. Zoe
4. Brian  (correct one)
5. Elisa

What was the topic of the video you watched?

0. An introduction and a talk on humanities
1. Only an introduction  (correct one)
2. A student presenting themselves to their supervisor
3. A talk on humanities
4. A presentation of a vacuum cleaner
5. A talk on STEM subjects
