
dic = {}
dic['skills'] = ['skills', 'Technical skills', 'Technical Skill-Set', 'Areas of expertise','Technical Skill Stack', 'Technology', 'Technical Competencies', 'working knowledge','Skills Summary', 'Technical skills summary', 'SkillSet', 'Technology Competencies','Business Competencies', 'Core Competency', 'Technical Expertise', 'Specific Expertise','Core Skills', 'Software Skills', 'Technology & Tools', 'Tools & Technology', 'Business & Technical Skills','Domain expertise', 'Technical summary', 'Technical Acumen', 'Soft skills', 'Key skills', 'Tools & Methods','Professional Traits', 'Skills & Competencies', 'Core Competencies', 'Knowledge Areas', 'Managerial Competencies','Functional Competencies', 'Key Skill Competencies', 'Core Expertise', 'Core Qualifications', 'Highlighted Skills','Areas of Excellence', 'Trainings/Knowledge Base', 'Technology skills', 'Core Management Competencies','Technical Skills Set', 'IT Expertise', 'Tools and Technologies Summary','Technology Snapshot', 'Technical Specifications', 'skills & Technologies','Technical skills/Knowledge']
dic['experience'] = ['Experience', 'Professional Experience', 'Career Progression', 'Project Experience','Professional work experience', 'Professional Profile', 'Employment History', 'Projects Involved','Experience Highlights', 'work experience', 'Total Work Experience', 'Project Experience Highlights', 'Role', 'Work summary','Technical Experience', 'Experience & Projects', 'Experience Summary', 'Professional Portfolio','Professional Synopsis', 'Other Professional Experience', 'Career Highlights & Competencies','Volunteer Experience', 'Previous Clients I worked for', 'Project Details', 'Professional Background','Project Summaries', 'Projects', 'Extra-Curricular Activities', 'Leadership', 'Internship', 'Internships', 'Apprentice', 'Apprenticeship']
dic['summary'] = ['Summary','Professional Summary', 'Career Summary', 'Profile summary', 'Profile', 'Personal Statement','Profile Snapshot', 'Background Summary', 'Portfolio', 'Overview', 'Technical Summary', 'Executive Summary','Summary of Experience', 'Experience Summary', 'Summary of qualifications', 'Synopsis', 'Highlighted Summary','Summary of Skills', 'Highlights', 'Technical Profile', 'Professional Competencies', 'Key Strengths','Expertise Summary', 'Professional Expertise', 'Professional Profile', 'Background', 'About me', 'About''Executive Profile', 'Responsibility']
dic['project'] = ['Projects', 'Projects Handled', 'Project Details', 'Project Experience', 'MSIS Projects','Projects and research experience', 'Internship', 'Internships', 'Apprenticeship', 'Apprenticeships']
dic['Education'] = ['Education', 'Education & Credentials', 'Education details', 'Academic qualifications','Education & Training', 'Educational Qualification', 'Academic Background', 'Education & Certifications','Professional Qualification', 'Academics', 'Academic Credentials', 'Education/Certifications', 'Education Qualification','Educational Details']
dic['Achievements'] = ['Achievements', 'Honours and Awards', 'Special Accomplishments', 'Professional Accomplishments','Awards', 'Honors', 'Key Achievements', 'Notable Accomplishments Across the Career', 'accomplishment']
dic['Certifications'] = ['Certifications', 'Certifications/Professional Awards', 'Certificates Achieved','Professional Training and Certificates', 'Awards and Achievements', 'External certification','Certifications/Training', 'Other Certifications', 'certification/trainings', 'certificates', 'certificate' ]
dic['Interests'] = ['Interests', 'Areas of Interest']
dic['Personal Info'] = ['Personal Information', 'Personal Details']
dic['Additional info'] = ['Additional Information']

results = {}
key_list = []
for a in dic.keys():
    key_list.append(a)
print(key_list)
for a in key_list:
    with open('/home/akira/projects/PDF_parser/txt/Adarsh_Resume.txt', 'r' ) as txt:
        value = dic[a]
        line_number = 0
        for v1 in value:
            v1 = v1.upper()
            for line in txt:
                line_number = line_number + 1
                if v1 in line:
                    print('Found')
                    results[a] = line_number
print(results)