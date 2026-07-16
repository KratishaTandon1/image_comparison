# Executive Summary: Josh Talks AI Product Intern Assignment
**Date**: July 2026

---

## 1. Question 1: Text-to-Image Evaluation (Kirana Store Branding)
* **Goal**: Evaluate text-to-image models on generating WhatsApp promotional flyers for local Indian Kirana stores during festivals (Diwali, Ganesh Chaturthi).
* **Models Evaluated**: Gemini 3.1 Flash Preview, OpenAI DALL-E 3, Gemini 2.5 Flash.
* **Key Finding**: **Gemini 3.1 Flash Preview** achieved the highest overall score of **8.79 / 10**, showcasing superior cultural accuracy (accurate clay diyas, traditional laddoos) over **DALL-E 3 (8.50 / 10)**. DALL-E 3 had the best spelling accuracy for Devanagari text but suffered from "Western bias" in visual details.
* **Evidence Trail**: The evaluation is backed by **9 actual generated images** stored in `/q1/images/`, and a raw score sheet **`q1/rater_scores.csv`** containing individual ratings from **8 participants** with standard deviation calculations to show rating variance.

---

## 2. Question 2: Transcriber Fraud Detection (Josh Jobs Data)
* **Goal**: Analyze 51,783 transcription rows to identify transcribers doing poor-quality/cheating work.
* **The Punctuation Loophole**: Bad transcribers bypass the "no-edit" checks by simply adding a trailing Hindi full-stop (`।`) or space to Whisper's output and submitting immediately (<2 seconds) for a long audio clip. This was flagged in **3,569 tasks**.
* **The Speed Discrepancy**: The database column `segment_character_per_second` calculates speech density (`char_count / audio_duration`), which masks fraud. Engineering must calculate **Actual Typing Speed** (`edit_distance / time_taken`).

---

## 3. Product & Engineering Recommendations
1. **Real-time Flagging Rule**: Flag users whose **Rushed Trivial rate** (submission time < duration AND edit distance $\le 2$) exceeds **30%** of their tasks.
2. **Safety Guards**: Implement a **minimum of 5 completed tasks** before trigger flags activate, and route users to `SUSPENDED_PENDING_AUDIT` (temporary hold) instead of auto-banning to handle false alarms (e.g. text-expanders, boilerplate text).
3. **UX Prevention**: Disable the "Submit" button until the audio player reaches **80% playback duration**, forcing users to listen before editing.
4. **Interactive Dashboard**: View the model comparison playground by opening the designed [q1/q1_leaderboard_mockup.html](file:///c:/Users/prakh/Downloads/josh/q1/q1_leaderboard_mockup.html) in your browser.
