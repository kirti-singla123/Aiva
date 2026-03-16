import React from "react";
import "../Header.css";

function Header() {
  return (
    <div className="header">
      <div className="logo">AIVA</div>
      <div className="buttons">
        <button className="settings-btn">Settings</button>
        <button className="disconnect-btn">Disconnect</button>
      </div>
    </div>
  );
}

export default Header;
