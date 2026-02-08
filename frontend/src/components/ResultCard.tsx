type Props = {
  credit_score: number
  risk_tier: string
  default_probability: number
}

export default function ResultCard({
  credit_score,
  risk_tier,
  default_probability,
}: Props) {
  return (
    <div className="mt-6 rounded-xl bg-white p-6 shadow-md">
      <h2 className="text-xl font-semibold mb-4">Your Credit Assessment</h2>

      <div className="flex justify-between">
        <div>
          <p className="text-sm text-slate-500">Credit Score</p>
          <p className="text-3xl font-bold">{credit_score}</p>
        </div>

        <div>
          <p className="text-sm text-slate-500">Risk Tier</p>
          <p className="text-xl font-semibold">{risk_tier}</p>
        </div>

        <div>
          <p className="text-sm text-slate-500">Default Probability</p>
          <p className="text-xl font-semibold">
            {(default_probability * 100).toFixed(1)}%
          </p>
        </div>
      </div>
    </div>
  )
}
