import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate(); // Hook for navigation

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Email:", email);
    console.log("Password:", password);
    // Add authentication logic here (e.g., API call)
    // If login is successful, navigate to the home page
    alert("Login successful!");
    navigate("/"); // Navigate to the Home page
  };

  return (
    <div className="glass">
      <h1>Welcome,</h1>
      <h2>Log in to continue</h2>
      <form onSubmit={handleSubmit}>
        <div className="login">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
          />

          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
          />

          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
