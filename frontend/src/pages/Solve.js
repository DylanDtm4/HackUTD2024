import React from "react";
import FileUpload from "../components/FileUpload";
import RemoveFile from "../components/RemoveFile";
import "../styles/styles.css"; // Import the CSS file

function Solve() {
  return (
    <div className="container">
      <FileUpload />
      <RemoveFile />
    </div>
  );
}

export default Solve;
