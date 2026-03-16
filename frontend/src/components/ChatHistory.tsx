"use client"

export default function ChatHistory() {

  const chats = [
    "FastAPI CRUD",
    "Redis Queue System",
    "Notification Service"
  ]

  return (

    <div className="w-64 border-r h-screen p-4 bg-white">

      <h2 className="font-bold mb-4">History</h2>

      {chats.map((chat,i)=>(
        <div
          key={i}
          className="p-2 hover:bg-gray-100 rounded cursor-pointer"
        >
          {chat}
        </div>
      ))}

    </div>
  )
}