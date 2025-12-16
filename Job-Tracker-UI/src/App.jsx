import { Routes, Route, Navigate } from "react-router";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/JobsPage";
import "./App.css"
const isAuth = () => !!localStorage.getItem("access_token");

export default function App() {
  return (
    <div className="container">
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route
          path="/"
          element={isAuth() ? <Dashboard /> : <Navigate to="/login" />}
        />
      </Routes>
    </div>
  );
}
