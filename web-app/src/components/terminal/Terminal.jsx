import React, { useState } from "react";

// Styles
import "./terminal.css";

function Terminal() {
  const [terminalText, setTerminalText] = useState("Hello World!");

  return (
    <div className="terminal">
      <textarea cols="35" rows="15" readOnly value={terminalText} />
    </div>
  );
}

export default Terminal;
