import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Files from "./pages/Files";
import Calculate from "./pages/Calculate";
import Navbar from "./components/Navbar";

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/files" element={<Files />} />
        <Route path="/calculate" element={<Calculate />} />
      </Routes>
    </Router>
  );
};

export default App;
