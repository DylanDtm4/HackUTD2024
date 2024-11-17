import React, { useState, useRef } from "react";
import axios from "axios";
import LoadingOverlay from "./LoadingOverlay"; // Import the LoadingOverlay component

const FileUpload = () => {
  const [fileContents, setFileContents] = useState(""); // To store the file contents
  const [fileName, setFileName] = useState(""); // Store original file name
  const [loading, setLoading] = useState(false); // Track loading state
  const fileInputRef = useRef(null); // Create a ref for the file input

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFileName(selectedFile.name); // Store the original file name
      const reader = new FileReader();
      reader.onload = (e) => {
        setFileContents(e.target.result); // Store the file contents in state
      };
      reader.readAsText(selectedFile); // Read file as text
    }
  };

  const handleUpload = async () => {
    if (!fileContents) {
      alert("Please select a file to upload.");
      return;
    }

    try {
      setLoading(true); // Enter loading state

      // Get the processed content from handleProcessString
      const processedContent = await handleProcessString();

      // Create a new file with the processed content
      const newFileName = `SOLUTION_${fileName}`;
      const newFile = new File([processedContent], newFileName, {
        type: "text/plain",
      });

      console.log("New File Contents:", processedContent); // Debugging
      console.log("Original File Contents:", fileContents); // Debugging

      // Prepare the form data with the new file
      const formData = new FormData();
      formData.append("file", newFile);

      // Upload the file to the backend
      const response = await axios.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      // alert("File uploaded successfully!");

      // Get the CID and log the file URL
      const cid = response.data.IpfsHash;
      const fileUrl = `https://gateway.pinata.cloud/ipfs/${cid}`;
      console.log("File URL:", fileUrl);

      // Reset the file input after successful upload
      window.location.reload();
      resetFileInput();
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Failed to upload file content");
    } finally {
      setLoading(false); // Exit loading state
    }
  };

  const handleProcessString = async () => {
    try {
      // Send the file content as a string to the backend for processing
      const response = await axios.post("/api/process-string", {
        content: fileContents,
      });

      // alert("String processed successfully!");

      // Log the processed content
      console.log("Processed Content:", response.data.processedContent);

      // Return the processed content instead of updating the state directly
      return response.data.processedContent;
    } catch (error) {
      console.error("Processing failed:", error);
      alert("Failed to process string content");
      throw error; // Re-throw the error to propagate to handleUpload
    }
  };

  const resetFileInput = () => {
    setFileContents(""); // Clear file contents
    setFileName(""); // Clear file name
    if (fileInputRef.current) {
      fileInputRef.current.value = ""; // Reset the file input field
    }
  };

  return (
    <div className="container">
      <h1>Upload and Process File</h1>
      <div className="upload-container">
        <input type="file" onChange={handleFileChange} ref={fileInputRef} />
        <button onClick={handleUpload} disabled={loading}>
          Solve
        </button>
      </div>

      {fileContents && (
        <div className="file-contents">
          <h2>File Contents:</h2>
          <pre>{fileContents}</pre>
        </div>
      )}

      {/* Display the full-screen loader when loading */}
      {loading && <LoadingOverlay />}
    </div>
  );
};

export default FileUpload;
