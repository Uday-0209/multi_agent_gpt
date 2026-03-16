import Header from "@/components/Header"
import FeatureCard from "@/components/FeatureCard"
import Link from "next/link"

export default function Home() {

  return (

    <main className="bg-gray-50 min-h-screen">

      <Header />

      <div className="max-w-6xl mx-auto p-8">

        {/* HERO SECTION */}

        <div className="text-center mb-12">

          <h1 className="text-4xl font-bold mb-4">
            Multi-LLM Orchestration Platform
          </h1>

          <p className="text-gray-600 max-w-2xl mx-auto">
            This platform runs multiple AI models in parallel,
            compares their outputs, and uses a judge model
            to select or regenerate the best response.
          </p>

          <Link href="/orchestrator">
            <button className="mt-6 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
              Launch Orchestrator
            </button>
          </Link>

        </div>


        {/* FEATURES */}

        <div className="grid md:grid-cols-3 gap-6 mb-12">

          <FeatureCard
            title="Multi-Model Generation"
            description="Run OpenAI, Claude, Groq, Sarvam, or open-source models simultaneously."
          />

          <FeatureCard
            title="Parallel Streaming"
            description="Each model streams responses in real time for easy comparison."
          />

          <FeatureCard
            title="Judge Model"
            description="A judge model evaluates outputs and selects the best solution."
          />

          <FeatureCard
            title="Self-Correction"
            description="If outputs are insufficient, the system regenerates improved prompts."
          />

          <FeatureCard
            title="Cost Optimization"
            description="Models can be selected dynamically based on cost and quality."
          />

          <FeatureCard
            title="Extensible Architecture"
            description="Supports multiple LLM providers and scalable orchestration."
          />

        </div>


        {/* WORKFLOW */}

        <div className="bg-white border rounded-lg p-8">

          <h2 className="text-2xl font-bold mb-4">
            System Workflow
          </h2>

          <ol className="list-decimal ml-6 space-y-2 text-gray-700">

            <li>User submits a programming query</li>
            <li>SLM refines the prompt</li>
            <li>Multiple LLMs generate answers</li>
            <li>Responses stream live</li>
            <li>Judge model evaluates outputs</li>
            <li>Best answer is selected or regenerated</li>

          </ol>

        </div>

      </div>

    </main>
  )
}