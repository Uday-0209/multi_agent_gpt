"use client"

import { useState, useEffect } from "react"

export default function Orchestrator() {

  const [mode, setMode] = useState("single")
  const [modelCount, setModelCount] = useState(1)

  const [models, setModels] = useState(["gpt-4o"])
  const [prompt, setPrompt] = useState("")

  const [outputs, setOutputs] = useState<any>({})

  const [messages, setMessages] = useState<any[]>([])

  const availableModels = [
    "gpt-4o",
    "claude-3-opus",
    "sarvam-m",
    "llama3-70b-groq",
    "gpt4o_mini"
  ]

  /* Reset outputs whenever models change */

  useEffect(() => {

    const newOutputs:any = {}

    models.forEach(m => {
      newOutputs[m] = ""
    })

    setOutputs(newOutputs)

  }, [models])


  function changeMode(newMode: string) {

    setMode(newMode)

    if (newMode === "single") {

      setModelCount(1)
      setModels(["gpt-4o"])

    } else {

      setModelCount(2)
      setModels(["gpt-4o", "claude-3-opus"])

    }

  }


  function changeModelCount(n: number) {

    setModelCount(n)

    const newModels = Array(n).fill("gpt-4o")

    setModels(newModels)

  }


  function updateModel(index: number, value: string) {

    const newModels = [...models]

    newModels[index] = value

    setModels(newModels)

  }


async function runOrchestrator() {

  setOutputs({})

  const payload = {
    user_input: prompt,
    mode: mode,
    generation_models: models,
    judge_model: "gpt-4o",
    messages: messages
  }

  const response = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })

  const reader = response.body?.getReader()
  const decoder = new TextDecoder()

  if (!reader) return

  let buffer = ""

  while (true) {

    const { done, value } = await reader.read()

    if (done) break

    buffer += decoder.decode(value)

    const lines = buffer.split("\n")

    buffer = lines.pop() || ""

    for (const line of lines) {

      if (!line.startsWith("data:")) continue

      const event = JSON.parse(line.replace("data:", "").trim())

        /* SINGLE MODEL OUTPUT */

        if (event.single_llm?.outputs) {

        const outputs = event.single_llm.outputs

        Object.keys(outputs).forEach((model)=>{

            setOutputs((prev:any)=>({
            ...prev,
            [model]: outputs[model]
            }))

        })

        }

        /* MULTI MODEL OUTPUT */

        if (event.multi_llm?.outputs) {

        const outputs = event.multi_llm.outputs

        Object.keys(outputs).forEach((model)=>{

            setOutputs((prev:any)=>({
            ...prev,
            [model]: outputs[model]
            }))

        })

        }

        /* JUDGE OUTPUT */

        if (event.judge_llm) {

        setOutputs((prev:any)=>({
            ...prev,
            judge: event.judge_llm.final_answer
        }))

        }

    }

  }

}


  return (

    <div className="p-8 max-w-6xl mx-auto">

      <h1 className="text-2xl font-bold mb-6">
        Multi-LLM Orchestrator
      </h1>


      {/* MODE SELECTOR */}

      <div className="flex gap-4 mb-6">

        <select
          className="border p-2 rounded"
          value={mode}
          onChange={(e) => changeMode(e.target.value)}
        >

          <option value="single">Single LLM</option>
          <option value="multi">Multi LLM</option>

        </select>


        {mode === "multi" && (

          <select
            className="border p-2 rounded"
            value={modelCount}
            onChange={(e) =>
              changeModelCount(Number(e.target.value))
            }
          >

            <option value={2}>2 Models</option>
            <option value={3}>3 Models</option>

          </select>

        )}

      </div>


      {/* MODEL SELECTORS */}

      <div
        className={`grid gap-4 mb-6 ${
          modelCount === 1
            ? "grid-cols-1"
            : modelCount === 2
            ? "grid-cols-2"
            : "grid-cols-3"
        }`}
      >

        {models.map((model, index) => (

          <select
            key={index}
            className="border p-2 rounded w-full"
            value={model}
            onChange={(e) =>
              updateModel(index, e.target.value)
            }
          >

            {availableModels.map((m) => (
              <option key={m} value={m}>
                {m}
              </option>
            ))}

          </select>

        ))}

      </div>


      {/* PROMPT */}

      <textarea
        className="w-full border p-3 rounded mb-4"
        placeholder="Ask your programming question..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />


      <button
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        onClick={runOrchestrator}
      >
        Run Orchestrator
      </button>


      {/* OUTPUT PANELS */}

      <div
        className={`grid gap-4 mt-10 ${
          modelCount === 1
            ? "grid-cols-1"
            : modelCount === 2
            ? "grid-cols-2"
            : "grid-cols-3"
        }`}
      >

        {models.map((model, index) => (

          <div
            key={index}
            className="border rounded-lg p-4 bg-gray-50 min-h-[250px]"
          >

            <h3 className="font-bold mb-2 text-blue-600">
              {model}
            </h3>

            <pre className="text-sm whitespace-pre-wrap">
              {outputs[model] || "Waiting for response..."}
            </pre>

          </div>

        ))}

      </div>
      <div className="border rounded-lg p-4 bg-yellow-50 mt-6">

            <h3 className="font-bold mb-2">
                Judge Evaluation
            </h3>

            <pre className="text-sm whitespace-pre-wrap">
                {outputs["judge"] || "Waiting for judge..."}
            </pre>

        </div>

        <div className="border rounded p-4 h-[300px] overflow-y-auto">

            {messages.map((msg,i)=>(

            <div key={i} className="mb-3">

                <b>{msg.role}:</b> {msg.content}

            </div>

            ))}

        </div>
        

    </div>

  )

}