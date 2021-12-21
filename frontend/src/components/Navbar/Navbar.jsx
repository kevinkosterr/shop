import React from "react";

import { AiOutlineShoppingCart, AiOutlineUser } from "react-icons/ai";
import { FaCaretDown } from "react-icons/fa";
import { Link } from "react-router-dom";

const Navbar = ({ children }) => {
  return (
    <header class="text-gray-600 body-font w-full">
      <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <nav class="flex lg:w-2/5 flex-wrap items-center text-base md:ml-auto">
          {children}
        </nav>
        <Link
          to="/"
          className="flex order-first lg:order-none lg:w-1/5 title-font font-medium items-center text-gray-900 lg:items-center lg:justify-center mb-4 md:mb-0"
        >
          <img
            src={process.env.PUBLIC_URL + "/logo.png"}
            className="h-12"
            alt="company logo"
          ></img>
          <span class="text-xl">Example shop</span>
        </Link>
        <div class="lg:w-2/5 inline-flex lg:justify-end ml-5 lg:ml-0">
          <Link
            to="/account"
            className="mr-2 inline-flex items-center rounded-full bg-gray-100 border-0 px-2"
          >
            <AiOutlineUser size="25" />
          </Link>
          <button class="inline-flex items-center rounded-full bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">
            <AiOutlineShoppingCart size="25" />
            <span className="inline-flex items-center">
              <FaCaretDown />
            </span>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Navbar;
