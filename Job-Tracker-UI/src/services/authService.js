import api from "./api";

export const register = async (email, password) => {
  const res = await api.post("/auth/register", {
    email,
    password,
  });
  return res.data;
};

export const login = async (email, password) => {
  const res = await api.post("/auth/login", {
    email,
    password,
  });

  const token = res.data.access_token;

  localStorage.setItem("access_token", token);
  localStorage.setItem("user", JSON.stringify(res.data.user));

  return res.data;
};

export const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("user");
};
