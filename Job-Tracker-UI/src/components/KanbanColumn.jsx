import { updateJob } from "../services/JobService";
import KanbanCard from "./KanbanCard";

export default function KanbanColumn({ status, jobs, onChange }) {
  const handleDrop = async (e) => {
    e.preventDefault();
    const jobId = e.dataTransfer.getData("jobId");
    if (!jobId) return;

    await updateJob(jobId, { status });
    await onChange?.();
  };

  return (
    <div
      className={`kanban-column ${status.toLowerCase()}`}
      onDragOver={(e) => e.preventDefault()}
      onDrop={handleDrop}
    >
      <div className="kanban-column-header">
        {status} <span className="kanban-count">({jobs.length})</span>
      </div>

      <div className="kanban-column-body">
        {jobs.map((job) => (
          <KanbanCard key={job.id} job={job} />
        ))}
      </div>
    </div>
  );
}
