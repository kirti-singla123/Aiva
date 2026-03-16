import React from "react";
import "./PlanetOrb.css";

export default function PlanetOrb() {
  return (
    <div className="planet-scene">
      <div className="planet-wrapper">
        <div className="planet-core"></div>
        <div className="orbit orbit1"></div>
        <div className="orbit orbit2"></div>
        <div className="orbit orbit3"></div>
      </div>
    </div>
  );
}

