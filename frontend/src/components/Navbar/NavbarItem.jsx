import React from "react";
import { Link } from "react-router-dom";

const NavbarItem = ({ href, text, status }) => {
  return (
    <Link
      className={
        status
          ? "mr-5 hover:text-gray-900 text-gray-900 font-semibold"
          : "mr-5 hover:text-gray-900"
      }
      to={href}
    >
      {text}
    </Link>
  );
};

export default NavbarItem;
