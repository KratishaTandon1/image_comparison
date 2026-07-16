# 2-Minute Video Walkthrough Script

*Read this script at a steady, natural pace. Record your screen showing the [q1_leaderboard_mockup.html](file:///c:/Users/prakh/Downloads/josh/q1/q1_leaderboard_mockup.html) and your report files.*

---

**[0:00 - 0:25] Introduction & Question 1 (Use Case)**
"Hi, I'm Prakhar, and this is my walkthrough for the Josh Talks AI Product assignment. 
For Question 1, I designed a focused evaluation evaluating Text-to-Image models on **Festive Promotional Banners for Indian Kirana Stores**. 
Kirana stores represent over 90% of India's retail, and local shop owners increasingly use AI to create flyers for WhatsApp Statuses. I evaluated how Google Gemini 3.1, OpenAI GPT Image 1, and Gemini 2.5 perform on Hindi and English text integration and cultural accuracy."

**[0:25 - 0:50] What I Found (Q1)**
"I built this interactive evaluation playground *[show q1_leaderboard_mockup.html in your browser]* to compare model performance. 
My findings show that **Gemini 3.1 Flash Preview** is the overall winner with a score of **8.79 out of 10**. While **GPT Image 1** rendered text with the highest legibility, it suffered from Western bias—for example, rendering sweets that look like Western cookies rather than traditional Indian laddoos. Gemini 3.1 captured regional details like clay diyas and warm lighting much more authentically."

**[0:50 - 1:25] Question 2 (Data Insights & Loopholes)**
"For Question 2, I analyzed over fifty-thousand transcription tasks from the Josh Jobs platform. I discovered a significant loophole where transcribers are bypass-cheating the system. 
Users are adding a single Hindi punctuation full-stop *[point to report or q2_data_analysis.py]* or trailing space to Whisper's output. This tricks the system into setting `is_edited = True`, and the user submits the task in under 2 seconds without actually listening. I wrote a script that successfully flagged 3,569 cheating users using this pattern."

**[1:25 - 2:00] Recommendations & Why it Matters**
"To prevent this, my recommendation for the engineering team is to block users whose **Rushed Trivial rate** exceeds 30%. We should calculate their **Actual Typing Speed** as `edit_distance / time_taken`. If this exceeds 25 characters per second, it is a bot-paste, and we should flag it for human audit.
Furthermore, on the UX side, we should disable the 'Submit' button until the transcriber has played at least 80% of the audio clip. This ensures high-quality gold-standard datasets for Indic models. Thank you!"
