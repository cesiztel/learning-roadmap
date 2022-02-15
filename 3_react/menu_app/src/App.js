import logo from "./logo.svg";
import "./App.css";
import data from "../src/data/recipes.json";
import Menu from "../src/components/Menu";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Menu recipes={data} title="Delicious Recipes" />
      </header>
    </div>
  );
}

export default App;
