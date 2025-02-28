# TALK TO EXECUTE: AN INTELLIGENT VOICE-BASED SYSTEM CONTROL

## 📌 Project Overview
TALK TO EXECUTE is an advanced AI-powered **virtual voice assistant** designed to perform various system operations and automate tasks through voice commands. Built using **Python and integrated APIs**, this assistant enhances user experience by enabling hands-free control of multiple functionalities.

## 🚀 Features
- **System Control:** Open applications, switch tabs, minimize/maximize windows, and control clipboard operations (copy, paste, select, etc.).
- **Web Search & Automation:** Perform Wikipedia searches, open Google, play YouTube videos, and fetch real-time news updates.
- **System Utilities:** Check IP address, control volume/brightness, and shut down or restart the system.
- **Productivity Tools:** Send emails, execute mathematical calculations, and translate text replies into different languages.
- **Navigation & Assistance:** Show maps for routes, provide weather updates, and store important data.
- **API Integration:** Enhanced capabilities through third-party APIs for better efficiency and functionality.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - SpeechRecognition
  - Pyttsx3 (Text-to-Speech)
  - TensorFlow & Keras
  - Wikipedia API
  - Google API (for search & maps)
  - SMTP (for email automation)
  - Wolfram Alpha API (for calculations)
  - News API (for fetching real-time news)
  - Pynput (for keyboard control)
  - Psutil (for system resource monitoring)
  - Pycaw (for audio control)
  - Speedtest-cli (for internet speed tests)
  - YT-DLP (for YouTube content handling)
  
## 📂 Project Structure
```
TALK-TO-EXECUTE/
  ├── Data                              
      ├── .env                          # Stores the API keys, email and password.
      ├── chat_model                    # Directory that stores the trained model used to understand user's intent
      ├── chats.db                      # Database file that stores the chat history
      ├── intents.json                  # Data on which the model is trained
      ├── label_encoder.pickle          # Converts text labels into numerical values
      └── tokenizer.pickle              # Splits the text into individual tokens
  ├── Plugins
      ├── API_functionalities.py        # Contains functions that interact with different APIs
      ├── browsing_functionalities.py   # Contains functions for web browsing
      ├── database.py                   # Contains functions for interacting with the chat history database
      ├── gmail.py                      # Contains functions for sending emails
      ├── translator.py                 # Contains functions for translating text to different languages
      ├── main.py                       # It is the entry point of the virtual voice assistant
      ├── model_training.py             # Contains functions for training the intent recognition model
      ├── system_operations.py          # Contains functions for performing system operations
      └── websites.py                   # Contains a list of websites that the virtual voice assistant can open
  ├── requirements.txt                  # Lists the dependencies required for the project
  └── setup.py                          # Contains code for setting up the virtual voice assistant
```

## 🔧 Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Salman-Shaik28/TALK-TO-EXECUTE.git
   cd TALK-TO-EXECUTE
   ```
2. **Install Dependencies:**
   ```bash
   python setup.py
   ```
3. **Run the Application:**
   ```bash
   python main.py
   ```

## 🎯 Future Enhancements
- **Integration with AI models** for advanced NLP and better voice recognition.
- **Customizable commands** based on user preferences.
- **Mobile app extension** to control the PC remotely via voice.

## 👥 Contributors
- **Shaik Salman** ([GitHub](https://github.com/Salman-Shaik28))
- **pvssampath** ([GitHub](https://github.com/pvssampath))
- **Ikram-Shaik** ([GitHub](https://github.com/Ikram-Shaik))

## 📜 License
This project is licensed under the **MIT License**.

---
🚀 *TALK TO EXECUTE: Making system control seamless through voice commands!*

