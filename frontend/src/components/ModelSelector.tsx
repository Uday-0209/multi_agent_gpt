"use client"

interface Props{
  value:string
  onChange:(v:string)=>void
}

const models = [
  "gpt-4o",
  "claude-3-opus",
  "sarvam-m",
  "llama3-70b-groq"
]

export default function ModelSelector({value,onChange}:Props){

  return(

    <select
      className="border p-2 rounded w-full"
      value={value}
      onChange={(e)=>onChange(e.target.value)}
    >

      {models.map((m)=>(
        <option key={m} value={m}>
          {m}
        </option>
      ))}

    </select>

  )

}