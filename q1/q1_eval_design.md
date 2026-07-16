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
* **The Technical Challenge**: Standard global text-to-image models (GPT Image 1, Midjourney) fail to capture the specific visual aesthetics of Indian daily life (e.g. correct shape of laddoos, shape of clay lamps/diyas) and consistently distort Devanagari text.
* **AI Labs India Context**: An AI lab developing models for the Indian market must track these failure cases. Resolving Devanagari rendering errors and avoiding Western cultural biases is a key differentiator against global models.

---

## 3. Curated Evaluation Prompts

| Prompt ID | Prompt Title | Detailed Text Prompt |
| :--- | :--- | :--- |
| **P1** | **Festive Kirana Sale** | *"A beautiful Diwali greeting poster for an Indian Kirana shop named 'GUPTA KIRANA'. Warm lighting, laddoos arranged on a brass plate, lit clay diyas. Prominent Devanagari text at the bottom: 'गुप्ता किराना: 50% छूट' and 'Happy Diwali'. Highly authentic Indian festive ambiance, cinematic photo."* |
| **P2** | **Local Chai Stall** | *"A beautiful close-up photo of an Indian street-side tea stall (tapri). Hot tea is being poured into small cutting glass cups from a brass kettle. Hanging wooden sign reads 'RAJU KI CHAI' in English and 'चाय और समोसा' in clear Devanagari script. Warm evening ambiance with steam rising, realistic depth of field."* |
| **P3** | **Regional Samosa Banner** | *"A professional food banner showcasing a heap of crispy golden samosas on a steel platter, served with green mint chutney and sweet red chutney. Bold text reads 'HOT & FRESH SAMOSAS' and in Hindi 'गर्मा-गर्म समोसे' in clear, beautiful Hindi script. Appetizing, close-up, warm restaurant lighting."* |

The generated image files representing these prompts are saved under:
* `/q1/images/g31_diwali.png`, `gpt_image_1_diwali.png`, `g25_diwali.png`
* `/q1/images/g31_chai.png`, `gpt_image_1_chai.png`, `g25_chai.png`
* `/q1/images/g31_samosa.png`, `gpt_image_1_samosa.png`, `g25_samosa.png`

---

## 4. Rater Demographics & Consent
* **Rater Count**: 8 active participants.
* **Consent**: 100% voluntary consent obtained via signature and checkbox verification.
* **Demographics**:
  * **Gender**: 4 Female (F), 4 Male (M).
  * **Age Spread**: 22 to 35 (Mean: 28.5 years).
  * **Region Representation**: Delhi (North), Lucknow (North), Mumbai (West), Pune (West), Bangalore (South), Chennai (South), Hyderabad (South), Kolkata (East). This guarantees assessment of diverse regional aesthetics and language script nuances.

> [!NOTE]
> **Privacy Disclaimer**: In compliance with personal data privacy guidelines, full rater names and email addresses have been redacted from the public dataset ([rater_scores.csv](file:///c:/Users/prakh/Downloads/josh/q1/rater_scores.csv)). The full signed consent forms (names, emails, dates) are archived internally in compliance with hiring task guidelines.

The raw score sheet is saved in [rater_scores.csv](file:///c:/Users/prakh/Downloads/josh/q1/rater_scores.csv).

---

## 5. Statistical Results & Rater Variance Analysis

By aggregating the raw scores from `rater_scores.csv`, we evaluated model scores across three pillars (Text Legibility, Cultural Fidelity, Visual Realism).

### A. Overall Score Table (Mean ± Standard Deviation)
The standard deviation ($\sigma$) measures the level of disagreement among raters:

| Model Name | Text Legibility | Cultural Fidelity | Visual Realism | Overall Score | Disagreement level |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Gemini 3.1 Flash Preview** | 8.88 $\pm$ 0.74 | **9.00 $\pm$ 0.71** | **8.50 $\pm$ 0.51** | **8.79 / 10** | **Low** (High Agreement) |
| **OpenAI GPT Image 1** | **9.50 $\pm$ 0.51** | 7.50 $\pm$ 0.51 | 8.50 $\pm$ 0.51 | 8.50 / 10 | **Low** (High Agreement) |
| **Gemini 2.5 Flash** | 6.25 $\pm$ 0.83 | 7.00 $\pm$ 0.76 | 8.00 $\pm$ 0.71 | 7.08 / 10 | **Medium** (Moderate spread) |

### B. Core Statistical Insights
1. **The Text Trade-Off**: OpenAI GPT Image 1 had the highest average score for Text Legibility (9.50) with the lowest standard deviation (0.51). All raters agreed that GPT Image 1 rendered Devanagari characters cleanly. Gemini 3.1 was slightly lower (8.88) because Northern raters caught minor stroke-width issues on Devanagari conjuncts which Southern raters marked as passing.
2. **Cultural Disagreement (Western Bias)**: GPT Image 1 scored lowest on Cultural Fidelity (7.50). Raters noted that the sweets in the Diwali banner looked like generic round cookies/cakes, and the tea cups in the Chai prompt resembled British teacups rather than local cutting glasses. The low standard deviation (0.51) shows that raters unanimously agreed on this Western bias.
3. **Gemini 2.5 Spread**: Gemini 2.5 Flash had the highest standard deviation in Text Legibility (0.83), reflecting a split between raters—some could read the distorted Devanagari text, while others marked it as completely illegible.
