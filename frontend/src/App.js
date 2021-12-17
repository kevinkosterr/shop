import "./App.css";
import Navbar from "./components/Navbar";
import Product from "./components/Products/Product";

function App() {
  return (
    <div className="App">
      <Navbar/>
        <Product title={"Test"} price={10} uid={123123213}/>
    </div>
  );
}

export default App;
