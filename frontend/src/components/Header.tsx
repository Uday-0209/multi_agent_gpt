export default function Header() {
  return (
    <header className="w-full border-b bg-white">
      <div className="max-w-6xl mx-auto p-4 flex justify-between items-center">

        <h1 className="text-xl font-bold">
          Multi-LLM Orchestrator
        </h1>

        <p className="text-sm text-gray-500">
          FastAPI • LangGraph • Multi-Model AI
        </p>

      </div>
    </header>
  )
}