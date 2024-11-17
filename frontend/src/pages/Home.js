import React from "react";
import "../styles/styles.css"; // Import the CSS file

function Home() {
  return (
    <div className="container">
      <h1>
        Welcome to <strong>TopoLogic</strong>
      </h1>
      <p>
        TopoLogic is your ultimate tool for solving word problems with speed,
        precision, and ease. Here's how you can make the most of its features:
      </p>

      <h2>1. Solve Page</h2>
      <p>This is where the magic happens!</p>
      <ol className="list-style">
        <li>
          <strong>Upload Files:</strong> Add your word problem files to the
          project's database.
        </li>
        <li>
          <strong>Compute Solutions:</strong> TopoLogic extracts variables,
          applies advanced topological logic, and calculates the solution
          instantly.
        </li>
        <li>
          <strong>Detailed Results:</strong> View the solution along with a
          step-by-step explanation to understand how it was solved.
        </li>
        <li>
          <strong>Manage Files:</strong> Remove files that are no longer needed,
          keeping your workspace clean and organized.
        </li>
      </ol>

      <h2>2. About Page</h2>
      <p>Curious about TopoLogic?</p>
      <ol className="list-style">
        <li>
          Learn more about the project's purpose, the innovative technology
          powering it, and how it streamlines problem-solving.
        </li>
        <li>
          Discover why TopoLogic is the perfect tool for tackling word problems
          efficiently.
        </li>
      </ol>

      <p>
        With TopoLogic, solving complex word problems has never been simpler.
        Explore the features, upload your files, and let TopoLogic handle the
        rest!
      </p>
    </div>
  );
}

export default Home;
