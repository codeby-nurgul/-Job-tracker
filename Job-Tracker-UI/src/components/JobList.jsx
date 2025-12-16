import { useEffect, useState } from "react";
import { getJobs, deleteJob } from "../services/JobService";
import "../styles/JobList.css";

export default function JobList() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  const loadJobs = async () => {
    try {
      const data = await getJobs({});
      setJobs(data);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadJobs();
  }, []);

  const handleDelete = async (id) => {
    if (!confirm("Delete this job?")) return;
    await deleteJob(id);
    loadJobs();
  };

  if (loading) return <p className="joblist-loading">Loading...</p>;

  return (
    <div className="joblist-wrapper">
      <table className="joblist-table">
        <thead>
          <tr>
            <th>Company</th>
            <th>Position</th>
            <th>Status</th>
            <th>Apply Date</th>
            <th>Delete</th>
          </tr>
        </thead>

        <tbody>
          {jobs.map((job) => (
            <tr key={job.id}>
              <td>{job.company_name}</td>
              <td>{job.position}</td>
              <td>
                <span className={`status-badge ${job.status.toLowerCase()}`}>
                  {job.status}
                </span>
              </td>
              <td>{job.apply_date}</td>
              <td>
                <button
                  className="delete-btn"
                  onClick={() => handleDelete(job.id)}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
