import React, { useState, useRef } from "react";
import axios from "axios";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [uploadedData, setUploadedData] = useState(null);
  const fileInputRef = useRef(null); // Create a ref for the file input

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file to upload.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      setUploadedData(response.data);
      resetFileInput(); // Reset the file input after successful upload
      window.location.reload();
    } catch (error) {
      console.error("Upload failed:", error);
    }
  };

  const resetFileInput = () => {
    setFile(null); // Clear the file state
    if (fileInputRef.current) {
      fileInputRef.current.value = ""; // Reset the file input field
    }
  };

  return (
    <div>
      <h1>Upload File to Pinata</h1>
      <input type="file" onChange={handleFileChange} ref={fileInputRef} />
      <button onClick={handleUpload}>Upload</button>
      {uploadedData && (
        <div>
          <h3>File Uploaded:</h3>
          <pre>{JSON.stringify(uploadedData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
