University Time Table Scheduler
Purpose
This program facilitates the scheduling of lab sessions for different semesters and sections, including the assignment of faculties to teach specific subjects.

Input Instructions
Semester and Section Input:

Enter the semester (1-8) as an integer (e.g., 1).
Enter the section (A/B) in uppercase (e.g., A).
Enter the day on which you wish to schedule the lab class (e.g., Monday).
Faculty Input:

Enter the total number of faculties to be scheduled across all semesters.
For each faculty:
Enter the unique name of the faculty.
Enter the total number of subjects handled by that faculty across departments.
For each subject:
Enter the semester name (1-8) as an integer.
Enter the section (A/B) in uppercase.
Enter the subject handled by that faculty for that semester and section.
Constraints and Prioritization
Each faculty can handle a maximum of 3 classes per semester.
Maintain the priority order of subjects.
Avoid assigning subjects with the same index in the priority list to the same faculty.
Ensure that the chosen subject for a faculty does not exceed the maximum number of classes (2 for 7-hour subjects, 3 for 6-hour subjects).
Example
Example scenario for Ramesh:
Ramesh takes 2 classes: Semester 2, Section A, and Semester 5, Section B.
Priority order of subjects:
Sem 2, Sec A: ["C", "Data Science", "Maths", "HSE", "BEEE"]
Sem 5, Sec B: ["M.I", "Computer Networks", "ToC", "Crypto", "A.I"]
Ensure subjects chosen for Ramesh do not have the same index and have consistent subject hours.
Conclusion
This program aims to efficiently schedule lab sessions and assign faculties to subjects, ensuring optimal resource utilization while adhering to constraints and prioritization.
