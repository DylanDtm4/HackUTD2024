import React, { useEffect, useState } from "react";
import axios from "axios";

const FileDisplay = () => {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchFiles = async () => {
    try {
      const response = await axios.get("/api/files");
      setFiles(response.data.rows); // Adjust based on API response structure
      setLoading(false);
    } catch (error) {
      console.error("Error fetching files:", error);
      setLoading(false);
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
      <h1>Uploaded Files</h1>
      {files.length > 0 ? (
        <ul>
          {files.map((file, index) => (
            <li key={index}>
              <p>Filename: {file.metadata.name || "N/A"}</p>
              <a
                href={`https://gateway.pinata.cloud/ipfs/${file.ipfs_pin_hash}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                Access File
              </a>
            </li>
          ))}
        </ul>
      ) : (
        <p>No files uploaded yet.</p>
      )}
    </div>
  );
};

export default FileDisplay;
