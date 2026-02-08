import CreditForm from "./components/CreditForm"

export default function App() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="w-full max-w-4xl rounded-2xl bg-white p-8 shadow-xl">
        <h1 className="text-3xl font-bold mb-2">CreditLens</h1>
       

        <p className="text-slate-600 mb-6">
          AI-powered credit risk assessment
        </p>

        <CreditForm />
      </div>
    </div>
  )
}
