import React from "react";
import FileUpload from "./components/FileUpload";
import FileDisplay from "./components/FileDisplay";
import RemoveFile from "./components/RemoveFile";
import "./styles/styles.css"; // Import the CSS file

function App() {
  return (
    <div className="bg">
      <div className="container">
        <FileUpload />
        <FileDisplay />
        <RemoveFile />
      </div>
    </div>
  );
}

export default App;
