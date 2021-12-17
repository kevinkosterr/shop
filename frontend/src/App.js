import "./App.css";
import Navbar from "./components/Navbar";
import {Products} from "./components/Products/Products";
import {ApolloProvider} from "@apollo/client";
import client from "./graphql/Client";


function App() {

    return (
        <ApolloProvider client={client} >
            <div className="App">
                <Navbar/>
                <Products/>
            </div>
        </ApolloProvider>
    );
}

export default App;
