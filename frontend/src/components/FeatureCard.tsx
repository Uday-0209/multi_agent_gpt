interface Props {
  title: string
  description: string
}

export default function FeatureCard({ title, description }: Props) {

  return (
    <div className="border rounded-lg p-6 bg-white shadow-sm">

      <h3 className="text-lg font-semibold mb-2">
        {title}
      </h3>

      <p className="text-gray-600 text-sm">
        {description}
      </p>

    </div>
  )
}