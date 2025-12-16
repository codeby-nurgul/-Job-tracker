import { useState } from "react";
import { createJob } from "../services/JobService";
import "../styles/JobCreate.css";

export default function JobCreate({ onCreated }) {
  const [form, setForm] = useState({
    company_name: "",
    position: "",
    status: "Applied",
    apply_date: "",
  });

  const submit = async (e) => {
    e.preventDefault();
    await createJob(form);
    await onCreated?.();
    setForm({ company_name: "", position: "", status: "Applied", apply_date: "" });
  };

  return (
    <form className="job-info-form" onSubmit={submit}>
      <input
        placeholder="Company"
        value={form.company_name}
        onChange={(e) => setForm({ ...form, company_name: e.target.value })}
      />
      <input
        placeholder="Position"
        value={form.position}
        onChange={(e) => setForm({ ...form, position: e.target.value })}
      />
      <select
        value={form.status}
        onChange={(e) => setForm({ ...form, status: e.target.value })}
      >
        <option>Applied</option>
        <option>Interview</option>
        <option>Offer</option>
        <option>Rejected</option>
      </select>
      <input
        type="date"
        value={form.apply_date}
        onChange={(e) => setForm({ ...form, apply_date: e.target.value })}
      />
      <button type="submit">Add Job</button>
    </form>
  );
}
