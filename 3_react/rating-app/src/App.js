import { useState } from "react";
import "./App.css";
import colorData from "./color-data.json";
import ColorList from "./components/ColorList";

function App() {
  const [colors, setColors] = useState(colorData);
  return (
    <ColorList
      colors={colors}
      onRemoveColor={(id) => {
        // my code
      }}
    />
  );
}

export default App;
