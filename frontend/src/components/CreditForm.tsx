import { useState } from "react"
import { predictCredit } from "../api/predict"
import ResultCard from "./ResultCard"

export default function CreditForm() {
  const [form, setForm] = useState<any>({
  RevolvingUtilizationOfUnsecuredLines: "",
  age: "",
  "NumberOfTime30-59DaysPastDueNotWorse": "",
  DebtRatio: "",
  MonthlyIncome: "",
  NumberOfOpenCreditLinesAndLoans: "",
  NumberOfTimes90DaysLate: "",
  NumberRealEstateLoansOrLines: "",
  "NumberOfTime60-89DaysPastDueNotWorse": "",
  NumberOfDependents: "",
})


  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setForm({ ...form, [e.target.name]: Number(e.target.value) })
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true)

    try {
      const res = await predictCredit(form)
      setResult(res)
    } catch (err) {
      alert("Prediction failed. Check backend.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <form
        onSubmit={handleSubmit}
        className="grid grid-cols-1 md:grid-cols-2 gap-4"
      >
        {Object.keys(form).map((key) => (
          <div key={key}>
            <label className="text-sm text-slate-600">{key}</label>
            <input
              name={key}
              required
              type="number"
              step="any"
              className="w-full rounded-lg border p-2"
              onChange={handleChange}
            />
          </div>
        ))}

        <button
          type="submit"
          className="col-span-full mt-4 rounded-xl bg-slate-900 py-3 text-white hover:bg-slate-800"
        >
          {loading ? "Analyzing..." : "Analyze Credit Risk"}
        </button>
      </form>

      {result && <ResultCard {...result} />}
    </>
  )
}
