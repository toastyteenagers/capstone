# capstone
# A Multi-Layered Biometric Access Control Device That Detects Duress Of An Authenticated User
Team 11: Hayden Coffing, Roohan Amin, Owen Boxx Alexander Raam
Instructors: David Feil-Seifer, Devrin Lee, Sara Davis
TAs: Vinh Le, Zach Estreito
Advisor(s): Ignacio Astaburuaga, CSE Instructor

Our group, motivated by multiple reports of pharmaceutical drugs being stolen or replaced, sought to create a new kind of drug cabinet. We are implementing a drug cabinet that will combine facial recognition, facial emotion recognition, and heart rate analysis to determine if a user is under duress and is verified. We expect this implementation to decrease loss in pharmacy and hospital settings, in addition to preventing more pernicious attacks by, say, swapping fentanyl with saline. 

We are taking great lengths to make sure the software and hardware components of our project are open source and available, so it may be of greatest use to those who need it. The platform the team has settled upon is deploying a Python program on a powerful, CUDA accelerated project board. We plan on using off the shelf facial recognition and facial emotion recognition libraries, combined with bespoke heart rate analysis software to determine duress. The hardware of our project will consist of a central nVidia Jetson project board, which will control our display, webcam, and heart rate monitors. 

Our project is significant in its novelty and application. No such product has ever been made that combines biometric and facial emotion recognition to determine if a user is under duress. Furthermore, no such device has been used to secure drugs in a pharmacy setting.We expect our product to stand as a unique application of novel technologies, and we hope to have it lead the way for further innovation and research into securing the most dangerous drugs in hospitals. We also hope to provide an open source solution for those hoping to emulate our project’s functionality in other applications. The project will be completely open source, and schematics will be made available upon completion. We hope that the project will be extended and expanded on in the future. 

Problem Domain Book:
The excellent "Deep Learning" by Ian Goodfellow Et Al. ![book image](https://m.media-amazon.com/images/I/A1GbblX7rOL._AC_UF1000,1000_QL80_.jpg)

[Analysis of Heart Rate Physiology](https://www.researchgate.net/figure/Distribution-of-average-daily-resting-heart-rates-The-average-daily-RHR-for-57-836_fig2_339061433)

[Video Based Stress Detection](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7582689/)

[Analysis of HRV on Physiological Stress](https://onlinelibrary.wiley.com/doi/abs/10.1111/sms.12683)

[PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) ![PyQt6 logo](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pythonguis.com%2Ftopics%2Fpyqt6%2F&psig=AOvVaw2E2Mp1sk7IqV3B9u7pFrF8&ust=1707372653941000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCPDtmvbImIQDFQAAAAAdAAAAABAE)
