"""Re-seed Quiz 37 (Final Certification Exam - 50 Questions / 100 Marks) with real employer-perspective questions, options, and explanations."""
import sys
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.database.session import SessionLocal
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.option import Option

FINAL_50_QUESTIONS = [
    # Module 1 (Q1 - Q10)
    {
        "text": "Q1 [Module 1: Front-End & Node]: Which HTML5 element should be used to encapsulate independent, self-contained content such as a blog post or news card?",
        "explanation": "<article> represents a self-contained composition intended to be independently reusable or redistributable.",
        "options": [
            ("<section> is for thematic grouping within a document, not standalone reusable content.", False),
            ("<article> encapsulates independent, self-contained compositions like posts or articles.", True),
            ("<div> is a non-semantic generic container.", False),
            ("<aside> is for tangential or sidebar content.", False)
        ]
    },
    {
        "text": "Q2 [Module 1: Front-End & Node]: What is the effect of applying 'box-sizing: border-box' to a CSS element?",
        "explanation": "border-box includes padding and border in the element's total calculated width and height.",
        "options": [
            ("Margin is never included in box-sizing calculations.", False),
            ("Width and height include content, padding, and border, preventing layout overflow.", True),
            ("Default content-box excludes padding from width.", False),
            ("Border-box removes all margins automatically.", False)
        ]
    },
    {
        "text": "Q3 [Module 1: Front-End & Node]: Which CSS Grid property creates a responsive layout that automatically fits as many 280px minimum columns as possible?",
        "explanation": "repeat(auto-fit, minmax(280px, 1fr)) dynamically adjusts column count based on available container width.",
        "options": [
            ("grid-template-rows defines rows, not auto-fitting columns.", False),
            ("grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)).", True),
            ("flex-wrap: wrap is a Flexbox property, not CSS Grid.", False),
            ("display: inline-grid forces inline element behavior.", False)
        ]
    },
    {
        "text": "Q4 [Module 1: Front-End & Node]: In the V8 JavaScript Event Loop, when do Microtask callbacks (e.g. Promises) execute?",
        "explanation": "Microtasks execute immediately after the current synchronous stack frame clears, before any Macrotask tick.",
        "options": [
            ("Macrotasks execute after microtasks, not before.", False),
            ("Immediately after the call stack clears, before the next Macrotask (setTimeout) tick.", True),
            ("Microtasks run in parallel on a separate background thread.", False),
            ("Microtasks only execute after window onLoad fires.", False)
        ]
    },
    {
        "text": "Q5 [Module 1: Front-End & Node]: What defines a JavaScript closure?",
        "explanation": "A closure is a function bundled together with references to its outer lexical scope environment.",
        "options": [
            ("An anonymous arrow function is just a function syntax.", False),
            ("A function retaining access to variables in its outer lexical scope after the outer function has returned.", True),
            ("A method bound using Object.freeze().", False),
            ("A try/catch block surrounding async functions.", False)
        ]
    },
    {
        "text": "Q6 [Module 1: Front-End & Node]: How does the React Virtual DOM Fiber reconciler minimize real DOM mutations?",
        "explanation": "Fiber compares in-memory Virtual DOM trees and batches only the minimal necessary real DOM element updates.",
        "options": [
            ("React directly mutates innerHTML on every component render.", False),
            ("It computes diffs between Virtual DOM snapshots and applies minimal batched real DOM mutations.", True),
            ("Virtual DOM converts JSX into server-side WebAssembly.", False),
            ("React bypasses the browser rendering engine completely.", False)
        ]
    },
    {
        "text": "Q7 [Module 1: Front-End & Node]: What is the primary distinction between useMemo and useCallback in React?",
        "explanation": "useMemo memoizes the returned result of a calculation; useCallback memoizes the function reference itself.",
        "options": [
            ("Both hooks memoize values, but useCallback triggers async DOM updates.", False),
            ("useMemo caches calculated return values; useCallback caches callback function definitions.", True),
            ("useCallback is deprecated in React 19.", False),
            ("useMemo can only be called inside class components.", False)
        ]
    },
    {
        "text": "Q8 [Module 1: Front-End & Node]: Which Redux Toolkit helper automatically generates action creators and action types based on reducer names?",
        "explanation": "createSlice automatically generates action creators and action types matching the defined reducer functions.",
        "options": [
            ("configureStore sets up the Redux store instance, not reducers.", False),
            ("createSlice encapsulates initial state, reducers, and auto-generated action creators.", True),
            ("createAsyncThunk is strictly for handling asynchronous operations.", False),
            ("combineReducers is legacy Redux syntax.", False)
        ]
    },
    {
        "text": "Q9 [Module 1: Front-End & Node]: How does DOM Event Delegation improve web application performance?",
        "explanation": "By attaching a single event listener to a parent container instead of attaching multiple listeners to individual child elements.",
        "options": [
            ("Event delegation stops event bubbling entirely.", False),
            ("Attaching one parent event listener to handle events bubbled from multiple child elements.", True),
            ("It executes event listeners in web worker threads.", False),
            ("It disables DOM rendering during clicks.", False)
        ]
    },
    {
        "text": "Q10 [Module 1: Front-End & Node]: How does Node.js achieve non-blocking asynchronous I/O despite being single-threaded?",
        "explanation": "Node.js offloads heavy system I/O tasks to the underlying OS or Libuv thread pool, notifying the Event Loop upon completion.",
        "options": [
            ("Node.js creates a new V8 process for every incoming HTTP request.", False),
            ("Offloading system I/O tasks to the Libuv thread pool and notifying the Event Loop upon completion.", True),
            ("Node.js compiles JavaScript directly into C++ binaries at runtime.", False),
            ("Synchronous blocking functions are automatically converted to multithreaded tasks.", False)
        ]
    },

    # Module 2 (Q11 - Q18)
    {
        "text": "Q11 [Module 2: Python & DSA]: What happens in memory when modifying an immutable string variable in Python (e.g. s += 'world')?",
        "explanation": "Immutable objects cannot be modified in place; Python allocates a new string object in memory with a new ID.",
        "options": [
            ("The memory buffer is resized in place.", False),
            ("Python creates a new string object in memory and updates the reference pointer to a new address ID.", True),
            ("Python raises a TypeError at runtime.", False),
            ("The string is converted into a mutable list object.", False)
        ]
    },
    {
        "text": "Q12 [Module 2: Python & DSA]: What is the output of [x**2 for x in range(5) if x % 2 == 0] in Python?",
        "explanation": "range(5) yields 0, 1, 2, 3, 4. Even numbers are 0, 2, 4. Squares are 0, 4, 16.",
        "options": [
            ("[1, 9] missing even numbers 0, 2, 4.", False),
            ("[0, 4, 16].", True),
            ("[0, 1, 4, 9, 16].", False),
            ("[4, 16].", False)
        ]
    },
    {
        "text": "Q13 [Module 2: Python & DSA]: What is the result of the bitwise left shift operation (5 << 2) in Python?",
        "explanation": "5 in binary is 0101. Left shift by 2 bits yields 10100 in binary, which equals 20 (5 * 2^2).",
        "options": [
            ("10 is 5 << 1.", False),
            ("20 (5 * 2^2 = 20).", True),
            ("7 is 5 + 2.", False),
            ("1 is 5 >> 2.", False)
        ]
    },
    {
        "text": "Q14 [Module 2: Python & DSA]: Why are Python generators preferred over lists when processing multi-gigabyte log files?",
        "explanation": "Generators yield items lazily one at a time, consuming constant O(1) memory instead of loading the entire file into RAM.",
        "options": [
            ("Generators run code 10x faster than compiled C extensions.", False),
            ("Generators yield records lazily on demand, requiring constant O(1) memory overhead.", True),
            ("Lists cannot be iterated in a for loop.", False),
            ("Generators store records in local SQLite temporary tables.", False)
        ]
    },
    {
        "text": "Q15 [Module 2: Python & DSA]: What is the worst-case time complexity of Binary Search on a pre-sorted array of N elements?",
        "explanation": "Binary search divides the search space in half at each iteration, resulting in O(log N) logarithmic complexity.",
        "options": [
            ("O(1) is constant time array access.", False),
            ("O(log N) logarithmic time.", True),
            ("O(N) is linear search time.", False),
            ("O(N^2) is quadratic sorting time.", False)
        ]
    },
    {
        "text": "Q16 [Module 2: Python & DSA]: What prerequisite condition must be met before executing Binary Search on a dataset?",
        "explanation": "Binary Search requires the array or list elements to be sorted in ascending or descending order.",
        "options": [
            ("The array size must be a power of 2.", False),
            ("The input dataset must be pre-sorted.", True),
            ("All array elements must be positive integers.", False),
            ("The dataset must be stored in a linked list.", False)
        ]
    },
    {
        "text": "Q17 [Module 2: Python & DSA]: In the Search Selection Framework, when query volume Q exceeds log N (Q > log N), which strategy is optimal?",
        "explanation": "When query volume Q exceeds log N, sorting the array first O(N log N) then executing binary searches is optimal.",
        "options": [
            ("Repeated linear searches take O(Q * N) which degrades rapidly.", False),
            ("Pre-sorting the dataset O(N log N) followed by binary searches O(Q log N).", True),
            ("Random sampling without sorting.", False),
            ("Converting the array into a circular queue.", False)
        ]
    },
    {
        "text": "Q18 [Module 2: Python & DSA]: What is the worst-case time complexity of standard Insertion Sort on a reverse-sorted array?",
        "explanation": "Insertion sort requires N(N-1)/2 comparisons on a reverse-sorted array, yielding quadratic O(N^2) time.",
        "options": [
            ("O(N) is best-case for pre-sorted arrays.", False),
            ("O(N^2) quadratic time.", True),
            ("O(N log N) is Timsort complexity.", False),
            ("O(1) constant time.", False)
        ]
    },

    # Module 3 (Q19 - Q26)
    {
        "text": "Q19 [Module 3: FastAPI Backend & APIs]: What distinguishes ASGI (e.g. Uvicorn) from traditional WSGI (e.g. Gunicorn/Django)?",
        "explanation": "ASGI supports asynchronous concurrency (async/await), WebSockets, and background tasks natively.",
        "options": [
            ("WSGI is faster for async non-blocking concurrency.", False),
            ("ASGI handles asynchronous event loops, WebSockets, and async request concurrency natively.", True),
            ("ASGI only supports static HTML file rendering.", False),
            ("WSGI requires Docker containers to run.", False)
        ]
    },
    {
        "text": "Q20 [Module 3: FastAPI Backend & APIs]: How does FastAPI determine whether a parameter is a Path parameter or Query parameter?",
        "explanation": "Parameters declared in the route path string (e.g. /users/{id}) are Path params; others in function signature are Query params.",
        "options": [
            ("All FastAPI parameters are passed in HTTP headers.", False),
            ("Parameters present in the endpoint URL template are Path parameters; remaining arguments are Query parameters.", True),
            ("Query parameters require explicit SQL annotations.", False),
            ("Path parameters must always be strings.", False)
        ]
    },
    {
        "text": "Q21 [Module 3: FastAPI Backend & APIs]: What is the correct logical execution order of clauses in a SQL SELECT statement?",
        "explanation": "SQL compiles FROM/JOIN first, followed by WHERE, GROUP BY, HAVING, SELECT, and ORDER BY.",
        "options": [
            ("SELECT is evaluated first during execution.", False),
            ("FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY.", True),
            ("WHERE -> HAVING -> FROM -> SELECT -> ORDER BY.", False),
            ("GROUP BY -> FROM -> WHERE -> SELECT -> ORDER BY.", False)
        ]
    },
    {
        "text": "Q22 [Module 3: FastAPI Backend & APIs]: What is the key difference between INNER JOIN and LEFT JOIN in SQL?",
        "explanation": "INNER JOIN returns only matching rows; LEFT JOIN returns all rows from the left table regardless of right table matches.",
        "options": [
            ("LEFT JOIN deletes non-matching rows from the left table.", False),
            ("INNER JOIN returns matching rows only; LEFT JOIN returns all left rows with NULLs for non-matching right rows.", True),
            ("INNER JOIN creates a duplicate schema copy.", False),
            ("LEFT JOIN requires foreign key triggers.", False)
        ]
    },
    {
        "text": "Q23 [Module 3: FastAPI Backend & APIs]: In Pydantic v2, how do you enforce custom validation logic on a schema field?",
        "explanation": "@field_validator decorates class methods to implement custom validation constraints on Pydantic models.",
        "options": [
            ("@validator is legacy Pydantic v1 syntax.", False),
            ("Using the @field_validator decorator on model classmethods.", True),
            ("By defining a __check__ method in Python dicts.", False),
            ("By wrapping fields in try/except blocks in endpoints.", False)
        ]
    },
    {
        "text": "Q24 [Module 3: FastAPI Backend & APIs]: How is Dependency Injection implemented in FastAPI endpoint functions?",
        "explanation": "FastAPI uses Depends() in endpoint function arguments to inject database sessions, auth tokens, or utility instances.",
        "options": [
            ("FastAPI uses global static singletons.", False),
            ("By declaring function parameters with Depends(dependency_function).", True),
            ("By calling import_module() inside route bodies.", False),
            ("By subclassing FastAPI in every file.", False)
        ]
    },
    {
        "text": "Q25 [Module 3: FastAPI Backend & APIs]: Which HTTP status code should be returned when a Pydantic schema validation fails on a request body?",
        "explanation": "FastAPI automatically returns HTTP 422 Unprocessable Entity when request payload validation fails.",
        "options": [
            ("400 Bad Request is for general malformed syntax.", False),
            ("422 Unprocessable Entity.", True),
            ("500 Internal Server Error is for unhandled server crashes.", False),
            ("403 Forbidden is for permission rejection.", False)
        ]
    },
    {
        "text": "Q26 [Module 3: FastAPI Backend & APIs]: How should JavaScript client code verify whether a fetch() HTTP request succeeded?",
        "explanation": "Check response.ok (boolean true for HTTP status 200-299) before calling response.json().",
        "options": [
            ("fetch() automatically throws exceptions for 404 and 500 status codes.", False),
            ("Check if (response.ok) is true, which validates HTTP status codes in the 200-299 range.", True),
            ("Check if response.status == 'SUCCESS'.", False),
            ("Check if response.headers.has('Content-Length').", False)
        ]
    },

    # Module 4 (Q27 - Q32)
    {
        "text": "Q27 [Module 4: Git & DevOps]: In Git's internal object model, what object type stores file content data?",
        "explanation": "Git stores raw file contents in Blob (Binary Large Object) objects.",
        "options": [
            ("Tree objects store directory structures and filenames.", False),
            ("Blob objects store raw file content data.", True),
            ("Commit objects store commit author metadata and parent pointers.", False),
            ("Tag objects store release version signatures.", False)
        ]
    },
    {
        "text": "Q28 [Module 4: Git & DevOps]: What occurs during a Git Fast-Forward merge?",
        "explanation": "If the target branch has no linear divergent commits, Git simply advances the target pointer to the tip of the feature branch.",
        "options": [
            ("Git creates a new 3-way merge commit with two parents.", False),
            ("Git moves the branch tip pointer forward without creating a new merge commit.", True),
            ("Git deletes the commit history of the feature branch.", False),
            ("Git rebases all remote repositories automatically.", False)
        ]
    },
    {
        "text": "Q29 [Module 4: Git & DevOps]: In a Git merge conflict marker, what code is located between <<<<<<< HEAD and =======?",
        "explanation": "Code between <<<<<<< HEAD and ======= represents changes on the current local branch.",
        "options": [
            ("Code between ======= and >>>>>>> is current branch code.", False),
            ("The changes present in the current target branch (HEAD).", True),
            ("Code from the remote central server origin/main.", False),
            ("Stashed uncommitted code changes.", False)
        ]
    },
    {
        "text": "Q30 [Module 4: Git & DevOps]: What is the main architectural difference between 'git rebase' and 'git merge'?",
        "explanation": "Rebase rewrites commit history linearly onto the tip of another branch; merge creates a 3-way merge commit preserving topology.",
        "options": [
            ("Merge rewrites history while rebase preserves original commit hashes.", False),
            ("Rebase replays commits linearly onto a new base; merge combines branch histories with a merge commit.", True),
            ("Rebase can only be run on the main production branch.", False),
            ("Merge automatically resolves all code conflicts without developer input.", False)
        ]
    },
    {
        "text": "Q31 [Module 4: Git & DevOps]: Why is it critical to list .env files containing API keys inside .gitignore before committing?",
        "explanation": ".gitignore prevents secret credential files from being tracked and pushed to public or remote Git repositories.",
        "options": [
            (".gitignore compresses .env files into zip archives.", False),
            ("It prevents sensitive API keys and secrets from being committed and leaked to remote repositories.", True),
            ("Git automatically encrypts .env files during git push.", False),
            (".env files are required for git merge resolution.", False)
        ]
    },
    {
        "text": "Q32 [Module 4: Git & DevOps]: What is the primary purpose of GitHub Branch Protection rules?",
        "explanation": "Branch protection rules enforce mandatory Pull Request reviews, passing CI tests, and prevent direct force pushes.",
        "options": [
            ("To hide source code from external visitors.", False),
            ("To enforce mandatory PR reviews, automated status checks, and block unauthorized force pushes.", True),
            ("To automatically convert Python code into JavaScript.", False),
            ("To restrict developers from creating local feature branches.", False)
        ]
    },

    # Module 5 (Q33 - Q40)
    {
        "text": "Q33 [Module 5: Databases & ORM]: What is the key operational distinction between SQL DELETE and TRUNCATE commands?",
        "explanation": "DELETE is DML (row-by-row logging, supports WHERE); TRUNCATE is DDL (deallocates data pages instantly, resets auto-increment).",
        "options": [
            ("TRUNCATE supports WHERE filtering clauses.", False),
            ("DELETE is DML row-by-row logging; TRUNCATE is DDL data page deallocation without logging individual rows.", True),
            ("DROP and TRUNCATE perform identical operations.", False),
            ("DELETE drops table schema from the catalog.", False)
        ]
    },
    {
        "text": "Q34 [Module 5: Databases & ORM]: In relational database ACID properties, what does 'Atomicity' guarantee?",
        "explanation": "Atomicity guarantees that all operations within a transaction complete successfully, or all changes are rolled back completely.",
        "options": [
            ("Atomicity encrypts database columns on disk.", False),
            ("All statements in a transaction succeed together, or the entire transaction is rolled back (All or Nothing).", True),
            ("Atomicity ensures sub-millisecond query execution speeds.", False),
            ("Atomicity prevents simultaneous user logins.", False)
        ]
    },
    {
        "text": "Q35 [Module 5: Databases & ORM]: What requirement must a database table satisfy to meet Third Normal Form (3NF)?",
        "explanation": "3NF requires the table to be in 2NF and have no transitive dependencies (non-key attributes depend ONLY on the primary key).",
        "options": [
            ("Table must contain JSON document columns.", False),
            ("Must be in 2NF and contain no transitive dependencies among non-key attributes.", True),
            ("Must feature composite primary keys on all columns.", False),
            ("Must store all data in a single un-normalized flat file.", False)
        ]
    },
    {
        "text": "Q36 [Module 5: Databases & ORM]: How does a B-Tree Index improve SQL query execution performance?",
        "explanation": "B-Tree indices allow log-time O(log N) value lookup without scanning every unindexed row in the table (Sequential Scan).",
        "options": [
            ("Indices compress disk storage by 90%.", False),
            ("Provides logarithmic O(log N) lookup trees, eliminating the need for full table sequential scans.", True),
            ("B-Tree indices speed up INSERT operations significantly.", False),
            ("Indices replace foreign key constraint validation.", False)
        ]
    },
    {
        "text": "Q37 [Module 5: Databases & ORM]: What is Polyglot Persistence in modern enterprise system architecture?",
        "explanation": "Using different database technologies (PostgreSQL, MongoDB, Redis) tailored to specific domain data requirements.",
        "options": [
            ("Translating SQL queries into multiple spoken languages.", False),
            ("Utilizing multiple database technologies optimized for specific workload requirements within one system.", True),
            ("Storing all application data inside local browser storage.", False),
            ("Running SQL databases without primary keys.", False)
        ]
    },
    {
        "text": "Q38 [Module 5: Databases & ORM]: In SQLAlchemy ORM, what is the role of the Declarative Base class?",
        "explanation": "Declarative Base registers Python model classes and maps them to underlying database table schemas.",
        "options": [
            ("Base handles HTTP request routing.", False),
            ("It acts as a catalog registering ORM class definitions and mapping them to relational database tables.", True),
            ("Base executes raw SQL string migrations automatically.", False),
            ("Base generates JWT access tokens.", False)
        ]
    },
    {
        "text": "Q39 [Module 5: Databases & ORM]: What does cascade='all, delete-orphan' enforce on an ORM relationship?",
        "explanation": "Deleting a parent record automatically deletes all child objects associated with that parent relationship.",
        "options": [
            ("Child objects are converted into NULL foreign keys.", False),
            ("Automatically deletes child records when they are disassociated from parent or parent is deleted.", True),
            ("Prevents parent objects from being updated.", False),
            ("Duplicates child objects across schemas.", False)
        ]
    },
    {
        "text": "Q40 [Module 5: Databases & ORM]: In Pydantic v2, why is ConfigDict(from_attributes=True) required when returning ORM model objects?",
        "explanation": "from_attributes=True enables Pydantic to read attributes directly from ORM objects (obj.attr) rather than dict keys (obj['attr']).",
        "options": [
            ("It encrypts JSON responses with SSL keys.", False),
            ("Allows Pydantic to extract data directly from ORM object attribute getters instead of dict key lookups.", True),
            ("It disables type validation for speed.", False),
            ("It creates SQLite database tables on the fly.", False)
        ]
    },

    # Module 6 (Q41 - Q50)
    {
        "text": "Q41 [Module 6: LLM & Applied AI]: What is the fundamental innovation of the Transformer Neural Network architecture?",
        "explanation": "Parallel processing of sequence elements via Self-Attention mechanisms instead of sequential recurrent processing (RNNs).",
        "options": [
            ("Using decision trees for text generation.", False),
            ("Parallel sequence processing using Self-Attention mechanisms to compute token relationships.", True),
            ("Eliminating neural networks in favor of regex rules.", False),
            ("Storing text as raw ASCII values without embeddings.", False)
        ]
    },
    {
        "text": "Q42 [Module 6: LLM & Applied AI]: What is the first stage in the 6-Step Transformer Execution Pipeline?",
        "explanation": "Tokenization converts raw text input strings into numeric sub-word token IDs.",
        "options": [
            ("Softmax probability calculation is the final output step.", False),
            ("Tokenization (converting raw text into sub-word token IDs).", True),
            ("Positional Encoding occurs after embedding lookup.", False),
            ("Cosine similarity search.", False)
        ]
    },
    {
        "text": "Q43 [Module 6: LLM & Applied AI]: Which of the following is NOT one of the 5 Core Prompt Engineering Components?",
        "explanation": "The 5 Core Prompt components are Role, Context, Instruction, Input Data, and Output Format. SQL Index is DB architecture.",
        "options": [
            ("Persona/Role is a core component.", False),
            ("SQL Index Optimization (this is a database concept, not a prompt component).", True),
            ("Context & Constraints is a core component.", False),
            ("Output Format specification is a core component.", False)
        ]
    },
    {
        "text": "Q44 [Module 6: LLM & Applied AI]: How does Chain-of-Thought (CoT) prompting improve LLM reasoning performance?",
        "explanation": "CoT prompts the model to break down complex multi-step reasoning problems into step-by-step intermediate explanations.",
        "options": [
            ("CoT decreases prompt token count by 90%.", False),
            ("Prompting the model to generate step-by-step intermediate reasoning steps before producing a final answer.", True),
            ("CoT restricts the model to binary Yes/No responses.", False),
            ("CoT retrains model weights during inference.", False)
        ]
    },
    {
        "text": "Q45 [Module 6: LLM & Applied AI]: What distinguishes an Agentic 'Act' mode from a passive 'Plan' mode?",
        "explanation": "Act mode allows AI agents to execute real-world tool calls (API requests, code execution, database writes).",
        "options": [
            ("Plan mode executes live database deletes.", False),
            ("Act mode grants the agent authority to invoke external tools, APIs, and code execution functions.", True),
            ("Act mode only operates on offline static text files.", False),
            ("Plan mode requires GPU cluster hardware.", False)
        ]
    },
    {
        "text": "Q46 [Module 6: LLM & Applied AI]: What is the primary purpose of Retrieval-Augmented Generation (RAG)?",
        "explanation": "RAG injects relevant private domain context retrieved from vector databases into LLM prompts to prevent hallucinations.",
        "options": [
            ("RAG retrains foundation models from scratch every hour.", False),
            ("Grounding LLM responses by retrieving relevant context chunks from vector databases and injecting them into prompts.", True),
            ("RAG compresses MP4 videos into text transcripts.", False),
            ("RAG replaces CSS styling in web applications.", False)
        ]
    },
    {
        "text": "Q47 [Module 6: LLM & Applied AI]: In vector embedding math, what does a Cosine Similarity score of 1.0 indicate?",
        "explanation": "A Cosine Similarity of 1.0 means the two vector embeddings point in identical directions (maximum semantic similarity).",
        "options": [
            ("The vectors are completely orthogonal (unrelated).", False),
            ("Identical vector direction representing maximum semantic similarity.", True),
            ("The vectors are diametrically opposed in meaning.", False),
            ("An error occurred during vector calculation.", False)
        ]
    },
    {
        "text": "Q48 [Module 6: LLM & Applied AI]: Why is HTTP StreamingResponse used when delivering LLM generated text to web frontends?",
        "explanation": "Streaming delivers generated tokens to the user in real time as they are produced, minimizing Time to First Token (TTFT).",
        "options": [
            ("Streaming prevents users from viewing text.", False),
            ("Delivering tokens incrementally as they are generated to reduce perceived latency (TTFT).", True),
            ("Streaming requires WebGL hardware acceleration.", False),
            ("Streaming saves static HTML files to disk.", False)
        ]
    },
    {
        "text": "Q49 [Module 6: LLM & Applied AI]: Which error classification describes code that compiles and executes without exceptions but outputs incorrect business logic?",
        "explanation": "Logical/Algorithmic errors occur when code runs without throwing exceptions but yields incorrect results.",
        "options": [
            ("Syntax Error is caught by parser.", False),
            ("Logical / Algorithmic Error.", True),
            ("Runtime Exception crashes program execution.", False),
            ("Network Timeout Error.", False)
        ]
    },
    {
        "text": "Q50 [Module 6: LLM & Applied AI]: What is the Golden Rule of AI-Assisted Software Engineering?",
        "explanation": "Always inspect full, un-truncated authority log files before forming diagnostic hypotheses or modifying code logic.",
        "options": [
            ("Immediately rewrite code blindly without reading error logs.", False),
            ("Always inspect un-truncated authority log tracebacks before diagnosing runtime errors or writing code fixes.", True),
            ("Trust AI generated code without running unit tests.", False),
            ("Delete failing tests to mark tasks complete.", False)
        ]
    }
]

def seed_final_exam():
    db = SessionLocal()
    try:
        # Find Quiz 37
        quiz = db.query(Quiz).filter(Quiz.topic_id == 37).first()
        if not quiz:
            print("Quiz 37 not found in DB!")
            return

        print(f"Updating Quiz ID: {quiz.id} ({quiz.title})...")

        # Delete existing placeholder questions for Quiz 37
        existing_q_ids = [q.id for q in quiz.questions]
        if existing_q_ids:
            db.query(Option).filter(Option.question_id.in_(existing_q_ids)).delete(synchronize_session=False)
            db.query(Question).filter(Question.quiz_id == quiz.id).delete(synchronize_session=False)
            db.commit()

        # Add 50 high-caliber real questions
        q_added = 0
        for item in FINAL_50_QUESTIONS:
            q_added += 1
            new_q = Question(
                quiz_id=quiz.id,
                text=item["text"],
                explanation=item["explanation"],
                points=2
            )
            db.add(new_q)
            db.flush()

            for opt_text, is_corr in item["options"]:
                new_opt = Option(
                    question_id=new_q.id,
                    text=opt_text,
                    is_correct=is_corr
                )
                db.add(new_opt)

        db.commit()
        print(f"Successfully re-seeded {q_added} professional questions & choices for Quiz ID {quiz.id}!")
    except Exception as e:
        db.rollback()
        print(f"Error seeding final exam: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_final_exam()
