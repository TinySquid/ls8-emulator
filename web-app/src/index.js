import React from "react";
import ReactDOM from "react-dom";

// Main app (emulator)
import Emulator from "./main/Emulator";

import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <Emulator />
  </React.StrictMode>,
  document.getElementById("root")
);
