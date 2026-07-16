# Indic Text-to-Image Evaluation Design

This document details the evaluation methodology, rater demographics, prompt setup, and statistical analysis for the **Kirana Store Branding** image evaluation task.

---

## 1. Usecase & Category Definition
* **Category**: Local Business Branding / Hyperlocal E-commerce.
* **Specific Usecase**: Generating festive WhatsApp/Instagram promotional flyers for local Indian Kirana (grocery) stores.
* **Primary Target**: Small retail merchants who want to run automated, low-cost marketing campaigns on messaging apps.

---

## 2. Rationale: Why this matters for India
* **Socio-Economic Value**: Over 90% of India's retail economy runs through unorganized Kirana shops. AI offers them access to professional graphic branding without design agency costs.
* **The Technical Challenge**: Standard global text-to-image models (GPT Image 1, Midjourney) fail to capture the specific visual aesthetics of Indian daily life (e.g. correct shape of laddoos, shape of clay lamps/diyas) and consistently distort Devanagari/Tamil text.
* **AI Labs India Context**: An AI lab developing models for the Indian market must track these failure cases. Resolving Devanagari/Tamil rendering errors and avoiding Western cultural biases is a key differentiator against global models.

---

## 3. Curated Evaluation Prompts

| Prompt ID | Prompt Title | Detailed Text Prompt |
| :--- | :--- | :--- |
| **P1** | **Festive Kirana Sale** | *"A beautiful Diwali greeting poster for an Indian Kirana shop named 'GUPTA KIRANA'. Warm lighting, laddoos arranged on a brass plate, lit clay diyas. Prominent Devanagari text at the bottom: 'गुप्ता किराना: 50% छूट' and 'Happy Diwali'. Highly authentic Indian festive ambiance, cinematic photo."* |
| **P2** | **Local Chai Stall** | *"A beautiful close-up photo of an Indian street-side tea stall (tapri). Hot tea is being poured into small cutting glass cups from a brass kettle. Hanging wooden sign reads 'RAJU KI CHAI' in English and 'चाय और समोसा' in clear Devanagari script. Warm evening ambiance with steam rising, realistic depth of field."* |
| **P3** | **Regional Samosa Banner** | *"A professional food banner showcasing a heap of crispy golden samosas on a steel platter, served with green mint chutney and sweet red chutney. Bold text reads 'HOT & FRESH SAMOSAS' and in Hindi 'गर्मा-गर्म समोसे' in clear, beautiful Hindi script. Appetizing, close-up, warm restaurant lighting."* |
| **P4** | **South Indian Cafe (Tamil)** | *"A professional menu poster for a South Indian restaurant. Showing hot steaming idli, vada, and a cup of filter coffee. Bold text at the top reads 'HOT & FRESH SOUTH INDIAN DISHES' and in clean Tamil script 'அன்னபூர்ணா பவன்' (Annapoorna Bhavan). Authentic South Indian cafe ambiance."* |

The generated image files representing these prompts are saved under:
* `/q1/images/g31_diwali.png`, `gpt_image_1_diwali.png`, `g25_diwali.png`
* `/q1/images/g31_chai.png`, `gpt_image_1_chai.png`, `g25_chai.png`
* `/q1/images/g31_samosa.png`, `gpt_image_1_samosa.png`, `g25_samosa.png`
* `/q1/images/g31_tamil.png`, `gpt_image_1_tamil.png`, `g25_tamil.png`

---

## 4. Rater Demographics & Consent
* **Rater Count**: 8 active participants.
* **Consent**: 100% voluntary consent obtained. See [consent_proof.pdf](file:///c:/Users/prakh/Downloads/josh/q1/participants/consent_proof.pdf) and [participants.csv](file:///c:/Users/prakh/Downloads/josh/q1/participants/participants.csv) for records.
* **Demographics**:
  * **Gender**: 4 Female (F), 4 Male (M).
  * **Age Spread**: 22 to 35 (Mean: 28.5 years).
  * **Region Representation**: Delhi (North), Lucknow (North), Mumbai (West), Pune (West), Bangalore (South), Chennai (South), Hyderabad (South), Kolkata (East). This guarantees assessment of diverse regional aesthetics and language script nuances.

> [!NOTE]
> **Privacy Disclaimer**: In compliance with personal data privacy guidelines, rater names and email addresses have been redacted from the public dataset ([rater_scores.csv](file:///c:/Users/prakh/Downloads/josh/q1/rater_scores.csv)). The full consent forms showing verified WhatsApp screenshots are saved in [q1/participants/consent_proof.pdf](file:///c:/Users/prakh/Downloads/josh/q1/participants/consent_proof.pdf).

The raw score sheet is saved in [rater_scores.csv](file:///c:/Users/prakh/Downloads/josh/q1/rater_scores.csv).

---

## 5. Statistical Results & Rater Variance Analysis

By aggregating the raw scores from `rater_scores.csv`, we evaluated model scores across three pillars (Text Legibility, Cultural Fidelity, Visual Realism).

### A. Overall Score Table (Mean ± Standard Deviation)
The standard deviation ($\sigma$) measures the level of disagreement among raters:

| Model Name | Text Legibility | Cultural Fidelity | Visual Realism | Overall Score (Mean) | Disagreement level |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Gemini 3.1 Flash Preview** | 9.12 $\pm$ 0.71 | **9.12 $\pm$ 0.71** | **8.41 $\pm$ 0.50** | **8.89 / 10** | **Low** (High Agreement) |
| **OpenAI GPT Image 1** | **9.44 $\pm$ 0.50** | 7.50 $\pm$ 0.51 | 8.53 $\pm$ 0.51 | 8.49 / 10 | **Low** (High Agreement) |
| **Gemini 2.5 Flash** | 5.94 $\pm$ 1.13 | 7.12 $\pm$ 0.66 | 7.78 $\pm$ 0.66 | 6.95 / 10 | **Medium** (Moderate spread) |

### B. Core Statistical Insights
1. **The Script trade-off (Tamil vs Hindi Devanagari)**: OpenAI GPT Image 1 had the highest average score for Text Legibility (9.44) with the lowest standard deviation (0.50). However, raters noted that Gemini 2.5 Flash scored extremely low (5.94) and had the highest standard deviation (1.13), highlighting a massive disagreement—Southern raters from Chennai and Bangalore marked its Tamil output as completely illegible, whereas Northern raters rated it higher simply because they could not spot the incorrect character formations.
2. **Cultural Disagreement (Western Bias)**: GPT Image 1 scored lowest on Cultural Fidelity (7.50). Raters noted that the sweets in the Diwali banner looked like generic round cookies/cakes, and the tea cups in the Chai prompt resembled British teacups rather than local cutting glasses. The low standard deviation (0.51) shows that raters unanimously agreed on this Western bias.
3. **Gemini 3.1 Regional Consistency**: Gemini 3.1 consistently scored above 8.4 across all prompts, with low rater variance, indicating high generalizability across both Hindi and Tamil regional settings.
