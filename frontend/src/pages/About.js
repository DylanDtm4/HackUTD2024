import React from "react";
import "../styles/styles.css"; // Import the CSS file

function About() {
  return (
    <div className="container">
      <h1>About TopoLogic</h1>
      <p>
        Meet <strong>TopoLogic</strong>, the ultimate app for solving word
        problems with speed and precision, powered by the blazing performance of
        SambaNova. TopoLogic transforms complex problems into solutions by:
      </p>
      <ol>
        <li>
          <strong>Extracting Key Variables:</strong> Automatically identify the
          essential elements of your problem.
        </li>
        <li>
          <strong>Classifying Problems:</strong> Match each problem to its
          category for quick resolution.
        </li>
        <li>
          <strong>Topological Ordering:</strong> Execute operations in the
          perfect sequence, adhering to PEMDAS rules for error-free
          calculations.
        </li>
        <li>
          <strong>Applying Custom Formulas:</strong> Seamlessly use pre-defined
          formulas from an external file to generate instant solutions.
        </li>
      </ol>
      <p>
        Fast, intuitive, and educational, <strong>TopoLogic</strong> isn’t just
        an app—it’s your go-to partner for smarter problem-solving.
      </p>
    </div>
  );
}

export default About;
