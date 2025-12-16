import KanbanColumn from "./KanbanColumn";
import "../styles/Kanban.css";

const STATUSES = ["Applied", "Interview", "Offer", "Rejected"];

export default function KanbanBoard({ jobs = [], onChange }) {
  return (
    <div className="kanban-board">
      {STATUSES.map((status) => (
        <KanbanColumn
          key={status}
          status={status}
          jobs={jobs.filter((j) => j.status === status)}
          onChange={onChange}
        />
      ))}
    </div>
  );
}
