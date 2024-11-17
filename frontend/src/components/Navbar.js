import React from "react";
import { Link } from "react-router-dom"; // Import Link from react-router-dom
import "../styles/navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="container">
        <ul className="nav-links">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/files">Files</Link>
          </li>
          <li>
            <Link to="/calculate">Calculate</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
