"use client"

interface Props {
  mode: string
  setMode: (mode:string)=>void
}

export default function ModeSelector({mode,setMode}:Props){

  return(

    <select
      className="border p-2 rounded"
      value={mode}
      onChange={(e)=>setMode(e.target.value)}
    >

      <option value="single">Single LLM</option>
      <option value="multi">Multi LLM</option>

    </select>

  )
}