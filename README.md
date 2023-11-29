# Emotion Detection: AI Web App
An Emotion Detection system that processes input provided by the user in text format and deciphers the associated emotion expressed.
## Demo
https://github.com/AravindR97/Emotion_Detection-repo/assets/132665408/fdd0b229-47f0-4d84-b5ad-d755dcd0f5ce
## Description
Emotion detection involves the process extracting the finer emotions: joy, sadness, anger, and so on, from statements rather than the simple polarity that sentiment analysis provides. This makes emotion detection a very important branch of study and businesses use such systems widely for their AI based recommendation systems, automated chat bots, and so on. For this project, I used the Emotion Predict function of IBM's Watson AI Natural Language Processing Library.

The following tasks were done as part of this project:
  1. Created an Emotion Detection application using the functions from embeddable AI libraries.
  2. Extracted relevant information from the output received from the function.
  3. Tested and packaged the application created using the Emotion Detection function..
  4. Completed web deployment of the application using Flask.
  5. Incorporated error handling in the application to account for invalid input to the application.
  6. Written codes that are in perfect compliance with PEP8 guidelines, getting 10/10 score in static code analysis.

## Getting Started
### Dependencies
* Python
* HTML5
* JavaScript
* Requests
* IBM Watson AI NLP Library
* Flask
### Installation
For this project, you need access to Watson AI Natural Language Processing Library
  * Go to https://www.ibm.com/products/natural-language-processing
  * Click on 'Start your Free Guided Trial'
  * The next 5 pages will give you many options to choose from. Choose each option as shown below:
      ![IBM_NLP](https://github.com/AravindR97/Emotion_Detection-repo/assets/132665408/a84ddeac-9963-4652-a9a3-ca41c7b1126e)
  * Click Next
  * Go to Step 3 and generate a container URL by logging in or signing up:
      ![IBM_NLP2](https://github.com/AravindR97/Emotion_Detection-repo/assets/132665408/74369763-a822-4167-8da2-37177a508df8)
  * After log-in, a pop-up showing the container URL will be shown. Copy the URL and save it for future use.


### How to run the program
  * Fork this repository
  * Clone it to your local PC
  * In the repository, go to EmotionDetection & open emotion_detection.py in a code editor
  * Inside emotion_detector function, paste the container URL you saved to the variable 'base_url' & uncomment it.
  * Save the file, open commandline, navigate to the repository and run server.py. Your app will be hosted on web.
  * Go to localhost address '127.0.0.1:5000' on any browser to use the app.

## Credits
This project was done as part of the certification [Developing Applications with Python and Flask](https://www.coursera.org/learn/python-project-for-ai-application-development?) by IBM on Coursera.
