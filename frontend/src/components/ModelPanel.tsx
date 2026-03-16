"use client"

interface Props{
  model:string
  output:string
}

export default function ModelPanel({model,output}:Props){

  return(

    <div className="border rounded-lg p-4 bg-gray-50">

      <h3 className="font-bold mb-2">
        {model}
      </h3>

      <pre className="text-sm whitespace-pre-wrap">
        {output}
      </pre>

    </div>

  )

}