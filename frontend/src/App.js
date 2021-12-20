import "./App.css";
import Navbar from "./components/Navbar/Navbar";
import { Products } from "./components/Products/Products";
import { ApolloProvider } from "@apollo/client";
import client from "./graphql/Client";
import NavbarItem from "./components/Navbar/NavbarItem";

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App flex">
        <Navbar>
          <NavbarItem text="Home" href="/" />
          <NavbarItem text="Shop" href="/shop" />
          <NavbarItem text="About us" href="/" />
          <NavbarItem text="Contact" href="/" />
        </Navbar>
        
      </div>
    </ApolloProvider>
  );
}

export default App;
