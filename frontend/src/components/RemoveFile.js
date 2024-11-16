import React, { useEffect, useState } from "react";
import axios from "axios";

const RemoveFile = () => {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [deleting, setDeleting] = useState(null);

  // Fetch files from the backend
  const fetchFiles = async () => {
    setLoading(true);
    try {
      const response = await axios.get("/api/files");
      if (response.data?.rows) {
        setFiles(response.data.rows); // Adjust based on API response structure
      } else {
        console.warn("Unexpected response structure:", response.data);
        setFiles([]);
      }
    } catch (error) {
      console.error(
        "Error fetching files:",
        error.response?.data || error.message
      );
    } finally {
      setLoading(false);
    }
  };

  // Remove file by its IPFS hash
  const removeFile = async (fileHash) => {
    setDeleting(fileHash);
    try {
      const response = await axios.delete(`/api/delete-file/${fileHash}`);

      if (response.status === 200) {
        // Filter out the deleted file from the list
        setFiles((prevFiles) =>
          prevFiles.filter((file) => file.ipfs_pin_hash !== fileHash)
        );
        alert("File deleted successfully!");
      } else {
        console.error("Failed to delete file:", response.data);
        alert(
          `Failed to delete file: ${response.data.error || "Unknown error"}`
        );
      }
      window.location.reload();
    } catch (error) {
      console.error(
        "Error deleting file:",
        error.response?.data || error.message
      );
      const errorMsg =
        error.response?.data?.details?.message || "Unknown error occurred.";
      alert(`An error occurred: ${errorMsg}`);
    } finally {
      setDeleting(null);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  if (loading) {
    return <p>Loading files...</p>;
  }

  return (
    <div>
      <h1>Manage Uploaded Files</h1>
      {files.length > 0 ? (
        <ul>
          {files.map((file) => (
            <li key={file.ipfs_pin_hash}>
              <p>Filename: {file.metadata?.name || "N/A"}</p>
              <a
                href={`https://gateway.pinata.cloud/ipfs/${file.ipfs_pin_hash}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                Access File
              </a>
              <button
                onClick={() => removeFile(file.ipfs_pin_hash)}
                disabled={deleting === file.ipfs_pin_hash}
                style={{ marginLeft: "10px" }}
              >
                {deleting === file.ipfs_pin_hash ? "Deleting..." : "Remove"}
              </button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No files uploaded yet.</p>
      )}
    </div>
  );
};

export default RemoveFile;
