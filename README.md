# IAS Mains Answer Generator

## ⚠️ STRICT LICENSE AND USAGE RULES

### LICENSE AGREEMENT

**Copyright © 2024 - All Rights Reserved**

This software and its associated content are protected by copyright law. Unauthorized copying, distribution, modification, public display, or public performance of this copyrighted work is strictly prohibited.

### PERMITTED USAGE

1. **Personal Use Only**: This application is intended for personal educational purposes only.
2. **No Commercial Use**: Commercial use, distribution, or monetization is strictly prohibited.
3. **No Redistribution**: You may not redistribute, sell, lease, or transfer this software to any third party.
4. **No Modification**: You may not modify, reverse engineer, or create derivative works.
5. **No Public Display**: You may not publicly display or demonstrate this software without explicit written permission.

### RESTRICTIONS

- **No Sharing**: Do not share this code, application, or generated content with others
- **No API Integration**: Do not integrate this application with other systems or APIs
- **No Data Collection**: Do not collect, store, or analyze data from this application
- **No Academic Misuse**: This tool is for learning purposes only, not for academic dishonesty
- **No Competitive Use**: Do not use this application for competitive examinations or assessments

### ENFORCEMENT

Violation of these terms may result in:
- Legal action for copyright infringement
- Immediate termination of access
- Potential damages and legal fees

## Project Description

The IAS Mains Answer Generator is an AI-powered tool designed to assist with UPSC IAS Mains examination preparation. It uses advanced language models to break down complex questions into structured steps and generate comprehensive answers from a pro-India perspective.

## Features

- **Question Analysis**: Breaks down complex IAS questions into 3-5 structured steps
- **Step-by-Step Answer Generation**: Creates detailed responses for each step
- **Answer Synthesis**: Combines individual step answers into comprehensive final responses
- **Pro-India Perspective**: Generates answers with a focus on Indian interests and viewpoints
- **Structured Output**: Provides well-organized, mains-style answers

## Technical Architecture

### Components

- **`src/app.py`**: Main Streamlit application interface
- **`src/prompt_functions.py`**: Core AI functions for question processing and answer generation
- **`data/`**: Directory for storing question data and training materials
- **`notebook/`**: Jupyter notebooks for development and analysis
- **`output/`**: Generated answers and results storage

### Dependencies

- OpenAI API (GPT-4.1-mini)
- Streamlit
- JSON processing
- Python 3.8+

## Installation and Setup

### Prerequisites

1. Python 3.8 or higher
2. OpenAI API key
3. Streamlit

### Setup Instructions

1. Clone the repository (private access only)
2. Install dependencies:
   ```bash
   pip install openai streamlit
   ```
3. Configure OpenAI API key in Streamlit secrets
4. Run the application:
   ```bash
   streamlit run src/app.py
   ```

## Usage Guidelines

### Educational Purpose Only

This tool is designed for:
- Understanding question structure and analysis
- Learning answer framing techniques
- Practicing time management for IAS Mains
- Developing critical thinking skills

### Responsible Usage

- Use as a learning aid, not a replacement for study
- Verify and cross-reference generated content
- Maintain academic integrity
- Respect examination guidelines and rules

## Security and Privacy

- API keys are stored securely using Streamlit secrets
- No user data is collected or stored
- Generated content is not logged or analyzed
- Local processing only - no external data transmission

## Support and Maintenance

- This is a private educational tool
- No public support or maintenance provided
- Updates and improvements are at the discretion of the copyright holder

## Legal Notice

This software is provided "as is" without warranty of any kind. The copyright holder shall not be liable for any damages arising from the use of this software.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by these license terms and usage restrictions.**

**Last Updated**: Jul 2025
**Version**: 1.0.0 