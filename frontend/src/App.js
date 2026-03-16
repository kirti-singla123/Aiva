import ChatPanel from "./components/ChatPanel";
import "./App.css";

function App() {
  return (
    <div className="app">
      <div className="header">AIVA</div>

      <div className="main-layout">
        <ChatPanel />
      </div>
    </div>
  );
}

export default App;