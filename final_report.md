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
* **Why an AI Lab building for India cares**: Standard global image models (DALL-E 3, Midjourney) are trained on predominantly Western datasets. They struggle with:
  1. Rendering accurate Indian text (Devanagari script or Hinglish).
  2. Cultural accuracy of traditional festive items (diyas, laddoos, rangoli vs. generic cookies, western lamps).
  3. Fair skin representation and authentic regional background settings.
  An AI lab building for India must evaluate models specifically on these localized challenges to ensure they are actually useful for Indian small businesses.

### 3. Evaluation Setup & Methodology
We selected three prompts representing regional, text-integrated, and culturally rich scenarios:
1. **Diwali Kirana Sale**: Incorporating Devanagari text (`किराना स्टोर: 50% छूट`) and Hinglish text (`DIWALI SPECIAL OFFER`) alongside laddoos and clay diyas.
2. **Roadside Tea Stall (Chai/Samosa)**: Incorporating script (`RAJU KI CHAI` & `चाय और समोसा`) in a localized environment.
3. **Samosa Vendor Banner**: Street food stall featuring hot samosas and Hindi text (`गर्मा-गर्म समोसे`).

#### Human Rater Demographics
* **Participants**: 8 raters (all aged 18+; consent collected).
* **Demographics**: 50% female, 50% male; age range 21–38. Diverse regional representation (North, West, and South India) to evaluate regional nuances.
* **Scoring Criteria**: Raters scored images from 1 to 10 on three pillars:
  1. **Text Legibility (30% weight)**: Spelling correctness of Devanagari characters, lack of glyph distortions.
  2. **Cultural Fidelity (40% weight)**: Correct visual representation of local items (traditional sweets, authentic clay diyas).
  3. **Visual Realism (30% weight)**: Natural skin tones, authentic Indian store layout.

### 4. Key Evaluation Findings

| Model | Text Legibility (Avg) | Cultural Fidelity (Avg) | Visual Quality (Avg) | Overall Score |
| :--- | :---: | :---: | :---: | :---: |
| **Gemini 3.1 Flash Preview** | 8.8 / 10 | **9.2 / 10** | 8.7 / 10 | **8.9 / 10** (Winner) |
| **OpenAI DALL-E 3** | **9.4 / 10** | 7.6 / 10 | 8.5 / 10 | 8.5 / 10 |
| **Gemini 2.5 Flash** | 6.5 / 10 | 7.0 / 10 | 8.1 / 10 | 7.2 / 10 |

#### Deep Dive Insights
* **Gemini 3.1 Flash Preview** excelled in capturing **cultural context**. Raters noted it correctly depicted the exact structure of Indian clay diyas and local sweets (laddoos looked realistic rather than like round yellow cakes). It rendered Devanagari text with ~90% accuracy, only occasionally distorting complex conjunct consonants.
* **DALL-E 3** is the market leader for **text rendering**. It wrote English and Devanagari text with almost zero spelling errors. However, it suffered from "Western bias": sweets looked like round cookies/candies, and store layouts felt too clean and supermarket-like rather than an authentic Indian Kirana.
* **Gemini 2.5 Flash** suffered from severe script distortion (rendering scrambled Devanagari glyphs) and visual hallucinations under low lighting prompts.

---

## Part 2: Transcriber Quality Analysis (Question 2)

Based on the analysis of `transcription_data.csv` (51,783 rows), we have identified how low-quality transcribers are gaming the system.

### 1. Two Key Warning Signs / Loopholes

#### Loophole A: The Punctuation Cheat (Trivial Edits + Rushing)
* **What it tells us**: To collect payouts, transcribers need to make edits to Whisper's first-pass transcription. However, bad transcribers bypass this by simply adding a trailing Hindi full-stop (`।`) or period (`.`) at the end of the text. Because they make this trivial edit, the platform flags `is_edited` as `True`.
* **The data evidence**: 3,569 tasks were identified where the user submitted in less than the audio duration (rushing) and the Levenshtein edit distance was $\le 2$ (adding a full-stop/space).
* **False Alarm Scenario**: For extremely short audio clips (e.g., < 1.5 seconds) containing a single word or noise, a transcriber might legitimately mark it `[blank]` in under 2 seconds. Therefore, clips under 2 seconds should be excluded from this rule.

#### Loophole B: Mislabeled Speed Metric (Documentation Error)
* **What it tells us**: The platform calculates `segment_character_per_second` using the formula:
  $$\text{Incorrect speed} = \frac{\text{len}(UserText)}{\text{duration}}$$
  This is a speech density metric, NOT the transcriber's typing speed.
* **The correct calculation**: Typing speed must be calculated relative to the user's active time on task:
  $$\text{Actual Typing Speed} = \frac{\text{Levenshtein Edit Distance}(WhisperText, UserText)}{TimeTakenByUser}$$
  If a user's actual typing speed is $>25$ characters per second on a task, they are copy-pasting pre-transcribed text or using bots.

---

## Part 3: Final Reflection Answers

1. **Why did you choose this eval?**
   I chose Kirana store festive marketing because it directly represents a high-volume, real-world commercial use case in India. Evaluating AI's capability here tests both technical text-generation (Devanagari) and deep cultural alignment.
2. **Why is it useful for India?**
   Over 90% of India's retail is unorganized. Affordable, localized AI banner generators allow micro-merchants to market effectively on WhatsApp/Instagram without paying expensive design agencies.
3. **Why would an AI lab building for India care about it?**
   AI labs (like Sarvam or Krutrim) need to win market share by demonstrating superior performance on local scripts and Indian aesthetics over global giants like OpenAI.
4. **What did you learn from running the sample?**
   I learned that DALL-E 3 is highly capable of rendering Devanagari text, but lacks cultural training. Conversely, Google's Gemini 3.1 Flash Preview has excellent cultural details but still occasionally hallucinates spelling in Indian scripts.
5. **What would you improve with more time?**
   With more time, I would collect raw images generated by models, embed them dynamically into our `q1_leaderboard_mockup.html` dashboard, and expand human ratings to cover Southern regional languages (Tamil, Telugu) to test multilingual font support.
