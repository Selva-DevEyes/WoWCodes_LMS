"""Git & GitHub and AI & ML course topics and quizzes seed data."""

GIT_AI_TOPICS = {
    "git-github": [
        ("Git Basics", "git-basics", "Repository initialization, staging area, commits, and status", """# Git Basics

Git is a distributed version control system designed to track changes in source code.

## Essential Git Commands

```bash
# Initialize a new Git repository
git init

# Check working tree status
git status

# Stage files for commit
git add index.html script.js
# Or stage all changes
git add .

# Commit staged changes with message
git commit -m "feat: add user authentication layout"

# View commit history
git log --oneline
```

## The Three States of Git

1. **Working Directory**: Files currently being edited.
2. **Staging Area (Index)**: Files marked for inclusion in the next commit snapshot.
3. **Git Directory (Repository)**: Committed snapshot history saved permanently in `.git`.
"""),

        ("Branching & Merging", "branching-merging", "Creating feature branches, merging, and resolving conflicts", """# Git Branching & Merging

Branches isolate experiment feature development without affecting the stable `main` branch.

## Branch Workflow

```bash
# Create and switch to new feature branch
git checkout -b feature/login-page

# Make commits on feature branch...

# Switch back to main branch
git checkout main

# Merge feature branch into main
git merge feature/login-page

# Delete feature branch after merge
git branch -d feature/login-page
```

## Resolving Merge Conflicts

When two branches alter the same line of code differently, Git prompts for manual conflict resolution:

```diff
<<<<<<< HEAD (Current Branch)
console.log("Welcome User");
=======
console.log("Hello Guest");
>>>>>>> feature/login-page
```
Choose the correct code, remove conflict markers, stage, and commit.
"""),

        ("Remote Repositories", "github-remotes", "Connecting to GitHub, push, pull, fetch, and .gitignore", """# GitHub & Remote Repositories

GitHub hosts remote Git repositories in the cloud for team collaboration.

## Working with Remotes

```bash
# Link local repo to remote GitHub repository
git remote add origin https://github.com/user/repository.git

# Push local commits to remote main branch
git push -u origin main

# Fetch latest changes from remote without merging
git fetch origin

# Pull (Fetch + Merge) remote changes into local branch
git pull origin main
```

## `.gitignore` File

Prevent secret `.env` files, build output (`dist/`), and `node_modules` from being pushed to public repositories.
"""),

        ("Pull Requests & Code Review", "pull-requests", "Pull request workflow, code reviews, and CI checks", """# Pull Requests & Code Review

Pull Requests (PRs) inform team members about changes pushed to a feature branch on GitHub.

## PR Best Practices

1. **Keep PRs Atomic**: Focus each PR on a single logical feature or bugfix.
2. **Provide Clear Descriptions**: Explain what changes were made and how to test them.
3. **Automated CI Checks**: Ensure build scripts and unit tests pass before requesting review.
4. **Squash and Merge**: Combine multiple experimental commits into a clean single commit upon merging to `main`.
""")
    ],

    "ai-ml": [
        ("Intro to AI & Machine Learning", "intro-ai-ml", "Artificial Intelligence principles, training vs inference, and ML paradigms", """# Intro to AI & Machine Learning

Machine Learning (ML) is a subset of Artificial Intelligence where systems learn patterns from data rather than following explicitly programmed rules.

## Core Concepts

- **Traditional Programming**: Rules + Data = Answers.
- **Machine Learning**: Answers + Data = Rules (Models).
- **Training**: Feeding data to an algorithm so it learns weights and parameters.
- **Inference**: Passing new, unseen data to a trained model to make predictions.

## Machine Learning Paradigms

1. **Supervised Learning**: Model trained on labeled inputs/outputs.
2. **Unsupervised Learning**: Model discovers hidden patterns in unlabeled data.
3. **Reinforcement Learning**: Agent learns by trial and error receiving rewards/penalties.
"""),

        ("Supervised & Unsupervised Learning", "ml-algorithms", "Classification, Regression, K-Means clustering, and PCA", """# Supervised & Unsupervised Learning

## Supervised Learning Algorithms

- **Regression**: Predicts continuous numerical values (e.g. house price, temperature).
  - Examples: Linear Regression, Decision Tree Regressor.
- **Classification**: Predicts discrete categorical labels (e.g. Spam vs Not Spam, Disease Diagnosis).
  - Examples: Logistic Regression, Support Vector Machines (SVM), Random Forests.

## Unsupervised Learning Algorithms

- **Clustering**: Grouping data points based on feature similarity without pre-assigned labels.
  - Example: **K-Means Clustering** for customer segmentation.
- **Dimensionality Reduction**: Reducing feature space dimensions while preserving variance.
  - Example: **Principal Component Analysis (PCA)**.
"""),

        ("Neural Networks & Deep Learning", "neural-networks", "Layers, activation functions, backpropagation, and CNNs/RNNs", """# Neural Networks & Deep Learning

Deep Learning uses Artificial Neural Networks (ANNs) inspired by biological brain structures.

## Neural Network Components

- **Input Layer**: Receives raw feature data.
- **Hidden Layers**: Perform mathematical transformations via weighted connections.
- **Output Layer**: Produces prediction probabilities.
- **Activation Functions**: Introduce non-linearity (e.g. **ReLU**, **Sigmoid**, **Softmax**).

## Training via Backpropagation

1. **Forward Pass**: Data moves forward through network to generate prediction.
2. **Loss Calculation**: Computes error difference between prediction and true label.
3. **Backpropagation**: Calculates gradients of error with respect to weights using chain rule.
4. **Gradient Descent**: Updates weights in opposite direction of gradient to minimize loss.
"""),

        ("LLMs & Prompt Engineering", "llms-prompt-engineering", "Transformers, tokens, zero-shot/few-shot prompting, and RAG", """# LLMs & Prompt Engineering

Large Language Models (LLMs) like Gemini and GPT are deep learning models trained on vast text corpora using the **Transformer** architecture.

## Key Technical Concepts

- **Transformer Architecture**: Uses **Self-Attention** mechanisms to process sequence tokens in parallel rather than sequentially.
- **Tokens**: Basic units of text (words or sub-words) processed by LLMs (~1 token ≈ 4 characters).
- **Context Window**: Maximum number of tokens an LLM can hold in memory during a session.

## Prompt Engineering Patterns

- **Zero-Shot Prompting**: Direct task instruction without examples.
- **Few-Shot Prompting**: Providing 2-3 input/output examples inside the prompt to guide output format.
- **Chain of Thought (CoT)**: Instructing model to "think step-by-step" before returning final answer.
- **Retrieval-Augmented Generation (RAG)**: Combining vector databases with LLMs to query external documents without retraining.
""")
    ]
}

GIT_AI_QUIZZES = {
    "git-github-git-basics": [
        {
            "level": "easy",
            "title": "Git Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command initializes a brand new Git repository in the current directory?",
                    "explanation": "git init creates a new empty .git repository folder.",
                    "options": [("git start", False), ("git init", True), ("git create", False), ("git new", False)],
                },
            ],
        }
    ],
    "git-github-branching-merging": [
        {
            "level": "medium",
            "title": "Branching & Merging Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command creates a new branch named 'feature' AND immediately switches to it?",
                    "explanation": "git checkout -b feature (or git switch -c feature) creates and switches branch.",
                    "options": [("git branch feature", False), ("git checkout -b feature", True), ("git merge feature", False), ("git commit -b feature", False)],
                },
            ],
        }
    ],
    "git-github-github-remotes": [
        {
            "level": "easy",
            "title": "Remote Repositories Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which git command fetches remote changes AND automatically merges them into the current branch?",
                    "explanation": "git pull performs a git fetch followed by git merge.",
                    "options": [("git fetch", False), ("git pull", True), ("git push", False), ("git sync", False)],
                },
            ],
        }
    ],
    "git-github-pull-requests": [
        {
            "level": "medium",
            "title": "Pull Requests Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the primary benefit of 'Squash and Merge' when combining a PR into main?",
                    "explanation": "Squash and merge condenses all intermediate feature branch commits into a single clean commit on main.",
                    "options": [("It deletes the main branch", False), ("It condenses multiple feature commits into a single clean commit", True), ("It skips code reviews", False), ("It runs tests faster", False)],
                },
            ],
        }
    ],
    "ai-ml-intro-ai-ml": [
        {
            "level": "easy",
            "title": "Intro to AI & ML Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What distinguishes Machine Learning from traditional programming?",
                    "explanation": "ML algorithms learn patterns from data (answers + inputs = rules) rather than executing fixed rules.",
                    "options": [("ML does not use computers", False), ("ML algorithms learn patterns from data automatically", True), ("ML only works with text", False), ("ML requires no training", False)],
                },
            ],
        }
    ],
    "ai-ml-ml-algorithms": [
        {
            "level": "medium",
            "title": "ML Algorithms Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which algorithm type predicts continuous numerical values like house prices?",
                    "explanation": "Regression algorithms predict continuous numbers.",
                    "options": [("Classification", False), ("Regression", True), ("Clustering", False), ("Dimensionality Reduction", False)],
                },
            ],
        }
    ],
    "ai-ml-neural-networks": [
        {
            "level": "hard",
            "title": "Neural Networks Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What mathematical function introduces non-linearity into a neural network layer?",
                    "explanation": "Activation functions like ReLU or Sigmoid introduce non-linearity, allowing networks to learn complex functions.",
                    "options": [("Cost function", False), ("Activation function (e.g. ReLU)", True), ("Loss function", False), ("Gradient descent", False)],
                },
            ],
        }
    ],
    "ai-ml-llms-prompt-engineering": [
        {
            "level": "hard",
            "title": "LLMs & Prompt Engineering Quiz",
            "passing_score": 80,
            "questions": [
                {
                    "text": "What architectural innovation powers modern Large Language Models like Gemini?",
                    "explanation": "The Transformer architecture using self-attention mechanisms powers modern LLMs.",
                    "options": [("Recurrent Neural Networks", False), ("Transformer Architecture with Self-Attention", True), ("Decision Trees", False), ("K-Nearest Neighbors", False)],
                },
            ],
        }
    ],
}
