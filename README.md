# Genie

Genie is an AI-powered software engineering assistant designed to help you solve programming problems, automate codebase modifications, provide examples, and enhance overall productivity during development.

## Features

- **Interactive Collaboration:** Genie assists with codebase modifications, bug fixes, explanations, and code examples during live sessions.
- **Automated Code Editing:** Directly modifies, adds, or removes files in your project as per your requests.
- **Knowledgeable Guidance:** Offers insightful explanations and solutions, tailored to your project's style and requirements.
- **Safe & Transparent Integration:** All codebase changes are presented as clear "code artefacts" for your review.

## Usage

### 1. Start Genie

Run the main script to launch Genie:

```bash
python main.py
```

Depending on your setup, this may start a command-line or web-based interface.

### 2. Interact with Genie

- **Get an Example:**  
  Ask Genie for code snippets, demonstrations, or explanations using natural language.
  > _Example: "How do I write a FastAPI route for file uploads?"_

- **Modify Your Codebase:**  
  Request direct changes, such as file creation, edits, renames, or removals.
  > _Example: "Add an endpoint to our API for user authentication."_

- **Review Changes:**  
  Genie presents every change as a "code artefact" so you can verify, approve, or discuss edits before applying them.

- **Iterate:**  
  Continue the conversation to refine solutions, fix bugs, or explore alternative approaches.

### 3. Custom Tools

Genie can leverage custom tools placed in the `tools/` directory or agents in the `agents/` directory for enhanced or specialized workflows.

## Best Practices

- **Codebase Style:** Genie automatically adapts to your existing code style—be as explicit as needed if you want something different.
- **Review Before Apply:** Always check presented artefacts before integration.
- **Provide Context:** The more details you share in your requests (e.g., error logs, file contents), the better Genie can assist.

## Project Structure

- `main.py` – Entry point to start Genie.
- `agents/` – Contains custom agent scripts.
- `tools/` – Utilities and helper modules.
- `README.md` – This documentation.

## Getting Help

If you have questions about Genie's usage or want to extend its capabilities, start a conversation with Genie itself or review the source code for more details.

---

Built with ❤️ by [Cosine AI](https://cosine.sh)