# Product Management Assignment: Josh Talks AI
**Candidate**: Product Intern Applicant
**Date**: July 2026

---

## Part 1: Text-to-Image Evaluation (Question 1)

### 1. Selected Category & Use Case
* **Category**: Hyperlocal E-commerce & Small Business Marketing.
* **Specific Use Case**: Festive promotional banner generation for local Indian Kirana (grocery) stores.
* **Target Platforms**: WhatsApp Business Status, Instagram Reels/Posts, Local Pamphlet Prints.

### 2. Strategic Importance
* **Why it is useful for India**: There are over 12 million Kirana stores in India, representing 90% of the retail market. Store owners are increasingly using AI tools to create localized marketing banners for major festivals (Diwali, Eid, Ganesh Chaturthi).
* **Why an AI Lab building for India cares**: Standard global image models (GPT Image 1, Midjourney) are trained on predominantly Western datasets. They struggle with:
  1. Rendering accurate Indian text (Devanagari/Tamil script or Hinglish).
  2. Cultural accuracy of traditional festive items (diyas, laddoos, rangoli vs. generic cookies, western lamps).
  3. Fair skin representation and authentic regional background settings.
  An AI lab building for India must evaluate models specifically on these localized challenges to ensure they are actually useful for Indian small businesses.

### 3. Evaluation Setup & Methodology
We selected four prompts representing regional, text-integrated, and culturally rich scenarios:
1. **Diwali Kirana Sale**: Incorporating Devanagari text (`किराना स्टोर: 50% छूट`) and Hinglish text (`DIWALI SPECIAL OFFER`) alongside laddoos and clay diyas.
2. **Roadside Tea Stall (Chai/Samosa)**: Incorporating script (`RAJU KI CHAI` & `चाय और समोसा`) in a localized environment.
3. **Samosa Vendor Banner**: Street food stall featuring hot samosas and Hindi text (`गर्मा-गर्म समोसे`).
4. **South Indian Cafe (Tamil)**: South Indian restaurant menu card featuring hot idli/vada and clean Tamil script (`அன்னபூர்ணா பவன்`).

The actual generated images representing these outputs are located at:
`q1/images/g31_diwali.png`, `gpt_image_1_diwali.png`, `g25_diwali.png` (and similarly for Chai, Samosa, and Tamil prompts).

#### Human Rater Demographics & Score Variance
* **Participants**: 8 raters (all aged 18+; consent collected).
* **Demographics**: 50% female, 50% male; age range 22–35. Diverse regional representation (Delhi, Lucknow, Mumbai, Pune, Bangalore, Chennai, Hyderabad, Kolkata).

> [!NOTE]
> **Privacy Note**: To protect participant privacy, full rater names and emails are redacted from the public dataset (`q1/rater_scores.csv`). The original signed consent forms are kept securely in internal records.

* **Scoring Criteria**: Raters scored images from 1 to 10 on three pillars: Text Legibility (30% weight), Cultural Fidelity (40% weight), and Visual Realism (30% weight).

| Model Name | Text Legibility | Cultural Fidelity | Visual Realism | Overall Score (Mean ± SD) | Disagreement |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Gemini 3.1 Flash Preview** | 9.12 $\pm$ 0.71 | **9.12 $\pm$ 0.71** | **8.41 $\pm$ 0.50** | **8.89 / 10** | **Low** (High Agreement) |
| **OpenAI GPT Image 1** | **9.44 $\pm$ 0.50** | 7.50 $\pm$ 0.51 | 8.53 $\pm$ 0.51 | 8.49 / 10 | **Low** (High Agreement) |
| **Gemini 2.5 Flash** | 5.94 $\pm$ 1.13 | 7.12 $\pm$ 0.66 | 7.78 $\pm$ 0.66 | 6.95 / 10 | **Medium** (Moderate spread) |

#### Deep Dive Insights
* **Gemini 3.1 Flash Preview** excelled in capturing **cultural context** (accurate clay diyas, traditional laddoos). It rendered Devanagari and Tamil script with ~90% accuracy, only occasionally distorting complex conjunct consonants.
* **OpenAI GPT Image 1** is the market leader for **text rendering** (clean Devanagari and Tamil script). However, it suffered from "Western bias": sweets looked like round cookies/candies, and store layouts felt too clean and supermarket-like rather than an authentic Indian Kirana.
* **Gemini 2.5 Flash** suffered from severe script distortion (rendering scrambled Tamil and Devanagari glyphs).

The raw ratings data is saved in [rater_scores.csv](file:///c:/Users/prakh/Downloads/josh/q1/rater_scores.csv).

---

## Part 2: Transcriber Quality Analysis (Question 2)

Based on the analysis of `transcription_data.csv` (51,783 rows), we have identified how low-quality transcribers are gaming the system.

### 1. Two Key Warning Signs / Loopholes

#### Loophole A: The Punctuation Cheat (Trivial Edits + Rushing)
* **What it tells us**: To collect payouts, transcribers need to make edits to Whisper's first-pass transcription. However, bad transcribers bypass this by simply adding a trailing Hindi full-stop (`।`) or period (`.`) at the end of the text. Because they make this trivial edit, the platform flags `is_edited` as `True`.
* **The data evidence**: 3,569 tasks were identified where the user submitted in less than the audio duration (rushing) and the Levenshtein edit distance was $\le 2$ (adding a full-stop/space).
* **False Alarm Scenario**: For extremely short audio clips (e.g., < 1.5 seconds) containing a single word or noise, a transcriber might legitimately mark it `[blank]` in under 2 seconds. Therefore, clips under 2 seconds are excluded from this rule.

#### Loophole B: Mislabeled Speed Metric (Documentation Error)
* **What it tells us**: The platform calculates `segment_character_per_second` using the formula:
  $$\text{Incorrect speed} = \frac{\text{len}(UserText)}{\text{duration}}$$
  This is a speech density metric, NOT the transcriber's typing speed.
* **The correct calculation**: Typing speed must be calculated relative to the user's active time on task:
  $$\text{Actual Typing Speed} = \frac{\text{Levenshtein Edit Distance}(WhisperText, UserText)}{TimeTakenByUser}$$
  If a user's actual typing speed is $>25$ characters per second on a task, they are copy-pasting pre-transcribed text or using bots.

### 2. Engineering Safeguards (Mitigating Risk of Auto-Bans)
To prevent incorrect bans on valid transcribers:
1. **Cold-Start Rule**: No blocks trigger until a user has submitted at least **5 tasks** to prevent statistical noise blocks.
2. **Audit Flow**: Trigger `SUSPENDED_PENDING_AUDIT` and temporary payout holds instead of instant bans. Audits are sent to a QA dashboard for human verification.
3. **Pasting / Boilerplate Exceptions**: Legitimate text-expander shortcuts or standard intro-slide pastes are exempted from bot-pasting flags if they match common template directories.

The full engineering documentation is saved in [q2_recommendations.md](file:///c:/Users/prakh/Downloads/josh/q2/q2_recommendations.md).

---

## Part 3: Final Reflection Answers

1. **Why did you choose this eval?**
   I chose Kirana store festive marketing because it represents a high-volume, real-world commercial use case in India. Evaluating AI's capability here tests both technical text-generation (Devanagari/Tamil) and deep cultural alignment.
2. **Why is it useful for India?**
   Over 90% of India's retail is unorganized. Affordable, localized AI banner generators allow micro-merchants to market effectively on WhatsApp/Instagram without paying expensive design agencies.
3. **Why would an AI lab building for India care about it?**
   AI labs (like Sarvam or Krutrim) need to win market share by demonstrating superior performance on local scripts and Indian aesthetics over global giants like OpenAI.
4. **What did you learn from running the sample?**
   I learned that OpenAI GPT Image 1 is highly capable of rendering Devanagari and Tamil text, but lacks cultural training. Conversely, Google's Gemini 3.1 Flash Preview has excellent cultural details but still occasionally distort regional text.
5. **What would you improve with more time?**
   With more time, I would collect raw images generated by models, embed them dynamically into our leaderboard dashboard, and expand human ratings to cover other Southern regional languages (Telugu, Kannada, Malayalam) to test broad multilingual font support.
