# Josh Talks AI - Product Intern Assignment

This repository contains the deliverables and codebase for the **Josh Talks AI Product Intern** hiring task (July 2026).

---

## 📂 Folder Structure

```
├── q1/                           # Question 1: Text-to-Image Evaluation
│   ├── images/                   # Actual generated image outputs from 3 models
│   │   ├── g31_diwali.png        # Gemini 3.1 Diwali banner
│   │   ├── gpt_image_1_diwali.png # OpenAI GPT Image 1 Diwali banner
│   │   └── ...                   # Chai stall and Samosa prompts
│   ├── q1_leaderboard_mockup.html # Premium interactive HTML dashboard
│   ├── q1_eval_design.md         # Detailed eval design & rater variance report
│   ├── rater_scores.csv          # Raw rating dataset of 8 raters (demographics & consent)
│   ├── generation_metadata.json  # Complete metadata proof of generation (model settings)
│   ├── prompts.md                # Human-readable markdown log of prompts, models, and settings
│   ├── consent_proof.md          # Consent proof, agreement statement, and verification logs
│   └── participants/             # Verified consent records
│       ├── consent_proof.pdf     # PDF of compiled WhatsApp consent screenshots (ignored via .gitignore for PII privacy)
│       └── participants.csv      # CSV sheet listing rater names, redacted emails, and actual ages
│
├── q2/                           # Question 2: Transcriber Quality Analysis
│   ├── q2_data_analysis.py       # Python detection script (processing 51k rows)
│   ├── q2_recommendations.md     # Engineering recommendations & safety guards
│   ├── transcription_data.csv    # Large 23MB raw transcriber dataset
│   └── flagged_transcribers.csv  # Output list of 3,569 flagged cheating users
│
├── scratch/                      # Loose scratch exploration scripts
│
├── final_report.md               # Main deliverable (Q1 & Q2 answers + reflection)
├── one_page_report.md            # 1-page Executive Summary
└── video_script.md               # Word-for-word 2-minute video walkthrough script
```

---

## 🚀 How to Run and View the Deliverables

### 1. Question 1: Image Evaluation Dashboard
1. Open the [q1/q1_leaderboard_mockup.html](file:///c:/Users/prakh/Downloads/josh/q1/q1_leaderboard_mockup.html) file in any modern web browser (Double-click or drag-and-drop into Chrome/Firefox/Edge).
2. Click through the **Prompt Tabs** (Festive Kirana Sale, Local Chai Stall, Regional Food Banner) to interactively see how the model outputs and raters' metrics change dynamically.

### 2. Question 2: Transcriber Data Analysis
Run the python detection script to process the dataset and generate the list of flagged cheating accounts:
```bash
cd q2
python q2_data_analysis.py
```
This will parse `transcription_data.csv`, check for rushed minimal-edit submissions (punctuation cheats), and write the results to `flagged_transcribers.csv`.

### 3. Submission Documents
* Read the **[final_report.md](file:///c:/Users/prakh/Downloads/josh/final_report.md)** for complete conceptual and data-backed answers.
* Read the **[one_page_report.md](file:///c:/Users/prakh/Downloads/josh/one_page_report.md)** for a quick high-level summary of findings.
* Read the **[video_script.md](file:///c:/Users/prakh/Downloads/josh/video_script.md)** for the walkthrough speaking script.
* **Compulsory Video Walkthrough Link**: [Watch the 2-minute Loom Video Walkthrough](https://www.loom.com/share/b6c087e2b77e4d0ea658fab56b6d36d7)
