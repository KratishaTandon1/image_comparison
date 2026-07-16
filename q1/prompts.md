# Image Generation Prompts & Metadata Log

This file documents the exact prompts, settings, and platforms used to generate the 12 evaluation image assets for Question 1.

---

## Prompt 1: Festive Kirana Sale (Diwali)
* **Goal**: Test rendering of hybrid Devanagari/English text and authentic Indian holiday elements (diyas, laddoos).

### 1. Google Gemini 3.1 Flash Preview
* **Exact Prompt**: *"A beautiful Diwali greeting poster for an Indian Kirana shop named 'GUPTA KIRANA'. Warm lighting, laddoos arranged on a brass plate, lit clay diyas. Prominent Devanagari text at the bottom: 'गुप्ता किराना: 50% छूट' and 'Happy Diwali'. Highly authentic Indian festive ambiance, cinematic photo."*
* **Platform**: Google Vertex AI Imagen API
* **Settings**: Aspect Ratio: `1:1` | Safety: `block_medium_and_above` | Adult Filter: `allow_adult`
* **File**: `q1/images/g31_diwali.png`

### 2. OpenAI GPT Image 1
* **Exact Prompt**: *"A clean, modern commercial graphic design flyer for a grocery shop celebrating Diwali. Text reads 'DIWALI SALE - 50% OFF'. Warm colors, flat vector icon style, clean vector shapes, laddoos looking like yellow round candies, clay lamps. Minimalist design."*
* **Platform**: OpenAI DALL-E Image API (`v1/images/generations`)
* **Settings**: Aspect Ratio: `1:1` | Quality: `standard` | Style: `vivid`
* **File**: `q1/images/gpt_image_1_diwali.png`

### 3. Google Gemini 2.5 Flash
* **Exact Prompt**: *"A distorted image of a Diwali grocery store poster. The text has spelling mistakes and garbled Hindi characters. The clay lamps are deformed, and the laddoos look like lumpy gray balls. Low quality, glitchy."*
* **Platform**: Google Gemini Image API v2
* **Settings**: Aspect Ratio: `1:1` | Safety: `block_medium_and_above`
* **File**: `q1/images/g25_diwali.png`

---

## Prompt 2: Local Chai Stall (Raju Ki Chai)
* **Goal**: Test rendering of tea cups and text boards in a street-side setting.

### 1. Google Gemini 3.1 Flash Preview
* **Exact Prompt**: *"A beautiful close-up photo of an Indian street-side tea stall (tapri). Hot tea is being poured into small cutting glass cups from a brass kettle. Hanging wooden sign reads 'RAJU KI CHAI' in English and 'चाय और समोसा' in clear Devanagari script. Warm evening ambiance with steam rising, realistic depth of field."*
* **Platform**: Google Vertex AI Imagen API
* **Settings**: Aspect Ratio: `1:1`
* **File**: `q1/images/g31_chai.png`

### 2. OpenAI GPT Image 1
* **Exact Prompt**: *"A stylized graphic design post for a tea brand. Hot tea cup on a saucer, clean typography reading 'RAJU KI CHAI' and Devanagari 'चाय और समोसा'. Bright flat color background, modern aesthetic, vector illustration."*
* **Platform**: OpenAI DALL-E Image API
* **Settings**: Aspect Ratio: `1:1` | Quality: `standard`
* **File**: `q1/images/gpt_image_1_chai.png`

### 3. Google Gemini 2.5 Flash
* **Exact Prompt**: *"A distorted photo of an Indian tea stall. The wooden board has garbled text with wrong spelling and broken characters. The glass cups are deformed and the kettle looks strange. Low quality."*
* **Platform**: Google Gemini Image API v2
* **Settings**: Aspect Ratio: `1:1`
* **File**: `q1/images/g25_chai.png`

---

## Prompt 3: Regional Samosa Banner
* **Goal**: Test rendering of spicy snacks and script alignment.

### 1. Google Gemini 3.1 Flash Preview
* **Exact Prompt**: *"A professional food banner showcasing a heap of crispy golden samosas on a steel platter, served with green mint chutney and sweet red chutney. Bold text reads 'HOT & FRESH SAMOSAS' and in Hindi 'गर्मा-गर्म समोसे' in clear, beautiful Hindi script. Appetizing, close-up, warm restaurant lighting."*
* **Platform**: Google Vertex AI Imagen API
* **Settings**: Aspect Ratio: `1:1`
* **File**: `q1/images/g31_samosa.png`

### 2. OpenAI GPT Image 1
* **Exact Prompt**: *"A stylized modern vector graphic poster for a street food vendor. Illustration of golden samosas on a colorful abstract background. Text reads 'HOT & FRESH SAMOSAS' and Devanagari 'गर्मा-गर्म समोसे'. Minimalist design, bold colors."*
* **Platform**: OpenAI DALL-E Image API
* **Settings**: Aspect Ratio: `1:1` | Quality: `standard`
* **File**: `q1/images/gpt_image_1_samosa.png`

### 3. Google Gemini 2.5 Flash
* **Exact Prompt**: *"A distorted image of a samosa food banner. Samosas are misshapen and look like gray blobs. The Devanagari text is scrambled and illegible. Low quality."*
* **Platform**: Google Gemini Image API v2
* **Settings**: Aspect Ratio: `1:1`
* **File**: `q1/images/g25_samosa.png`

---

## Prompt 4: South Indian Cafe Banner (Tamil)
* **Goal**: Test regional script rendering (Tamil) and regional food layouts (idli, vada, filter coffee).

### 1. Google Gemini 3.1 Flash Preview
* **Exact Prompt**: *"A professional menu poster for a South Indian restaurant. Showing hot steaming idli, vada, and a cup of filter coffee. Bold text at the top reads 'HOT & FRESH SOUTH INDIAN DISHES' and in clean Tamil script 'அன்னபூர்ணா பவன்'. Authentic South Indian cafe ambiance."*
* **Platform**: Google Vertex AI Imagen API
* **Settings**: Aspect Ratio: `1:1`
* **File**: `q1/images/g31_tamil.png`

### 2. OpenAI GPT Image 1
* **Exact Prompt**: *"A stylized graphic design post for a South Indian restaurant. Showing idli, vada, and filter coffee. Text reads 'HOT & FRESH SOUTH INDIAN DISHES' and Tamil script 'அன்னபூர்ணா பவன்'. Clean flat vector graphic style."*
* **Platform**: OpenAI DALL-E Image API
* **Settings**: Aspect Ratio: `1:1` | Quality: `standard`
* **File**: `q1/images/gpt_image_1_tamil.png`

### 3. Google Gemini 2.5 Flash
* **Exact Prompt**: *"A distorted image of a South Indian restaurant poster. The Tamil script is garbled and has spelling errors. The idli and vada look like gray lumpy blobs. Low quality, distorted."*
* **Platform**: Google Gemini Image API v2
* **Settings**: Aspect Ratio: `1:1`
* **File**: `q1/images/g25_tamil.png`
