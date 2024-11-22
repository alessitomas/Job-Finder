# CV Tailor
<div align="center">
<img src="https://github.com/user-attachments/assets/6ad11723-5c95-4275-aaac-1ac339e888c4" width="50%" />
</div>


## You can access the palftorm in the following link: 

**[RemuseTailor](https://resumetailor.streamlit.app/)**

## Project Overview


**CV Tailor** is an innovative tool designed to assist job seekers in tailoring their resumes for specific job positions. By analyzing the job description and comparing it to the user's uploaded resume, the system provides personalized feedback to enhance the resume's alignment with the job requirements. This tool goes beyond generic resume improvement tips, focusing instead on providing actionable, role-specific insights, particularly helpful for career changers or those applying for niche roles.


### Features:
1. **Upload Resume (PDF)**: Users can upload their resume in PDF format.
2. **Job-Specific Feedback**: Enter the desired job position, and the system evaluates the resume against the job requirements.
3. **Detailed Feedback**: The tool highlights:
   - **Strengths**: Points in the resume that align well with the job requirements.
   - **Weaknesses**: Missing or underrepresented skills and experiences.
   - **Suggestions**: Specific recommendations for improvement.
4. **Score & Suggestions**: Provides a score (0-10) based on the resume's alignment with the job, along with actionable tips to enhance it.
5. **Deployed on Streamlit**: Easy-to-use interface accessible online.

---

## Problem Statement

Finding a job can be challenging, particularly when transitioning between career fields. Current resume-building tools focus primarily on formatting or offer generic advice that lacks specificity for a particular role or industry. **CV Tailor** addresses this gap by providing:
- Tailored recommendations based on job-specific keywords and requirements.
- Insights for career changers to adapt their existing skills to new roles.
- Measurable impact by directly improving the likelihood of resume shortlisting.

---

## Research on Existing Solutions (Part A)

### Findings:
- **Generic Resume Builders**: Tools like Zety and Novoresume focus on layout and formatting rather than personalized job fit.
- **Limited Career Change Support**: No widely available tools specifically help candidates transition between industries or fields.

**Conclusion**: There is a significant gap in tools offering personalized, job-specific resume feedback with an emphasis on career transitions.

---

## Measuring Impact (Part B)

### User Study Results:
1. **Sample Size**: Feedback from 10 users who tested the tool was collected.
2. **Metrics**:
   - **User Satisfaction**: Average satisfaction score of 8.5/10.  
   <div align="center">
   <img src="https://github.com/user-attachments/assets/981230b3-c826-4c5d-af23-7db3268b0fba" width="300" />
   </div>

   
   - **Ease of Use**: 90% found the tool easy to use.  
   <div align="center">
   <img src="https://github.com/user-attachments/assets/7dea3fb8-6602-4b68-9f08-8dc5464fd584" width="300" />
   </div>

   
   - **Time Saved**: Users reported a 30-50% reduction in time spent tailoring resumes.
   <div align="center">
   <img src="https://github.com/user-attachments/assets/2e4230f1-14a3-473b-88e9-e729c85befb3" width="300" />
   </div>

   - **Hallucination Evaluation Result**: 30% of users felt the tool provided inaccurate or made-up information.
This suggests that a notable portion of users encountered issues with the tool's accuracy, which could impact trust. Improving the tool’s ability to provide reliable and fact-based responses should be a priority to enhance user confidence.
   <div align="center">   
   <img src="https://github.com/user-attachments/assets/4410066b-1b02-4cb5-bd00-c82cc9a54532" width="300" />
   </div>




### Key Feedback:
- Users appreciated the specificity of suggestions and the scoring mechanism.
- Career changers found the tool particularly useful for identifying transferable skills.
- Suggestions to improve included adding examples of "ideal resumes" for specific roles.

---

## How It Works

1. **Upload Resume**:
   - Users upload their resume in PDF format.
   - The text is extracted using the `PyPDF2` library.
   
2. **Enter Job Description**:
   - Users provide the name or description of the job they want to apply for.

3. **Processing**:
   - The tool uses Google's **Generative AI Gemini Model** to analyze the resume against the job requirements.
   - Feedback is generated based on:
     - Keywords and technologies mentioned in the job description.
     - Skills and experiences highlighted in the resume.

4. **Output**:
   - A comprehensive report with:
     - Positive aspects of the resume.
     - Areas to improve or add.
     - A final score out of 10.

5. **Deployment**:
   - Hosted on Streamlit for user-friendly interaction.

---

## Example Outputs

### Example 1: Software Engineering Intern
**Strengths**:
- Technical skills like Python, C++, SQL, and Git match job requirements.
- Demonstrated project experience in backend development and computer graphics.
  
**Weaknesses**:
- Lack of experience with specific frameworks like TensorFlow or PyTorch.
- Missing keywords related to system design and distributed systems.

**Suggestions**:
- Add a section detailing familiarity with Agile methodologies.
- Highlight any academic or personal projects using the specified frameworks.

---

### Example 2: Civil Engineer Role
**Strengths**:
- Leadership skills demonstrated through committee work.
- Strong analytical and organizational abilities.

**Weaknesses**:
- No experience in structural design or engineering-specific software.
- Missing keywords like "AutoCAD" and "structural calculations."

**Suggestions**:
- Take an online course on engineering software like AutoCAD.
- Rewrite the resume to emphasize transferable skills.

---

## Video Pitch

[Link to Video Pitch](https://example.com)

---
