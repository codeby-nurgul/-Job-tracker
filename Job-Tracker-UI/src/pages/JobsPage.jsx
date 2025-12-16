import { useEffect, useState } from "react";
import JobCreate from "../components/JobCreate";
import JobList from "../components/JobList";
import KanbanBoard from "../components/KanbanBoard";
import { getJobs } from "../services/JobService";
import "../styles/JobsPage.css";

export default function JobsPage() {
  const [view, setView] = useState("list"); // "kanban" da yapabilirsin
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadJobs = async () => {
    const data = await getJobs({});
    setJobs(Array.isArray(data) ? data : []);
  };

  useEffect(() => {
    (async () => {
      try {
        await loadJobs();
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  return (
    <div className="job-page">
      <h1 className="job-page-title">Job Applications</h1>

      <JobCreate onCreated={loadJobs} />

      <div className="view-toggle">
        <button
          className={view === "list" ? "active" : ""}
          onClick={() => setView("list")}
          type="button"
        >
          List
        </button>
        <button
          className={view === "kanban" ? "active" : ""}
          onClick={() => setView("kanban")}
          type="button"
        >
          Kanban
        </button>
      </div>

      {loading ? (
        <p className="joblist-loading">Loading...</p>
      ) : view === "list" ? (
        <JobList jobs={jobs} onChange={loadJobs} />
      ) : (
        <KanbanBoard jobs={jobs} onChange={loadJobs} />
      )}
    </div>
  );
}
