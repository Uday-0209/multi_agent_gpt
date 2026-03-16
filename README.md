<h1 align="center">Multi-LLM Orchestrator</h1>

<p align="center">
A modular AI platform that orchestrates multiple Large Language Models, compares their outputs,
and automatically selects the best answer using a judge model.
</p>

<hr>

<h2>Project Overview</h2>

<p>
Multi-LLM Orchestrator is an AI system designed to run multiple LLMs simultaneously,
evaluate their responses, and select the best solution automatically.
</p>

<p>
The platform is designed for tasks such as:
</p>

<ul>
<li>Programming assistance</li>
<li>Code generation</li>
<li>Technical explanation</li>
<li>Research comparison</li>
<li>AI model benchmarking</li>
</ul>

<p>
Instead of relying on a single LLM, the system uses a combination of models and a judge model
to ensure higher quality outputs.
</p>

<hr>

<h2>Architecture</h2>

<pre>
User Input
     │
     ▼
SLM (Prompt Refinement)
     │
     ▼
Decision Node
     │
     ├── Single LLM Execution
     │
     └── Multi-LLM Execution
             │
             ▼
      Judge Model Evaluation
             │
             ▼
        Final Answer
</pre>

<hr>

<h2>Core Components</h2>

<h3>1. Prompt Refinement (SLM)</h3>
<p>
A small language model refines the user query before it is passed to the main generation models.
This improves clarity and ensures better responses.
</p>

<h3>2. Model Selection Engine</h3>
<p>
The system dynamically selects the best models based on:
</p>

<ul>
<li>User input</li>
<li>Mode (Single or Multi model)</li>
<li>Cost optimization</li>
<li>Model capabilities</li>
</ul>

<h3>3. Multi-Model Generation</h3>
<p>
When multi-model mode is selected, the system runs multiple models in parallel.
Each model generates a response independently.
</p>

<h3>4. Judge Model</h3>
<p>
The judge model evaluates all responses and decides whether to:
</p>

<ul>
<li>Select the best response</li>
<li>Refine an existing response</li>
<li>Regenerate the solution</li>
</ul>

<hr>

<h2>Supported LLM Providers</h2>

<ul>
<li>OpenAI</li>
<li>Anthropic</li>
<li>Groq</li>
<li>Sarvam</li>
<li>Open-source LLMs</li>
</ul>

<p>
The system is provider-agnostic and can easily integrate additional models.
</p>

<hr>

<h2>Technology Stack</h2>

<table>
<tr>
<th>Layer</th>
<th>Technology</th>
</tr>

<tr>
<td>Backend</td>
<td>FastAPI</td>
</tr>

<tr>
<td>AI Orchestration</td>
<td>LangGraph + LangChain</td>
</tr>

<tr>
<td>Frontend</td>
<td>Next.js + TypeScript</td>
</tr>

<tr>
<td>Database</td>
<td>PostgreSQL (future)</td>
</tr>

<tr>
<td>Vector DB</td>
<td>Planned Integration</td>
</tr>

</table>

<hr>

<h2>Frontend Features</h2>

<ul>
<li>Interactive AI interface</li>
<li>Single or Multi-LLM execution mode</li>
<li>Dynamic model selection</li>
<li>Parallel response comparison</li>
<li>Judge evaluation output</li>
<li>Chat-style conversation interface</li>
</ul>

<hr>

<h2>Backend Features</h2>

<ul>
<li>LangGraph workflow orchestration</li>
<li>Provider abstraction layer</li>
<li>Streaming responses</li>
<li>Model comparison system</li>
<li>Automatic prompt refinement</li>
<li>Conversation memory support</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
multi_agent_GPT
│
├── app
│   ├── core
│   │   ├── model_registry.py
│   │   └── provider_factory.py
│   │
│   ├── graph
│   │   ├── nodes
│   │   │   ├── slm_node.py
│   │   │   ├── single_llm_node.py
│   │   │   ├── multi_llm_node.py
│   │   │   └── judge_node.py
│   │   │
│   │   └── state.py
│   │
│   └── providers
│       ├── openai_provider.py
│       ├── groq_provider.py
│       └── sarvam_provider.py
│
├── ai-orchestrator-ui
│   ├── src
│   │   ├── app
│   │   └── components
│
└── README.md
</pre>

<hr>

<h2>How It Works</h2>

<ol>
<li>User submits a query</li>
<li>SLM refines the prompt</li>
<li>System selects appropriate models</li>
<li>Models generate responses in parallel</li>
<li>Judge model evaluates outputs</li>
<li>Best response is returned</li>
</ol>

<hr>

<h2>Example Workflow</h2>

<pre>
User Query:
"Build a FastAPI CRUD API"

System Execution:
1. Refine prompt
2. Run GPT-4o and Claude
3. Compare responses
4. Judge selects best answer
</pre>

<hr>

<h2>Future Enhancements</h2>

<ul>
<li>Vector database for memory</li>
<li>Persistent chat history</li>
<li>Cost-aware model routing</li>
<li>Execution sandbox for generated code</li>
<li>Model voting system</li>
</ul>

<hr>

<h2>License</h2>

<p>
MIT License
</p>

<p align="center">
Built with ❤️ using FastAPI, LangGraph, and modern AI infrastructure.
</p>
