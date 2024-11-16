import React from "react";
import FileUpload from "./components/FileUpload";
import FileDisplay from "./components/FileDisplay";
import RemoveFile from "./components/RemoveFile";
import "./styles/styles.css"; // Import the CSS file

function App() {
  return (
    <div class="container">
      <FileUpload />
      <FileDisplay />
      <RemoveFile />
    </div>
  );
}

export default App;
