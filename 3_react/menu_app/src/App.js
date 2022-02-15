import logo from './logo.svg';
import './App.css';
import Counter from './01_Counter/Counter';
import Greeting from "./02_Greeting/Greeting";
import GreetingLocalStorage from "./03_GreetingsLocalStorage/GreetingLocalStorage";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h3>01 - Counter</h3>
        <Counter />
        <h3>02 - Greeting</h3>
        <Greeting />
        <h3>03 - GreetingLocalStorage</h3>
        <GreetingLocalStorage />
      </header>
    </div>
  );
}

export default App;
