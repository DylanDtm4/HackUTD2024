import React from "react";
import ReactDOM from "react-dom";
import "./LoadingOverlay.css"; // Import its styles

import { bouncy } from "ldrs";

bouncy.register(); // Registers the <l-bouncy> loader globally

const LoadingOverlay = ({ keyValue }) => {
  return ReactDOM.createPortal(
    <div className="loading-overlay">
        <l-bouncy
          size="55"
          speed="1.8" 
          color="#00a3a3"
        ></l-bouncy>
      <div className="fallback-spinner"></div>
    </div>,
    document.body // Render outside of the component hierarchy
  );
};

export default LoadingOverlay;
