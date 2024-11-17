# **HackUTD2024: Ripple Effect Project**
A Flask-based API for interacting with [Pinata](https://www.pinata.cloud/) (IPFS) to upload and retrieve files, combined with a **Math Problem Solver** that optimizes [SambaNova's advanced OpenAI technology](https://sambanova.ai/) to read and solve word problems, while displaying step-by-step explanations.

---
## The Team
- [DylanDtm4](https://github.com/DylanDtm4): Front end developer
- [NealKapadia](https://github.com/NealKapadia): Front end developer
- [JuuyouSan](https://github.com/JuuyouSan): Back end developer
- [justi-lai](https://github.com/justi-lai): Back end developer

---
## Program
- **Math Problem Solver**: Upload a .txt file containing a word math problem, and this program will solve it while displaying a step-by-step walk through on how to solve the question

---

## Features

- **Upload Files**: Upload files to Pinata's IPFS using the `/api/upload` endpoint.
- **List Files**: Retrieve a list of pinned files from Pinata via the `/api/files` endpoint.

---
## Future Features
- **More Math Function**: Currently, this program only offers simple arithmetic such as addition, subtraction, multiplication, and division. Possible future features could involve calculus
- **More File Diversity**: The program is capable of only reading .txt files. Future possible features could involve reading from .pdf files or image files