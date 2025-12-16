import api from "./api";

export const getJobs = async ({ status, page = 1, limit = 10 }) => {
  const params = { page, limit };
  if (status) params.status = status;

  const res = await api.get("/jobs", { params });
  return res.data;
};

export const getJob = async (jobId) => {
  const res = await api.get(`/jobs/${jobId}`);
  return res.data;
};

export const createJob = async (payload) => {
  const res = await api.post("/jobs", payload);
  return res.data;
};

export const updateJob = async (jobId, payload) => {
  const res = await api.put(`/jobs/${jobId}`, payload);
  return res.data;
};

export const deleteJob = async (jobId) => {
  await api.delete(`/jobs/${jobId}`);
};
