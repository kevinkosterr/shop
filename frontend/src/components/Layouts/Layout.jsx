import React from "react";
import Footer from "../Footer/Footer";
import Navbar from "../Navbar/Navbar";
import NavbarItem from "../Navbar/NavbarItem";

const Layout = ({ children }) => {
  return (
    <div class="App h-screen flex-col flex">
      <Navbar>
        <NavbarItem text="Home" href="/" status="active" />
        <NavbarItem text="Shop" href="/shop" />
        <NavbarItem text="About us" href="/about" />
        <NavbarItem text="Contact" href="/contact" />
      </Navbar>
      <div className="main flex-grow mb-auto">{children}</div>
      <Footer/>
    </div>
  );
};

export default Layout;
