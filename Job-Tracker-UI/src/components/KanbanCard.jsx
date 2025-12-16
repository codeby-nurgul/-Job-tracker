export default function KanbanCard({ job }) {
  const onDragStart = (e) => {
    e.dataTransfer.setData("jobId", job.id);
  };

  return (
    <div className="kanban-card" draggable onDragStart={onDragStart}>
      <div className="kanban-card-title">
        {job.company_name ?? job.company}
      </div>
      <div className="kanban-card-sub">{job.position}</div>
      <div className="kanban-card-meta">{job.apply_date}</div>
    </div>
  );
}
